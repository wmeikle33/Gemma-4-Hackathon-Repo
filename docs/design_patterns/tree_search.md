# Tree Search Pattern

## Overview

The **Tree Search pattern** explores multiple possible solution paths before selecting a final answer or action.

Instead of committing immediately to the first generated solution, the system creates several candidate states, evaluates them, expands promising candidates, and abandons weak paths.

```text
                         Initial Task
                              │
                 ┌────────────┼────────────┐
                 ▼            ▼            ▼
              Path A       Path B       Path C
                │            │            │
          ┌─────┴─────┐      │       ┌────┴────┐
          ▼           ▼      ▼       ▼         ▼
        A1            A2    B1      C1          C2
          │                 │
          ▼                 ▼
      Candidate         Candidate
       Solution          Solution
```

The search continues until the system finds a satisfactory solution, exhausts its search budget, or reaches another stopping condition.

---

# Core Idea

Do not assume that the first reasoning path is the best one.

Instead:

1. Generate several possible next steps.
2. Evaluate those possibilities.
3. Expand the most promising paths.
4. Prune weak or invalid paths.
5. Backtrack when necessary.
6. Select the strongest final solution.

This approach trades additional computation for more deliberate exploration.

---

# Why Tree Search?

A linear agent normally follows one trajectory:

```text
Task

↓

Step 1

↓

Step 2

↓

Step 3

↓

Answer
```

If an early step is wrong, every later step may inherit that mistake.

Tree search maintains alternatives:

```text
Task
  │
  ├── Approach A
  │      ├── A1
  │      └── A2
  │
  ├── Approach B
  │      ├── B1
  │      └── B2
  │
  └── Approach C
         ├── C1
         └── C2
```

The system can compare approaches before committing to one.

---

# Components

## Root Node

The root represents the original task or starting state.

Example:

```text
Plan a product launch strategy.
```

Every search path begins from this state.

---

## Node

A node represents an intermediate state.

Depending on the application, a node may contain:

- A partial solution
- A reasoning step
- A plan
- A tool result
- An environment state
- A draft
- A sequence of actions
- Accumulated evidence
- A score
- A history of previous steps

Example:

```json
{
  "state_id": "node_12",
  "parent_id": "node_4",
  "depth": 3,
  "content": "Target small business customers first.",
  "score": 0.82,
  "status": "open"
}
```

---

## Branch

A branch represents a possible transition from one state to another.

Example:

```text
Current Plan

├── Focus on enterprise customers
├── Focus on small businesses
└── Focus on individual consumers
```

Each branch creates a new candidate path.

---

## Expansion

Expansion generates possible next states from a selected node.

Example:

```text
Selected Node

↓

Generate Three Possible Next Steps

↓

Create Three Child Nodes
```

The number of children generated is called the **branching factor**.

---

## Evaluator

The evaluator estimates how promising each node is.

Evaluation criteria may include:

- Correctness
- Relevance
- Feasibility
- Completeness
- Expected reward
- Risk
- Cost
- Progress toward the goal
- Policy compliance
- Evidence quality

Example output:

```json
{
  "node_id": "node_12",
  "score": 0.82,
  "valid": true,
  "reason": "The approach is feasible and supported by the available evidence."
}
```

---

## Search Controller

The controller manages the search process.

Responsibilities include:

- Selecting nodes to expand
- Enforcing depth limits
- Tracking visited states
- Managing the search budget
- Pruning weak paths
- Detecting completion
- Handling tool failures
- Selecting the final result

---

## Terminal Node

A terminal node represents a completed, failed, or abandoned path.

Examples include:

- A valid final answer
- A completed plan
- A solved problem
- An invalid state
- A policy violation
- A path exceeding its budget
- A state with no useful next action

---

# Basic Workflow

```text
Receive Task
      │
Create Root Node
      │
Generate Candidate Branches
      │
Evaluate Candidates
      │
Select Promising Node
      │
Expand Node
      │
Goal Reached?
      │
 ├── No → Continue Search
 └── Yes
        │
        ▼
 Select Final Solution
```

---

# Example

Suppose an agent must determine the best way to reduce customer churn.

