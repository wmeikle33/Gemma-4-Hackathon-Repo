 17. Agent Economics

## Introduction

Every design decision in an AI agent system has an economic impact. Agent economics is the practice of balancing **cost, latency, quality, reliability, and maintainability** to maximize the value delivered by an AI system.

A production-ready AI agent should not simply produce the best possible answer—it should produce the **best answer for an acceptable cost and response time**.

---

# 17.1 The Four Resources

Every AI system consumes four primary resources.

| Resource | Examples |
|----------|----------|
| Money | API costs, infrastructure, storage |
| Time | Latency, retries, deployment |
| Compute | CPUs, GPUs, RAM, vector search |
| Human Attention | Reviews, debugging, maintenance |

> Human time is usually the most expensive resource.

---

# 17.2 Cost Breakdown

A single user request often incurs costs across multiple components.

```text
User Request
    ↓
Routing
    ↓
LLM Calls
    ↓
Tool Calls
    ↓
Memory Retrieval
    ↓
Monitoring
    ↓
Storage
    ↓
Human Review (optional)
```

---

# 17.3 Model Selection Economics

| Model Size | Cost | Latency | Quality | Best Use |
|------------|------|---------|---------|----------|
| Small | Low | Low | Medium | Classification, extraction |
| Medium | Medium | Medium | High | General assistants |
| Large | High | High | Highest | Complex planning and reasoning |

**Guidelines**

- Start with the smallest model that meets quality requirements.
- Escalate only when confidence is low.
- Avoid using frontier models for routine tasks.

---

# 17.4 Token Economics

Large prompts increase both latency and API cost.

Sources of token usage include:

- System prompts
- User input
- Retrieved documents
- Tool outputs
- Conversation history
- Model responses

**Best Practices**

- Keep system prompts concise.
- Retrieve only relevant context.
- Summarize long conversations.
- Limit unnecessary output length.

---

# 17.5 Memory Economics

Memory improves personalization but introduces costs.

Topics to consider:

- Embedding generation
- Vector database storage
- Retrieval latency
- Memory expiration
- Memory summarization
- Memory pruning

Store only information that provides future value.

---

# 17.6 Tool Economics

Every external tool has a cost beyond API pricing.

Examples:

- Database queries
- Web search
- Email
- Calendar
- Code execution
- OCR
- External APIs

Each adds:

- latency
- maintenance
- monitoring
- authentication
- failure probability

---

# 17.7 Multi-Agent Economics

Benefits:

- Specialization
- Parallelism
- Modular design

Costs:

- Communication overhead
- Token consumption
- Coordination complexity
- Harder debugging

| Number of Agents | Coordination Cost |
|------------------|-------------------|
| 1 | Low |
| 2–3 | Low |
| 4–10 | Medium |
| 10+ | High |

Use multiple agents only when specialization outweighs coordination costs.

---

# 17.8 Retry Economics

Retries improve robustness but can waste resources.

Prefer:

- Exponential backoff
- Circuit breakers
- Fallback models
- Retry limits

Avoid blind retries of deterministic failures.

---

# 17.9 Latency Economics

Total latency is the sum of many small delays:

- Routing
- Retrieval
- LLM inference
- Tool execution
- Evaluation
- Formatting

Define latency budgets for each component.

---

# 17.10 Cache Economics

Caching reduces repeated work.

Useful caches include:

- Prompt cache
- Semantic cache
- Tool cache
- Embedding cache
- Response cache

Balance cache size with freshness.

---

# 17.11 Human Review Economics

Human review improves quality but creates bottlenecks.

Use it for:

- High-risk actions
- Legal or financial decisions
- Sensitive customer interactions

Avoid unnecessary review for low-risk automation.

---

# 17.12 Observability Economics

Monitoring itself has costs.

Examples:

- Log storage
- Dashboards
- Alerting
- Metrics collection
- Long-term retention

Collect enough data to debug problems without overwhelming storage.

---

# 17.13 Failure Economics

Failures create hidden costs:

- Customer dissatisfaction
- Lost trust
- Support tickets
- Engineering time
- Reputation damage

Preventing failures is often cheaper than recovering from them.

---

# 17.14 Scaling Economics

| Requests / Day | Primary Concern |
|----------------|-----------------|
| 100 | Development speed |
| 1,000 | API cost |
| 10,000 | Latency |
| 100,000 | Infrastructure |
| 1,000,000 | Reliability |

Architectures should evolve as scale increases.

---

# 17.15 Cost Optimization Patterns

Examples:

- Small model → confidence check → large model if necessary
- Cache → retrieve → LLM
- Parallel tool execution
- Selective memory retrieval
- Human escalation only for uncertain cases

---

# 17.16 Cost Anti-Patterns

## Everything Uses the Largest Model

Simple tasks rarely require frontier reasoning.

## Infinite Context

Long prompts increase latency and cost.

## Memory Everything

Unbounded memory eventually reduces retrieval quality.

## Blind Retries

Retrying deterministic failures wastes money.

## Tool Explosion

Too many tools increase routing complexity.

## Multi-Agent for Everything

Additional agents introduce communication overhead.

---

# 17.17 Design Principles

- Optimize total system cost, not just API cost.
- Simplicity often beats unnecessary sophistication.
- Measure before optimizing.
- Human time is expensive.
- Reliability is worth paying for.
- Remove unnecessary work before making work cheaper.

---

# 17.18 Practical Checklists

## Before Adding a New Agent

- [ ] Does it solve a distinct problem?
- [ ] Can an existing agent perform this task?
- [ ] What additional latency will it introduce?
- [ ] Is the added complexity justified?

## Before Using a Larger Model

- [ ] Have prompts been optimized?
- [ ] Could routing solve the issue?
- [ ] Could retrieval provide the missing context?
- [ ] Is the quality improvement worth the cost?

## Before Adding Memory

- [ ] What should be stored?
- [ ] How long should it be retained?
- [ ] How will stale information be removed?
- [ ] How will relevance be measured?

---

# 17.19 Key Takeaways

The most successful AI systems are not necessarily the most complex. They are the systems that deliver the greatest value for the resources they consume. Agent economics helps engineers balance quality, cost, latency, reliability, and maintainability to build scalable production-ready AI systems.
