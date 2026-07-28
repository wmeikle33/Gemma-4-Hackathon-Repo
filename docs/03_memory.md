# 03. Memory

> Memory enables AI systems to retain, retrieve, and use information beyond a single model invocation, allowing more personalized, consistent, and capable behavior.

---

# Introduction

Large language models are powerful reasoning engines, but they are **stateless** by default. Each request is processed independently unless previous information is explicitly provided.

Memory gives AI systems continuity. Instead of treating every interaction as brand new, an agent can remember relevant facts, preferences, previous actions, and long-running tasks.

This chapter explains why memory exists, the different types of memory, common architectures, design tradeoffs, and best practices for building reliable memory systems.

---

# Why Memory Exists

Language models do not automatically remember previous conversations or actions.

Without memory:

- Users repeat information.
- Long-running tasks lose context.
- Preferences are forgotten.
- Multi-session workflows become difficult.
- Personalized experiences are impossible.

Memory solves these problems by storing information outside the model and retrieving it when needed.

```text
Conversation
      ↓
Store Important Information
      ↓
Memory Store
      ↓
Future Request
      ↓
Retrieve Relevant Context
      ↓
Language Model
```

Memory is not about remembering **everything**—it is about remembering the **right things**.

---

# The Problem Memory Solves

Memory addresses several engineering challenges:

- **Context window limits** – conversations eventually exceed model limits.
- **Session continuity** – users expect the system to remember earlier interactions.
- **Personalization** – preferences should not be re-entered every session.
- **Long-running workflows** – tasks spanning hours or days require persistent state.
- **Knowledge reuse** – previously retrieved or generated information can often be reused.

---

# Evolution of Memory Systems

```text
No Memory
      ↓
Conversation History
      ↓
Session Memory
      ↓
Persistent Memory
      ↓
Semantic Memory
      ↓
Memory-Augmented Agents
```

Each stage improves the ability of AI systems to maintain useful context while balancing cost, latency, and complexity.

---

# What Is Memory?

Memory is information stored outside the language model that can be retrieved and incorporated into future reasoning.

A memory system generally includes:

- storage
- retrieval
- ranking
- updating
- expiration
- validation

---

# Types of Memory

## Why Different Memory Types Exist

Not all information should be stored the same way.

Some information is useful for only a few minutes, while other information remains valuable for months.

Choosing the correct memory type improves both performance and maintainability.

---

## Working Memory

### Why It Exists

Working memory stores information required only while completing the current task.

Examples:

- intermediate calculations
- current tool outputs
- execution state
- temporary variables

Advantages:

- simple
- fast
- automatically discarded

Tradeoffs:

- unavailable after the workflow ends

---

## Short-Term Memory

### Why It Exists

Short-term memory maintains conversational continuity during a single session.

Examples:

- previous questions
- clarification requests
- temporary goals

When to use:

- chatbots
- coding assistants
- tutoring systems

When not to use:

- long-term personalization

---

## Long-Term Memory

### Why It Exists

Some information remains valuable across multiple sessions.

Examples:

- preferred language
- communication style
- saved projects
- recurring workflows

Advantages:

- personalization
- continuity
- reduced repetition

Tradeoffs:

- requires governance
- may become outdated

---

## Episodic Memory

### Why It Exists

Stores experiences or completed interactions.

Examples:

- previous troubleshooting sessions
- completed support tickets
- prior analyses

Useful for reflecting on previous actions rather than storing general knowledge.

---

## Semantic Memory

### Why It Exists

Stores factual knowledge independent of individual conversations.

Examples:

- company policies
- product documentation
- technical references

Often implemented with embeddings and vector databases.

---

## Procedural Memory

### Why It Exists

Stores how to perform recurring tasks.

Examples:

- workflows
- tool usage patterns
- standard operating procedures

---

# Memory Lifecycle

```text
Observe
   ↓
Decide Whether to Store
   ↓
Store
   ↓
Index
   ↓
Retrieve
   ↓
Use
   ↓
Update or Expire
```

Every stage should be explicit.

---

# Memory Architecture

Typical architecture:

```text
User
  ↓
Agent
  ↓
Memory Manager
 ├── Working Memory
 ├── Session Store
 ├── Vector Database
 └── Relational Database
```

Responsibilities:

- decide what to store
- retrieve relevant memories
- remove stale information
- prevent duplicates

---

# What Should Be Stored?

Good candidates include:

- stable user preferences
- recurring project information
- important decisions
- verified facts
- task progress

Avoid storing:

- temporary prompts
- hallucinations
- secrets unless required
- duplicate information
- irrelevant conversation

---

# Retrieval Strategies

Common approaches include:

- keyword search
- vector similarity
- hybrid retrieval
- metadata filtering
- recency ranking

The goal is to retrieve the smallest amount of relevant context necessary for the task.

---

# Updating Memory

Memory should evolve over time.

Strategies include:

- overwrite outdated facts
- append new events
- summarize long histories
- merge duplicates
- archive inactive records

---

# Memory Tradeoffs

| Advantage | Tradeoff |
|-----------|----------|
| Better personalization | More storage |
| Longer context | Higher retrieval latency |
| Fewer repeated questions | Risk of stale information |
| Workflow continuity | More complex architecture |
| Better user experience | Privacy considerations |

---

# Common Failure Modes

| Failure | Cause | Mitigation |
|---------|-------|------------|
| Remembering everything | No filtering | Store only high-value information |
| Forgetting important facts | Weak retrieval | Improve ranking |
| Stale memories | No updates | Expire or refresh records |
| Duplicate memories | Poor deduplication | Merge similar entries |
| Hallucinated memory | Storing unverified outputs | Validate before saving |

---

# Memory Anti-Patterns

- Memory Everything
- Hidden State
- Never Expire Data
- Duplicate Storage
- Using Memory Instead of Retrieval
- Ignoring Privacy Requirements

---

# Design Principles

- Store intentionally.
- Retrieve minimally.
- Validate before saving.
- Separate temporary and persistent memory.
- Expire information when appropriate.
- Make memory observable and testable.

---

# Choosing the Right Memory

| Requirement | Recommended Memory |
|------------|--------------------|
| Current task | Working Memory |
| Single conversation | Short-Term Memory |
| User preferences | Long-Term Memory |
| Previous interactions | Episodic Memory |
| Reference knowledge | Semantic Memory |
| Reusable workflows | Procedural Memory |

---

# Related Chapters

- 01_agents.md
- 02_workflows.md
- 04_tools.md
- 05_routing.md
- 09_evaluation.md
- 10_monitoring.md
- 17_agent_economics.md

---

# Key Takeaways

- Memory exists because language models are stateless.
- Different memory types solve different problems.
- Good memory systems store only valuable information.
- Retrieval quality is often more important than storage size.
- Memory should be updated, validated, monitored, and expired over time.
- The best memory system is the simplest one that provides the required continuity without unnecessary complexity.