The initial branches might be:

```text
Reduce Customer Churn
        │
        ├── Improve onboarding
        ├── Change pricing
        ├── Improve customer support
        └── Add retention incentives
```

The system evaluates each approach.

```text
Improve onboarding:          0.78
Change pricing:              0.54
Improve customer support:    0.85
Add retention incentives:    0.69
```

The system expands the strongest path:

```text
Improve Customer Support
        │
        ├── Reduce response time
        ├── Add proactive outreach
        └── Improve agent training
```

After further evaluation, it may select:

```text
Improve customer support

↓

Reduce response time

↓

Introduce priority-based ticket routing
```

---

# Search Strategies

## Breadth-First Search

Breadth-first search explores every candidate at the current depth before moving deeper.

```text
Depth 0:        Root

Depth 1:     A    B    C

Depth 2:   A1 A2 B1 B2 C1 C2
```

Advantages:

- Explores alternatives evenly
- Can find shallow solutions
- Reduces early commitment

Trade-offs:

- High memory usage
- Expensive when branching is large
- May spend resources on weak paths

Use breadth-first search when good solutions are likely to be relatively shallow.

---

## Depth-First Search

Depth-first search follows one path deeply before exploring alternatives.

```text
Root

↓

A

↓

A1

↓

A1a
```

If the path fails, the system backtracks.

Advantages:

- Lower memory requirements
- Can reach deep solutions quickly
- Simple to implement

Trade-offs:

- May pursue a poor path for too long
- Sensitive to branch ordering
- Can miss better alternatives

Use depth-first search when search depth is important and branching is limited.

---

## Best-First Search

Best-first search expands the candidate with the strongest evaluation score.

```text
Open Nodes:

A: 0.61
B: 0.88  ← Expand
C: 0.72
```

Advantages:

- Focuses computation on promising paths
- Often more efficient than uniform exploration
- Supports task-specific scoring

Trade-offs:

- Depends heavily on evaluator quality
- May prematurely favor an incorrect path
- Can neglect diverse alternatives

---

## Beam Search

Beam search keeps only the best `k` candidates at each depth.

Example with beam width 2:

```text
Generated Candidates:

A: 0.91
B: 0.83
C: 0.65
D: 0.42

Keep:

A
B
```

Advantages:

- Controls computational growth
- Maintains multiple alternatives
- Easier to budget than unrestricted search

Trade-offs:

- May prune the eventual best solution
- Quality depends on beam width
- Similar candidates may reduce diversity

---

## Monte Carlo Tree Search

Monte Carlo Tree Search repeatedly:

1. Selects a promising node.
2. Expands the node.
3. Simulates or estimates an outcome.
4. Propagates the result back through the tree.

```text
Selection

↓

Expansion

↓

Simulation or Evaluation

↓

Backpropagation
```

It balances:

- **Exploitation:** expanding paths that already look strong
- **Exploration:** testing paths that have received less attention

This approach can be valuable for interactive environments, planning, games, and agent workflows with external feedback.

---

# Tree of Thoughts

**Tree of Thoughts** applies tree search to intermediate reasoning states.

Instead of generating only one chain of reasoning, the model generates multiple possible thoughts at each stage.

```text
Problem
  │
  ├── Thought A
  │      ├── Thought A1
  │      └── Thought A2
  │
  ├── Thought B
  │      ├── Thought B1
  │      └── Thought B2
  │
  └── Thought C
```

The system evaluates these thoughts and continues exploring the most promising ones.

A thought should be a meaningful intermediate unit, such as:

- A proposed subgoal
- A partial plan
- A possible explanation
- A mathematical transformation
- A draft section
- A candidate decision

Tree of Thoughts is one application of the broader Tree Search pattern.

---

# Agent Tree Search

In an agent system, nodes may represent complete action–observation states.

```text
Current State
      │
      ├── Search Documents
      │       │
      │       └── Observation A
      │
      ├── Query Database
      │       │
      │       └── Observation B
      │
      └── Ask User
              │
              └── Observation C
```

The search process may evaluate not only reasoning but also:

- Tool selection
- Tool results
- Environmental feedback
- Progress toward the task
- Cost incurred
- Safety constraints
- Recoverability

