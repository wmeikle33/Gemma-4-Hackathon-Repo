# Workflow DAG Pattern

## Overview

The **Workflow DAG pattern** represents an AI workflow as a **Directed Acyclic Graph (DAG)**.

Each node represents a task, agent, tool, validation step, or human review stage. Directed edges represent dependencies and determine how information moves through the workflow.

```text
            Input
              │
              ▼
         Retrieve Data
          /          \
         ▼            ▼
   Analyze Text   Analyze Metrics
         \            /
          ▼          ▼
          Combine Results
                 │
                 ▼
            Final Report
```

A DAG may contain:

- Sequential steps
- Parallel branches
- Conditional paths
- Validation stages
- Human approval gates
- Aggregation steps

Unlike an unrestricted agent loop, a Workflow DAG has an explicit structure and does not allow execution to cycle indefinitely.

---

## Core Idea

Represent the workflow as a graph in which:

- **Nodes** perform work.
- **Edges** represent dependencies or data flow.
- **Branches** allow parallel or conditional execution.
- **Join nodes** combine results.
- **Terminal nodes** complete the workflow.

Because the graph is acyclic, execution always moves toward completion.

---

## What Does DAG Mean?

A DAG has three defining characteristics.

### Directed

Edges point in a specific direction.

```text
Retrieve Data
      │
      ▼
Analyze Data
```

The analysis depends on retrieval, not the other way around.

### Acyclic

The graph cannot contain a path that returns to an earlier node.

Valid:

```text
A → B → C
```

Invalid:

```text
A → B → C → A
```

Cycles create loops and prevent the workflow from having a guaranteed completion path.

### Graph

The workflow can contain multiple paths rather than only one linear sequence.

```text
        A
       / \
      B   C
       \ /
        D
```

---

## Components

### Nodes

A node represents one unit of work.

Examples include:

- LLM prompt
- Agent
- Tool call
- Retrieval step
- Database query
- Code execution
- Validation
- Human approval
- Transformation
- Notification

Each node should have a clear responsibility.

Example:

```json
{
  "node_id": "summarize_documents",
  "type": "llm_task",
  "inputs": ["retrieved_documents"],
  "outputs": ["document_summary"]
}
```

---

### Edges

Edges connect nodes and define dependencies.

```text
Document Retrieval
        │
        ▼
Document Summarization
```

The summarization node cannot begin until retrieval is complete.

Edges may carry:

- Text
- Structured data
- Documents
- Tool outputs
- Status information
- Error information
- Approval decisions

---

### Entry Node

The entry node starts the workflow.

Examples include:

- User request
- Form submission
- File upload
- Scheduled trigger
- Webhook
- New email
- Database event

A workflow may have one or several entry triggers, but each execution should have a clearly identified starting point.

---

### Terminal Node

A terminal node marks the end of a workflow path.

Examples include:

- Return final answer
- Save report
- Send notification
- Escalate to human
- Record failure
- End without action

Every valid path should eventually reach a terminal state.

---

### Branch Node

A branch node selects between possible paths.

```text
Classify Request
       │
       ▼
   Request Type?
   ├── Support → Support Workflow
   ├── Sales → Sales Workflow
   └── Other → General Workflow
```

Branches may be based on:

- Rules
- Model classifications
- Risk scores
- Tool outputs
- User permissions
- Confidence
- Human decisions

---

### Join Node

A join node waits for multiple upstream branches and combines their outputs.

```text
Research Branch ─────┐
                     ├── Synthesis
Analysis Branch ─────┘
```

A join may wait for:

- All branches
- Any successful branch
- A minimum number of branches
- The first completed branch
- Only required branches

The join condition should be defined explicitly.

---

### Workflow Controller

The controller manages graph execution.

Responsibilities may include:

- Determining which nodes are ready
- Passing inputs between nodes
- Running independent nodes in parallel
- Tracking node status
- Enforcing timeouts
- Handling retries
- Recording outputs
- Detecting failures
- Ending the workflow

---

## Basic Workflow

