# Method Combinations - Multi-Method Workflow Patterns

**Purpose**: Solve complex problems by chaining multiple thinking methods in strategic sequences

**When to use**: Single methods aren't sufficient; problem requires multiple perspectives or phases

**Success principle**: "No single method solves everything. Combine intelligently for complex challenges."

---

## 🎯 Core Principles

### Why Combine Methods?

**Single-method limitations**:
- 5 Why finds root cause but doesn't create solutions
- SWOT identifies situation but doesn't plan execution
- SCAMPER generates ideas but doesn't validate them

**Combination advantages**:
- **Completeness**: Cover analysis → solution → validation cycle
- **Depth**: Multiple perspectives reveal hidden insights
- **Efficiency**: Right method for each phase (vs forcing one method)
- **Quality**: Cross-validation between methods

### Combination Rules

✅ **DO**:
- Use methods in logical sequence (analysis → ideation → execution)
- Let each method inform the next (outputs become inputs)
- Match method strengths to problem phases
- Validate outputs between methods

❌ **DON'T**:
- Combine incompatible methods (e.g., DMAIC + SCAMPER for same goal)
- Skip validation between methods
- Use combinations for simple problems
- Force all 15 methods into every problem

---

## 📚 Standard Combination Patterns

### Pattern 1: Root Cause → Breakthrough Solution → Iteration

**Workflow**: `5 Why → First Principles → PDCA`

**Use when**: Technical/systemic problem needs innovative solution, not just fixing symptoms

**Complexity**: Medium-Complex | **Time**: 2-3 hours | **Success Rate**: 85%

**Process**:
```
PHASE 1: Root Cause Analysis (5 Why)
  ↓ Find fundamental cause

PHASE 2: Breakthrough Solution (First Principles)
  ↓ Decompose to elements, reconstruct innovative solution

PHASE 3: Implementation (PDCA)
  ↓ Plan → Do → Check → Act (iterate until stable)
```

**Real Example**: E-commerce Platform Performance

```markdown
PHASE 1 (5 Why):
- Why is checkout slow? → Database queries taking 3s
- Why? → N+1 query problem
- Why? → ORM lazy loading + cart items loop
- Why? → Initial architecture didn't anticipate scale
- Why? → No performance testing in early stage
ROOT CAUSE: Architecture designed for 100 users, not 10,000

PHASE 2 (First Principles):
Elements: Users, Products, Cart, Orders, Payment
Fundamentals:
  - What MUST happen? → Validate items + Process payment
  - What's optional? → Real-time inventory, recommendations
  - What's parallelizable? → Inventory check, tax calc, shipping
SOLUTION: Async architecture + caching + batch queries

PHASE 3 (PDCA):
Plan: Implement async + Redis cache + query optimization
Do: Deploy to staging, test with load
Check: Response time 3s → 300ms ✅, but cache invalidation bug ❌
Act: Fix invalidation, redeploy, monitor
  → Iterate until stable 250ms average
```

**Outcome**: Sustainable 10x performance improvement with continuous monitoring

---

### Pattern 2: Strategic Planning Full Stack

**Workflow**: `Problem Definition → SWOT → 2x2 Matrix → GAP Analysis → OODA Loop`

**Use when**: Business strategy from assessment to execution monitoring

**Complexity**: Complex | **Time**: 3-5 hours (initial), then ongoing | **Success Rate**: 90%

**Process**:
```
PHASE 1: Problem Definition
  ↓ Clarify true strategic challenge

PHASE 2: Situational Analysis (SWOT)
  ↓ Strengths, Weaknesses, Opportunities, Threats

PHASE 3: Prioritization (2x2 Matrix)
  ↓ Maximize Strengths vs Address Weaknesses × High/Low Priority

PHASE 4: Execution Planning (GAP Analysis)
  ↓ Current → Target → Action plan

PHASE 5: Execution Monitoring (OODA Loop)
  ↓ Observe → Orient → Decide → Act (rapid iteration)
```

**Real Example**: SaaS Startup Market Entry

