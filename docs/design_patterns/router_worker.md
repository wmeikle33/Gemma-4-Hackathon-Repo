# Router–Worker Pattern

## Overview

The **Router–Worker pattern** uses a routing component to classify an incoming request and send it to the most appropriate specialized worker.

Instead of giving every task to one general-purpose agent, the system selects a worker with the instructions, tools, knowledge, or model best suited to that request.

```text
                 User Request
                       │
                       ▼
                    Router
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     Support       Research       Coding
      Worker        Worker        Worker
          │            │            │
          └────────────┴────────────┘
                       │
                       ▼
                 Final Response
```

The router decides **where the request should go**. The selected worker decides **how to complete it**.

---

# Core Idea

Separate request classification from task execution.

The router is responsible for:

- Understanding the request type
- Selecting an appropriate worker
- Passing relevant context
- Handling uncertain routing decisions

The worker is responsible for:

- Completing the assigned task
- Using approved tools
- Following domain-specific instructions
- Returning a result

This allows each component to remain focused on a narrow responsibility.

---

# Components

## Router

The router examines the incoming request and chooses a destination.

Routing decisions may be based on:

- User intent
- Topic
- Required tools
- Data source
- Risk level
- Language
- Request complexity
- Worker availability
- Cost or latency requirements

Example routing output:

```json
{
  "route": "billing_worker",
  "confidence": 0.91,
  "reason": "The user is disputing an invoice charge."
}
```

The router should return a structured decision rather than an unrestricted natural-language response.

---

## Workers

Workers are specialized execution components.

Examples include:

- Customer support worker
- Billing worker
- Research worker
- Coding worker
- Document-analysis worker
- Scheduling worker
- Translation worker

Each worker may have its own:

- System instructions
- Tools
- Model
- Knowledge sources
- Memory permissions
- Guardrails
- Output format

Workers should have clear and non-overlapping responsibilities whenever possible.

---

## Worker Registry

A worker registry describes the available workers.

Example:

```json
[
  {
    "name": "billing_worker",
    "description": "Handles invoices, refunds, charges, and payment questions."
  },
  {
    "name": "technical_support_worker",
    "description": "Handles bugs, setup issues, errors, and troubleshooting."
  },
  {
    "name": "sales_worker",
    "description": "Handles product comparisons, pricing plans, and purchase inquiries."
  }
]
```

The router uses these descriptions when selecting a destination.

Poor worker descriptions often produce poor routing decisions.

---

## Shared Interface

Workers should return results in a consistent format.

Example:

```json
{
  "status": "completed",
  "response": "The customer's invoice was reviewed.",
  "needs_escalation": false,
  "metadata": {
    "worker": "billing_worker"
  }
}
```

A shared interface makes orchestration, logging, and error handling easier.

---

## Fallback Worker

A fallback worker handles requests that cannot be routed confidently.

Possible fallback behaviors include:

- Ask the user for clarification
- Send the request to a general-purpose worker
- Escalate to a human
- Route to a safe default workflow

Example:

```text
Routing Confidence Low
          │
          ▼
    Fallback Worker
          │
          ▼
 Request Clarification
```

A fallback is safer than forcing an uncertain routing decision.

---

# Basic Workflow

```text
Receive Request
      │
Analyze Intent
      │
Select Worker
      │
Pass Context
      │
Worker Executes
      │
Validate Result
      │
Return Response
```

---

# Example

A customer submits the following request:

> I was charged twice for my subscription.

The router classifies it as a billing issue.

```text
Customer Request
       │
       ▼
     Router
       │
       ▼
 Billing Worker
       │
       ▼
Check Payment Records
       │
       ▼
Provide Resolution
```

A technical-support or sales worker is never invoked.

---

# Routing Strategies

## Rule-Based Routing

The system uses explicit conditions.

Example:

```text
Contains "refund" or "invoice"

↓

Billing Worker
```

Advantages:

- Predictable
- Fast
- Easy to audit
- Low cost

Limitations:

- Difficult to scale across ambiguous requests
- Requires ongoing rule maintenance

---

## Model-Based Routing

A language model classifies the request.

Example prompt:

```text
Classify the user request into one of these routes:

- billing
- technical_support
- sales
- general

Return only the route name.
```

Advantages:

- Handles natural language
- Supports ambiguous phrasing
- Requires fewer explicit rules

Limitations:

- Less deterministic
- Adds latency and cost
- Requires evaluation

---

## Embedding-Based Routing

The system compares the request with worker descriptions or example requests.

```text
User Request

↓

Embedding Similarity

↓

Closest Worker
```

This approach can be effective when routes are semantically distinct.

---

## Hybrid Routing