```text
Receive Input
      │
Validate Input
      │
Determine Ready Nodes
      │
Execute Nodes
      │
Store Outputs
      │
Unlock Dependent Nodes
      │
Continue Until Terminal State
```

A node becomes ready only when its required dependencies have completed successfully.

---

## Example

A user uploads a business report and requests an executive summary.

```text
File Uploaded
      │
      ▼
Validate File
      │
      ▼
Extract Text
      │
      ├───────────────┐
      ▼               ▼
Summarize Sections  Extract Metrics
      │               │
      └───────┬───────┘
              ▼
        Combine Results
              │
              ▼
       Validate Citations
              │
              ▼
       Generate Final Report
```

This workflow contains:

- Sequential dependencies
- Parallel processing
- A join
- A validation stage
- A final output

---

## Sequential Execution

Some nodes must run in order.

```text
Upload File
      │
      ▼
Extract Text
      │
      ▼
Generate Summary
      │
      ▼
Save Result
```

Sequential execution is appropriate when each step requires the previous step's output.

---

## Parallel Execution

Independent nodes can run simultaneously.

```text
                 Document
                /        \
               ▼          ▼
       Extract Entities  Summarize
               \          /
                ▼        ▼
                Combine
```

Parallel execution can reduce total latency.

It should only be used when branches do not depend on each other's intermediate results.

---

## Conditional Execution

A node may execute only when a condition is met.

```text
Evaluate Risk
      │
      ▼
High Risk?
 ├── Yes → Human Review
 └── No → Automatic Execution
```

Conditions should be:

- Explicit
- Observable
- Testable
- Logged

Avoid hiding important routing decisions inside free-form prompts.

---

## Fan-Out and Fan-In

### Fan-Out

One node starts several downstream tasks.

```text
Input
  ├── Analysis A
  ├── Analysis B
  └── Analysis C
```

### Fan-In

Several branches feed into one downstream node.

```text
Analysis A ─┐
Analysis B ─┼── Final Synthesis
Analysis C ─┘
```

Fan-out and fan-in are useful for research, document processing, evaluation, and multi-source analysis.

---

## Data Flow

Nodes should exchange explicit data.

Example:

```json
{
  "workflow_id": "report_1042",
  "node": "extract_metrics",
  "status": "completed",
  "output": {
    "revenue_growth": 0.12,
    "customer_churn": 0.04
  }
}
```

Explicit data flow improves:

- Debugging
- Reproducibility
- Validation
- Auditing
- Recovery

Avoid relying on undocumented shared memory between nodes.

---

## State Management

The workflow should maintain execution state.

Possible node states include:

```text
Pending
Ready
Running
Completed
Failed
Skipped
Waiting for Human
Cancelled
```

Example:

```json
{
  "workflow_id": "workflow_72",
  "nodes": {
    "retrieve": "completed",
    "analyze": "running",
    "validate": "pending",
    "publish": "pending"
  }
}
```

Explicit state prevents hidden progress and makes interrupted workflows easier to resume.

---

## Input and Output Contracts

Each node should define:

- Required inputs
- Optional inputs
- Output schema
- Error schema
- Timeout
- Retry policy
- Completion criteria

Example:

```json
{
  "node": "classify_ticket",
  "input": {
    "ticket_text": "string"
  },
  "output": {
    "category": "string",
    "confidence": "number"
  }
}
```

Well-defined contracts reduce integration errors between nodes.

---

## Deterministic and AI Nodes

A Workflow DAG can combine conventional software with AI components.

```text
Input Validation
      │
      ▼
Intent Classifier
      │
      ▼
Database Query
      │
      ▼
LLM Response
      │
      ▼
Schema Validation
```

Use deterministic nodes for:

- Calculations
- Validation
- Formatting
- Permission checks
- Data transformations
- Business rules

Use AI nodes for:

- Classification
- Summarization
- Extraction from unstructured text
- Reasoning
- Draft generation

Not every node should be an agent.

---

## Error Handling

Node failures should be handled explicitly.

```text
Execute Node
      │
      ▼
Success?
 ├── Yes → Continue
 └── No
       │
       ▼
   Retry Allowed?
   ├── Yes → Limited Retry
   └── No → Fallback or Failure Path
```

