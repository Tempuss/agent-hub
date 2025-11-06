# Toss Success Patterns - Custom Skill

A powerful custom skill for Claude that applies Toss's 7 battle-tested success patterns to achieve market entry, differentiation, and scaling, learning from Korea's fintech unicorn (0 → 20M+ users).

## What This Skill Does

This skill transforms Claude into a Toss pattern expert that:
- **Validates pain points** using Pain Point Score (Frequency × Intensity ≥ 20)
- **Designs expansion paths** with Trojan Horse strategy (3-stage: 0 → 1 → 2)
- **Creates 10x improvements** through extreme friction removal (90% reduction)
- **Builds viral loops** with clear metrics (Viral Coefficient K ≥ 1.0)
- **Implements data-driven iteration** through weekly experiments
- **Plans ecosystem expansion** with cross-selling strategies (30%+ conversion)
- **Leverages regulatory changes** as market opportunities

## When Claude Will Use This Skill

Claude will automatically invoke this skill when you:
- Plan market entry or product launch strategy
- Need to differentiate from competitors (10x better, not 2x)
- Design multi-product expansion roadmaps (Trojan Horse)
- Build viral growth mechanisms
- Validate PMF through data-driven experiments
- Scale to multi-product ecosystems
- Navigate regulatory environments (especially fintech, healthcare)

## File Structure

```
toss-patterns/
├── Skill.md          # Main skill definition (REQUIRED)
└── README.md         # This file

Note: REFERENCE.md includes Toss timeline (2013-2025) and detailed case studies
```

## Installation

### Option 1: Direct Use (Already in skills/)
If this skill is already in your skills/ folder, just ensure Claude Code's Skills feature is enabled.

### Option 2: Export as ZIP for Other Projects

1. **Create ZIP package**:
   ```bash
   cd skills
   zip -r toss-patterns.zip toss-patterns/
   ```

2. **Upload to Claude.ai or Claude Code**:
   - Go to Settings > Capabilities > Skills
   - Upload `toss-patterns.zip`
   - Activate the skill

### Option 3: Share with Others

Share the entire `toss-patterns/` directory or the ZIP file. Others can:
- Copy to their `skills/` directory, or
- Upload ZIP via Claude.ai/Claude Code settings

## Quick Start Guide

### Example 1: Market Entry with Patterns 1-3

**You ask**: "I'm entering the HR attendance market. How do I use Toss's approach?"

**Claude will**:
1. Invoke Toss Patterns skill
2. Apply **Pattern 1** (Pain Point Score): Manual tracking = 40 (Frequency 5 × Intensity 8)
3. Apply **Pattern 2** (Trojan Horse): GPS attendance → Payroll → Recruitment → HR platform
4. Apply **Pattern 3** (10x Improvement): 60s, 8 clicks → 6s, 1 click (90% reduction via GPS auto-detect)
5. Deliver integrated entry strategy with metrics

### Example 2: Viral Loop Design (Pattern 4)

**You ask**: "How do I create a referral mechanism for my SaaS product?"

**Claude will**:
1. Invoke Toss Patterns skill
2. Apply **Pattern 4** (Product = Marketing)
3. Calculate current Viral Coefficient K (e.g., 0.15)
4. Design referral mechanism (in-product button, rewards, simplified flow)
5. Project K goal (1.0) and actions to achieve 7x improvement

### Example 3: Industry Adaptation

**You ask**: "I'm in B2B SaaS. Do these fintech patterns apply?"

**Claude will**:
1. Invoke Toss Patterns skill
2. Identify essential patterns for B2B SaaS (1, 3, 5)
3. Adapt metrics (Viral Coef K=0.3 is good for B2B, not 1.0 like B2C)
4. Provide B2B-specific pattern checklists
5. Show industry-specific examples

## The 7 Success Patterns

### Pattern 1: Small Problem, Big Pain
**Focus**: Entry point via Pain Point Score ≥ 20 (Frequency × Intensity)

**When to Apply**: All stages (mandatory starting point)

### Pattern 2: Trojan Horse
**Focus**: 3-stage expansion path (Entry → Horizontal → Vertical)

**When to Apply**: Entry → Scale (design from Day 1, not after launch)

### Pattern 3: Friction Removal
**Focus**: 10x improvement through 90% reduction (eliminate, automate, predict)

**When to Apply**: All stages (differentiation driver)

### Pattern 4: Product = Marketing
**Focus**: Viral loops with Viral Coefficient K ≥ 1.0

**When to Apply**: Growth stage

### Pattern 5: Data-Driven
**Focus**: Weekly experiments with "If X, then Y" hypotheses

**When to Apply**: All stages (never stop experimenting)

### Pattern 6: Ecosystem
**Focus**: Multi-product cross-selling (30%+ conversion, 2-3 products per user)

**When to Apply**: Scale stage (after achieving PMF in Stage 0)

### Pattern 7: Regulation → Opportunity
**Focus**: Regulatory monitoring and proactive roadmap adjustments

**When to Apply**: Industry-specific (fintech, healthcare, education)

## Key Features

- **Pattern Combinations**: For Entry (1+2+3), For Growth (4+5), For Scale (6+7)
- **Industry Adaptations**: Fintech, B2B SaaS, E-commerce, Healthcare, Education
- **Pattern Checklists**: Actionable checklists for each of 7 patterns
- **Pro Tips**: Start with 1+3 (mandatory), design Pattern 2 from Day 1, never stop Pattern 5
- **Common Mistakes**: Addressed with clear fixes (e.g., Pain Point 15 ≠ "close enough")

## Testing Your Installation

After installing, try these prompts to verify the skill works:

1. **Test Pattern 1**: "Calculate Pain Point Score for manual expense tracking (3 times/week, 7/10 intensity)."

2. **Test Patterns 1-3**: "I'm entering the e-commerce logistics market. Apply Toss's entry patterns."

3. **Test Pattern 4**: "Design a viral loop for my productivity app."

4. **Test Industry Adaptation**: "Which Toss patterns work best for B2B SaaS?"

If Claude invokes the Toss Patterns skill and applies relevant patterns with metrics, the skill is working correctly.

## Customization

You can customize this skill by editing `Skill.md`:

- **Adjust thresholds**: Change Pain Point Score minimum (default: 20)
- **Add industry patterns**: Include domain-specific adaptations (e.g., government, finance)
- **Modify metrics**: Adjust Viral Coefficient targets for your market (B2B vs. B2C)
- **Add case studies**: Include examples relevant to your industry

## Troubleshooting

**Claude doesn't invoke the skill:**
- Check that the skill is activated in Settings > Capabilities
- Ensure your prompt involves market strategy or PMF planning
- Try being more explicit: "Apply Toss's success patterns to this problem"

**Patterns seem too fintech-specific:**
- Ask Claude to adapt for your industry: "How do these patterns apply to [your industry]?"
- Check Industry Adaptations table in Skill.md
- Adjust metrics (e.g., B2B SaaS K=0.3 is good, not 1.0)

**Need more context on Toss:**
- Ask Claude: "Tell me Toss's timeline from 2013-2025"
- Or check market-strategy/REFERENCE.md for detailed Toss case study

---

For detailed case studies and examples, see `REFERENCE.md` and `SKILL.md`.