This allows an agent to explore multiple possible action trajectories before selecting one.

---

# State Representation

Each node should contain enough information to evaluate and continue the path.

Possible fields include:

```json
{
  "node_id": "node_18",
  "parent_id": "node_7",
  "depth": 4,
  "task": "Investigate the failed payment.",
  "actions": [
    "retrieve_customer",
    "retrieve_invoice",
    "check_payment_status"
  ],
  "observations": [
    "Customer found",
    "Invoice found",
    "Payment declined"
  ],
  "candidate_next_step": "Check decline reason",
  "score": 0.86,
  "cost": 0.12,
  "status": "open"
}
```

State should be explicit rather than hidden inside an unstructured conversation history.

---

# Candidate Generation

Candidate quality strongly affects search quality.

Possible generation strategies include:

- Ask one model for several distinct options
- Use different models
- Use different prompts or personas
- Sample with different generation settings
- Generate rule-based actions
- Retrieve possible actions from a registry
- Combine model suggestions with deterministic options

Candidates should be meaningfully different.

Poor:

```text
1. Research the issue.
2. Look into the issue.
3. Investigate the issue.
```

Better:

```text
1. Search internal documentation.
2. Query transaction records.
3. Ask the customer for the error message.
```

---

# Branching Factor

The **branching factor** is the number of child nodes generated from each state.

A larger branching factor provides:

- More diversity
- Better exploration
- A greater chance of discovering unusual solutions

It also creates:

- More model calls
- Greater latency
- Higher cost
- More evaluation work
- Faster tree growth

Example:

```text
Branching factor: 2
Depth: 4

Maximum nodes:

1 + 2 + 4 + 8 + 16 = 31
```

Even modest branching factors can create large search spaces.

---

# Search Depth

Search depth represents the number of transitions from the root.

Greater depth may support:

- Longer plans
- More complex reasoning
- Additional tool interactions
- Better long-term outcomes

However, deeper searches increase:

- Cost
- Latency
- Error propagation
- State-management complexity
- Risk of loops

Depth should be limited according to task complexity.

---

# Node Evaluation

Nodes can be evaluated using several methods.

## Model-Based Evaluation

An LLM scores the candidate.

Example:

```text
Evaluate this candidate from 0 to 1 based on:

- correctness
- feasibility
- progress
- evidence
```

Advantages:

- Flexible
- Handles qualitative criteria
- Easy to adapt

Limitations:

- May be inconsistent
- Can favor its own outputs
- Adds model cost

---

## Rule-Based Evaluation

Deterministic rules validate the state.

Examples:

- Required fields exist
- Mathematical constraints are satisfied
- Tool call succeeded
- Output matches a schema
- No policy violation occurred

Rules are preferable when correctness can be checked deterministically.

---

## Tool-Based Evaluation

External tools evaluate the candidate.

Examples:

- Run generated code against tests
- Validate a query
- Check a calculation
- Test a workflow in a sandbox
- Verify a URL or citation
- Query the real environment

Tool feedback is often more reliable than model self-evaluation.

---

## Human Evaluation

A human may score or select candidate paths.

This is useful when:

- The decision is high risk
- Values or preferences are subjective
- Automated scoring is unreliable
- Accountability is required

---

## Hybrid Evaluation

Production systems may combine several signals.

Example:

```text
Final Score =
  40% task progress
+ 25% deterministic validation
+ 20% evidence quality
+ 10% cost efficiency
+  5% model confidence
```

Weights should be tested rather than chosen arbitrarily.

---

# Value Function

A value function estimates the expected usefulness of a state.

Conceptually:

```text
Value(node) = expected likelihood of reaching a good final outcome
```

Possible factors include:

- Distance from the goal
- Number of completed requirements
- Validity
- Evidence quality
- Estimated future cost
- Risk
- Remaining search depth

A weak value function may direct the search toward convincing but incorrect paths.

---

# Path Scoring

The system may score an entire path rather than only its latest node.

Example:

```text
Path Score =
  Current Node Quality
- Accumulated Cost
- Risk Penalty
- Repetition Penalty
+ Evidence Coverage
```

