# Research Tips by Thinking Method

How to effectively collect evidence for each thinking method

---

## 🔍 Root Cause Analysis

### 5 Why Research Strategy

**Goal**: Find evidence at each level of "Why"

**Research Targets**:
```
Why 1 (Symptom): Internal data (what we observe)
Why 2 (Cause): System logs, metrics
Why 3-4 (Depth): Industry cases, expert resources
Why 5 (Root): Principles, theories, benchmarks
```

**Recommended Sources**:
- **Tier 1**: Our actual data, internal logs
- **Tier 2**: Competitor case analysis, industry reports
- **Tier 3**: Forum discussions, technical blogs

**Example**: Slow API response time
```
Why 1: Database query takes 1800ms
  → Evidence: Our APM tool data

Why 2: Full table scan occurring
  → Evidence: Query execution plan analysis

Why 3: Missing index
  → Evidence: Migration checklist review

Why 4: No performance testing
  → Evidence: Other companies' success cases (Tier 2)

Why 5: Inadequate deployment process
  → Evidence: DevOps best practices documents (Tier 1)
```

---

### Fishbone Research Strategy

**Goal**: Collect evidence across 6 categories

**Research by Category**:

```
1. People
   └─ Research: Team capabilities, education level, industry standards
      Sources: HR data, training reports

2. Process
   └─ Research: Workflows, checklists, best practices
      Sources: Internal documents, industry standards

3. Technology
   └─ Research: Tool selection, configuration, versions
      Sources: Official documentation, technical blogs

4. Materials
   └─ Research: Data quality, libraries, dependencies
      Sources: Our inventory, vendor guides

5. Environment
   └─ Research: System resources, infrastructure, network
      Sources: Monitoring tools, system logs

6. Measurement
   └─ Research: Metrics definition, monitoring, alerts
      Sources: Our dashboards, industry standards
```

**Priority**: Investigate high-impact categories first

---

## 💡 Innovation

### SCAMPER Research Strategy

**Goal**: Find examples for each modification approach

**Research by Question**:

```
S (Substitute - Replace):
  Q: How do similar things work differently in other industries?
  Research: Adjacent industry cases, innovation examples

C (Combine - Combine):
  Q: Are there products that combine similar features?
  Research: Integrated product analysis, feature combination cases

A (Adapt - Adapt):
  Q: What has succeeded in different contexts?
  Research: Cross-industry cases, regional examples

M (Modify - Modify):
  Q: What happens when you change attributes?
  Research: Modified product performance, A/B test results

P (Put to another use - Different use):
  Q: Are there examples of using this differently?
  Research: Creative user examples, pivot cases

E (Eliminate - Remove):
  Q: Can it work without core features?
  Research: Minimum viable product (MVP) success cases

R (Reverse - Reverse):
  Q: What happens if you reverse it?
  Research: Reverse-engineering products, market reactions
```

**Recommended Research Sources**:
- **Tier 1**: Official market analysis, academic papers
- **Tier 2**: Successful startup blogs, industry cases
- **Tier 3**: Product Hunt, user reviews

---

### First Principles Research Strategy

**Goal**: Find evidence to validate fundamental assumptions

**Process**:

```
1. Identify core assumptions
   Research: Are our assumptions universal?
   Sources: Industry standards, scientific materials

2. Validate each assumption
   Research: Is this actually true? What are alternatives?
   Sources: Academic papers, experimental data

3. Confirm fundamental principles
   Research: What are the physical/economic laws?
   Sources: Textbooks, scientific papers

4. Reconstruct
   Research: Examples of reconstructing this way
   Sources: Disruptive innovation cases
```

**Example**: "Cars must run on gasoline"

```
Assumption 1: Energy is required → Confirmed (energy physics)
Assumption 2: Only gasoline works → False
  Evidence: Electric vehicles, hydrogen cars in practical use (Tesla, Toyota)

Reconstruction: Diversity of energy storage media → Electric vehicle innovation
```

