# ROI Analyzer - Custom Skill

A powerful custom skill for Claude that delivers rapid, rigorous financial analysis for investment decisions, turning 4 hours of spreadsheet work into 30 minutes of strategic insight.

## What This Skill Does

This skill transforms Claude into an executive financial analyst that:
- **Calculates ROI** in seconds with clear formulas (Net Profit / Investment × 100%)
- **Models 3 scenarios** (Best/Realistic/Worst) to de-risk decisions
- **Finds break-even points** for conversion-based and time-based investments
- **Recommends decisions** with clear INVEST/REVIEW/REJECT criteria
- **Saves 87.5% time** (4 hours spreadsheet work → 30 minutes analysis)

## When Claude Will Use This Skill

Claude will automatically invoke this skill when you:
- Need executive reports or financial summaries for leadership
- Evaluate investment opportunities (projects, features, contracts)
- Make Phase 0 → Phase 1 transition decisions
- Justify budgets with quantified ROI and payback periods
- Forecast 3-year revenue, costs, and profitability
- Perform scenario planning (Best/Realistic/Worst cases)

## File Structure

```
roi-analyzer/
├── Skill.md          # Main skill definition (REQUIRED)
├── REFERENCE.md      # Detailed formulas, sensitivity analysis, industry benchmarks
└── README.md         # This file
```

## Installation

### Option 1: Direct Use (Already in skills/)
If this skill is already in your skills/ folder, just ensure Claude Code's Skills feature is enabled.

### Option 2: Export as ZIP for Other Projects

1. **Create ZIP package**:
   ```bash
   cd skills
   zip -r roi-analyzer.zip roi-analyzer/
   ```

2. **Upload to Claude.ai or Claude Code**:
   - Go to Settings > Capabilities > Skills
   - Upload `roi-analyzer.zip`
   - Activate the skill

### Option 3: Share with Others

Share the entire `roi-analyzer/` directory or the ZIP file. Others can:
- Copy to their `skills/` directory, or
- Upload ZIP via Claude.ai/Claude Code settings

## Quick Start Guide

### Example 1: Phase 0 → Phase 1 Decision

**You ask**: "Should we invest 50M KRW in a 1-month Phase 0 trial? Phase 1 contract would be 208M KRW if we convert at 70%."

**Claude will**:
1. Invoke ROI Analyzer skill
2. Calculate 3 scenarios (Worst 30%, Realistic 70%, Best 90% conversion)
3. Compute ROI for each: Worst 25%, Realistic 191%, Best 274%
4. Find break-even: 27% conversion (very achievable)
5. Recommend: ✅ INVEST (low risk, high return)

### Example 2: 3-Year SaaS Projection

**You ask**: "We're investing 200M KRW in a B2B SaaS. MRR targets: Y1 10M, Y2 30M, Y3 60M. Operating costs 15M/month. Is it worth it?"

**Claude will**:
1. Invoke ROI Analyzer skill
2. Build year-by-year projections (Y1 -30% ROI, Y2 +90%, Y3 +270%)
3. Calculate payback period (18 months during Y2)
4. Compute 3-year cumulative: 460M KRW profit, 270% ROI
5. Recommend: ✅ INVEST (strong Y2 and Y3 profitability)

### Example 3: Quick Break-Even Check

**You ask**: "We're spending 100M KRW upfront. Monthly revenue will be 20M, costs 12M. Should we do it?"

**Claude will**:
1. Invoke ROI Analyzer skill
2. Calculate monthly net profit: 8M KRW
3. Find payback period: 12.5 months
4. Project 24-month cumulative: 96M KRW profit
5. Recommend: ⚠️ REVIEW (13-month payback is moderate; suggest negotiating lower upfront cost)

## The Four Core Metrics

### 1. ROI (Return on Investment)
**Formula**: (Net Profit / Investment) × 100%

**Targets**:
- ✅ INVEST: ROI > 100%
- ⚠️ REVIEW: ROI 50-100%
- ❌ REJECT: ROI < 50%

### 2. Break-Even Point
**Formula**: Investment / Revenue per unit (or Monthly Net Profit)

**Targets**:
- ✅ INVEST: Break-even < 50% of realistic target
- ⚠️ REVIEW: Break-even 50-70% of target
- ❌ REJECT: Break-even > 70% of target

### 3. Payback Period
**Formula**: Investment / Monthly Net Profit

**Targets**:
- ✅ INVEST: Payback < 12 months
- ⚠️ REVIEW: Payback 12-24 months
- ❌ REJECT: Payback > 24 months

### 4. Scenario Analysis
**Process**: Model Best/Realistic/Worst cases with different assumptions

**Rule**: If worst-case ROI ≥ 0%, investment is low-risk

## Key Features

- **87.5% Time Saving**: 4 hours spreadsheet work → 30 minutes analysis
- **3-Scenario Modeling**: Always includes Best/Realistic/Worst cases (not just optimistic)
- **Break-Even Threshold**: Knows minimum success rate required
- **Clear Recommendations**: INVEST/REVIEW/REJECT with reasoning
- **Executive Summaries**: 3-sentence format for leadership presentations
- **Industry Benchmarks**: SaaS, E-commerce, Hardware metrics (see REFERENCE.md)

## Testing Your Installation

After installing, try these prompts to verify the skill works:

1. **Test Phase 0 Decision**: "Should I invest 50M KRW in a Phase 0 trial with 70% expected conversion to 200M Phase 1?"

2. **Test 3-Year Projection**: "Analyze 200M investment for B2B SaaS with Y1 10M MRR, Y2 30M, Y3 60M, and 15M/month operating costs."

3. **Test Break-Even**: "Investment 100M, monthly revenue 20M, monthly costs 12M. What's the payback period?"

4. **Test Scenario Analysis**: "Create Best/Realistic/Worst case scenarios for a 50M investment with 30-90% conversion rates."

If Claude invokes the ROI Analyzer and provides clear calculations + recommendations, the skill is working correctly.

## Customization

You can customize this skill by editing `Skill.md`:

- **Adjust thresholds**: Change ROI targets (default: 100%+ for INVEST)
- **Add metrics**: Include domain-specific KPIs (LTV, CAC, churn for SaaS)
- **Modify decision criteria**: Adjust INVEST/REVIEW/REJECT rules for your risk tolerance
- **Industry templates**: Add pre-configured templates for your industry (see REFERENCE.md)

## Troubleshooting

**Claude doesn't invoke the skill:**
- Check that the skill is activated in Settings > Capabilities
- Ensure your prompt involves financial analysis or investment decisions
- Try being more explicit: "Calculate ROI and recommend whether to invest"

**Calculations seem wrong:**
- Verify you provided all costs (operating costs, not just initial investment)
- Check if multi-year projects need discount rate (time value of money)
- Ask Claude to show step-by-step calculations

**Need industry-specific benchmarks:**
- Ask Claude to refer to REFERENCE.md
- Or read REFERENCE.md directly for SaaS, E-commerce, Hardware industry standards

**Scenarios too optimistic:**
- Explicitly request pessimistic scenarios: "What if conversion is only 20%?"
- Ask for sensitivity analysis: "How does ROI change with ±20% assumptions?"

---

For detailed formulas and examples, see `REFERENCE.md` and `SKILL.md`.
