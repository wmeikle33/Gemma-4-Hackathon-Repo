# Reflection Pattern

## Overview

The **Reflection pattern** allows an AI system to evaluate its own work before producing a final result.

After generating an initial response, the model reflects on its output, identifies weaknesses, and revises the response if necessary.

Unlike the Generator–Critic pattern, reflection is performed by the same agent rather than a separate evaluator.

```text
Task
  │
  ▼
Generate
  │
  ▼
Reflect
  │
  ▼
Revise?
 ├── Yes
 │      ▼
 │  Improve Response
 │
 └── No
        ▼
 Final Answer
```

Reflection can improve quality while requiring fewer components than multi-agent architectures.

---

# Core Idea

Separate the work into two phases:

1. Produce an initial solution.
2. Critically evaluate that solution before returning it.

Reflection encourages the model to identify:

- Missing information
- Logical errors
- Weak explanations
- Inconsistencies
- Formatting problems
- Policy violations

---

# Components

## Generator

Produces the initial response.

Responsibilities include:

- Solving the task
- Calling tools if required
- Producing a draft

---

## Reflection Step

The same model examines its own output.

Questions may include:

- Is anything missing?
- Is this factually supported?
- Are there contradictions?
- Is the answer complete?
- Could it be clearer?
- Should another tool be used?

---

## Revision Step

If improvements are identified, the response is revised before being returned.

Not every response requires revision.

---

# Basic Workflow

```text
Receive Task
      │
Generate Draft
      │
Reflect
      │
Problems Found?
      │
 ├── No
 │      ▼
 │ Return Draft
 │
 └── Yes
        ▼
 Revise
        │
        ▼
 Return Final Answer
```

---

# Example

User asks:

> Explain recursion.

Initial draft:

```text
Recursion is when a function calls itself.
```

Reflection:

```text
Missing:

- Base case
- Example
- Practical use
```

Revision:

```text
Recursion is a programming technique in which a function calls itself to solve smaller instances of a problem. Every recursive algorithm requires a base case to stop further calls and prevent infinite recursion.
```

---

# Reflection Questions

Useful prompts include:

- Is the answer correct?
- Is anything missing?
- Are assumptions justified?
- Is evidence sufficient?
- Is the explanation clear?
- Can unnecessary detail be removed?
- Is another tool required?

---

# Reflection Depth

Reflection may vary depending on task complexity.

### Light Reflection

Grammar, formatting, clarity.

### Moderate Reflection

Logic, completeness, factual consistency.

### Deep Reflection

Alternative solutions, assumptions, trade-offs, risks.

Deeper reflection generally increases latency and cost.

---

# Single vs. Multiple Reflection Passes

### Single Pass

```text
Generate

↓

Reflect

↓

Return
```

Suitable for most applications.

---

### Multiple Passes

```text
Generate

↓

Reflect

↓

Revise

↓

Reflect Again

↓

Return
```

Limit the number of passes to avoid unnecessary iterations.

---

# Reflection Criteria

Possible evaluation dimensions include:

- Accuracy
- Completeness
- Clarity
- Safety
- Consistency
- Style
- Evidence
- Tool usage

Different applications may prioritize different criteria.

---

# Stopping Conditions

Reflection should stop when:

- No meaningful improvements remain.
- Maximum reflection passes are reached.
- Quality thresholds are satisfied.
- Human review is required.

Without stopping rules, reflection can become an endless optimization process.

---

# When to Use This Pattern

Use Reflection when:

- Higher-quality responses are desired.
- Tasks involve writing or reasoning.
- Minor improvements justify a small increase in latency.
- A full Generator–Critic workflow is unnecessary.

Typical applications include:

- Writing assistants
- Coding assistants
- Summarization
- Report generation
- Educational tools

---

# When Not to Use It

Avoid Reflection when:

- Responses are deterministic.
- Latency is critical.
- Simple formatting is sufficient.
- External validation is required.

Some tasks benefit more from independent review than self-review.

---

# Common Failure Modes

## Endless Reflection

The agent continually revises its response.

**Solution**

Limit reflection passes.

---

## Cosmetic Improvements

Reflection only changes wording without improving quality.

**Solution**

Focus on meaningful evaluation criteria.

---

## Confirmation Bias

The model fails to notice its own mistakes.

**Solution**

Use Generator–Critic or Human Review for high-risk tasks.

---

## Overediting

Reflection introduces unnecessary complexity.

**Solution**

Only revise when measurable improvements exist.

---

## Reduced Diversity

Repeated revisions converge toward similar wording.

**Solution**

Stop once quality goals are met.

---

# Human Review

High-risk responses may still require human approval.

```text
Generate

↓

Reflect

↓

Human Review

↓

Final Response
```

Reflection complements human review but does not replace it.

---

# No-Code Implementation

Typical workflow:

1. Generate a draft.
2. Evaluate it against predefined criteria.
3. Revise if necessary.
4. Check stopping conditions.
5. Return the final response.

---

# Observability

Track:

- Reflection rate
- Number of revisions
- Reflection latency
- Token usage
- Cost per task
- Quality improvements
- User satisfaction

These metrics help determine whether reflection provides sufficient value.

---

# Evaluation Metrics

Useful metrics include:

- Improvement rate
- Revision frequency
- Average reflection passes
- User ratings
- Task success rate
- Cost increase
- Latency increase

Reflection should improve quality enough to justify its additional cost.

---

# Design Checklist

Before implementing Reflection, ensure that:

- Reflection criteria are clearly defined.
- Maximum reflection passes exist.
- Revisions improve quality rather than wording alone.
- Reflection outputs are observable.
- High-risk tasks can escalate to human review.

---

# Trade-Offs

| Advantage | Trade-Off |
|-----------|-----------|
| Better response quality | Increased latency |
| Simple architecture | Additional token usage |
| Easy to implement | Self-review may miss errors |
| Improves clarity | Limited independence |

---

# Related Patterns

- Generator–Critic
- Debate
- Planner–Executor
- Human-in-the-Loop
- Hybrid Patterns

---

# Related Anti-Patterns

- Blind Retries
- Infinite Loops
- Overplanning
- Hidden State

---

# Pattern Summary

The Reflection pattern improves response quality by allowing an AI system to evaluate and revise its own work before producing a final answer.

It provides a lightweight alternative to Generator–Critic workflows and is particularly useful for writing, reasoning, and content generation tasks where small improvements justify modest additional cost and latency.
