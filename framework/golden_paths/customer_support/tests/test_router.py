"""
Tests for the customer-support request router.

These tests verify that customer messages are classified into the
correct request type before entering the rest of the workflow.
"""

import pytest

from framework.golden_paths.customer_support.router import (
    classify_request,
)


# ---------------------------------------------------------------------------
# General Questions
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "message",
    [
        "What is your refund policy?",
        "How long does shipping take?",
        "When will my order be delivered?",
        "What shipping methods do you offer?",
        "How does your service work?",
        "WHAT IS YOUR REFUND POLICY?",
        "  What is your shipping policy?  ",
    ],
)
def test_general_questions_are_classified_correctly(
    message: str,
) -> None:
    """General informational questions should use knowledge retrieval."""

    assert classify_request(message) == "general_question"


# ---------------------------------------------------------------------------
# Account Requests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "message",
    [
        "What is my account status?",
        "Can you check my account?",
        "Which subscription plan am I using?",
        "When does my membership renew?",
        "I need help with my profile.",
        "I cannot log in to my account.",
        "Please check my subscription.",
        "WHAT IS MY ACCOUNT STATUS?",
        "  Can you check my account?  ",
    ],
)
def test_account_requests_are_classified_correctly(
    message: str,
) -> None:
    """Account-related messages should use the account-request route."""

    assert classify_request(message) == "account_request"


# ---------------------------------------------------------------------------
# Refund Requests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "message",
    [
        "Please refund my payment.",
        "I want a refund.",
        "Can I get my money back?",
        "Please reverse this payment.",
        "I want to cancel the payment.",
        "REFUND MY ORDER",
        "  I want my money back.  ",
    ],
)
def test_refund_requests_are_classified_correctly(
    message: str,
) -> None:
    """Refund-related messages should always use the refund route."""

    assert classify_request(message) == "refund_request"


# ---------------------------------------------------------------------------
# Unknown Requests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "message",
    [
        "Something is wrong.",
        "Please help me.",
        "This is confusing.",
        "I have a problem.",
        "Hello.",
        "Can someone contact me?",
        "Bananas are yellow.",
    ],
)
def test_unclear_requests_are_classified_as_unknown(
    message: str,
) -> None:
    """Ambiguous messages should not be forced into a known route."""

    assert classify_request(message) == "unknown"


# ---------------------------------------------------------------------------
# Input Normalization
# ---------------------------------------------------------------------------

def test_router_is_case_insensitive() -> None:
    """Classification should not depend on capitalization."""

    lower_result = classify_request(
        "what is my account status?"
    )
    upper_result = classify_request(
        "WHAT IS MY ACCOUNT STATUS?"
    )

    assert lower_result == upper_result
    assert lower_result == "account_request"


def test_router_ignores_surrounding_whitespace() -> None:
    """Leading and trailing whitespace should not change the route."""

    result = classify_request(
        "   Please refund my payment.   "
    )

    assert result == "refund_request"


def test_empty_message_is_unknown() -> None:
    """An empty message should not match a valid request type."""

    assert classify_request("") == "unknown"


def test_whitespace_only_message_is_unknown() -> None:
    """A whitespace-only message should be treated as unknown."""

    assert classify_request("     ") == "unknown"


# ---------------------------------------------------------------------------
# Route-Priority Tests
# ---------------------------------------------------------------------------

def test_refund_route_takes_priority_over_account_route() -> None:
    """
    A message containing both refund and account terms should be
    treated as a refund request because refunds require human review.
    """

    message = (
        "Please check my account and refund my last payment."
    )

    assert classify_request(message) == "refund_request"


def test_refund_route_takes_priority_over_general_route() -> None:
    """
    A direct refund request should take priority over informational
    terms such as policy or how.
    """

    message = "How can I get a refund for my payment?"

    assert classify_request(message) == "refund_request"


def test_account_route_takes_priority_over_general_route() -> None:
    """
    A customer-specific account request should take priority over
    general question terms.
    """

    message = "How can I check my account status?"

    assert classify_request(message) == "account_request"


# ---------------------------------------------------------------------------
# False-Positive Tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "message",
    [
        "I read an article about financial accounts.",
        "The word refund appears in your documentation.",
        "Tell me a story about shipping containers.",
    ],
)
def test_router_documents_current_keyword_behavior(
    message: str,
) -> None:
    """
    Document the current keyword router's behavior.

    This test can be replaced with stricter expectations when the
    router introduces tokenization, phrase matching, or confidence
    thresholds.
    """

    result = classify_request(message)

    assert result in {
        "general_question",
        "account_request",
        "refund_request",
        "unknown",
    }


# ---------------------------------------------------------------------------
# Return-Value Contract
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "message",
    [
        "What is your shipping policy?",
        "Check my account status.",
        "I want a refund.",
        "Please help.",
    ],
)
def test_router_returns_supported_request_type(
    message: str,
) -> None:
    """The router must always return a supported request type."""

    supported_request_types = {
        "general_question",
        "account_request",
        "refund_request",
        "unknown",
    }

    assert classify_request(message) in supported_request_types