This prevents a path with one strong-looking node from hiding a poor history.

---

# Pruning

Pruning removes paths that are unlikely to succeed.

Candidates may be pruned when:

- Their scores fall below a threshold
- They violate constraints
- They duplicate another state
- They exceed the cost budget
- They repeat previous actions
- They fail deterministic validation
- They cannot reach the objective
- A stronger path dominates them

```text
Candidate Paths
      │
      ├── Strong → Keep
      ├── Moderate → Consider
      └── Weak → Prune
```

Pruning controls search growth but may remove an initially weak path that would later become successful.

---

# Backtracking

Backtracking returns to an earlier state after a path fails.

```text
Root

↓

Path A

↓

Path A1

↓

Failure

↓

Backtrack to Path A

↓

Try Path A2
```

Backtracking is useful when:

- A tool returns an unexpected result
- A proposed plan proves infeasible
- A required condition cannot be satisfied
- A branch enters a repeated state
- New evidence contradicts the path

Without backtracking, the system may remain committed to an early mistake.

---

# Duplicate-State Detection

Different paths may reach equivalent states.

Example:

```text
Path A → Search → Retrieve Document X

Path B → Database Query → Retrieve Document X
```

The controller should detect equivalent states when possible.

Duplicate detection reduces:

- Repeated tool calls
- Search cost
- Redundant evaluation
- Infinite cycles

Possible identifiers include:

- Normalized state hashes
- Tool-call histories
- Semantic similarity
- Environment state IDs
- Completed-subgoal sets

---

# Search Budget

Tree search must operate within explicit limits.

Possible budgets include:

- Maximum nodes
- Maximum depth
- Maximum model calls
- Maximum tool calls
- Maximum tokens
- Maximum cost
- Maximum elapsed time
- Maximum failed branches

Example:

```json
{
  "max_depth": 5,
  "max_nodes": 30,
  "max_tool_calls": 12,
  "max_retries_per_node": 1
}
```

Search should return the best available result when the budget is exhausted.

---

# Stopping Conditions

Stop the search when:

- A valid solution is found.
- A target score is reached.
- Deterministic validation succeeds.
- No open nodes remain.
- The search budget is exhausted.
- Further exploration is unlikely to add value.
- A human decision is required.
- A safety boundary is reached.

Clear stopping rules prevent uncontrolled test-time computation.

---

# Final Selection

The highest-scoring node is not always automatically the best final answer.

Final selection may include:

- Deterministic validation
- Comparison of complete paths
- A separate judge
- Consensus among evaluators
- Human approval
- Cost-adjusted scoring
- Evidence verification

Example:

```text
Top Three Completed Paths

↓

Final Judge

↓

Selected Solution
```

The final output should be generated from the selected path rather than from unrelated discarded branches.

---

# Reflection and Search

Reflection can improve a tree-search process.

A failed or weak path can produce feedback such as:

```text
This path failed because the selected data source did not contain current pricing.
```

That reflection can guide future expansion:

```text
Failed Path

↓

Reflect on Failure

↓

Generate Better Alternatives

↓

Continue Search
```

Reflection should inform the search rather than create an unlimited revision loop.

---

# Tool Use

Tree-search agents may call tools while exploring branches.

Example:

```text
Current State
      │
      ├── Search Web
      ├── Query Database
      ├── Run Calculation
      └── Ask User
```

Tool calls require special care because they may:

- Have financial cost
- Modify external systems
- Reveal sensitive information
- Produce irreversible actions
- Change the environment for other branches

Read-only tools are much easier to explore safely than write-capable tools.

---

# Simulated vs. Real Actions

Some actions can be simulated before execution.

```text
Candidate Action

↓

Simulate Outcome

↓

Evaluate

↓

Execute Selected Action
```

For example:

- Draft an email without sending it
- Preview a database update
- Test code in a sandbox
- Estimate a transaction
- Model a scheduling change

Irreversible actions should generally not be executed independently across several speculative branches.

---

# Environment Changes

In interactive environments, one branch may change the state of the real system.

Example:

```text
Branch A → Deletes a record

Branch B → Assumes the record still exists
```

