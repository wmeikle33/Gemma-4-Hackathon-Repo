# Map–Reduce Pattern

## Overview

The **Map–Reduce pattern** divides a large task into many smaller, independent subtasks (the **Map** phase), processes those subtasks in parallel, and then combines the results into a final output (the **Reduce** phase).

Originally developed for distributed computing, Map–Reduce is equally valuable in AI systems for processing large amounts of data that exceed a model's context window or would benefit from parallel execution.

```text
Large Task
     │
     ▼
 Split into Chunks
     │
     ▼
┌───────────────┐
│   Map Phase   │
├─────┬─────┬───┤
│     │     │   │
▼     ▼     ▼   ▼
Chunk Chunk Chunk Chunk
  A     B     C     D
│     │     │     │
└─────┴─────┴─────┘
      ▼
 Reduce Phase
      ▼
 Final Result
```

The Map–Reduce pattern improves scalability, throughput, and context management.

---

# Core Idea

Instead of solving one very large problem, solve many small problems independently.

The workflow consists of two stages:

**Map**

- Divide work
- Process chunks independently

**Reduce**

- Merge results
- Remove duplication
- Produce a coherent final output

---

# Components

## Input

The original task.

Examples:

- Large document
- Dataset
- Source code
- Customer reviews
- Log files
- Research papers

---

## Map Phase

Each worker processes one chunk independently.

Possible outputs include:

- Summary
- Classification
- Extraction
- Translation
- Embeddings
- Code analysis
- Question answering

Workers should not depend on one another.

---

## Reduce Phase

The reducer combines all intermediate outputs.

Responsibilities include:

- Merging information
- Removing duplicates
- Resolving conflicts
- Organizing content
- Producing the final response

---

## Controller

The controller manages:

- Chunk creation
- Worker assignment
- Parallel execution
- Result collection
- Error handling
- Final reduction

---

# Basic Workflow

```text
Receive Task
      │
Split into Chunks
      │
Map Phase
      │
Collect Results
      │
Reduce Phase
      │
Return Final Output
```

---

# Example

Summarize a 500-page report.

```text
Report

↓

Split into 50 Sections

↓

50 Independent Summaries

↓

Combine Summaries

↓

Executive Summary
```

No worker needs to read the entire document.

---

# Chunking

Choosing good chunks is critical.

Examples:

- Chapters
- Paragraphs
- Pages
- Source files
- Database rows
- Customer reviews

Poor chunking often reduces final quality.

---

# Parallel Processing

Independent chunks can execute simultaneously.

```text
Chunk A

Chunk B

Chunk C

Chunk D

↓

Parallel Processing

↓

Intermediate Results
```

Parallel execution reduces overall latency.

---

# Reduce Strategies

Different tasks require different reduction methods.

Examples include:

### Concatenation

Simply combine outputs.

Useful for:

- Lists
- Reports

---

### Summarization

Summarize the intermediate summaries.

Useful for:

- Long documents
- Research papers

---

### Voting

Choose the most common answer.

Useful for:

- Classification
- Entity recognition

---

### Ranking

Sort results.

Useful for:

- Search
- Recommendations

---

### Aggregation

Calculate totals or statistics.

Useful for:

- Analytics
- Dashboards

---

# Multi-Level Reduction

Very large workloads may require several reduction stages.

```text
1000 Documents

↓

100 Summaries

↓

10 Meta-Summaries

↓

Final Summary
```

Hierarchical reduction scales better than combining everything at once.

---

# Example Applications

Map–Reduce works well for:

- Document summarization
- Code review
- Contract analysis
- Log analysis
- Customer feedback
- Research synthesis
- Large datasets
- Compliance reviews
- Multi-file repositories

---

# Context Window Management

Map–Reduce helps overcome context window limitations.

Instead of:

```text
Entire Repository

↓

One Prompt
```

Use:

```text
Repository

↓

Individual Files

↓

Per-File Analysis

↓

Combined Report
```

This approach enables processing datasets that exceed a model's maximum context.

---

# Error Handling

Failures should be isolated.

```text
Worker Failure

↓

Retry Chunk

↓

Continue Remaining Work
```

One failed chunk should not require restarting the entire workflow.

---

# Quality Control

Reducers should verify:

- Missing chunks
- Duplicate information
- Contradictions
- Formatting consistency
- Coverage

Quality checks improve final outputs.

---

# When to Use This Pattern

Use Map–Reduce when:

- Data is too large for one prompt
- Work can be divided independently
- Parallel execution is beneficial
- Large document collections exist
- Multiple files require processing

Typical applications include:

- Enterprise search
- Knowledge management
- Code analysis
- Research assistants
- Document intelligence

---

# When Not to Use It

Avoid this pattern when:

- Tasks are very small
- Chunks depend heavily on each other
- Sequential reasoning is required
- Global context is essential

Some problems cannot be divided effectively.

---

# Common Failure Modes

## Poor Chunking

Chunks break logical boundaries.

**Solution**

Split by meaningful semantic units.

---

## Context Loss

Important information spans multiple chunks.

**Solution**

Use overlapping chunks or hierarchical processing.

---

## Weak Reduction

The reducer simply concatenates results.

**Solution**

Require synthesis rather than aggregation alone.

---

## Duplicate Information

Multiple chunks report the same facts.

**Solution**

Deduplicate during reduction.

---

## Missing Chunks

Some chunks are never processed.

**Solution**

Track chunk completion.

---

# Chunk Size Trade-Off

Small chunks:

- Better parallelism
- Lower context usage
- More reduction work

Large chunks:

- Better context
- Fewer workers
- Higher token usage

The optimal chunk size depends on the task.

---

# No-Code Implementation

Typical workflow:

1. Receive a document.
2. Split into chunks.
3. Send chunks to workers.
4. Process chunks in parallel.
5. Collect outputs.
6. Run the reducer.
7. Validate the final result.
8. Return the response.

---

# Observability

Track:

- Number of chunks
- Chunk size
- Processing time
- Worker failures
- Retry count
- Reduction time
- Total latency
- Token usage

These metrics help optimize scalability.

---

# Evaluation Metrics

Useful metrics include:

- Processing throughput
- Total latency
- Cost per document
- Chunk success rate
- Reduction quality
- Coverage
- Duplicate rate
- User satisfaction

---

# Design Checklist

Before implementing Map–Reduce, ensure that:

- Chunks are independent.
- Chunk sizes are appropriate.
- Parallel execution is beneficial.
- The reducer performs synthesis.
- Missing chunks are detected.
- Duplicate information is removed.
- Failures are isolated.
- Metrics are collected.

---

# Trade-Offs

| Advantage | Trade-Off |
|-----------|-----------|
| Handles very large datasets | Requires orchestration |
| Parallel execution | Reduction complexity |
| Better scalability | Potential context loss |
| Lower context requirements | More workflow stages |
| Improved throughput | Additional aggregation logic |

---

# Related Patterns

- Pipeline
- Manager–Worker
- Router
- Event-Driven
- Hybrid Patterns

---

# Related Anti-Patterns

- Overplanning
- Tool Explosion
- Too Many Agents
- Hidden State
- Infinite Loops

---

# Pattern Summary

The Map–Reduce pattern processes large tasks by dividing them into independent chunks, executing those chunks in parallel, and combining the results into a coherent final output.

It is one of the most effective patterns for overcoming context window limitations, improving scalability, and processing large document collections. Success depends on meaningful chunking, effective reduction, and careful quality control.
