# AI Persona Creator - Claude Skill

Create highly accurate AI personas (95%+) using web research and psychological analysis for negotiations, proposals, and persuasion.

## Installation

### Option A: Upload ZIP to Claude
1. Download `ai-persona-creator.zip`
2. Go to Claude → Settings → Skills
3. Click "Upload Skill"
4. Select the ZIP file
5. Enable the skill

### Option B: Manual Installation (Claude Code)
```bash
cp -r ai-persona-creator ~/skills/
```

## Quick Start (30 seconds)

```
Create an AI persona for:
- Job/Role: E-commerce CTO
- Project: Headless commerce platform migration
- Goal: Get technical approval
```

Claude automatically:
1. Runs 32-48 web searches
2. Cross-verifies 3+ sources
3. Applies 7 psychological frameworks
4. Generates persona with citations
5. Self-refines (3 rounds, 90%+ quality)

## What You Get

4 files per persona:
1. `web-search-results.md` - Raw research data (32-48 searches)
2. `research-findings.md` - Cross-verified insights (3+ sources)
3. `psychology-profile.md` - 7-framework analysis
4. `persona-prompt.md` - Final usable persona (ready to activate)

## Key Features

✅ **Research-backed** (not guesswork): 32-48 searches, 3+ independent sources
✅ **7 psychological frameworks**: Kahneman, Cialdini, Voss, Navarro, Ariely, Evolution, Organization
✅ **Hidden motivations revealed**: What stakeholders won't say out loud
✅ **Self-refining**: 3-round quality assurance (90%+ target)
✅ **Actionable**: Specific persuasion tactics, red flags, alternatives

## Use Cases

| Scenario | Example |
|----------|---------|
| **Security Approvals** | Convince CISO to approve cloud/SaaS |
| **Budget Approvals** | Persuade CFO/finance teams |
| **Investment Pitches** | Understand VC/investor psychology |
| **Sales Enablement** | Create deep buyer personas |
| **Negotiation Prep** | Analyze counterparty before meetings |
| **Proposal Writing** | Identify stakeholder blind spots |

## Example Results

### E-commerce CTO

**Input**: "E-commerce CTO, headless commerce platform"

**Output** (60-min automated):
- Core fear: Platform downtime during peak sales (95%)
- Decision style: 75% data-driven (performance metrics)
- Top vulnerabilities: Authority (90%), Scarcity (85%)
- Strategy: Performance benchmarks + competitor adoption + ROI projections

**Persona Quote**:
> "Your architecture looks solid. But what keeps me up is explaining to the CEO
> why we had outages during Black Friday.
>
> [Research]: '67% of CTOs face executive pressure after performance incidents'
>
> What I need:
> 1. Load testing results (prove scalability)
> 2. 3 similar-scale e-commerce platforms using this (social proof)
> 3. Migration roadmap with zero-downtime plan (risk mitigation)"

### VC Investment Partner

**Input**: "VC Partner, Series A"

**Output**:
- Core fear: Missing next unicorn (90%)
- Decision style: 60% social proof (peer validation)
- Top vulnerabilities: Scarcity (90%), Social Proof (95%)
- Strategy: FOMO + "closing soon" + other VC interest

## Files Guide

- `Skill.md` - Main skill documentation (quick reference, examples)
- `REFERENCE.md` - Detailed 7-framework guide + persona template
- `EXAMPLES.md` - 3 complete walkthroughs (CISO, VC, Hospital)
- `README.md` - This file (installation & quick start)

---

For detailed usage, see `SKILL.md`. For complete framework guide, see `REFERENCE.md`.