Possible solutions include:

- Use isolated environments
- Simulate actions
- Restrict exploration to read-only tools
- Clone environment state
- Require approval before write actions
- Commit only the selected branch

Tree search is safest when speculative actions do not modify shared production state.

---

# Human-in-the-Loop

Human review may occur at several stages.

## Before Search

A human approves:

- The objective
- Search budget
- Available tools
- Constraints

## During Search

A human resolves:

- Ambiguous goals
- High-risk branches
- Conflicting candidates
- Missing information

## Before Final Action

A human approves the selected path before an external action is performed.

```text
Search Candidates

↓

Select Best Path

↓

Human Approval

↓

Execute
```

---

# When to Use This Pattern

Use Tree Search when:

- Several plausible solution paths exist
- Early choices strongly affect later outcomes
- Backtracking is valuable
- Candidate states can be evaluated
- The task requires planning or strategic lookahead
- The first generated answer is often unreliable
- Additional computation is justified by higher expected quality
- External feedback can distinguish strong and weak paths

Typical applications include:

- Complex planning
- Mathematical reasoning
- Code generation and debugging
- Interactive web tasks
- Strategic decision support
- Constraint satisfaction
- Game-playing systems
- Multi-step research
- Workflow optimization
- Tool-using agents

---

# When Not to Use It

Avoid Tree Search when:

- The task is simple
- A deterministic algorithm already exists
- One tool call is sufficient
- Candidate states cannot be evaluated meaningfully
- Latency is critical
- The cost of exploration exceeds the value of improvement
- Actions are irreversible and cannot be simulated
- Global search is unnecessary
- A fixed pipeline already solves the task reliably

Tree search should not replace conventional algorithms merely because an LLM is available.

---

# Common Failure Modes

## Search Explosion

The number of nodes grows too quickly.

```text
Branching factor: 5
Depth: 6

Potential nodes: thousands
```

**Solution**

Use beam limits, pruning, depth limits, and strict budgets.

---

## Weak Evaluator

The evaluator gives high scores to convincing but incorrect candidates.

**Solution**

Combine model scoring with deterministic tests, tools, evidence, or human review.

---

## Premature Pruning

A path is removed before its value becomes clear.

**Solution**

Preserve some candidate diversity and avoid excessively narrow beams.

---

## No Meaningful Diversity

Generated branches are nearly identical.

**Solution**

Require distinct strategies, actions, assumptions, or information sources.

---

## Repeated States

The search revisits the same state through different paths.

**Solution**

Track visited states and detect semantic duplicates.

---

## Infinite Backtracking

The system repeatedly explores and abandons similar branches.

**Solution**

Track failed approaches and enforce node, depth, and reroute limits.

---

## Cost-Blind Search

The system explores every possible branch regardless of expense.

**Solution**

Include model, tool, token, and latency costs in node scoring and search budgets.

---

## Irreversible Exploration

Multiple branches perform real-world actions.

**Solution**

Simulate, sandbox, draft, or require human approval before committing actions.

---

## Hidden Search State

The controller does not record which nodes were explored or why they were pruned.

**Solution**

Maintain explicit node, edge, score, action, and evaluation records.

---

## Evaluator Confirmation Bias

The same model generates and evaluates its own candidates.

**Solution**

Use independent evaluators, deterministic validation, tools, or multiple evaluation methods.

---

## Reward Hacking

Candidates optimize for the scoring rubric rather than the true objective.

**Solution**

Evaluate end-to-end outcomes and audit whether scores correlate with real success.

---

## Search Without a Goal Test

The system explores indefinitely because completion is poorly defined.

**Solution**

Specify measurable terminal conditions before starting the search.

---

# No-Code Implementation

A no-code Tree Search workflow may use:

1. A trigger containing the original task.
2. A data table to store nodes.
3. A generation step that creates candidate branches.
4. A loop that processes open nodes.
5. An evaluator that scores each candidate.
6. Conditional logic that prunes weak candidates.
7. A queue that selects the next node.
8. A stopping-condition check.
9. A final-selection step.
10. Logging and human approval where necessary.

Example:

```text
Task Trigger
      │
      ▼
Create Root Record
      │
      ▼
Generate Candidates
      │
      ▼
Store Candidate Records
      │
      ▼
Score Candidates
      │
      ▼
Keep Top Candidates
      │
      ▼
Goal Reached?
  ├── No → Expand Again
  └── Yes → Select Result
```

Possible no-code building blocks include:

- Loop or iterator nodes
- Conditional branches
- Tables or databases
- Subworkflows
- Structured LLM outputs
- Approval steps
- Counters
- Queue records
- Webhook triggers

For simpler workflows, beam search is usually easier to implement than unrestricted tree search.

---

# Observability

Track the search process at both node and workflow level.

## Node-Level Metrics

- Node ID
- Parent node
- Depth
- Candidate content
- Evaluation score
- Expansion status
- Tool calls
- Token usage
- Cost
- Pruning reason
- Completion status

## Workflow-Level Metrics

- Total nodes generated
- Nodes expanded
- Nodes pruned
- Maximum depth
- Average branching factor
- Completed paths
- Search duration
- Total model calls
- Total tool calls
- Total cost
- Final path score
- Task success

A visual tree trace can make debugging substantially easier.

---

# Evaluation Metrics

Useful metrics include:

- Task completion rate
- Final-answer accuracy
- Search success rate
- Nodes explored per task
- Average search depth
- Branching factor
- Pruning rate
- Backtracking rate
- Evaluator accuracy
- Cost per successful task
- Latency
- Tool-call efficiency
- Improvement over a single-path baseline

Tree search should be compared against a simpler baseline.

For example:

```text
Single-Pass Agent

vs.

ReAct Agent

vs.

Tree-Search Agent
```

The additional complexity is justified only when it produces meaningful improvements.

---

# Tree Search vs. Chain of Thought

| Tree Search | Chain of Thought |
|---|---|
| Explores multiple paths | Follows one reasoning path |
| Supports backtracking | Usually does not backtrack |
| Evaluates intermediate candidates | Usually generates steps sequentially |
| Requires search control | Requires less orchestration |
| Higher cost and latency | Lower cost and latency |
| Better for ambiguous solution spaces | Better for straightforward reasoning |

Tree search is useful when choosing the wrong early step could derail the entire solution.

---

# Tree Search vs. ReAct

| Tree Search | ReAct |
|---|---|
| Maintains multiple candidate trajectories | Usually follows one action trajectory |
| Can revisit earlier states | Continues from the latest observation |
| Explicitly scores and prunes branches | Selects the next action iteratively |
| Uses greater test-time computation | Usually uses fewer simultaneous alternatives |
| Best when several paths deserve exploration | Best when each next step depends on new observations |

The patterns can be combined:

```text
Tree Search

↓

Each Branch Uses ReAct

↓

Compare Action Trajectories
```

---

# Tree Search vs. Planner–Executor

| Tree Search | Planner–Executor |
|---|---|
| Explores several possible plans | Usually creates one primary plan |
| Supports branching and backtracking | Revises the plan when necessary |
| Evaluates competing paths | Executes an approved sequence |
| Higher search cost | More predictable cost |
| Best for uncertain solution spaces | Best for structured multi-step work |

Use Planner–Executor when a reasonable plan can be created upfront.

Use Tree Search when several plans must be compared before committing.

---

# Tree Search vs. Debate

| Tree Search | Debate |
|---|---|
| Explores candidate paths | Compares competing arguments |
| Maintains parent–child states | Maintains participant positions |
| Expands promising candidates | Agents challenge one another |
| Uses a search strategy | Uses interaction and judging |
| Best for planning and exploration | Best for competing interpretations |

Debate may evaluate viewpoints, while Tree Search explores possible trajectories.

---

# Tree Search vs. Reflection

| Tree Search | Reflection |
|---|---|
| Explores multiple alternatives | Revises one existing output |
| Maintains a structured search space | Usually uses a linear revision loop |
| Supports pruning and backtracking | Identifies weaknesses and improves |
| More expensive | Lighter-weight |
| Best for path-dependent problems | Best for improving a draft |

Reflection may also be used inside each tree-search node.

---

