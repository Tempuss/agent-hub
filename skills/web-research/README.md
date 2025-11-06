# Web Research with Sources - Claude Custom Skill

Conduct thorough web research with credible sources and URLs for market analysis, competitor research, and technical comparisons.

---

## What This Skill Does

This skill enables Claude to:

- **Research markets and industries** with credible, cited sources
- **Compare technologies** using official docs, benchmarks, and case studies
- **Analyze competitors** with data from authoritative publications
- **Find case studies** and real-world examples with proper attribution
- **Create structured reports** with executive summaries and actionable insights

**Key Features**:
- 4-step research methodology (Design → Execute → Document → Structure)
- Credibility filtering (Official > Academic > Media)
- Source verification with web search tools
- Standard templates for reports, briefs, and comparisons
- Quality checklists to ensure reliable output

---

## Installation

### Option 1: Claude.ai Web Interface

1. **Download** this skill as a ZIP file
2. **Navigate** to Claude.ai settings
3. **Click** "Skills" in the sidebar
4. **Upload** the `web-research.zip` file
5. **Enable** the skill in your settings

### Option 2: Claude Code CLI

If using this skill within a project:

1. **Copy** the `web-research/` folder to `skills/`
2. The skill will be automatically available for use

---

## How to Use

### Automatic Activation

Claude will automatically use this skill when you say:

**Research Keywords**:
- "research", "investigate", "find information about"
- "search for", "what's the latest on"
- "find case studies", "industry trends"

**Comparison Keywords**:
- "compare technologies", "benchmark"
- "competitor analysis", "alternatives to"

**Example Prompts**:
```
"Research the current state of AI in manufacturing automation"

"Compare React vs Vue.js for enterprise dashboards"

"Find case studies of successful digital transformation in manufacturing"

"Analyze Salesforce's AI features vs HubSpot"
```

### Manual Activation

You can also explicitly reference the skill:

```
Using the web-research skill, investigate [topic] and create
an executive brief with credible sources.
```

---

## Usage Examples

### Example 1: Market Research

**Your Request**:
```
"Research the digital MR platform market. I need market size,
growth rate, and key players for a business plan."
```

**Claude's Output**:
```markdown
# Digital MR Platform Market Analysis - 2024

**Date**: 2024-10-27
**Purpose**: Market sizing for business plan

---

## 📊 Executive Summary

**Key Finding 1**: $2.8B market in 2023 → $7.2B by 2028 (CAGR 20.7%)
**Source**: Grand View Research (2024-01)

**Key Finding 2**: 73% of manufacturing companies planning digital transformation
**Source**: Gartner Survey (2024-03)

**Key Finding 3**: Average deal size $250K-$500K (mid-market)
**Source**: SaaS Capital Benchmarks (2024-02)

**Recommendation**: Strong market tailwinds; position as AI-first
solution to differentiate.

---

## 📚 References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| 1 | Digital Automation in Manufacturing 2024 | Grand View | 2024-01 | [URL] |
| 2 | 2024 Manufacturing Technology Survey | Gartner | 2024-03 | [URL] |
| 3 | B2B SaaS Benchmarks Q1 2024 | SaaS Capital | 2024-02 | [URL] |

**Total Sources**: 3 (Official: 2, Industry: 1)
```

### Example 2: Technology Comparison

**Your Request**:
```
"Compare Python vs Go for building microservices. Need performance,
ecosystem maturity, and hiring considerations."
```

