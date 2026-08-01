# Account Help

## Account Status

Customers can ask whether their account is active, paused, suspended, or closed.

Account status information must be retrieved using the approved read-only account tool. The support agent must not guess an account's status from the customer's message.

## Supported Account Information

The customer-support workflow may provide the following information when it is returned by an approved tool:

- Current account status
- Current subscription plan
- Next renewal date
- Whether the account was found

The workflow must not expose passwords, payment-card details, security answers, internal identifiers, access tokens, or other sensitive account information.

## Account Not Found

If the account tool cannot locate an account, the agent should:

1. Tell the customer that the account could not be located.
2. Avoid suggesting that the account does not exist.
3. Ask the customer to verify the account details through an approved support channel.
4. Escalate the request when identity verification or manual investigation is required.

Example response:

> I could not locate the account using the available information. Please verify that you are using the correct account details. A support specialist may need to review the request.

## Login Problems

For common login problems, customers should first:

1. Confirm that they are using the correct email address or username.
2. Check whether Caps Lock is enabled.
3. Use the approved password-reset process.
4. Check their spam or junk folder for the reset email.
5. Wait a few minutes before requesting another reset email.

The support agent must never ask a customer to provide their password.

## Password Resets

Passwords cannot be viewed or retrieved by support agents.

Customers who forget their password should use the official password-reset process. The support agent may explain the reset steps but must not create, request, store, or transmit a password on the customer's behalf.

If the customer cannot access the email address associated with the account, the request must be escalated for identity verification.

## Paused Accounts

A paused account may temporarily restrict access to paid features.

The support agent may explain the account's current status when that status is returned by the account tool. The agent must not reactivate or modify the account unless an approved action tool and authorization policy are available.

In the golden-path implementation, account changes are not supported and must be escalated.

## Suspended Accounts

Suspended accounts require human review.

The agent should not speculate about the reason for a suspension unless an approved source explicitly provides that information.

Example response:

> Your account is currently suspended. A support specialist will need to review the account before any changes can be made.

## Closing an Account

Requests to close or delete an account may have legal, billing, privacy, or data-retention consequences.

The golden-path workflow must not close accounts automatically. These requests must be escalated to a human reviewer.

The agent may explain the general process but must not claim that the account has been closed until an authorized system confirms the action.

## Billing and Subscription Changes

The account-status tool is read-only.

The workflow may display the customer's current plan and renewal date, but it cannot:

- Change a subscription plan
- Cancel a subscription
- Update payment information
- Apply discounts
- Issue refunds
- Modify a renewal date

Requests for these actions must be transferred to an authorized workflow or human support specialist.

## Security and Privacy Rules

The support agent must:

- Use only approved tools to retrieve account information
- Reveal only the minimum information needed to answer the request
- Avoid exposing internal system details
- Never request passwords or full payment-card details
- Escalate requests involving identity verification
- Avoid making account changes through a read-only workflow

## Human Review Is Required When

A request must be escalated when:

- The account cannot be found
- The customer cannot access the registered email address
- The account is suspended
- The customer reports unauthorized access
- Identity verification is required
- The customer wants to close or delete the account
- The customer requests a billing or subscription change
- The requested action is not supported by an approved tool

## Example Questions

This document may be relevant to questions such as:

- What is the status of my account?
- Which subscription plan am I using?
- When does my account renew?
- Why can't I log in?
- How do I reset my password?
- Why is my account paused?
- Can you reactivate my account?
- Can you close my account?
- Can you change my subscription?
- Why can't you find my account?

## Implementation Note

In the customer-support golden path, account information is retrieved from a local read-only mock tool.

This document provides general account-support guidance. It must not be treated as a source of customer-specific account data.

