# Planner–Executor Pattern

## Overview

The **Planner–Executor pattern** separates strategic planning from task execution.

The planner determines **what should be done**, while the executor performs the work. This separation allows plans to be reviewed, modified, or optimized before any actions are taken.

```text
User Task
    │
    ▼
 Planner
    │
Execution Plan
    │
    ▼
 Executor
    │
    ▼
Results
```

By separating planning from execution, AI systems become easier to monitor, debug, and improve.

---

# Core Idea

Separate **thinking** from **doing**.

The planner decides:

- Objectives
- Task order
- Dependencies
- Required tools
- Success criteria

The executor:

- Calls tools
- Retrieves information
- Generates outputs
- Performs actions
- Reports progress

---

# Components

## Planner

The planner is responsible for:

- Understanding the objective
- Breaking tasks into steps
- Selecting tools
- Identifying dependencies
- Estimating complexity
- Producing an execution plan

The planner should not directly perform the work.

---

## Executor

The executor carries out the plan.

Typical responsibilities include:

- Tool execution
- API calls
- Retrieval
- Code execution
- Database queries
- Content generation

The executor follows the approved plan while reporting status and errors.

---

## Shared Context

Both components may share:

- User request
- Constraints
- Available tools
- Memory
- Intermediate results

Only the necessary context should be shared.

---

# Basic Workflow

```text
Receive Task
      │
Planner Creates Plan
      │
Validate Plan
      │
Executor Performs Tasks
      │
Collect Results
      │
Return Response
```

---

# Example

User request:

> Create a market research report.

Planner:

```text
1. Identify competitors
2. Gather pricing information
3. Analyze trends
4. Write report
```

Executor:

```text
Search competitors

↓

Collect pricing

↓

Analyze data

↓

Generate report
```

---

# Planning Granularity

Plans may be:

### High-Level

```text
Research

↓

Analyze

↓

Report
```

Useful for simple workflows.

---

### Detailed

```text
Retrieve documents

↓

Extract key facts

↓

Compare findings

↓

Generate summary

↓

Validate citations
```

Useful for complex or regulated workflows.

---

# Static vs. Dynamic Planning

## Static Planning

The entire plan is created before execution begins.

Advantages:

- Predictable
- Easy to review
- Simple auditing

---

## Dynamic Planning

The plan can change during execution.

Example:

```text
Tool Failure

↓

Planner Updates Plan

↓

Continue Execution
```

Useful when information is uncertain or changing.

---

# Replanning

Execution may reveal new information.

```text
Planner

↓

Executor

↓

Unexpected Result

↓

Planner Revises Plan

↓

Continue
```

Replanning should be limited to prevent endless planning cycles.

---

# Tool Selection

The planner determines which tools are required.

Example:

```text
Research

↓

Web Search

Data Analysis

↓

Python

Report

↓

LLM
```

The executor invokes those tools.

---

# Validation

Plans should be validated before execution.

Checks may include:

- Missing steps
- Invalid dependencies
- Tool availability
- Policy compliance
- Estimated cost
- Time constraints

---

# Progress Tracking

The executor should report progress.

Example:

```text
Research

✓ Complete

Analysis

In Progress

Report

Pending
```

Progress visibility improves monitoring and recovery.

---

# Error Handling

If execution fails:

```text
Executor Failure

↓

Retry?

↓

Alternative Tool?

↓

Replan?

↓

Escalate?
```

Not every error requires a completely new plan.

---

# When to Use This Pattern

Use the Planner–Executor pattern when:

- Tasks involve multiple steps
- Tool usage requires coordination
- Plans benefit from review
- Execution may take significant time
- Cost optimization is important

Typical applications include:

- Research assistants
- Coding agents
- Workflow automation
- Travel planning
- Business analysis
- Enterprise AI assistants

---

# When Not to Use It

Avoid this pattern when:

- Tasks are trivial
- One prompt is sufficient
- Deterministic workflows already exist
- Planning adds unnecessary latency

Simple requests often do not require explicit planning.

---

# Common Failure Modes

## Overplanning

The planner generates unnecessary detail.

**Solution**

Plan only to the level required.

---

## Weak Plans

Important steps are omitted.

**Solution**

Validate plans before execution.

---

## Planner Never Stops

The planner continuously revises the plan.

**Solution**

Limit replanning attempts and define completion criteria.

---

## Executor Ignores the Plan

Execution diverges without justification.

**Solution**

Require execution logs and progress reporting.

---

## Tool Mismatch

The selected tools cannot complete the planned work.

**Solution**

Validate tool availability before execution.

---

# Human Review

High-risk plans may require approval.

```text
Planner

↓

Human Approval

↓

Executor
```

This is useful for:

- Financial transactions
- Legal workflows
- Infrastructure changes
- Customer communications

---

# No-Code Implementation

Typical workflow:

1. Receive a request.
2. Generate a plan.
3. Validate the plan.
4. Approve if required.
5. Execute each step.
6. Monitor progress.
7. Replan if necessary.
8. Return the final result.

---

# Observability

Track:

- Planning time
- Execution time
- Number of replans
- Tool success rate
- Plan completion rate
- Failed steps
- Cost
- Token usage

Monitoring helps identify inefficient planning or execution.

---

# Evaluation Metrics

Useful metrics include:

- Plan accuracy
- Task completion rate
- Replanning frequency
- Execution latency
- Tool success rate
- Cost per task
- User satisfaction

The goal is to improve execution quality while minimizing unnecessary planning.

---

# Design Checklist

Before implementing the Planner–Executor pattern, ensure that:

- Planning and execution responsibilities are separate.
- Plans contain enough detail to execute reliably.
- Tool availability is verified.
- Replanning has clear limits.
- Progress is tracked.
- High-risk plans can be reviewed.
- Failures are logged and recoverable.

---

# Trade-Offs

| Advantage | Trade-Off |
|-----------|-----------|
| Better organization | Additional planning overhead |
| Easier debugging | Increased latency |
| Better tool coordination | More orchestration logic |
| Supports review and approval | Higher implementation complexity |
| Easier replanning | More token usage |

---

# Related Patterns

- Manager–Worker
- Pipeline
- Router
- Human-in-the-Loop
- Hybrid Patterns

---

# Related Anti-Patterns

- Overplanning
- Blind Retries
- Infinite Loops
- God Agent
- Hidden State

---

# Pattern Summary

The Planner–Executor pattern separates strategic planning from execution.

The planner focuses on deciding what should be done, while the executor performs the work. This separation improves transparency, allows plans to be validated or approved before execution, and makes complex workflows easier to monitor, debug, and optimize.
