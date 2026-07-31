from dataclasses import dataclass

from .schemas import SupportResponse


@dataclass
class EvaluationResult:
    passed: bool
    checks: dict[str, bool]


def evaluate_response(
    response: SupportResponse,
) -> EvaluationResult:
    checks = {
        "has_request_id": bool(response.request_id),
        "has_response": bool(response.response.strip()),
        "valid_escalation": (
            response.requires_human_review
            == (response.status == "escalated")
        ),
        "refunds_are_escalated": (
            response.request_type != "refund_request"
            or response.requires_human_review
        ),
        "completed_retrieval_has_citation": (
            response.request_type != "general_question"
            or response.status != "completed"
            or bool(response.citations)
        ),
    }

    return EvaluationResult(
        passed=all(checks.values()),
        checks=checks,
    )