Hybrid routing combines deterministic rules with model-based classification.

Example:

```text
High-Risk Keyword?

├── Yes → Human Review
└── No
      │
      ▼
   Model Router
```

Rules can handle obvious or high-risk cases while the model handles ambiguous requests.

---

# Single-Route Execution

The standard Router–Worker pattern selects one worker.

```text
Router

├── Worker A
├── Worker B
└── Worker C
```

Only the selected worker executes.

This keeps the workflow efficient and avoids unnecessary model or tool calls.

---

# Multi-Label Requests

Some user requests contain more than one intent.

Example:

> Cancel my plan and refund last month's charge.

This request may involve:

- Account management
- Billing

Possible strategies include:

### Choose the Primary Route

Send the complete request to the worker best able to resolve it.

### Split the Request

Create separate tasks for each intent.

### Escalate to a Manager

Use a Manager–Worker workflow when multiple workers must collaborate.

Router–Worker should not become an uncontrolled multi-agent workflow simply because a request contains several topics.

---

# Confidence-Based Routing

The router may attach a confidence score.

```text
Confidence ≥ 0.85

↓

Route Automatically

Confidence < 0.85

↓

Fallback or Clarification
```

Confidence thresholds should be calibrated using real routing data.

A model-generated confidence score should not automatically be treated as a reliable probability.

---

# Context Handoff

The router should pass only the context the worker needs.

Useful context may include:

- Original request
- Selected intent
- Relevant user data
- Retrieved documents
- Previous workflow results
- Constraints
- Required output format

Example:

```json
{
  "route": "technical_support_worker",
  "task": "Help the user resolve a login error.",
  "context": {
    "error_code": "AUTH-401",
    "product": "Admin Portal"
  }
}
```

Avoid passing unnecessary information to every worker.

---

# Tool Isolation

Different workers may have access to different tools.

Example:

| Worker | Tool Access |
|---|---|
| Billing worker | Payment and invoice systems |
| Support worker | Ticketing and diagnostic tools |
| Sales worker | CRM and product catalog |
| Research worker | Search and document retrieval |

Restricting tool access reduces:

- Security risk
- Tool-selection errors
- Prompt complexity
- Accidental actions

The router should not automatically expose every tool to every worker.

---

# Model Selection

Workers may use different models.

Example:

| Component | Model Requirement |
|---|---|
| Router | Small, fast classification model |
| General support worker | Medium conversational model |
| Research worker | Larger reasoning model |
| Extraction worker | Small structured-output model |

This allows the architecture to balance quality, latency, and cost.

The router itself often does not require the most capable model.

---

# Output Validation

Worker responses should be validated before reaching the user or downstream system.

Validation may check:

- Required fields
- Correct format
- Policy compliance
- Tool success
- Citation presence
- Unsupported claims
- Escalation requirements

Example:

```text
Worker Result
      │
      ▼
   Validator
      │
 ├── Valid → Return
 └── Invalid → Retry, Reroute, or Escalate
```

---

# Rerouting

A worker may determine that it received the wrong task.

Example:

```text
Technical Worker

↓

Identifies Billing Issue

↓

Return Routing Error

↓

Router Selects Billing Worker
```

Rerouting should be limited to prevent loops.

Recommended controls include:

- Maximum reroute count
- Previous-route tracking
- No immediate return to the same failed worker
- Human escalation after repeated failures

---

# Error Handling

Possible failures include:

- Router returns an invalid worker
- Selected worker is unavailable
- Worker lacks required tools
- Worker fails to complete the task
- Worker reports an incorrect route
- Routing confidence is too low

Example recovery flow:

```text
Worker Failure
      │
      ▼
Retry Same Worker?
      │
 ├── Yes → Limited Retry
 └── No
      │
      ▼
Alternative Worker?
      │
 ├── Yes → Reroute
 └── No → Human Escalation
```

Do not blindly retry the same route without changing the conditions that caused the failure.

---

# Human-in-the-Loop

Human review may be triggered when:

- Routing confidence is low
- The request is high risk
- Multiple routes appear equally appropriate
- Workers repeatedly reject the request
- Sensitive actions are required
- The user disputes the automated result

```text
Router
  │
  ▼
Uncertain or High-Risk?
  │
  ├── No → Worker
  └── Yes → Human Reviewer
```

---

# When to Use This Pattern

Use Router–Worker when:

- Requests fall into distinct categories
- Specialized workers provide better results
- Workers require different tools or knowledge
- Only one worker usually needs to handle each request
- Centralized routing simplifies the user experience
- Cost or model selection varies by task type

Typical applications include:

- Customer support
- Enterprise assistants
- IT help desks
- Document processing
- Sales automation
- HR assistants
- Multi-domain knowledge systems
- Tool-selection systems

