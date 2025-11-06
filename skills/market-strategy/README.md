# Market Strategy - Custom Skill

A powerful custom skill for Claude that enables systematic market entry and PMF (Product-Market Fit) achievement using Toss's battle-tested 16-question framework.

## What This Skill Does

This skill transforms Claude into a PMF-focused market strategist that:
- **Validates pain points** systematically using Pain Point Score (Frequency × Intensity ≥ 20)
- **Designs Trojan Horse paths** for multi-stage expansion (0 → 1 → 2)
- **Creates 10x better solutions** through extreme friction removal (90% reduction)
- **Validates PMF** via data-driven weekly experiments
- **Scales to ecosystems** with cross-selling strategies (30%+ conversion)

## When Claude Will Use This Skill

Claude will automatically invoke this skill when you:
- Plan market entry or beachhead market selection
- Design product strategy from 0→1 or 1→10
- Need to validate whether a problem is worth solving
- Want to create differentiated solutions (10x better, not 2x)
- Design multi-product expansion roadmaps
- Set up weekly experiment cycles for PMF validation

## File Structure

```
market-strategy/
├── Skill.md          # Main skill definition (REQUIRED)
├── REFERENCE.md      # Detailed guide to 16 questions & industry adaptations
└── README.md         # This file
```

## Installation

### Option 1: Direct Use (Already in skills/)
If this skill is already in your skills/ folder, just ensure Claude Code's Skills feature is enabled.

### Option 2: Export as ZIP for Other Projects

1. **Create ZIP package**:
   ```bash
   cd skills
   zip -r market-strategy.zip market-strategy/
   ```

2. **Upload to Claude.ai or Claude Code**:
   - Go to Settings > Capabilities > Skills
   - Upload `market-strategy.zip`
   - Activate the skill

### Option 3: Share with Others

Share the entire `market-strategy/` directory or the ZIP file. Others can:
- Copy to their `skills/` directory, or
- Upload ZIP via Claude.ai/Claude Code settings

## Quick Start Guide

### Example 1: Market Entry Planning

**You ask**: "I'm building a B2B SaaS for HR teams. How do I find the right entry point?"

**Claude will**:
1. Invoke Market Strategy skill
2. Apply **Part 1** (Q1-Q4 Entry Discovery)
3. Calculate Pain Point Scores for potential problems
4. Select highest-scoring problem (Score ≥ 20)
5. Design Trojan Horse expansion path (Stage 0 → 1 → 2)
6. Deliver prioritized entry strategy with metrics

### Example 2: Creating 10x Better Solutions

**You ask**: "Our onboarding flow takes 2 minutes and 8 steps. How do we make it 10x better?"

**Claude will**:
1. Invoke Market Strategy skill
2. Apply **Part 2** (Q5-Q8 Differentiation)
3. Measure current friction (time, clicks, cognitive load)
4. Set 10x goal (90% reduction → 12 seconds, 2 clicks)
5. Apply 3 tactics: Eliminate, Automate, Predict
6. Provide redesigned flow with validation plan

### Example 3: PMF Validation with Weekly Experiments

**You ask**: "We launched our MVP. How do we validate PMF systematically?"

**Claude will**:
1. Invoke Market Strategy skill
2. Apply **Part 3** (Q9-Q12 Validation)
3. Define North Star Metric + Supporting Metrics
4. Set 12-week targets (Week 4, Week 8, Week 12 milestones)
5. Design 2-3 weekly experiments with "If X, then Y" hypotheses
6. Provide experiment log template and prioritization matrix

## The 16-Question Framework

### Part 1: Entry Discovery (Q1-Q4)
Find the right market entry point with high pain and low friction.

**Key Concepts**:
- **Pain Point Score** = Frequency (1-10) × Intensity (1-10), Target ≥ 20
- **Trojan Horse** 3-stage path: Entry (0) → Expansion (1) → Ecosystem (2)

### Part 2: Differentiation (Q5-Q8)
Create 10x better solutions through extreme friction removal.

**Key Concepts**:
- **Friction Measurement**: Time, Clicks, Cognitive Load, Physical Barriers
- **10x Goal**: 90% reduction (not 2x or 5x)
- **3 Tactics**: Eliminate, Automate, Predict

### Part 3: Validation (Q9-Q12)
Validate PMF through data-driven weekly experiments.

**Key Concepts**:
- **North Star Metric** + 3-5 Supporting Metrics
- **Weekly Experiments**: 2-3 max, "If X, then Y will Z%" format
- **12-Week Milestones**: Week 4, 8, 12 checkpoints

### Part 4: Expansion (Q13-Q16)
Scale from one product to multi-product ecosystem.

**Key Concepts**:
- **Adjacent Markets**: Same user different need (horizontal), Same need different user (vertical)
- **Cross-Selling**: 30%+ conversion rate, 2-3 products per user average
- **Synergy**: Products reinforce each other via data/network effects

## Key Features

- **Pain Point Scoring**: Objective formula (Frequency × Intensity) to prioritize problems
- **Trojan Horse Strategy**: Multi-stage expansion planning from day 1
- **10x Thinking**: Not incremental (2x), but transformational (10x/90% reduction)
- **Weekly Experiments**: Systematic validation with hypothesis-driven approach
- **Evidence-Based**: All decisions backed by customer interviews, data, surveys
- **Industry Adaptations**: B2B SaaS, E-commerce, Healthcare, Fintech (see REFERENCE.md)

## Testing Your Installation

After installing, try these prompts to verify the skill works:

1. **Test Part 1 (Entry Discovery)**: "I'm entering the e-commerce market. Help me find the right beachhead using Pain Point Score."

2. **Test Part 2 (Differentiation)**: "Our checkout flow has 10 steps and takes 3 minutes. How do we achieve 10x improvement?"

3. **Test Part 3 (Validation)**: "We have an MVP with 50 users. Design a 12-week PMF validation plan with weekly experiments."

4. **Test Part 4 (Expansion)**: "We achieved PMF with Product A. What adjacent markets should we expand to next?"

If Claude invokes the Market Strategy skill and follows the 16-question framework, the skill is working correctly.

## Customization

You can customize this skill by editing `Skill.md`:

- **Adjust description**: Change when Claude invokes the skill
- **Add industry metrics**: Include domain-specific KPIs (e.g., CAC, LTV for SaaS)
- **Modify thresholds**: Adjust Pain Point Score threshold (default 20) for your market
- **Add case studies**: Include examples relevant to your industry

## Troubleshooting

**Claude doesn't invoke the skill:**
- Check that the skill is activated in Settings > Capabilities
- Ensure your prompt involves market planning or PMF validation
- Try being more explicit: "Use market strategy framework to plan entry"

**Skill invoked but incomplete:**
- The question may be too broad (ask more specific questions)
- Check that Skill.md formatting is correct (YAML frontmatter required)

**Need industry-specific guidance:**
- Ask Claude to refer to REFERENCE.md
- Or read REFERENCE.md directly for B2B SaaS, E-commerce, Healthcare, Fintech adaptations

**Pain Point Score seems arbitrary:**
- The score is a heuristic, not absolute truth
- Always validate with customer interviews (5-10 minimum)
- Adjust Frequency/Intensity scales based on your context

---

For detailed usage, see `SKILL.md`. For complete framework guide, see `REFERENCE.md`.