Possible failure strategies include:

- Retry with a limit
- Use an alternative tool
- Skip an optional node
- Route to a fallback node
- Request human assistance
- End the workflow safely
- Move the task to a failure queue

---

## Retry Policies

Retries should be defined per node.

Example:

```json
{
  "node": "external_api_call",
  "max_attempts": 3,
  "backoff": "exponential",
  "retry_on": [
    "timeout",
    "rate_limit",
    "temporary_service_error"
  ]
}
```

Do not retry failures caused by:

- Invalid input
- Missing permissions
- Unsupported requests
- Policy violations
- Permanent tool errors

Retries should not create cycles in the graph. They are controlled execution behavior within a node, not new graph paths returning to previous nodes.

---

## Timeouts

Every external or nondeterministic node should have a timeout.

```text
Tool Call
    │
    ▼
Complete Within Limit?
├── Yes → Continue
└── No → Timeout Handler
```

Timeouts prevent one stalled node from blocking the entire workflow.

---

## Optional Nodes

Some nodes may be optional.

Example:

```text
Generate Draft
      │
      ▼
Needs Translation?
 ├── Yes → Translate
 └── No → Continue
```

Skipped nodes should be recorded explicitly rather than appearing as missing executions.

---

## Human Approval Nodes

Human review can be modeled as a node.

```text
Generate Refund Recommendation
             │
             ▼
       Human Approval
        ├── Approve
        ├── Modify
        └── Reject
```

The workflow may pause while waiting for a reviewer.

The node should define:

- Required reviewer role
- Review deadline
- Escalation policy
- Approval options
- Data shown to the reviewer
- Audit requirements

---

## Event-Driven DAG Execution

A Workflow DAG may be triggered by external events.

```text
Invoice Uploaded
       │
       ▼
Workflow DAG Starts
       │
       ▼
Extract → Validate → Store → Notify
```

The Event-Driven pattern determines **when** the workflow starts.

The Workflow DAG determines **how** the workflow executes.

---

## Dynamic DAGs

Some workflows build parts of the graph at runtime.

Example:

```text
Analyze Request
       │
       ▼
Determine Required Tasks
       │
       ├── Research
       ├── Data Analysis
       └── Legal Review
```

Dynamic DAGs can adapt to the task but are harder to:

- Validate
- Predict
- Audit
- Estimate
- Secure

Use a predefined set of allowed node types and graph constraints.

---

## Static vs. Dynamic DAGs

| Static DAG | Dynamic DAG |
|---|---|
| Defined before execution | Constructed or modified at runtime |
| Predictable | Flexible |
| Easier to test | Harder to validate |
| Easier to audit | More adaptable |
| Stable cost structure | Variable cost |
| Best for repeatable workflows | Best for variable complex tasks |

Use static DAGs unless runtime graph generation provides clear value.

---

## Subworkflows

A node may invoke another DAG as a reusable subworkflow.

```text
Main Workflow
      │
      ├── Customer Verification Subworkflow
      ├── Document Analysis Subworkflow
      └── Notification Subworkflow
```

Subworkflows improve:

- Reuse
- Modularity
- Testing
- Ownership
- Maintenance

Avoid making every small action a separate subworkflow.

---

## Workflow Versioning

Changes to a production DAG should be versioned.

Example:

```text
customer_support_v1

customer_support_v2

customer_support_v3
```

Versioning helps preserve:

- Reproducibility
- Audit history
- Compatibility
- Rollback capability
- Evaluation comparisons

An in-progress workflow should normally continue using the version with which it started.

---

## Idempotency

Nodes should be idempotent where possible.

Running the same node twice should not create an incorrect duplicate effect.

Poor:

```text
Run Node Twice
      │
      ▼
Send Two Refunds
```

Better:

```text
Refund Already Issued?
├── Yes → Return Existing Result
└── No → Issue Refund
```

Idempotency is especially important when:

- Workflows resume after failures
- Nodes are retried
- Events are delivered more than once
- External tools have side effects

---

## Checkpointing