---

# When Not to Use It

Avoid Router–Worker when:

- One worker can handle all requests reliably
- The number of routes is very small and deterministic
- Tasks require several workers to collaborate
- The request must be decomposed into multiple subtasks
- Routing overhead exceeds the value of specialization

Use a simple conditional workflow when classification is trivial.

Use Manager–Worker when several workers must contribute to the same task.

---

# Common Failure Modes

## Ambiguous Worker Boundaries

Several workers appear equally suitable.

Example:

```text
Account Worker

Billing Worker

Subscription Worker
```

All three may claim responsibility for subscription cancellation.

**Solution**

Define mutually understandable worker scopes and provide positive and negative routing examples.

---

## Route Overlap

Worker responsibilities overlap heavily.

**Solution**

Consolidate similar workers or establish clear precedence rules.

---

## Wrong Route

The router sends a task to an unsuitable worker.

**Solution**

Evaluate routing accuracy, improve route descriptions, and add fallback handling.

---

## Forced Routing

The router always selects a worker even when confidence is low.

**Solution**

Allow clarification, fallback, or human escalation.

---

## Router Bottleneck

Every request depends on one overloaded routing component.

**Solution**

Use lightweight routing, caching, deterministic rules, or scalable routing services.

---

## Excessive Rerouting

Workers repeatedly pass the task between one another.

```text
Worker A

↓

Worker B

↓

Worker A

↓

Worker B
```

**Solution**

Track routing history and enforce reroute limits.

---

## Worker Proliferation

A new worker is created for every minor request type.

**Solution**

Create workers around meaningful capabilities rather than narrow keywords.

---

## Weak Context Handoff

The worker receives a route label but not enough information to complete the task.

**Solution**

Pass the original request, relevant evidence, constraints, and expected output.

---

## Router Hallucination

The model selects a worker that does not exist.

**Solution**

Restrict output to a registered worker list and validate the route before execution.

---

## Hidden Routing Logic

Routing decisions are not recorded.

**Solution**

Log the selected route, confidence, routing method, and relevant decision metadata.

---

# No-Code Implementation

A typical no-code workflow may use:

1. A form, message, email, or webhook trigger.
2. A classification step.
3. A structured route output.
4. Conditional branches for each worker.
5. Specialized prompts and tools inside each branch.
6. A shared output formatter.
7. A fallback or escalation branch.
8. Logging for routing and worker results.

Example:

```text
Incoming Message
       │
       ▼
Intent Classifier
       │
 ┌─────┼──────────┐
 ▼     ▼          ▼
Sales Billing Technical
 ▼     ▼          ▼
Worker Worker     Worker
 └─────┴──────────┘
       │
       ▼
Standard Response
```

No-code platforms can implement this using conditional branches, workflow routers, classifiers, subworkflows, and approval steps.

---

# Observability

Track both router performance and worker performance.

## Router Metrics

- Route distribution
- Routing accuracy
- Low-confidence rate
- Fallback rate
- Rerouting rate
- Invalid-route rate
- Routing latency
- Routing cost

## Worker Metrics

- Completion rate
- Error rate
- Tool success rate
- Response latency
- Escalation rate
- User satisfaction
- Cost per request

A low worker success rate may indicate either a weak worker or incorrect routing.

---

# Evaluation

Create a routing evaluation dataset containing:

- Example request
- Expected route
- Acceptable alternative routes
- Risk level
- Whether clarification is required

Example:

| Request | Expected Route |
|---|---|
| “Why was I charged twice?” | Billing |
| “The application crashes at login.” | Technical Support |
| “Which plan supports 50 users?” | Sales |
| “I need help, but I am not sure where.” | Fallback or clarification |

Evaluation should include:

- Clear requests
- Ambiguous requests
- Multi-intent requests
- Adversarial wording
- Requests outside all worker scopes
- Requests containing sensitive actions

---

# Evaluation Metrics

Useful metrics include:

- Routing accuracy
- Precision by route
- Recall by route
- Confusion matrix
- Fallback accuracy
- Unnecessary escalation rate
- Incorrect automatic-routing rate
- End-to-end task completion
- Cost per completed request
- Average latency

End-to-end success matters more than classification accuracy alone.

A route can be technically correct while still producing a poor outcome.

---

# Router–Worker vs. Router

A router is a component.

Router–Worker is a complete execution pattern.

| Router | Router–Worker |
|---|---|
| Selects a destination | Selects and invokes a worker |
| May route to workflows, tools, or models | Routes specifically to specialized workers |
| Does not define worker behavior | Includes worker responsibilities and handoff |
| Can exist inside many architectures | Describes the full request-to-worker flow |

