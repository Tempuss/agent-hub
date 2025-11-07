# Problem Definition Thinking

## Definition
Systematically clarify and define the true problem before attempting to solve it. This foundational thinking method prevents wasted effort on solving the wrong problem or addressing symptoms instead of root causes.

## Core Principle
> "All problem-solving begins with correctly defining the problem." - Peter Drucker

Most failures in problem-solving stem not from poor solutions, but from solving the wrong problem or only partially understanding what needs to be solved.

## Steps

### 1. Initial Problem Statement
Write down the problem as you first understand it:
- What is the perceived issue?
- Who identified it?
- When was it noticed?

### 2. Challenge the Problem Statement
Ask clarifying questions to test assumptions:
- Is this the real problem or a symptom?
- What evidence supports this being a problem?
- Who is affected and how?
- What is the impact/cost of not solving it?

### 3. Identify Root vs. Symptom
Distinguish between:
- **Symptom**: Observable manifestation (e.g., "Our API response time is slow")
- **Root Problem**: Underlying cause (e.g., "Missing database index on user_id column")

Use 5 Why or Fishbone to uncover if needed.

### 4. Define Problem Dimensions
Frame the problem across multiple dimensions:
- **Scope**: What is included/excluded?
- **Constraints**: What limitations exist?
- **Context**: What's the business/technical environment?
- **Success Criteria**: How will we know it's solved?

### 5. Establish Clear Success Metrics
Define measurable outcomes:
- **Quantitative**: Measurable metrics (response time < 100ms)
- **Qualitative**: Qualitative outcomes (improved user satisfaction)
- **Timeline**: When should this be solved?
- **Acceptance Criteria**: What passes/fails?

### 6. Reframe and Validate
Rewrite the problem statement with new clarity:
- Original: "Our application is slow"
- Refined: "API response time increased from 100ms to 2000ms for 40% of requests, affecting user experience and causing 15% increase in abandonment rate"

Validate with stakeholders:
- Does everyone agree on this definition?
- Are key constraints captured?
- Is success measurable?

## Pros
- Prevents solving the wrong problem (saves weeks/months of wasted effort)
- Uncovers hidden assumptions and constraints
- Aligns team understanding before starting work
- Creates clear success criteria
- Reduces rework and iteration cycles

## Cons
- Takes upfront time (30-60 minutes)
- Requires stakeholder involvement
- May reveal problems are larger/different than expected
- Can be uncomfortable (challenges initial assumptions)

## Example

### Scenario: "Startup has high customer churn"

**Initial Problem**: "Customers are leaving; we need better retention"

**Challenge Phase**:
- Is churn actually above industry average? → Yes, 8% monthly vs 3% industry average
- Which customer segments churn most? → Mid-market, after 3-4 months
- Why are they leaving? → Feature gap, poor onboarding, or pricing?
- What evidence exists? → Customer surveys, usage data, exit interviews

**Root vs Symptom**:
- Symptom: "Customers cancel subscriptions"
- Root causes identified:
  - Weak onboarding (60% of churned customers never used advanced features)
  - Feature gap vs competitors (35% cited missing features)
  - Support responsiveness (20% cited slow support response)

**Problem Dimensions**:
- **Scope**: Mid-market segment only (enterprise and SMB are stable)
- **Constraints**: Limited engineering resources (1 designer, 2 engineers)
- **Context**: Competitor just launched feature X; market consolidating
- **Success**: Reduce mid-market monthly churn to 3% within 6 months

**Success Metrics**:
- Quantitative: Churn rate 8% → 3% by Month 6
- Qualitative: Feature adoption increases 30% among new customers
- Timeline: Phase 1 (Onboarding) - 2 months, Phase 2 (Features) - 3 months, Phase 3 (Validation) - 1 month

**Refined Problem Definition**:
"Mid-market customer monthly churn is 8% (5x industry average). Primary causes are weak onboarding (60% of churned customers) and feature gaps vs competitors (35%). We must reduce this to 3% within 6 months using only 1 designer and 2 engineers. Success metrics: churn rate reduction and 30% increased feature adoption."

## When to Use
- **Before major projects**: Ensure you're solving the right problem
- **When multiple solutions proposed**: Clarify what problem each solves
- **Cross-functional conflicts**: Align on what the actual problem is
- **Resource constraints**: Ensure effort targets highest-impact problems
- **Strategic decisions**: Define business problems clearly before planning
- **Post-mortem analysis**: Prevent similar problems by understanding root causes

## When NOT to Use
- Emergency situations requiring immediate action (use OODA Loop instead, then circle back to proper problem definition)
- Very simple/obvious problems (e.g., "typo in code")
- Low-stakes decisions

## Success Context
- **All problem types**: 100% recommended before applying other methods
- Best for: Ensuring right problem selection before investing effort
- Use with: 5 Why (for root cause), Fishbone (for multi-causal analysis), SWOT (for strategic context)
- Complement: After problem definition, choose specific method from other frameworks

## Anti-Patterns to Avoid

### 1. Jumping to Solutions
**Wrong**: "Our API is slow → Let's add caching"
**Right**: "Our API is slow → Understand which operations, for which users, under what conditions → Then solve"

### 2. Accepting Surface Problem
**Wrong**: "Developers are unmotivated"
**Right**: "What specific behaviors indicate unmotivation? Is it low code quality, missed deadlines, or lack of innovation? What's driving it?"

### 3. Ignoring Context and Constraints
**Wrong**: "Build the perfect solution"
**Right**: "Build a solution that works with 2 engineers, 3-month timeline, and existing tech stack"

### 4. No Success Criteria
**Wrong**: "Improve customer satisfaction"
**Right**: "Improve NPS from 35 to 50 within Q2, with focus on response time and feature completeness"

### 5. Misaligned Stakeholders
**Wrong**: Engineering solving what they think Marketing needs
**Right**: Marketing, Engineering, and Product align on specific problem definition first

## Integration with Framework

**Use BEFORE other methods**:
1. Problem Definition (5-15 min)
2. Select appropriate method based on clarified problem
3. Apply chosen method (5 Why, SWOT, Design Thinking, etc.)

**Examples**:
- Problem Definition → 5 Why (root cause analysis)
- Problem Definition → SWOT (strategic planning)
- Problem Definition → First Principles (technical innovation)
- Problem Definition → Design Thinking (user-centric solutions)

---

**Version**: 2.0
**Thinking Type**: Foundational (use BEFORE other methods)
**Complexity**: Simple-Medium
**Time Investment**: 30-60 minutes for complex problems
**Success Rate**: 100% (prevents wasted effort on wrong problems)