```markdown
PHASE 1 (Problem Definition):
REAL PROBLEM: "How to achieve product-market fit in 6 months with $500K runway"
(NOT "How to get more customers" ← symptom)

PHASE 2 (SWOT):
Strengths: Strong technical team, unique AI algorithm
Weaknesses: No sales process, unknown brand, expensive CAC
Opportunities: Market growing 40% YoY, competitors expensive
Threats: 3 well-funded competitors entering, recession risk

PHASE 3 (2x2 Matrix):
High Priority:
  A (Maximize Strength): Open-source AI library → developer community
  B (Address Weakness): 5 pilot partnerships → testimonials + PR
Low Priority:
  C (Strength): Long-term R&D on advanced features
  D (Weakness): Ignore enterprise sales (focus SMB first)

PHASE 4 (GAP Analysis):
Current: 0 paying customers, 3 months runway, 2 inbound/week
Target: 50 customers, $50K MRR, 12 months runway, 50 inbound/week
Actions:
  - Month 1: Launch open-source, activate community
  - Month 2: Close 5 pilot partners, get case studies
  - Month 3: PR push, inbound optimization
  - Month 4-6: Scale what works, raise bridge round

PHASE 5 (OODA Loop - Weekly):
Week 1: Observe (10 GitHub stars, 2 pilots interested)
        Orient (developer community slower than expected)
        Decide (double down on partnerships, adjust OSS)
        Act (reach out to 20 more prospects)

Week 2: Observe (1 pilot signed, 50 GitHub stars)
        Orient (momentum building, testimonial ready)
        Decide (accelerate PR push)
        Act (submit to TechCrunch, ProductHunt)
        ... iterate weekly
```

**Outcome**: Adaptive strategy with rapid feedback loops, achieves PMF in 5 months

---

### Pattern 3: Innovation Pipeline (User-Centric Product Development)

**Workflow**: `Design Thinking (Empathize/Define) → SCAMPER (Ideate) → TRIZ (Optimize) → Pareto (Prioritize)`

**Use when**: Creating new product/feature with user needs + technical constraints

**Complexity**: Complex | **Time**: 1-2 weeks | **Success Rate**: 88%

**Process**:
```
PHASE 1: User Research (Design Thinking - Empathize/Define)
  ↓ Understand users, define problem from their perspective

PHASE 2: Ideation (SCAMPER)
  ↓ Generate variations: Substitute, Combine, Adapt, Modify, etc.

PHASE 3: Constraint Resolution (TRIZ)
  ↓ Solve technical contradictions (e.g., fast vs reliable)

PHASE 4: Prioritization (Pareto)
  ↓ Identify critical 20% of features for 80% impact
```

**Real Example**: Mobile Banking App Redesign

```markdown
PHASE 1 (Design Thinking):
Empathize:
  - Interviews with 20 users: "Transfers are scary, afraid of mistakes"
  - Observation: Users triple-check recipient, amount
Define:
  - POV: Users need confidence that transfers will succeed correctly
  - HMW: How might we provide transfer confidence without slowing process?

PHASE 2 (SCAMPER):
Substitute: What if visual confirmation instead of text?
Combine: Recipient photo + amount in one confirmation screen?
Adapt: Use voice confirmation like Alexa?
Modify: Add "undo" window like Gmail?
Put to other use: Save frequent recipients as "favorites"?
Eliminate: Remove multi-step confirmation, use single smart confirm?
Reverse: What if we show what WON'T happen (wrong accounts grayed out)?

IDEAS: 12 concepts generated

PHASE 3 (TRIZ - Resolve Contradictions):
Contradiction: Need speed ↑ but also confidence (safety) ↑
TRIZ Principles Applied:
  - #15 Dynamics: Adaptive confirmation (simple for small $ fast, detailed for large $ slow)
  - #10 Prior Action: Pre-validate recipient (green checkmark for saved contacts)
  - #6 Universality: One screen does multiple jobs (shows who, how much, when)

SOLUTION: Smart confirmation screen with visual + adaptive detail

PHASE 4 (Pareto):
Analyze user data:
  - 80% of transfers: saved recipients, < $100
  - 15% of transfers: new recipients, any amount
  - 5% of transfers: large amounts > $1000

PRIORITIZE (20% features, 80% impact):
  1. Visual confirmation for saved recipients (covers 80%) - MUST HAVE
  2. Smart confidence bar for new/large transfers (covers risky 20%) - MUST HAVE
  3. Undo window (nice-to-have but high confidence boost) - SHOULD HAVE
  4. Voice confirmation (innovative but low ROI) - DEPRIORITIZE
```

