"""
Tests for customer support workflow policies.

These tests verify that routing, tool permissions, and
human-review requirements are enforced correctly.
"""

import pytest

from framework.golden_paths.customer_support.policies import (
    HUMAN_REVIEW_REQUIRED,
    TOOL_PERMISSIONS,
    requires_human_review,
    tool_is_allowed,
)


# ---------------------------------------------------------------------------
# Human Review Policies
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "request_type,expected",
    [
        ("general_question", False),
        ("account_request", False),
        ("refund_request", True),
        ("unknown", False),
    ],
)
def test_requires_human_review(request_type, expected):
    """Verify which request types require human review."""

    assert requires_human_review(request_type) is expected


def test_refund_request_requires_review():
    """Refund requests must always require review."""

    assert requires_human_review("refund_request")


def test_general_question_does_not_require_review():
    """General policy questions should not require review."""

    assert not requires_human_review("general_question")


def test_account_request_does_not_require_review():
    """Read-only account requests should not require review."""

    assert not requires_human_review("account_request")


# ---------------------------------------------------------------------------
# Tool Permissions
# ---------------------------------------------------------------------------

def test_account_tool_allowed():
    """Account requests may call the account lookup tool."""

    assert tool_is_allowed(
        "account_request",
        "get_account_status",
    )


def test_general_question_has_no_tools():
    """General questions should not require tool access."""

    assert not tool_is_allowed(
        "general_question",
        "get_account_status",
    )


def test_refund_request_cannot_call_account_tool():
    """Refund workflow cannot access account tool."""

    assert not tool_is_allowed(
        "refund_request",
        "get_account_status",
    )


def test_unknown_request_has_no_tool_access():
    """Unknown requests should not have tool access."""

    assert not tool_is_allowed(
        "unknown",
        "get_account_status",
    )


# ---------------------------------------------------------------------------
# Unknown Tool Handling
# ---------------------------------------------------------------------------

def test_unknown_tool_is_rejected():
    """Unknown tools should always be rejected."""

    assert not tool_is_allowed(
        "account_request",
        "delete_database",
    )


def test_empty_tool_name_is_rejected():
    """Empty tool names should never be allowed."""

    assert not tool_is_allowed(
        "account_request",
        "",
    )


# ---------------------------------------------------------------------------
# Policy Definitions
# ---------------------------------------------------------------------------

def test_human_review_policy_contains_refund_request():
    """Refund requests must appear in the review policy."""

    assert "refund_request" in HUMAN_REVIEW_REQUIRED


def test_tool_permissions_defined():
    """Every request type should have a permission definition."""

    expected = {
        "general_question",
        "account_request",
        "refund_request",
        "unknown",
    }

    assert expected.issubset(TOOL_PERMISSIONS.keys())


# ---------------------------------------------------------------------------
# Allowed Tool Lists
# ---------------------------------------------------------------------------

def test_account_request_allowed_tools():
    """Verify account-request tool permissions."""

    assert TOOL_PERMISSIONS["account_request"] == {
        "get_account_status",
    }


def test_general_question_allowed_tools():
    """General questions should not call tools."""

    assert TOOL_PERMISSIONS["general_question"] == set()


def test_refund_request_allowed_tools():
    """Refund requests should not execute tools."""

    assert TOOL_PERMISSIONS["refund_request"] == set()


def test_unknown_allowed_tools():
    """Unknown requests should not execute tools."""

    assert TOOL_PERMISSIONS["unknown"] == set()


# ---------------------------------------------------------------------------
# Security Regression Tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "tool_name",
    [
        "delete_account",
        "issue_refund",
        "modify_subscription",
        "change_password",
        "update_payment_method",
    ],
)
def test_sensitive_tools_are_not_allowed(tool_name):
    """Sensitive operations must never be executable."""

    assert not tool_is_allowed(
        "account_request",
        tool_name,
    )


# ---------------------------------------------------------------------------
# Future-Proofing
# ---------------------------------------------------------------------------

def test_every_human_review_type_exists():
    """
    Every human-review request type should also exist
    in the tool permission table.
    """

    for request_type in HUMAN_REVIEW_REQUIRED:
        assert request_type in TOOL_PERMISSIONS
