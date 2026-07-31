from dataclasses import dataclass, field
from typing import Any, Literal


RequestType = Literal[
    "general_question",
    "account_request",
    "refund_request",
    "unknown",
]

WorkflowStatus = Literal[
    "completed",
    "needs_clarification",
    "escalated",
    "failed",
]


@dataclass
class SupportRequest:
    request_id: str
    user_id: str
    message: str


@dataclass
class ToolCall:
    tool_name: str
    arguments: dict[str, Any]
    result: dict[str, Any] | None = None


@dataclass
class SupportResponse:
    request_id: str
    status: WorkflowStatus
    request_type: RequestType
    response: str
    requires_human_review: bool = False
    citations: list[str] = field(default_factory=list)
    tool_calls: list[ToolCall] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