**Outcome**: User-validated, technically sound, prioritized product roadmap

---

### Pattern 4: Complex System Debugging (Multi-Factor Issues)

**Workflow**: `Fishbone → Pareto → 5 Why → First Principles`

**Use when**: Systemic problems with multiple contributing factors, unclear priority

**Complexity**: Complex | **Time**: 2-4 hours | **Success Rate**: 92%

**Process**:
```
PHASE 1: Map All Factors (Fishbone)
  ↓ Identify People, Process, Technology, Environment factors

PHASE 2: Prioritize Factors (Pareto)
  ↓ Which 20% of factors cause 80% of impact?

PHASE 3: Root Cause Drill-Down (5 Why)
  ↓ For top factors, find fundamental cause

PHASE 4: Systemic Solution (First Principles)
  ↓ Reconstruct system to prevent recurrence
```

**Real Example**: DevOps Pipeline Failures (30% failure rate)

```markdown
PHASE 1 (Fishbone):
Categories:
  PEOPLE: Junior devs unfamiliar with CI/CD, on-call fatigue
  PROCESS: No code review for config, manual rollback steps
  TECHNOLOGY: Flaky tests, old Jenkins version, Docker cache issues
  ENVIRONMENT: Staging ≠ production, resource contention

PHASE 2 (Pareto - Analyze 100 recent failures):
Root causes:
  - Flaky tests (timeout): 45 failures (45%) ← TOP
  - Environment drift: 25 failures (25%) ← TOP
  - Config errors: 18 failures (18%)
  - Resource issues: 8 failures (8%)
  - Other: 4 failures (4%)

INSIGHT: Fix top 2 = address 70% of failures

PHASE 3 (5 Why on "Flaky Tests"):
- Why timeout? → Tests wait for external API (mock.api.com)
- Why external API? → Integration tests need real responses
- Why real responses? → No proper mocking framework
- Why no mocking? → Team didn't know how to mock complex OAuth flows
- Why didn't know? → No senior DevOps mentor, no training

ROOT: Knowledge gap + technical debt (no mocking framework)

PHASE 3b (5 Why on "Environment Drift"):
- Why drift? → Staging updated manually, prod via Terraform
- Why manual? → "Faster to test things manually"
- Why faster? → Terraform apply takes 15 minutes
- Why 15 min? → Recreates entire infrastructure each time
- Why recreates? → Terraform state not properly managed

ROOT: Terraform misuse + lack of infrastructure-as-code discipline

PHASE 4 (First Principles - Systemic Redesign):
Elements: Code, Tests, Build, Deploy, Monitor
Fundamentals:
  - MUST: Every env identical (staging = prod)
  - MUST: Tests isolated (no external deps)
  - SHOULD: Fast feedback (< 5 min build)

SOLUTION ARCHITECTURE:
1. Mocking layer: Implement OAuth mock framework (addresses flaky tests)
2. IaC enforcement: Staging via Terraform too + state locking (fixes drift)
3. Test optimization: Parallel execution + Docker layer caching (speed)
4. Knowledge: Weekly DevOps workshops + runbooks (prevent recurrence)

IMPLEMENTATION PRIORITY:
  Week 1: Mocking framework (addresses 45% failures)
  Week 2: Staging IaC parity (addresses 25% failures)
  Week 3: Test optimization
  Week 4: Documentation + training
```

**Outcome**: Failure rate 30% → 5% in 4 weeks, sustainable process established

---

### Pattern 5: Rapid Response to Emerging Crisis

**Workflow**: `OODA Loop → Fishbone → 5 Why → PDCA`

**Use when**: Fast-moving situation requiring immediate action + systematic fix

**Complexity**: Medium-Complex | **Time**: Immediate (hours) + follow-up (days) | **Success Rate**: 86%

