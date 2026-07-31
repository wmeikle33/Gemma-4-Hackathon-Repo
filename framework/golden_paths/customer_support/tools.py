MOCK_ACCOUNTS = {
    "user-123": {
        "account_status": "active",
        "plan": "standard",
        "renewal_date": "2026-08-15",
    },
    "user-456": {
        "account_status": "paused",
        "plan": "premium",
        "renewal_date": None,
    },
}


def get_account_status(user_id: str) -> dict:
    account = MOCK_ACCOUNTS.get(user_id)

    if account is None:
        return {
            "success": False,
            "error": "account_not_found",
        }

    return {
        "success": True,
        "account": account,
    }
