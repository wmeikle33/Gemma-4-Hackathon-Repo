# AI Agent Design Patterns

This section documents the most common architectural patterns used to build AI agents and multi-agent systems.

Rather than focusing on a specific framework, these patterns describe reusable approaches that can be implemented in any no-code platform, orchestration engine, or programming language.

---

## What Is a Design Pattern?

A design pattern is a reusable solution to a recurring architectural problem.

Patterns describe:

- how components interact
- when to use an approach
- common trade-offs
- failure modes
- implementation ideas

Patterns are building blocks rather than complete systems.

---

# Learning Path

If you're new to AI agents, read these patterns in roughly this order.

## Beginner

1. ReAct
2. Retrieval Pipeline
3. Human-in-the-Loop
4. Reflection

These patterns introduce the core concepts behind modern AI agents.

---

## Intermediate

5. Planner–Executor
6. Router–Worker
7. Manager–Worker
8. Workflow DAG
9. Event-Driven

These patterns focus on orchestrating increasingly complex systems.

---

## Advanced

10. Tree Search
11. Debate
12. Generator–Critic
13. Map–Reduce
14. Hybrid Patterns

These patterns improve reasoning quality, scalability, and robustness.

---

# Pattern Categories

## Reasoning

- ReAct
- Reflection
- Debate
- Tree Search
- Generator–Critic

These patterns improve an agent's reasoning process.

---

## Workflow Orchestration

- Workflow DAG
- Planner–Executor
- Manager–Worker
- Router–Worker
- Event-Driven

These patterns coordinate work between multiple tasks or agents.

---

## Knowledge

- Retrieval Pipeline

These patterns improve information retrieval and grounding.

---

## Human Collaboration

- Human-in-the-Loop

These patterns introduce human oversight where appropriate.

---

## Parallelism

- Map–Reduce

These patterns divide work into parallel tasks.

---

## Hybrid Systems

- Hybrid Patterns

These patterns combine multiple architectural approaches.

---

# Choosing a Pattern

| If you need... | Use |
|---------------|-----|
| Tool use during reasoning | ReAct |
| Better answers through self-review | Reflection |
| Multiple viewpoints | Debate |
| Explore many possible solutions | Tree Search |
| External knowledge | Retrieval Pipeline |
| Human approval | Human-in-the-Loop |
| Task planning | Planner–Executor |
| Route requests to specialists | Router–Worker |
| Coordinate multiple workers | Manager–Worker |
| Explicit workflow dependencies | Workflow DAG |
| Event-triggered execution | Event-Driven |
| Parallel processing | Map–Reduce |
| Multiple combined approaches | Hybrid Patterns |

---

# Comparison Matrix

| Pattern | Single Agent | Multi-Agent | Parallel | Planning | Search | Human Review |
|----------|--------------|-------------|----------|----------|--------|--------------|
| ReAct | ✓ | | | | | |
| Reflection | ✓ | | | | | |
| Debate | | ✓ | ✓ | | | |
| Generator–Critic | ✓ | ✓ | | | | |
| Retrieval Pipeline | ✓ | ✓ | | | | |
| Human-in-the-Loop | ✓ | ✓ | | | | ✓ |
| Planner–Executor | | ✓ | | ✓ | | |
| Router–Worker | | ✓ | | | | |
| Manager–Worker | | ✓ | ✓ | ✓ | | |
| Workflow DAG | ✓ | ✓ | ✓ | | | |
| Event-Driven | ✓ | ✓ | ✓ | | | |
| Map–Reduce | | ✓ | ✓ | | | |
| Tree Search | ✓ | ✓ | | ✓ | ✓ | |
| Hybrid Patterns | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

---

# Pattern Relationships

```text
                     Hybrid Patterns
                            │
        ┌───────────────────┼────────────────────┐
        │                   │                    │
        ▼                   ▼                    ▼
     ReAct          Planner–Executor      Workflow DAG
        │                   │                    │
        ▼                   ▼                    ▼
   Reflection        Manager–Worker      Event-Driven
        │                   │
        ▼                   ▼
 Generator–Critic    Router–Worker

Retrieval Pipeline
        │
        ▼
Human-in-the-Loop
```

Many production systems combine several of these patterns.

For example:

- ReAct + Retrieval Pipeline
- Planner–Executor + Manager–Worker
- Workflow DAG + Human-in-the-Loop
- Router–Worker + Retrieval Pipeline

---

# How to Read Each Pattern

Each pattern follows the same structure:

1. Overview
2. Core Idea
3. Components
4. Workflow
5. Example
6. When to Use
7. When Not to Use
8. Failure Modes
9. No-Code Implementation
10. Observability
11. Evaluation
12. Trade-Offs
13. Related Patterns
14. Related Anti-Patterns

This consistent format makes it easier to compare patterns.

---

# Design Principles

Throughout this repository, the following principles are emphasized:

- Prefer simple architectures first.
- Make state explicit.
- Separate responsibilities.
- Minimize unnecessary agents.
- Keep workflows observable.
- Validate important outputs.
- Limit retries.
- Design for recovery.
- Use humans where automation is unsafe.

---

# Common Misconceptions

- More agents are not always better.
- A workflow is not the same as a reasoning process.
- Retrieval is not reasoning.
- Reflection is not Debate.
- Planner–Executor is not Manager–Worker.
- Router–Worker is not Tool Routing.
- Workflow DAGs do not replace ReAct.
- Dynamic systems still require guardrails.

---

# Related Documentation

- Workflows
- Routing
- Tools
- Memory
- Prompts
- Guardrails
- Human Review
- Evaluation
- Monitoring

These documents explain the individual building blocks that can be combined into the design patterns described here.

---

# Contributing

When adding a new pattern:

- Explain the architectural problem it solves.
- Describe the core components.
- Include an example workflow.
- Document failure modes.
- Explain trade-offs.
- Compare it with similar patterns.
- Reference related patterns and anti-patterns.
