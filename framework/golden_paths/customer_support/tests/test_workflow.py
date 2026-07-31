from framework.golden_paths.customer_support.schemas import (
    SupportRequest,
)
from framework.golden_paths.customer_support.workflow import (
    CustomerSupportWorkflow,
)


def test_general_question_uses_knowledge_base() -> None:
    workflow = CustomerSupportWorkflow()

    request = SupportRequest(
        request_id="req-test-1",
        user_id="user-123",
        message="What is your refund policy?",
    )

    result = workflow.run(request)

    assert result.status == "completed"
    assert result.request_type == "general_question"
    assert result.citations


def test_account_request_calls_account_tool() -> None:
    workflow = CustomerSupportWorkflow()

    request = SupportRequest(
        request_id="req-test-2",
        user_id="user-123",
        message="What is my account status?",
    )

    result = workflow.run(request)

    assert result.status == "completed"
    assert result.request_type == "account_request"
    assert len(result.tool_calls) == 1
    assert result.tool_calls[0].tool_name == "get_account_status"


def test_refund_request_is_escalated() -> None:
    workflow = CustomerSupportWorkflow()

    request = SupportRequest(
        request_id="req-test-3",
        user_id="user-123",
        message="Please refund my last payment.",
    )

    result = workflow.run(request)

    assert result.status == "escalated"
    assert result.requires_human_review is True
    assert result.tool_calls == []


def test_unknown_request_asks_for_clarification() -> None:
    workflow = CustomerSupportWorkflow()

    request = SupportRequest(
        request_id="req-test-4",
        user_id="user-123",
        message="Something is not right.",
    )

    result = workflow.run(request)

    assert result.status == "needs_clarification"