Checkpointing records completed work so the workflow can resume without starting over.

```text
Extract Data       ✓
Analyze Data       ✓
Generate Report    Failed
Publish Report     Pending
```

After recovery, execution resumes at the failed node rather than repeating every completed step.

Checkpoints may store:

- Node status
- Inputs
- Outputs
- Errors
- Execution time
- Model version
- Prompt version
- Tool version

---

## Caching

Reusable node outputs may be cached.

Example:

```text
Document Hash Exists?
├── Yes → Reuse Extraction
└── No → Extract Document
```

Caching can reduce:

- Cost
- Latency
- Repeated tool calls
- Duplicate model usage

Cache invalidation rules should account for:

- Input changes
- Source freshness
- Model changes
- Prompt changes
- Permission changes

---

## Workflow Compensation

Some completed actions may need to be reversed after a later failure.

Example:

```text
Reserve Inventory
        │
        ▼
Charge Payment
        │
        ▼
Shipment Creation Fails
        │
        ▼
Cancel Reservation and Refund Payment
```

A compensating action reverses or mitigates a previous side effect.

Not every operation can be perfectly reversed, so compensation behavior should be designed before execution.

---

## When to Use This Pattern

Use a Workflow DAG when:

- Tasks have explicit dependencies
- Workflows are repeatable
- Some steps can run in parallel
- Execution order matters
- Progress must be observable
- Failures must be recoverable
- Human approval stages exist
- Auditability is required
- Several tools or systems are coordinated
- Predictable completion is important

Typical applications include:

- Document processing
- Customer support automation
- Data pipelines
- Report generation
- Employee onboarding
- Compliance review
- Research workflows
- Content approval
- Financial operations
- Enterprise automation

---

## When Not to Use It

Avoid a Workflow DAG when:

- A single prompt solves the task
- The workflow contains only one or two simple steps
- The next action cannot be predicted structurally
- The environment requires continuous open-ended exploration
- Graph orchestration adds more complexity than value
- A deterministic script is sufficient

Use ReAct or Tree Search when execution requires open-ended exploration.

Use a simple pipeline when the workflow is entirely linear.

---

## Common Failure Modes

### DAG Overengineering

A simple workflow is divided into too many nodes.

**Solution**

Create nodes around meaningful units of work rather than every small operation.

---

### Hidden Dependencies

A node relies on data that is not represented by an incoming edge.

**Solution**

Make all required inputs and dependencies explicit.

---

### Invalid Cycles

The graph accidentally allows a path to return to an earlier node.

**Solution**

Validate the graph before execution and separate retries from graph structure.

---

### Weak Node Contracts

Downstream nodes cannot reliably interpret upstream outputs.

**Solution**

Use structured input and output schemas.

---

### Join Deadlock

A join waits forever for a branch that was skipped or failed.

**Solution**

Define whether the join requires all branches, successful branches, or selected branches.

---

### Excessive Branching

The workflow contains too many possible paths.

**Solution**

Simplify routing rules and consolidate similar branches.

---

### Shared Mutable State

Parallel nodes modify the same data unpredictably.

**Solution**

Use immutable outputs, isolated state, or controlled write operations.

---

### Duplicate Side Effects

Retries or repeated events perform an action more than once.

**Solution**

Use idempotency keys and completion records.

---

### Silent Node Failure

A node fails but downstream execution continues with incomplete data.

**Solution**

Define required and optional dependencies explicitly.

---

### Workflow Version Drift

Prompts, tools, or nodes change during execution.

**Solution**

Pin each workflow execution to specific component versions.

---

### Unbounded Dynamic Graphs

A planner continually adds new nodes.

**Solution**

Set graph-size, depth, cost, and node-type limits.

---

### Excessive Human Waiting

Many workflows remain paused for approval.

**Solution**

Track approval queues, deadlines, ownership, and escalation policies.

---

## No-Code Implementation

A no-code Workflow DAG may use:

1. A trigger node.
2. Input validation.
3. Conditional branches.
4. Parallel workflow paths.
5. Tool or model nodes.
6. Join or aggregation nodes.
7. Human approval stages.
8. Error branches.
9. State storage.
10. A final output node.

