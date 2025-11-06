# Market Strategy Reference Guide

## Full 16-Question Framework

### Part A: Entry Point Discovery (Q1-Q4)

#### Q1: What is the "small problem, big pain"?

**Template**:
```
[Problem]:
[User Pain]:
[Existing Limitations]:
[Evidence]:
- User interviews: [N people]
- Surveys: [N responses]
- Competitor reviews: [N analyzed]
```

**Toss Example**:
```
[Problem]: Money transfer complexity
[User Pain]:
- ActiveX installation required
- Certificate + security card needed
- 7-step process (90 seconds)
[Existing Limitations]:
- Banks: Complex UI, mandatory certificates
- KakaoPay: Limited to KakaoTalk users
[Evidence]:
- Interviews: 200 people (85% complained)
- Reviews: 5,000+ reviews analyzed (avg 2.3/5 for banks)
```

#### Q2: Pain Point Score = Frequency × Intensity

**Scoring Guide**:
- **Frequency (1-10)**:
  - 10: Multiple times daily
  - 5: Once daily or 3-5 times/week
  - 3: 1-3 times/week
  - 1: Monthly or less

- **Intensity (1-10)**:
  - 10: Causes financial loss or critical failure
  - 8-9: Significant frustration, time waste (30+ min)
  - 5-7: Moderate annoyance (5-30 min)
  - 1-4: Minor inconvenience (<5 min)

**Threshold**:
- 20+: 🔥 High Priority (Go!)
- 10-20: ⚠️ Medium (Validate more)
- <10: ❌ Low Priority (Avoid)

#### Q3: Current Solutions Analysis

**Competitor Analysis Template**:
```
Competitor A: [Name]
  Strengths: [Top 3]
  Weaknesses: [Top 3]
  User Complaints: [From reviews]
  Market Share: [%]
  Pricing: [Model]

Alternative: [Current workaround]
  Why used: [Reasons]
  Limitations: [Pain points]
  Switching cost: [Barriers]
```

#### Q4: Trojan Horse Strategy

**3-Stage Template**:
```
Stage 0 (Entry): [Low-barrier product]
  - Value: [User gets in 5 minutes]
  - Barrier: [Why easy to try]
  - Data: [What we collect]

Stage 1 (6 months): [Natural expansion]
  - Prerequisite: [MAU or usage threshold]
  - Connection: [Why natural from Stage 0]
  - Revenue: [Business model]

Stage 2 (1-2 years): [Platform play]
  - Prerequisite: [Success metrics]
  - Ecosystem: [Partners or integrations]
  - Defensibility: [Moat created]
```

**Checklist**:
- [ ] Stage 0 provides standalone value
- [ ] Each stage reduces friction for next
- [ ] Data accumulates for expansion
- [ ] Expansion path is obvious to users

---

### Part B: Differentiation Strategy (Q5-Q8)

#### Q5: Friction Mapping (3 Layers)

**Customer Journey**:
1. **Onboarding**: First signup to first value
2. **First Use**: Initial feature experience
3. **Reuse**: Returning user experience

**Measure**:
- Time: Stopwatch or analytics
- Clicks: User testing or session replay
- Cognitive Load: Think-aloud protocol

#### Q6: 10x Improvement Framework

**3 Methods**:
1. **Step Elimination**: Remove 9 of 10 steps
2. **Automation**: Replace manual with AI/detection
3. **Prediction**: Anticipate and pre-fill

**Example (HR Attendance)**:
```
Current: 8 steps, 60 seconds
1. Open app
2. Select date
3. Search employee name
4. Select employee
5. Choose "attendance"
6. Enter time
7. Add note
8. Submit

10x Goal: 1 step, 6 seconds
1. App auto-detects GPS → Logs attendance

Method: Automation (GPS + time detection)
```

#### Q7: "Wow" Moment Design

**3 Components**:
1. **Unexpected**: Exceeds expectations
2. **Immediate**: Happens fast (seconds, not minutes)
3. **Shareable**: User wants to tell others

**Template**:
```
Aha Moment: "[Quote from user test]"
Trigger: After [specific action]
Emotion: [Surprise, delight, relief]
Share Trigger: "[What makes them share]"
Measurement: [% who share within 24h]
```

#### Q8: Viral Coefficient Formula

```
K = i × c
Where:
- K = Viral Coefficient (target: 1.0+)
- i = Invites sent per user
- c = Conversion rate of invites

Example:
- 100 users send 50 invites (i = 0.5)
- 30 sign up from invites (c = 0.6)
- K = 0.5 × 0.6 = 0.3

To reach K = 1.0:
- Increase i to 2.0 (2 invites/user), or
- Increase c to 100% (all invites convert)
```

---

### Part C: Validation (Q9-Q12)

#### Q9: Hypothesis Template

```
Hypothesis: "If [change X], then [metric Y] will [improve by Z%]"

Success Criteria: [Metric Y] ≥ [Target]
Failure Criteria: [Metric Y] < [Baseline] OR [Critical metric drops]
Validation Method: [A/B test, user test, rollout]
Timeline: [1-2 weeks max]
Sample Size: [Minimum N for significance]
```

**Example**:
```
Hypothesis: "If GPS auto-attendance, then signup conversion will increase by 100%"

Success: Conversion ≥ 20% (current 10%)
Failure: Conversion < 10% OR Retention D7 drops below 30%
Method: A/B test (50/50 split)
Timeline: 2 weeks
Sample: 200 signups minimum
```

#### Q10: MVP Scope (The "MVP of MVP")