# Tree Search vs. Manager–Worker

| Tree Search | Manager–Worker |
|---|---|
| Explores alternative states | Delegates defined subtasks |
| Branches represent possible paths | Workers represent responsibilities |
| Selects the best trajectory | Combines completed work |
| May discard most branches | Usually expects useful worker outputs |
| Best for uncertainty and exploration | Best for decomposition and coordination |

A Manager–Worker system can execute a selected tree-search plan, but the patterns solve different architectural problems.

---

# Tree Search vs. Map–Reduce

| Tree Search | Map–Reduce |
|---|---|
| Explores competing possibilities | Processes independent data partitions |
| Branches may be discarded | Mapped outputs are normally retained |
| Paths may depend on previous states | Map operations are usually independent |
| Uses evaluation and pruning | Uses aggregation or synthesis |
| Best for planning and reasoning | Best for large-scale parallel processing |

Tree Search partitions the **solution space**.

Map–Reduce partitions the **input data**.

---

# Security and Safety

Tree search may increase risk because it explores more actions than a single-path system.

Important controls include:

- Read-only exploration by default
- Least-privilege tool access
- Sandboxed execution
- Action simulation
- Sensitive-data filtering
- Human approval for irreversible actions
- Per-branch cost limits
- Audit logs
- Environment isolation
- Policy checks before expansion

An unsafe candidate should be rejected before it becomes an executable branch.

---

# Cost and Latency

Tree search can be substantially more expensive than a linear workflow.

Approximate total cost depends on:

```text
Nodes Generated
×
Generation Cost
+
Nodes Evaluated
×
Evaluation Cost
+
Tool Calls
+
Final Synthesis
```

Cost can be controlled through:

- Smaller models for candidate generation
- Rule-based pruning
- Caching
- Narrow beam widths
- Shallow depth limits
- Early stopping
- Selective tool use
- More capable models only for final evaluation

The objective is not to explore the largest possible tree.

The objective is to spend additional computation only where it increases the probability of success.

---

# Design Checklist

Before implementing Tree Search, ensure that:

- The task genuinely benefits from exploring alternatives.
- Nodes have an explicit state representation.
- Candidate branches are meaningfully different.
- A reliable evaluation method exists.
- Branching factor and depth are limited.
- Search budgets are explicit.
- Duplicate states are detected.
- Weak paths can be pruned.
- Backtracking is supported where useful.
- Terminal conditions are measurable.
- Tool actions are safe to explore.
- Irreversible actions require approval.
- Search traces are observable.
- Cost and latency are measured.
- Performance is compared with a simpler baseline.

---

# Trade-Offs

| Advantage | Trade-Off |
|---|---|
| Explores multiple solutions | Higher model and tool cost |
| Reduces early commitment | Increased latency |
| Supports backtracking | More state management |
| Can improve difficult reasoning | Evaluator quality becomes critical |
| Uses environmental feedback | Greater orchestration complexity |
| Handles uncertain planning | Search space may grow rapidly |
| Provides alternative candidates | Requires strict stopping conditions |

---

# Related Patterns

- ReAct
- Reflection
- Planner–Executor
- Manager–Worker
- Generator–Critic
- Debate
- Map–Reduce
- Human-in-the-Loop
- Hybrid Patterns

---

# Related Anti-Patterns

- Infinite Loops
- Overplanning
- Blind Retries
- Hidden State
- Model Overkill
- Too Many Agents
- Tool Explosion
- Premature Multi-Agent

---

# Pattern Summary

The Tree Search pattern explores multiple possible reasoning, planning, or action paths before selecting a final solution.

Each node represents an intermediate state, while branches represent possible next steps. A search controller generates candidates, evaluates their expected value, expands promising paths, prunes weak ones, and backtracks when necessary.

Tree search is most valuable when early decisions strongly influence later outcomes, several plausible approaches exist, and candidate states can be evaluated meaningfully. It should not be applied automatically to simple tasks because its branching structure can create substantial cost, latency, and operational complexity.

The best implementation is not the one that explores the most branches. It is the one that uses a controlled search budget to achieve a measurable improvement over a simpler, single-path workflow.
