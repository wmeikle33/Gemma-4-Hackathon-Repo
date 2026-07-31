from pathlib import Path

from .knowledge import LocalKnowledgeBase
from .policies import requires_human_review, tool_is_allowed
from .router import classify_request
from .schemas import SupportRequest, SupportResponse, ToolCall
from .tools import get_account_status


class CustomerSupportWorkflow:
    def __init__(self) -> None:
        knowledge_dir = Path(__file__).parent / "knowledge_base"
        self.knowledge_base = LocalKnowledgeBase(knowledge_dir)

    def run(self, request: SupportRequest) -> SupportResponse:
        request_type = classify_request(request.message)

        if request_type == "unknown":
            return SupportResponse(
                request_id=request.request_id,
                status="needs_clarification",
                request_type=request_type,
                response=(
                    "I am not certain which type of support you need. "
                    "Please provide more details about your request."
                ),
            )

        if requires_human_review(request_type):
            knowledge_results = self.knowledge_base.search(
                request.message
            )

            citations = [
                result.source for result in knowledge_results
            ]

            return SupportResponse(
                request_id=request.request_id,
                status="escalated",
                request_type=request_type,
                response=(
                    "Refund requests require review by a support "
                    "specialist. I have prepared this request for "
                    "human review."
                ),
                requires_human_review=True,
                citations=citations,
            )

        if request_type == "account_request":
            tool_name = "get_account_status"

            if not tool_is_allowed(request_type, tool_name):
                return SupportResponse(
                    request_id=request.request_id,
                    status="failed",
                    request_type=request_type,
                    response="The required tool is not permitted.",
                    errors=["tool_not_allowed"],
                )

            result = get_account_status(request.user_id)

            tool_call = ToolCall(
                tool_name=tool_name,
                arguments={"user_id": request.user_id},
                result=result,
            )

            if not result["success"]:
                return SupportResponse(
                    request_id=request.request_id,
                    status="escalated",
                    request_type=request_type,
                    response=(
                        "I could not locate the account. "
                        "A support specialist should review this request."
                    ),
                    requires_human_review=True,
                    tool_calls=[tool_call],
                )

            account = result["account"]

            return SupportResponse(
                request_id=request.request_id,
                status="completed",
                request_type=request_type,
                response=(
                    f"Your account is {account['account_status']} "
                    f"on the {account['plan']} plan."
                ),
                tool_calls=[tool_call],
            )

        knowledge_results = self.knowledge_base.search(
            request.message
        )

        if not knowledge_results:
            return SupportResponse(
                request_id=request.request_id,
                status="needs_clarification",
                request_type=request_type,
                response=(
                    "I could not find enough information to answer "
                    "that question confidently."
                ),
            )

        best_result = knowledge_results[0]

        return SupportResponse(
            request_id=request.request_id,
            status="completed",
            request_type=request_type,
            response=best_result.content,
            citations=[best_result.source],
        )