**Process**:
```
PHASE 1: Immediate Response (OODA Loop - Minutes to Hours)
  ↓ Observe → Orient → Decide → Act RAPIDLY

PHASE 2: Situation Mapping (Fishbone - Hours)
  ↓ Once stabilized, map all contributing factors

PHASE 3: Root Cause (5 Why - Hours)
  ↓ Find fundamental cause to prevent recurrence

PHASE 4: Permanent Fix (PDCA - Days to Weeks)
  ↓ Plan → Do → Check → Act until systemically resolved
```

**Real Example**: Security Breach Detection

```markdown
PHASE 1 (OODA Loop - 0-2 hours):
Observe: Alert - 1000 failed login attempts from unknown IPs
Orient: Potential credential stuffing attack, user DB may be compromised
Decide: Immediate lockdown - block IPs, force password resets, enable MFA
Act: Deploy IP blocks, email users, activate incident response team

  → ITERATE (30 min later):
Observe: Attack stopped, but 5 accounts had suspicious access
Orient: Accounts from last week's phishing attempt
Decide: Revoke those sessions, forensics on accessed data
Act: Session revocation, audit logs analysis

  → Crisis contained in 2 hours

PHASE 2 (Fishbone - Hours 2-4):
Categories:
  PEOPLE: Users fell for phishing, support team slow to escalate
  PROCESS: No automated breach detection, manual IP blocking
  TECHNOLOGY: No rate limiting on login, MFA not enforced, old auth library
  ENVIRONMENT: Cloud firewall rules too permissive

PHASE 3 (5 Why - Hours 4-6):
- Why credential stuffing? → Users reused passwords from breached sites
- Why reused? → No password manager, no password complexity enforcement
- Why no enforcement? → Legacy auth system didn't support it
- Why legacy? → "Too risky to touch auth, might break login"
- Why risky? → No comprehensive test coverage for auth flows

ROOT: Technical debt in auth system + lack of security-first culture

PHASE 4 (PDCA - Week 1-4):
Plan:
  - Immediate: Rate limiting, IP reputation service, MFA enforcement
  - Short-term: Upgrade auth library, add security tests
  - Long-term: Security training, breach simulation drills

Do (Week 1):
  - Implement rate limiting (Cloudflare)
  - Enable MFA for all users
  - Add auth test coverage to 80%

Check (Week 2):
  - No breach attempts bypassed rate limiting ✅
  - MFA adoption: 60% (target 90%) ❌
  - Tests catching edge cases ✅

Act (Week 3):
  - Incentivize MFA (offer premium features)
  - Continue auth lib upgrade
  - Schedule red team exercise

  → Iterate until security posture satisfactory
```

**Outcome**: Crisis resolved in hours, systemic vulnerability closed in weeks

---

## 🎨 Advanced Combination Strategies

### Strategy 1: Parallel Methods (Multiple Perspectives)

**Use when**: Need different angles on same problem

**Example**: Architecture Decision
```
Run in parallel:
  - SWOT: Internal/external factors
  - First Principles: Fundamental requirements
  - Kepner-Tregoe: Systematic option comparison

Then synthesize: Dialectic (integrate opposing views)
```

### Strategy 2: Iterative Deepening (Progressive Refinement)

**Use when**: Initial method reveals need for deeper analysis

**Example**: Process Optimization
```
Round 1: Pareto → Identify top 20% issues
Round 2: 5 Why → Find root causes of top issues
Round 3: First Principles → Redesign problematic processes
Round 4: PDCA → Implement + iterate
```

### Strategy 3: Validation Chain (Cross-Check Outputs)

**Use when**: High-stakes decisions need multiple validations

**Example**: Strategic Investment
```
SWOT → GAP Analysis → Kepner-Tregoe → Dialectic
Each method validates previous outputs
Final decision has 4-layer validation
```

---

## 🚫 Anti-Patterns (What NOT to Do)

### ❌ Anti-Pattern 1: Kitchen Sink Approach
**Description**: Using all 15 methods for every problem
**Why bad**: Over-engineering, analysis paralysis, wasted time
**Fix**: Select 2-4 methods maximum based on problem phases

