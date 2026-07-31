# Customer Support Golden Path

## Purpose

This example demonstrates a complete AI-agent workflow using
deterministic local components.

## Supported Requests

- General policy questions
- Account-status requests
- Refund requests

## Workflow

1. Validate the request.
2. Classify the request.
3. Apply permission and escalation policies.
4. Retrieve knowledge or invoke an allowed tool.
5. Produce a structured response.
6. Evaluate and audit the result.

## Safety Boundaries

- The workflow cannot issue refunds.
- Account tools are read-only.
- Unknown requests require clarification.
- Refund requests require human review.

## Run

```bash
python run_golden_path.py \
  --input framework/golden_paths/customer_support/sample_inputs/general_question.json