**Rule**: If you can validate hypothesis in 2 weeks with <100 users, it's the right size.

**3-Feature Max**:
```
Core: [Must have to test hypothesis]
Nice-to-have: [Defer to v2]
Polish: [Skip for MVP]
```

#### Q11: Metrics Hierarchy

```
Tier 1: North Star Metric (1 only)
  → Most important indicator of value delivery

Tier 2: Supporting Metrics (3-5)
  → Leading indicators of North Star

Tier 3: Guardrail Metrics (2-3)
  → Ensure you're not breaking things
```

**Example (HR SaaS)**:
```
North Star: Weekly attendance logs per user
  Why: Direct measure of usage = value

Supporting:
- Retention D7: 30%+ (are they coming back?)
- Completion rate: 80%+ (can they use it?)
- Time saved: 10 min/day (real benefit?)

Guardrail:
- Error rate: <5% (is it working?)
- Support tickets: <10/month (frustration check)
```

#### Q12: Experiment Cadence

**Weekly Cycle**:
```
Monday: Review last week + Plan this week (1 hour)
Tue-Thu: Execute experiments
Friday: Analyze data
Weekend: Prepare next Monday's plan

Experiments per week: 2-3 max (focus!)
```

---

### Part D: Expansion (Q13-Q16)

#### Q13: Adjacent Market Selection

**Criteria**:
- [ ] Current users already need it
- [ ] Data synergy exists (reuse what we have)
- [ ] Tech stack reusable (faster to build)
- [ ] Competitive advantage clear (we're better positioned)

#### Q14: Cross-Selling Math

**Formula**:
```
ARPU Growth = Base ARPU × (1 + Cross-sell Rate × Additional ARPU %)

Example:
- Base: $50/month (Product A only)
- Cross-sell Rate: 30% buy Product B
- Product B adds: $30/month
- New ARPU: $50 × (1 + 0.3 × 0.6) = $59/month
```

#### Q15: Regulatory Monitoring

**3 Types**:
1. **Enablers**: Changes that create opportunity (e.g., certificate abolition)
2. **Constraints**: New rules that limit (e.g., data privacy)
3. **Neutral**: No direct impact but industry shift

**Monitoring Checklist**:
- [ ] Weekly: Industry news scan (15 min)
- [ ] Monthly: Regulation review meeting
- [ ] Quarterly: Update product roadmap based on changes

#### Q16: Build vs Partner Decision Matrix

```
        │ Build In-House │ Partner      │
────────┼────────────────┼──────────────┤
Core?   │       ✅       │      ❌      │
Data?   │       ✅       │      ❌      │
Speed?  │       ❌       │      ✅      │
Cost?   │       ❌       │      ✅      │
```

**Build When**:
- Core competency
- Critical data collection
- Long-term competitive advantage

**Partner When**:
- Speed to market critical
- Non-core functionality
- Regulatory/license barriers

---

## Industry Adaptations

### B2B SaaS

**Key Differences**:
- Lower viral coefficients (0.3 is good)
- Longer sales cycles (focus on retention)
- Enterprise requires compliance (Pattern 7 critical)

**Adapted Q8** (Viral Loop):
```
Target: K = 0.3 (not 1.0)
Method: NPS-based referrals + case studies
Measurement: "Would recommend" survey score
```

### E-commerce

**Key Differences**:
- High churn (retention is everything)
- Unit economics critical (Pattern 5 data-driven)
- Fast iteration possible (Pattern 4 viral loops)

**Adapted Q11** (Metrics):
```
North Star: Monthly repeat purchases
Supporting: CAC, LTV, Retention M3
Guardrail: Return rate <10%
```

### Healthcare

**Key Differences**:
- Heavy regulation (Pattern 7 mandatory)
- Low friction critical (Pattern 3)
- Trust > Speed (slower expansion)

**Adapted Q13** (Expansion):
```
Stage 0: Simple symptom checker (low barrier)
Stage 1: Telemedicine (after trust built)
Stage 2: Chronic care management (data moat)
Timeline: 2x longer than typical SaaS
```

---

## Pattern Combinations

### For Seed Stage (Months 0-6)

**Focus**: Patterns 1, 3, 5
- Q1-Q4: Find Pain Point 20+
- Q5-Q6: Achieve 10x improvement
- Q9-Q12: Weekly experiments

**Skip**: Patterns 6, 7 (too early)

### For Series A (Months 6-18)

**Focus**: Patterns 2, 4, 5
- Q4: Execute Trojan Horse expansion
- Q7-Q8: Optimize viral loops
- Q11: Scale metrics tracking

### For Series B+ (18+ months)

**Focus**: Patterns 6, 7
- Q13-Q14: Multi-product cross-selling
- Q15-Q16: Regulatory moats + ecosystem

---

## Common Mistakes

### Mistake 1: "The Score is 15, close enough"

**Problem**: 15 < 20 = Medium priority, not High
**Fix**: Find stronger pain point or increase frequency/intensity

### Mistake 2: "10x is impossible"

**Problem**: Accepting 2x improvement ("good enough")
**Fix**: Use 3 methods (eliminate + automate + predict)

### Mistake 3: "We'll expand after we're big"

**Problem**: No Trojan Horse path = harder growth
**Fix**: Design Stage 0→1→2 from Day 1

### Mistake 4: "Too many experiments = faster learning"

**Problem**: 10 experiments/week = diluted focus
**Fix**: 2-3 experiments max, chosen by impact/effort matrix

---

**See Skill.md for**: Quick reference, examples, worksheets