### ❌ Anti-Pattern 2: Incompatible Combinations
**Examples**:
- DMAIC (process quality) + SCAMPER (creative ideation) for same goal
- Kepner-Tregoe (systematic decision) + Dialectic (synthesis) on simple choice
**Why bad**: Methods fight each other, conflicting outputs
**Fix**: Check method compatibility in [INDEX.md](INDEX.md)

### ❌ Anti-Pattern 3: Skipping Validation Between Methods
**Description**: Method A output → Method B input without checking
**Why bad**: Garbage in, garbage out; errors compound
**Fix**: Validate each method's output before proceeding

### ❌ Anti-Pattern 4: Forcing Linear Sequences
**Description**: Rigid "always do A then B then C" without adaptation
**Why bad**: Real problems aren't linear; need flexibility
**Fix**: Use OODA mindset - observe results, orient, decide next method

---

## 📊 Combination Selection Matrix

| Problem Type | Primary Method | Complement With | Total Time | Outcome |
|--------------|----------------|-----------------|------------|---------|
| **Technical debt** | 5 Why | First Principles + PDCA | 2-3 hrs | Sustainable fix |
| **Business strategy** | SWOT + 2x2 | GAP Analysis + OODA | 3-5 hrs | Execution plan |
| **Product innovation** | Design Thinking | SCAMPER + TRIZ + Pareto | 1-2 weeks | Validated roadmap |
| **System failure** | Fishbone | Pareto + 5 Why + First Principles | 2-4 hrs | Root fix |
| **Crisis response** | OODA Loop | Fishbone + 5 Why + PDCA | Hours-weeks | Quick + permanent |
| **Architecture decision** | First Principles | Kepner-Tregoe + Dialectic | 3-4 hrs | Validated choice |
| **Market entry** | SWOT | GAP + OODA + Pareto | 4-6 hrs | Adaptive strategy |

---

## ✅ Combination Best Practices

### 1. Start with Problem Definition
**Always**: Begin with [Problem Definition](problem-definition.md) before any combination
**Why**: Ensures you're solving the right problem with right methods

### 2. Map Before Combining
```
Phase 1: Analysis (understand) → 5 Why, Fishbone, SWOT
Phase 2: Ideation (create) → SCAMPER, TRIZ, First Principles, Design Thinking
Phase 3: Execution (act) → GAP, PDCA, OODA
Phase 4: Synthesis (integrate) → Dialectic, 2x2 Matrix
```

### 3. Validate Between Methods
- Document each method's output
- Check: "Does this output logically feed next method?"
- Resolve contradictions before proceeding

### 4. Use OODA Mindset
- After each method: Observe results, Orient (did it work?), Decide next step
- Don't be rigid - adapt sequence based on what you learn

### 5. Know When to Stop
- Quality check: "Is this sufficient to make decision/take action?"
- Don't combine for the sake of combining
- 2-4 methods usually sufficient; >5 = likely over-engineering

---

## 🎯 Quick Start: Choose Your Combination

**Need root cause + solution?** → Pattern 1 (5 Why → First Principles → PDCA)

**Planning business strategy?** → Pattern 2 (SWOT → 2x2 → GAP → OODA)

**Developing new product?** → Pattern 3 (Design Thinking → SCAMPER → TRIZ → Pareto)

**Debugging complex system?** → Pattern 4 (Fishbone → Pareto → 5 Why → First Principles)

**Responding to crisis?** → Pattern 5 (OODA → Fishbone → 5 Why → PDCA)

**Custom combination?** → Follow [Best Practices](#-combination-best-practices) above

---

## 📚 Related Resources

- **Single Method Selection**: [QUICK_SELECTOR.md](QUICK_SELECTOR.md)
- **Method Catalog**: [INDEX.md](INDEX.md)
- **User Guide**: [GUIDE.md](../GUIDE.md)
- **AI Execution**: [SKILL.md](../SKILL.md)

---

**Version**: 2.2.0
**Last Updated**: 2025-11-07
**Purpose**: Multi-method workflow patterns for complex problem-solving
**Key Principle**: "Combine methods strategically, not mechanically"