Example:

```text
Form Submitted
      │
      ▼
Validate Request
      │
      ▼
Classify Request
      │
 ┌────┴──────────┐
 ▼               ▼
Retrieve Data   Check Account
 └──────┬────────┘
        ▼
 Generate Recommendation
        │
        ▼
 High Risk?
 ├── No → Execute
 └── Yes → Human Approval
```

Useful no-code building blocks include:

- Triggers
- Routers
- Conditional nodes
- Iterators
- Subworkflows
- Data tables
- Approval tasks
- Webhooks
- Delay nodes
- Error handlers

---

## Observability

Track workflow execution at both graph and node level.

### Workflow-Level Metrics

- Workflow start time
- Workflow completion time
- Completion rate
- Failure rate
- Cancellation rate
- Total cost
- Total model calls
- Total tool calls
- Human-review time
- End-to-end latency

### Node-Level Metrics

- Node status
- Execution duration
- Input size
- Output size
- Token usage
- Tool latency
- Retry count
- Failure reason
- Model version
- Prompt version
- Cache status

A visual execution trace should show:

```text
Node A  ✓
Node B  ✓
Node C  Failed
Node D  Skipped
```

---

## Evaluation Metrics

Useful metrics include:

- End-to-end task success
- Workflow completion rate
- Node failure rate
- Average execution time
- Critical-path latency
- Parallel speedup
- Retry rate
- Human escalation rate
- Cost per completed workflow
- Recovery success rate
- Output quality
- User satisfaction

The performance of individual nodes should not be evaluated separately from the final workflow outcome.

---

## Critical Path

The **critical path** is the longest sequence of dependent nodes that determines total workflow duration.

Example:

```text
Path A: 2s → 3s → 5s = 10s

Path B: 2s → 1s → 2s = 5s
```

Path A is the critical path.

Optimizing nodes outside the critical path may not reduce total latency.

---

## Workflow DAG vs. Pipeline

| Workflow DAG | Pipeline |
|---|---|
| Supports branching | Usually linear |
| Supports parallel execution | Usually sequential |
| May contain multiple terminal paths | Usually has one primary path |
| Models complex dependencies | Models ordered stages |
| Requires graph orchestration | Easier to implement |

A pipeline can be represented as a simple DAG in which every node has one primary successor.

Use a pipeline when the workflow is linear.

Use a Workflow DAG when dependencies form a broader graph.

---

## Workflow DAG vs. Planner–Executor

| Workflow DAG | Planner–Executor |
|---|---|
| Workflow structure is explicit | Planner determines steps |
| Usually predefined | May create plans dynamically |
| Predictable execution paths | Adaptable execution paths |
| Easier to test and audit | Better for uncertain tasks |
| Nodes execute according to dependencies | Executor follows a generated plan |

A planner may generate a DAG, but the generated structure should still be validated before execution.

---

## Workflow DAG vs. ReAct

| Workflow DAG | ReAct |
|---|---|
| Follows an explicit graph | Selects actions iteratively |
| Predictable dependencies | Next action depends on observations |
| Guaranteed acyclic structure | May enter loops without controls |
| Best for repeatable workflows | Best for uncertain environments |
| Easier to audit | More flexible |

Use a DAG when the process is known.

Use ReAct when the process must be discovered during execution.

---

## Workflow DAG vs. Tree Search

| Workflow DAG | Tree Search |
|---|---|
| Executes required workflow paths | Explores competing candidate paths |
| Nodes represent scheduled work | Nodes represent possible states |
| Most executed outputs are retained | Many branches are discarded |
| Focuses on orchestration | Focuses on exploration |
| Predictable resource usage | Potentially high search cost |

A DAG defines what work should happen.

Tree Search explores which solution path should be selected.

---

## Workflow DAG vs. Event-Driven

| Workflow DAG | Event-Driven |
|---|---|
| Defines execution dependencies | Defines reactions to events |
| Coordinates steps in one workflow | Connects producers and consumers |
| Has a bounded execution structure | May trigger many independent workflows |
| Focuses on task progression | Focuses on system responsiveness |

