# ReAct Pattern

## Overview

The **ReAct (Reason + Act)** pattern alternates between reasoning about a problem and taking actions to gather information or interact with external systems.

Instead of trying to solve a task entirely through internal reasoning, the AI can use tools, observe their outputs, and refine its reasoning before deciding the next action.

```text
Question
    │
    ▼
Reason
    │
    ▼
Action
    │
    ▼
Observation
    │
    ▼
Reason
    │
    ▼
Action
    │
    ▼
Final Answer
```

This iterative cycle enables AI systems to solve problems that require external information, calculations, or multiple steps.

---

# Core Idea

Rather than relying solely on the model's internal knowledge, ReAct continuously alternates between:

- Thinking
- Acting
- Observing

Each observation informs the next reasoning step.

---

# Components

## Reasoning

The agent determines:

- What information is missing
- Which tool should be used
- Whether enough evidence has been collected
- What to do next

---

## Action

The agent performs an action.

Examples include:

- Web search
- Database query
- Calculator
- Code execution
- API call
- Retrieval
- File search

---

## Observation

The action returns new information.

Examples:

- Search results
- Retrieved documents
- Calculation output
- API response
- Tool error

The observation becomes input for the next reasoning step.

---

# Basic Workflow

```text
Receive Question
      │
Reason
      │
Choose Tool
      │
Execute Tool
      │
Observe Result
      │
Need More Information?
      │
 ├── Yes
 │      │
 │      ▼
 │   Continue ReAct Loop
 │
 └── No
        │
        ▼
 Generate Final Answer
```

---

# Example

User asks:

> What is the population of the capital city of Canada?

```text
Reason

Need capital.

↓

Action

Search "Capital of Canada"

↓

Observation

Ottawa

↓

Reason

Need population.

↓

Action

Search "Ottawa population"

↓

Observation

Population found.

↓

Final Answer
```

The model never needed to memorize the answer.

---

# Tool Selection

The reasoning step determines which tool is most appropriate.

Examples:

| Goal | Tool |
|------|------|
| Find information | Search |
| Analyze data | Python |
| Retrieve documents | Vector database |
| Query records | SQL |
| Generate image | Image model |

Choosing the correct tool is often more important than choosing the largest model.

---

# Multi-Step Reasoning

Many problems require multiple cycles.

```text
Reason

↓

Action

↓

Observation

↓

Reason

↓

Action

↓

Observation

↓

Answer
```

The loop continues until the objective is complete.

---

# Stopping Conditions

The agent should stop when:

- The objective is achieved.
- Sufficient evidence exists.
- No useful actions remain.
- Maximum iterations are reached.
- Human review is required.

Clear stopping conditions prevent unnecessary loops.

---

# Error Handling

Tools may fail.

```text
Tool Failure

↓

Retry?

↓

Alternative Tool?

↓

Ask User?

↓

Stop
```

The agent should adapt rather than repeatedly calling the same failing tool.

---

# Memory

ReAct may use memory to retain:

- Previous observations
- Completed actions
- Tool outputs
- User preferences

Memory should support reasoning without causing unnecessary context growth.

---

# When to Use This Pattern

Use ReAct when:

- External information is required.
- Tool usage is necessary.
- Multi-step reasoning is expected.
- Information changes frequently.
- Interactive problem solving is valuable.

Typical applications include:

- Research assistants
- Coding assistants
- Customer support
- Enterprise search
- Travel planning
- Data analysis

---

# When Not to Use It

Avoid ReAct when:

- The task is deterministic.
- No tools are needed.
- One prompt is sufficient.
- Tool calls would increase cost without improving quality.

Simple tasks rarely benefit from iterative reasoning.

---

# Common Failure Modes

## Infinite Tool Loops

The agent repeatedly calls tools without making progress.

**Solution**

Limit iterations and detect repeated actions.

---

## Wrong Tool Selection

The agent chooses an inappropriate tool.

**Solution**

Provide clear tool descriptions and routing rules.

---

## Ignoring Observations

The agent fails to incorporate new information.

**Solution**

Require reasoning to explicitly reference observations.

---

## Tool Hallucination

The agent attempts to use tools that do not exist.

**Solution**

Restrict actions to registered tools.

---

## Excessive Reasoning

The agent spends too much time planning instead of acting.

**Solution**

Balance reasoning with execution and set iteration limits.

---

# Human Review

Escalate to a human when:

- Tool failures persist.
- High-risk actions are requested.
- Confidence remains low.
- Conflicting observations cannot be resolved.

---

# No-Code Implementation

Typical workflow:

1. Receive a request.
2. Generate the next reasoning step.
3. Select a tool.
4. Execute the tool.
5. Record the observation.
6. Decide whether another iteration is needed.
7. Return the final response.

---

# Observability

Track:

- Number of reasoning steps
- Tool calls
- Tool success rate
- Average iterations
- Total latency
- Token usage
- Cost per workflow
- Failure rate

---

# Evaluation Metrics

Useful metrics include:

- Task completion rate
- Tool selection accuracy
- Average iterations
- Cost per task
- Latency
- Tool failure rate
- User satisfaction

---

# Design Checklist

Before implementing ReAct, ensure that:

- Available tools are clearly defined.
- Reasoning informs tool selection.
- Observations are incorporated into later reasoning.
- Iteration limits exist.
- Tool failures are handled.
- Human escalation is available for exceptional cases.

---

# Trade-Offs

| Advantage | Trade-Off |
|-----------|-----------|
| Dynamic problem solving | More latency |
| Uses external knowledge | Additional tool costs |
| Handles changing information | More orchestration |
| Better factual grounding | More opportunities for failure |
| Flexible workflows | Harder debugging |

---

# Related Patterns

- Planner–Executor
- Router
- Event-Driven
- Human-in-the-Loop
- Hybrid Patterns

---

# Related Anti-Patterns

- Blind Retries
- Infinite Loops
- Hidden State
- Tool Explosion
- Overplanning

---

# Pattern Summary

The ReAct pattern alternates between reasoning and acting, allowing AI systems to gather information, use tools, and refine their understanding before producing a final answer.

It is particularly effective for tasks requiring external information or multiple steps, but it should include clear stopping conditions, robust tool handling, and observability to avoid inefficient reasoning loops
