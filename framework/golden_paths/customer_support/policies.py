from .schemas import RequestType


HUMAN_REVIEW_REQUIRED: set[RequestType] = {
    "refund_request",
}


def requires_human_review(request_type: RequestType) -> bool:
    return request_type in HUMAN_REVIEW_REQUIRED


def tool_is_allowed(
    request_type: RequestType,
    tool_name: str,
) -> bool:
    allowed_tools = {
        "account_request": {"get_account_status"},
        "general_question": set(),
        "refund_request": set(),
        "unknown": set(),
    }

    return tool_name in allowed_tools.get(request_type, set())