**Claude's Output**:
```markdown
# Python vs Go for Microservices - Comparison

**Date**: 2024-10-27

---

## Quick Comparison

| Criterion | Python | Go | Winner | Source |
|-----------|--------|----|----|--------|
| Performance | 6/10 | 9/10 | Go | TechEmpower Benchmarks |
| Ecosystem | 10/10 | 7/10 | Python | GitHub Stats 2024 |
| Developer Pool | 9/10 | 6/10 | Python | Stack Overflow 2024 |
| Learning Curve | 8/10 | 7/10 | Python | Developer Survey |

---

## Recommendation

**Choose Go** if:
- Performance is critical (high-throughput services)
- Building cloud-native apps (Kubernetes, Docker)
- Team is small and can learn new language

**Choose Python** if:
- Ecosystem richness is priority (ML, data, APIs)
- Need large talent pool for hiring
- Rapid prototyping and iteration speed matters

---

## References
[Full citations for benchmarks, surveys, official docs]
```

### Example 3: Competitor Analysis

**Your Request**:
```
"Analyze how Notion and Coda differ in their AI features
and pricing models."
```

**Claude's Output**:
- Feature comparison matrix (with sources from official sites)
- Pricing breakdown (from official pricing pages via WebFetch)
- AI capabilities analysis (from product announcements)
- Use case recommendations (based on third-party reviews)
- 5+ credible sources cited

---

## File Structure

```
web-research/
├── SKILL.md                      # Main skill definition (read first)
├── SOURCE-CREDIBILITY-GUIDE.md   # ⭐ 4-tier source credibility framework (CRITICAL!)
├── REFERENCE.md                  # Templates, examples, checklists
└── README.md                     # This file (installation & usage)
```

**What Each File Contains**:

- **SKILL.md**: Core methodology, trigger keywords, quick reference tables
- **SOURCE-CREDIBILITY-GUIDE.md**: ⭐ 4-tier credibility classification (90-100%, 70-90%, 50-70%, 30-50%), research purpose strategies, verification checklists, tool-specific strategies (MUST READ!)
- **REFERENCE.md**: Copy-paste templates, real examples, output formats
- **README.md**: Installation, usage examples, troubleshooting

---

## How It Works

### 4-Step Process

```
1. Design Queries
   ↓
   Extract keywords → Create 3-5 targeted searches

2. Execute Research
   ↓
   WebSearch → Filter by credibility → WebFetch for details

3. Document Sources
   ↓
   Summarize + Cite source + Include URL + Note credibility

4. Create Document
   ↓
   Use template → Add insights → Quality check
```

### Credibility Filter

**⚠️ CRITICAL**: For detailed credibility assessment, ALWAYS refer to **SOURCE-CREDIBILITY-GUIDE.md**

The skill automatically prioritizes sources:

| Priority | Source Type | Examples | Credibility |
|----------|------------|----------|-------------|
| 1 | Official | .gov, company sites, .edu | Tier 1 (90-100%) |
| 2 | Academic | Peer-reviewed journals, arXiv | Tier 1 (90-100%) |
| 3 | Authoritative Media | Forbes, HBR, TechCrunch | Tier 2 (70-90%) |
| 4 | Expert Blogs | Industry experts (verify credentials) | Tier 2-3 (60-90%) |
| 5 | Community | Stack Overflow, Reddit (reference only) | Tier 3 (50-70%) |

**Full Credibility Guide**: See `SOURCE-CREDIBILITY-GUIDE.md` for:
- 4-Tier credibility classification (90-100%, 70-90%, 50-70%, 30-50%)
- Research purpose-based source selection strategies
- Information verification checklists
- Real-world scenario applications

---

## Customization

### Modify Credibility Standards

Edit `Skill.md` to adjust credibility criteria for your domain:

```markdown
### Credibility Criteria (Custom for [Your Industry])

| Level | Source Type | Examples |
|-------|------------|----------|
| ✅ High | [Your trusted sources] | [Examples] |
| ⚠️ Medium | [Secondary sources] | [Examples] |
| ❌ Low | [Avoid these] | [Examples] |
```

### Add Domain-Specific Templates

Add new templates to `REFERENCE.md`:

```markdown
### Template 4: [Your Use Case]

[Your custom template here]
```

### Modify Trigger Keywords

Edit the frontmatter in `Skill.md`:

```yaml
description: Use when [your custom triggers]. Ensures credible sources.
```

---

## Troubleshooting

### Skill Not Activating

**Problem**: Claude doesn't use the skill automatically

**Solutions**:
1. Use explicit trigger words: "research", "investigate", "compare"
2. Manually reference: "Using the web-research skill, [request]"
3. Check skill is enabled in Claude settings
4. Verify description in frontmatter includes your use case

### Sources Not Credible Enough

**Problem**: Results include low-quality sources

**Solutions**:
1. Explicitly request: "Use only official and academic sources"
2. Specify source types: "Find this info from .gov or .edu sites"
3. Add domain filter: "Search site:nih.gov for [topic]"

### Missing Sources

**Problem**: Some findings lack citations

**Solutions**:
1. Remind: "Ensure ALL findings include sources"
2. Use post-research checklist from `REFERENCE.md`
3. Request: "Add sources for claims in paragraph 3"

### Links Are Broken

**Problem**: URLs return 404 errors

**Solutions**:
1. Check Web Archive: https://archive.org
2. Search for updated link with article title
3. Use official site search instead

### Output Too Long/Too Short

**Problem**: Report not the right length

**Solutions**:
- Too long: Request "quick research brief" template
- Too short: Request "full research report" template
- Specify: "I need a 5-minute read" or "comprehensive analysis"

---

## FAQ

### Q: Does this skill work in all languages?

**A**: Yes, but search results are primarily English. The skill automatically creates both English and target language queries for broader coverage.

### Q: Can I use this for academic research?

**A**: Yes, the skill prioritizes academic sources (journals, papers). Request "Use academic sources only" for literature reviews.

### Q: How recent is the information?

**A**: The skill checks publication dates and prioritizes recent sources (<2 years). Explicitly request "latest 2024 data" for maximum currency.

### Q: Can it access paywalled content?

**A**: No, WebFetch can't access paywalled articles. The skill will look for press releases, summaries, or alternative open-access sources.

### Q: How many sources does it typically find?

**A**: 3-10 sources for quick briefs, 10-20+ for comprehensive reports. Specify if you need more: "Find at least 15 sources."

### Q: Can I export the results?

**A**: Yes, all output is in markdown format. Copy to your editor or ask Claude to "save this as a .md file" (if using Claude Code).

---

## Best Practices

### Before Research

1. **Define scope clearly**: "Research [topic] focusing on [aspect]"
2. **Specify output format**: Brief, full report, or comparison
3. **Set credibility bar**: "Use only official sources" if needed
4. **Note time period**: "Latest 2024 data" or "2020-2024 trends"

### During Research

1. **Review sources**: Ask "What's the credibility of source #3?"
2. **Request more**: "Find 2 more academic sources for claim X"
3. **Verify links**: "Test all URLs before finalizing"

### After Research

1. **Use checklists**: Reference `REFERENCE.md` quality checklist
2. **Verify facts**: "Cross-check the 68% statistic from another source"
3. **Export properly**: Save with metadata (date, sources, version)

---

## Tips for Better Results

### Tip 1: Be Specific

```
❌ "Research AI in manufacturing"
✅ "Research AI adoption rates in manufacturing automation,
    focusing on ROI data from 2022-2024"
```

### Tip 2: Specify Source Types

```
"Use official manufacturing industry reports and academic journals only"
"Find this data from government sources (.gov)"
"Include analyst reports from Gartner, Forrester, or McKinsey"
```

### Tip 3: Request Output Format

```
"Create a 5-minute executive brief"
"I need a comprehensive 20-page report"
"Just give me top 3 findings with sources"
```

### Tip 4: Set Credibility Standards

```
"Only include sources from peer-reviewed journals"
"Prioritize official company announcements over news articles"
"Avoid blog posts; use official documentation"
```

---

---

For detailed usage and examples, see related documentation files.