A router answers:

> Where should this request go?

The Router–Worker pattern also defines:

> What happens after the route is selected?

---

# Router–Worker vs. Manager–Worker

These patterns are related but solve different problems.

| Router–Worker | Manager–Worker |
|---|---|
| Selects one appropriate worker | Delegates subtasks to one or more workers |
| Classifies the incoming request | Decomposes a larger objective |
| Usually invokes one worker | May invoke several workers |
| Usually does not aggregate multiple outputs | Often combines worker outputs |
| Best for distinct request categories | Best for complex, decomposable tasks |
| Routing is the central responsibility | Coordination is the central responsibility |

A router asks:

> Which worker should handle this request?

A manager asks:

> Which tasks must be completed, and who should complete each one?

---

# Router–Worker vs. Tool Routing

A worker is not the same as a tool.

| Worker Routing | Tool Routing |
|---|---|
| Selects an agent or workflow | Selects a callable capability |
| Worker may reason and use several tools | Tool performs a defined operation |
| Suitable for domain-level specialization | Suitable for action-level selection |
| Often uses specialized instructions | Usually uses a strict interface |

Example:

```text
Router

↓

Travel Worker

↓

Flight Search Tool
```

The router chooses the domain specialist. The worker chooses the required tool.

---

# Router–Worker vs. Mixture of Experts

Router–Worker may resemble a Mixture-of-Experts architecture, but the concepts operate at different levels.

| Router–Worker | Mixture of Experts |
|---|---|
| Application-level architecture | Model-level architecture |
| Routes requests to agents or workflows | Routes tokens or representations to neural experts |
| Explicit and observable components | Usually internal to a model |
| Can use different tools and systems | Experts are parts of one model |

The similarity is conceptual: both route inputs toward specialized capabilities.

---

# Security and Permissions

Workers should receive only the permissions required for their responsibilities.

Example:

| Worker | Allowed Actions |
|---|---|
| Support worker | Read tickets, draft replies |
| Billing worker | Read invoices, propose refunds |
| Refund approver | Approve refunds |
| Sales worker | Read product data, update CRM leads |

The router must not become a way to bypass authorization.

Important controls include:

- Worker-specific credentials
- Least-privilege tool access
- User authorization checks
- Sensitive-action approval
- Audit logging
- Data-access boundaries

Routing decides which worker is suitable. It does not determine whether an action is authorized.

---

# Cost and Latency

Router–Worker can reduce cost when lightweight components handle simple tasks.

Example:

```text
Simple FAQ
    │
    ▼
Small Support Worker

Complex Research
    │
    ▼
Advanced Research Worker
```

However, the architecture introduces routing overhead.

Total workflow cost may include:

```text
Routing Cost
+
Worker Cost
+
Tool Cost
+
Validation Cost
+
Retry or Escalation Cost
```

The router should provide enough value to justify the additional step.

---

# Design Checklist

Before implementing Router–Worker, ensure that:

- Each worker has a clear responsibility.
- Worker scopes do not overlap excessively.
- The router uses a registered worker list.
- Routing output is structured and validated.
- Low-confidence requests have a fallback.
- Context handoff is explicitly defined.
- Worker tool access follows least privilege.
- Multi-intent requests are handled deliberately.
- Rerouting has strict limits.
- Router and worker metrics are recorded.
- High-risk routes can require human review.
- The architecture is simpler than using one general worker.

---

# Trade-Offs

| Advantage | Trade-Off |
|---|---|
| Better specialization | Additional routing step |
| Smaller worker prompts | Route-maintenance overhead |
| Worker-specific tools and permissions | Risk of incorrect routing |
| Easier domain-level evaluation | Ambiguous requests need fallback handling |
| Supports model and cost optimization | More components to monitor |
| Clear separation of responsibilities | Worker boundaries may become difficult to maintain |

---

# Related Patterns

- Router
- Manager–Worker
- Planner–Executor
- ReAct
- Retrieval Pipeline
- Human-in-the-Loop
- Hybrid Patterns

---

# Related Anti-Patterns

- Everything Is an Agent
- God Agent
- Too Many Agents
- Tool Explosion
- Hidden State
- Blind Retries
- Infinite Loops

---

# Pattern Summary

The Router–Worker pattern classifies an incoming request and sends it to the most appropriate specialized worker.

The router focuses on destination selection, while workers focus on execution. This separation enables specialized prompts, tools, models, permissions, and evaluation strategies without requiring one large general-purpose agent.

The pattern is most effective when requests fall into reasonably distinct categories and one worker can usually complete each request. When a task requires decomposition and collaboration among several workers, the Manager–Worker pattern is generally more appropriate.