---

## 🎯 Strategic Planning

### SWOT Research Strategy

**Research Depth by Element**:

```
Strengths:
├─ Internal evidence: Financial, technical data
└─ External validation: Customer feedback, competitive analysis

Weaknesses:
├─ Internal assessment: Our evaluation
└─ External benchmark: Competitors, industry standards

Opportunities:
├─ Market research: Market size, growth rate
└─ Trends: Technology, consumer behavior changes

Threats:
├─ Competitor analysis: Competitor strategy, market entry
└─ External factors: Regulation, economic changes
```

**How to Build High-Credibility SWOT**:

1. **Strengths/Weaknesses**: Data-driven (internal metrics)
2. **Opportunities**: Market research (Tier 1-2 reports)
3. **Threats**: Competitor analysis (public information + industry reports)

**What to Avoid**:
- ❌ Subjective opinions only (no evidence)
- ❌ Outdated materials (doesn't reflect trends)
- ❌ Single source only (insufficient verification)

---

### GAP Analysis Research Strategy

**Goal**: Quantify the distance from current → desired state

```
Current State Measurement:
├─ Internal data (our metrics)
└─ External benchmark (competitors, industry)

Target State Setting:
├─ Market research (achievable level)
└─ Vision (our ambitions)

Gap Analysis:
├─ Capability gap: Technology/talent shortage
├─ Resource gap: Budget/time shortage
└─ Process gap: Methodology changes needed
```

**Research Priorities**:
1. Accurate measurement of our current state
2. Competitor/industry benchmarks
3. Best-in-class examples

---

## ⚙️ Process Improvement

### Pareto Research Strategy

**Goal**: Validate the 80/20 principle with data

**Process**:

```
1. Data collection
   └─ Accurate measurement of current state (internal data)

2. Classification and sorting
   └─ Sort by impact

3. Calculate cumulative percentage
   └─ Identify top 20%

4. Benchmark comparison
   └─ Compare with industry standards (Tier 2 data)

5. Study improvement cases
   └─ Other companies' improvement results (Tier 2-3 cases)
```

**High-Confidence Pareto**:
- ✅ Minimum 1+ month of data
- ✅ Sufficient sample size (minimum 100 incidents)
- ✅ Validation with external benchmarks
- ❌ Subjective categorization
- ❌ Insufficient data

**Example**: Customer satisfaction improvement

```
Complaint frequency by type:
- Slow response: 45% ← Top 20% in Pareto
- Inaccurate information: 28% ← Top 20% in Pareto
- Rude customer support: 12%
- Other: 15%

Top 2 = 73% can be resolved
→ Concentrate resources on these two areas

Benchmark: Similar companies reduced churn by 30% through similar improvements
→ We can expect similar results
```

---

### PDCA Research Strategy

**Evidence Collection by Stage**:

```
Plan (Plan):
├─ Evidence: Historical data, industry cases
├─ Hypothesis: Improving this will result in X% improvement
└─ Research: Similar improvement cases

Do (Execute):
├─ Measurement: Accurate data collection
└─ Record: Detailed logging

Check (Verify):
├─ Comparison: Plan vs actual
├─ Root cause analysis: Why the difference?
└─ External verification: Validate our results with benchmarks

Act (Improve):
├─ Adjust: Revise the plan
├─ Scale: Generalize successful areas
└─ Learn: Reflect for next cycle
```

**High-Confidence PDCA**:
- Minimum 2-3 cycles (confirm it's not short-term luck)
- Comparison with external benchmarks
- Both qualitative and quantitative evidence

---

## ⚡ Decision Making

### OODA Loop Research Strategy

**Fast Decision-Making + Evidence Balance**:

```
Observe (Observe):
├─ Real-time data (primary information)
└─ Time constraint: Only essential information

Orient (Orient):
├─ Experience-based judgment
└─ Similar past situations (quick retrieval)

Decide (Decide):
├─ Decide with 70% information (don't wait for perfection)
└─ Risk calculation: Decision delay vs incomplete decision

Act (Act):
├─ Fast execution
└─ Continuous monitoring
```

**Research in OODA**:
- Pre-preparation: Industry standards, experience accumulation
- During observation: Real-time data only (speed priority)
- Result verification: Deep analysis afterward

---

### Kepner-Tregoe Research Strategy

**Goal**: Evidence-based analysis for systematic decision-making

```
Problem Analysis:
├─ What is the problem?
├─ Where does it occur?
├─ When does it occur?
└─ Research: Objective facts (documentation, data)

Cause Analysis:
├─ List possible causes
├─ Evaluate probability of each cause
└─ Research: Scientific evidence

Decision Analysis:
├─ Possible options
├─ Pros and cons of each option
├─ Risk assessment
└─ Research: Case analysis, benchmarks
```

**High-Confidence Kepner-Tregoe**:
- Tier 1 problem analysis (facts only)
- Tier 2 cause analysis (testing/verification)
- Tier 1-2 decision-making (cases/benchmarks)

---

## 🤝 Integration (Synthesis)

### Dialectic Research Strategy

**Goal**: Validate both opposing perspectives

```
Thesis (Argument):
└─ Research: Evidence for perspective A

Antithesis (Counter-argument):
└─ Research: Evidence for perspective B

Synthesis (Integration):
└─ Research: Cases integrating both perspectives
   (historical cases, organizational change cases, etc.)
```

**Example**: Innovation vs Stability

```
Thesis: "Fast innovation is the key to growth"
  Evidence: Tesla, Amazon, and other rapid innovation companies

Antithesis: "Stability and quality are important"
  Evidence: Toyota quality philosophy, safety-focused airlines

Synthesis: "Balance between innovation and stability"
  Evidence: Amazon - Speed + Stability
           Toyota - Innovation + Quality prioritization
```

---

## 📊 Information Sources Guide

### Efficient Research Planning

**Research depth by time allocation**:

```
30-minute research:
├─ Internal data (required)
└─ 1-2 online resources

2-hour research:
├─ Internal analysis
├─ 3-5 Tier 2 sources
└─ 1 Tier 1 resource

1-day research:
├─ Deep internal analysis
├─ 10+ sources (diverse perspectives)
├─ Tier 1-2 resources
└─ Expert interviews
```

### Best credibility information by source

**Information available from Tier 1 sources**:
```
Academic papers → Principles, theories, scientific evidence
Government data → Market size, regulations, statistics
Official documentation → Technical specifications, vendor benchmarks
Official announcements → Company performance, strategy
```

**Information available from Tier 2 sources**:
```
Industry reports → Market analysis, trends
Expert blogs → Case studies, practical experience
Trusted media → News, in-depth reports
Conferences → Latest trends, case studies
```

**Information available from Tier 3-4 sources**:
```
User forums → Real user experience, problems
Social media → Real-time reactions, sentiment
Blogs/comments → Diverse perspectives, opinions
```

---

## 🎯 Research Efficiency Tips

### Research Checklist

```
[ ] Is time constraint clear?
[ ] Is the required information specific?
[ ] Are source credibility criteria established?
[ ] Is the internal/external information ratio appropriate?
[ ] Have multiple perspectives been collected?
[ ] Have conflicting information sources been verified?
```

### Tips for quick research

1. **Specific questions**: "Is the market big?" (✗) vs "What is our segment's market size?" (✓)
2. **Source prioritization**: Find Tier 1 first (high credibility)
3. **Quick verification**: Cross-check with minimum 2 sources
4. **Sufficiency mindset**: Perfection not required, 60%+ confidence enables decision-making

---

**Version**: 1.0.0
**Last Updated**: 2025-11-07
**Purpose**: Practical research methodology by thinking method
