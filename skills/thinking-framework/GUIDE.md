# Thinking Framework - Practical User Guide

**🚀 NEW in v3.0**: Adaptive Sequential Thinking MCP integration - automatically enhances complex analysis with structured multi-step reasoning

**🚀 NEW in v2.2**: [60-Second Quick Selector](reference/QUICK_SELECTOR.md) - Select the right method without reading all docs!

**Quick navigation**: Need immediate help? Jump to [Quick Selector](reference/QUICK_SELECTOR.md) | [Problem Type Selector](#problem-type-selector) | [Common Mistakes](#common-mistakes-and-solutions)

---

## What Is This?

The Thinking Framework provides 15 proven problem-solving methods in a structured system. Instead of ad-hoc thinking, you'll systematically approach problems using battle-tested methodologies.

**v3.0 Enhancement**: When using AI-assisted analysis (SKILL.md), complex problems automatically benefit from Sequential Thinking MCP integration - exposing transparent reasoning chains, enabling hypothesis testing, and achieving higher quality analysis. Works perfectly with or without MCP available.

**Core principle**: "All problem-solving begins with correctly defining the problem." Use [Problem Definition](reference/problem-definition.md) FIRST, then select the appropriate specialized method.

**When to use**: Complex problems, strategic decisions, root cause analysis, innovation challenges, process improvements, or anytime you want to ensure you're solving the RIGHT problem.

**When NOT to use**: Simple questions with obvious answers, straightforward tasks, basic information lookups, or emergency situations requiring immediate action (use OODA Loop instead, then circle back to proper problem definition).

---

## The Starting Point: Problem Definition

**BEFORE anything else**, clarify what the real problem is:

→ **[Problem Definition Thinking](reference/problem-definition.md)**

**Why first?** Most problem-solving failures come from solving the wrong problem. Spend 30-60 minutes clarifying:
- Is this the real problem or a symptom?
- What evidence supports this?
- What are the hidden assumptions?
- How will you measure success?

**Example**: "Our API is slow" (symptom) → "Missing database index on user_id column" (real problem)

---

## Problem Type Selector

### 🔍 "I need to find WHY something happened"
→ **Root Cause Analysis** (use AFTER Problem Definition)

**Start with**: [5 Why](reference/5-why.md) (single cause) or [Fishbone](reference/fishbone.md) (multiple factors)

**Example scenarios**:
- Production bug investigation
- Customer churn analysis
- Performance degradation
- Process failure

**Quick decision**: If you can trace a single chain of causation, use 5 Why. If multiple systems/factors are involved, use Fishbone.

---

### 💡 "I need to innovate or create something new"
→ **Creative Innovation**

**Start with**:
- [SCAMPER](reference/scamper.md) - Quick modification of existing ideas (15-30 min)
- [Design Thinking](reference/design-thinking.md) - User-centric innovation (days/weeks)
- [First Principles](reference/first-principles.md) - Breakthrough innovation (1-2 hours)
- [TRIZ](reference/triz.md) - Technical contradictions (30-60 min)

**Quick decision tree**:
```
Improving existing product? → SCAMPER
Creating for users? → Design Thinking
Challenging fundamental assumptions? → First Principles
Engineering problem with trade-offs? → TRIZ
```

**⚠️ AVOID**: DMAIC, Kepner-Tregoe (0% success rate for creative problems)

---

### 🎯 "I need to plan strategy or make decisions"
→ **Strategic Planning**

**Start with**: [SWOT](reference/swot.md) + [GAP Analysis](reference/gap-analysis.md)

**Critical requirement**: When using SWOT for strategic decisions, you MUST add a 2x2 priority matrix (33% failure rate without it).

**Example scenarios**:
- Business strategy
- Product roadmap
- Market entry planning
- Competitive positioning

**Process**:
1. SWOT to assess situation
2. Create 2x2 matrix (Maximize Strengths vs Address Weaknesses × High/Low Priority)
3. GAP Analysis to plan execution (Current → Target → Action Plan)

---

### ⚙️ "I need to improve a process or workflow"
→ **Process Improvement**

**Start with**:
- [Pareto](reference/pareto.md) - Identify top 20% of issues (requires data)
- [PDCA](reference/pdca.md) - Iterative improvement cycles
- [GAP Analysis](reference/gap-analysis.md) - Goal-oriented planning

**Quick decision**:
- Have quantitative data? → Pareto (prioritize critical few)
- Need continuous improvement? → PDCA (iterative cycles)
- Clear target state? → GAP Analysis (bridge planning)

---

### ⚡ "I need to make fast decisions"
→ **Decision Making**

**Start with**:
- [OODA Loop](reference/ooda-loop.md) - Rapid iteration (minutes to hours)
- [Kepner-Tregoe](reference/kepner-tregoe.md) - Systematic analysis (1-2 hours)

**Quick decision**: Time-sensitive and dynamic? → OODA Loop. High-stakes requiring thorough analysis? → Kepner-Tregoe.

---

### 🤝 "I need to resolve conflicting viewpoints"
→ **Synthesis & Integration**

**Start with**: [Dialectic Synthesis](reference/dialectic.md)

**When to use**: Both sides have legitimate points that need integration, not just a choice between them.

**⚠️ AVOID**: Using for simple problems (over-engineering)

---

## Real-World Examples

### Example 1: Startup Running Out of Money

**Problem**: 3 months of runway left, unclear path to profitability

**Method Selection**: Strategic Planning (SWOT + GAP)

**Process**:
1. **SWOT Analysis**:
   - Strengths: Strong technology, passionate team
   - Weaknesses: No sales process, expensive burn rate
   - Opportunities: Market growing 40% YoY
   - Threats: Well-funded competitors entering

2. **2x2 Priority Matrix**:
   ```
   High Priority:
   - Maximize Strength: Leverage tech via open-source strategy
   - Address Weakness: Build sales process via partnerships

   Low Priority:
   - Strength: Long-term R&D
   - Weakness: Ignore non-critical gaps (e.g., enterprise features)
   ```

3. **GAP Analysis**:
   - Current: $0 MRR, 3 months runway
   - Target: $50K MRR, 12 months runway
   - Actions: 5 pilot partnerships (60 days), raise bridge round (45 days)

**Outcome**: Clear 90-day action plan with prioritized initiatives

---

### Example 2: Production Outage Investigation

**Problem**: API response time increased from 100ms to 2000ms

**Method Selection**: Root Cause Analysis (5 Why)

**Process**:
- **Why 1**: Why is response time slow? → Database queries taking 1800ms
- **Why 2**: Why are queries slow? → Full table scans on orders table
- **Why 3**: Why full table scans? → Missing index on `user_id` column
- **Why 4**: Why is index missing? → Recent migration didn't include it
- **Why 5**: Why wasn't it caught? → No performance testing in staging

**Root Cause**: Missing performance testing in deployment pipeline

**Fix**: Add index (immediate), implement load testing (prevent future)

---

### Example 3: Product Innovation Under Constraint

**Problem**: Need faster product delivery but higher speed reduces reliability

**Method Selection**: Creative Innovation (TRIZ)

**Contradiction**: Speed ↑ vs Reliability ↓

**TRIZ Principles Applied**:
- #10 Prior Action: Pre-deploy assets closer to users (CDN)
- #3 Local Quality: Critical paths get reliability focus, non-critical get speed
- #15 Dynamics: Adaptive speed based on user context

**Solution**: Hybrid approach with CDN + critical path optimization + adaptive delivery

---

### Example 4: Improving Customer Support

**Problem**: Customer satisfaction declining, too many issues to fix

**Method Selection**: Process Improvement (Pareto)

**Data Collection** (1 month):
- Complaint A (slow response): 450 cases (45%)
- Complaint B (wrong info): 280 cases (28%)
- Complaint C (rude staff): 120 cases (12%)
- Other: 150 cases (15%)

**Insight**: A + B = 73% of complaints

**Action**: Focus resources on response time and knowledge base (top 2 issues)

**Result**: 73% reduction potential by fixing just 2 root causes

---

## Common Mistakes and Solutions

### Mistake 0: Skipping Problem Definition
**Symptom**: Solving the problem perfectly but finding it was the wrong problem all along

**Example**: Building a feature that technically solves the stated requirement but doesn't address the actual business need

**Solution**: ALWAYS start with [Problem Definition](reference/problem-definition.md). Spend 30-60 minutes clarifying the real problem before picking a solution method. This prevents weeks of wasted effort.

---

### Mistake 1: Using Wrong Method for Problem Type
**Symptom**: Method feels forced, results unsatisfying

**Examples**:
- Using DMAIC for creative innovation (0% success)
- Using Dialectic for simple problems (over-engineering)
- Using simple methods for complex systems (incomplete analysis)

**Solution**: Refer to [Problem Type Selector](#problem-type-selector) or [reference/INDEX.md](reference/INDEX.md)

---

### Mistake 2: SWOT Without Prioritization
**Symptom**: Long list of items, no clear action plan

**Why it fails**: 33% failure rate when 2x2 priority matrix omitted

**Solution**: ALWAYS add 2x2 matrix (Maximize Strengths vs Address Weaknesses × High/Low Priority)

---

### Mistake 3: Over-Engineering Simple Problems
**Symptom**: Spending 60 minutes on a 5-minute problem

**Why it fails**: Using Divide & Conquer (A Routine) for simple problems = 50% success rate

**Solution**:
- Simple (1-2 steps)? → Use B Routine (5 Why, Pareto)
- Medium (3-5 steps)? → Use B or C Routine
- Complex (5+ interdependent factors)? → Use A Routine

---

### Mistake 4: Stopping at Surface Solutions
**Symptom**: Problem keeps recurring

**Why it fails**: Didn't dig deep enough to root cause

**Solution**:
- Use 5 Why to drill down causal chain
- Use Fishbone for multi-factor analysis
- Don't stop at first explanation

---

### Mistake 5: Skipping Pre-Flight Checks
**Symptom**: Realize mid-analysis that method doesn't fit

**Why it fails**: Complexity mismatch or method-problem incompatibility

**Solution**: Always assess complexity first:
- Simple: Single cause, clear path → B Routine
- Medium: Multiple factors, some ambiguity → B or C Routine
- Complex: Systemic, 5+ factors → A Routine

---

## How to Get Started

### First Time Using This Framework

1. **Identify your problem type** using [Problem Type Selector](#problem-type-selector)
2. **Read the recommended method** in [reference/](reference/) directory
3. **Follow the steps** in the method guide
4. **Reflect** on what worked and what could improve

### Regular Users

- Bookmark [reference/INDEX.md](reference/INDEX.md) for quick method selection
- Review [Common Mistakes](#common-mistakes-and-solutions) periodically
- Experiment with combining methods for complex problems

### Advanced Users

- Study method combinations in [reference/INDEX.md](reference/INDEX.md)
- Use SKILL.md for AI-assisted systematic analysis
- Track success rates for your specific problem types

---

## Quick Reference Card

| Your Situation | Use This | Read |
|----------------|----------|------|
| **ANY problem** (FIRST STEP) | Problem Definition | [Foundational method](reference/INDEX.md#0-foundational-method-use-first) |
| Need to find root cause | 5 Why or Fishbone | [Root cause methods](reference/INDEX.md#1-root-cause-analysis-methods) |
| Need to innovate | SCAMPER, TRIZ, Design Thinking, First Principles | [Innovation methods](reference/INDEX.md#2-innovation--breakthrough-methods) |
| Planning strategy | SWOT + GAP (with 2x2 matrix!) | [Strategic methods](reference/INDEX.md#3-strategic-planning-methods) |
| Improving process | Pareto, PDCA, GAP | [Process methods](reference/INDEX.md#4-process-improvement-methods) |
| Making decisions | OODA Loop, Kepner-Tregoe | [Decision methods](reference/INDEX.md#5-decision-making-methods) |
| Resolving conflict | Dialectic | [Synthesis methods](reference/INDEX.md#6-synthesis--integration-methods) |

---

## Additional Resources

- **🚀 NEW: 60-Second Quick Selector**: [reference/QUICK_SELECTOR.md](reference/QUICK_SELECTOR.md)
- **🚀 NEW: Method Combinations**: [reference/METHOD_COMBINATIONS.md](reference/METHOD_COMBINATIONS.md)
- **Complete method catalog**: [reference/INDEX.md](reference/INDEX.md)
- **AI execution prompts**: SKILL.md (for systematic AI-assisted analysis)
- **Project overview**: README.md
- **Individual methods**: [reference/](reference/) directory

---

**Version**: 3.0.0 (NEW: Adaptive Sequential Thinking MCP integration for 95%+ success rate)
**Last Updated**: 2025-11-07
**Skill Type**: Practical Guide
**Target Audience**: Practitioners and users
**Key Enhancement**: Automatic AI reasoning enhancement with transparent multi-step analysis when MCP available
