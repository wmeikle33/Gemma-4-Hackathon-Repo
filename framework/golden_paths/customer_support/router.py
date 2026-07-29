from .schemas import RequestType


REFUND_TERMS = {
    "refund",
    "money back",
    "reverse payment",
    "cancel payment",
}

ACCOUNT_TERMS = {
    "account",
    "subscription",
    "membership",
    "profile",
    "login",
    "status",
}

GENERAL_TERMS = {
    "policy",
    "shipping",
    "delivery",
    "hours",
    "how",
    "what",
    "when",
}


def classify_request(message: str) -> RequestType:
    normalized = message.lower().strip()

    if any(term in normalized for term in REFUND_TERMS):
        return "refund_request"

    if any(term in normalized for term in ACCOUNT_TERMS):
        return "account_request"

    if any(term in normalized for term in GENERAL_TERMS):
        return "general_question"

    return "unknown"