These patterns often work together:

```text
External Event
      │
      ▼
Start Workflow DAG
      │
      ▼
Execute Dependent Tasks
```

---

## Workflow DAG vs. Manager–Worker

| Workflow DAG | Manager–Worker |
|---|---|
| Dependencies are explicitly modeled | Manager dynamically delegates work |
| Nodes may be tools, agents, or rules | Workers are execution specialists |
| Coordination is graph-based | Coordination is manager-based |
| Best for repeatable processes | Best for decomposable variable tasks |
| Usually predictable | Often adaptive |

A Manager–Worker system may execute inside a DAG node, or the manager may construct a limited DAG of worker tasks.

---

## Security and Permissions

Each node should receive only the permissions it needs.

Example:

| Node | Permission |
|---|---|
| Retrieve customer record | Read customer data |
| Draft refund | Read billing policy |
| Approve refund | Approval permission |
| Issue refund | Payment write permission |
| Notify customer | Send-message permission |

Important controls include:

- Least-privilege credentials
- Node-specific tool access
- User authorization checks
- Sensitive-data filtering
- Approval before irreversible actions
- Audit logging
- Separation of duties
- Secure state storage

A valid graph path does not automatically mean the user is authorized to execute it.

---

## Cost and Latency

Total workflow cost may include:

```text
Model Calls
+
Tool Calls
+
Storage
+
Retries
+
Human Review
+
Orchestration
```

Cost can be controlled through:

- Parallel execution
- Caching
- Smaller models for simple nodes
- Conditional node execution
- Early termination
- Reusing subworkflow outputs
- Limiting retries
- Skipping unnecessary evaluation stages

Measure both total latency and critical-path latency.

---

## Design Checklist

Before implementing a Workflow DAG, ensure that:

- Every node has one clear responsibility.
- Dependencies are explicit.
- The graph contains no cycles.
- Input and output contracts are defined.
- Required and optional branches are distinguished.
- Join conditions are documented.
- Parallel nodes do not create unsafe state conflicts.
- Retry policies are limited.
- Timeouts are configured.
- Side-effecting nodes are idempotent.
- Failure and compensation paths exist.
- Human approval stages have deadlines and ownership.
- Workflow versions are recorded.
- Execution can resume from checkpoints.
- Node and workflow metrics are collected.
- The DAG is simpler than a more dynamic agent architecture.

---

## Trade-Offs

| Advantage | Trade-Off |
|---|---|
| Explicit execution structure | More orchestration logic |
| Predictable dependencies | Less flexible than open-ended agents |
| Supports parallel execution | Join and state management can be complex |
| Easier debugging | Requires careful node contracts |
| Strong auditability | Graph changes require versioning |
| Supports recovery and checkpoints | Additional state infrastructure |
| Reduces infinite-loop risk | Dynamic tasks may not fit fixed graphs |

---

## Related Patterns

- Pipeline
- Event-Driven
- Router–Worker
- Manager–Worker
- Planner–Executor
- Map–Reduce
- Retrieval Pipeline
- Human-in-the-Loop
- Hybrid Patterns

---

## Related Anti-Patterns

- Infinite Loops
- Hidden State
- Overplanning
- God Agent
- Tool Explosion
- Too Many Agents
- Blind Retries
- Everything Is an Agent

---

## Pattern Summary

The Workflow DAG pattern represents an AI workflow as a directed, acyclic graph of tasks and dependencies.

Nodes perform work, edges define execution order, branches enable conditional or parallel processing, and join nodes combine results. Because the graph is explicit and acyclic, the workflow is easier to observe, test, recover, and audit than an unrestricted agent loop.

Workflow DAGs are most effective for repeatable processes with known dependencies, such as document processing, approvals, reporting, compliance, and enterprise automation. They are less suitable for open-ended tasks in which the required steps cannot be determined before execution.

The goal is not to convert every operation into a graph node. The goal is to make meaningful dependencies, decisions, state transitions, and failure paths explicit while preserving the simplest architecture that reliably completes the workflow.

