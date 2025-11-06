---
name: web-research
description: Use when researching markets, analyzing competitors, comparing technologies, or finding case studies. Ensures all findings include credible sources and URLs.
---

# Web Research with Sources

## When to Use

Claude should automatically activate this skill when detecting:

**Research requests**:
- "research", "investigate", "find information about"
- "search for", "look up", "what's the latest on"
- "find case studies", "industry trends", "market analysis"

**Comparison requests**:
- "compare technologies", "benchmark", "alternatives to"
- "competitor analysis", "market landscape"
- "find references", "best practices"

**Proposal preparation**:
- "background research", "market data", "industry statistics"
- "credible sources for", "evidence that"

## Quick Reference

### 4-Step Research Process

| Step | Action | Output |
|------|--------|--------|
| 1. Design Queries | Extract keywords → Create 3-5 search queries | Search query list |
| 2. Execute Research | WebSearch → Filter by credibility → WebFetch details | Raw findings |
| 3. Document Sources | Summarize + Cite source + Include URL | Structured notes |
| 4. Create Document | Use standard template → Add insights | Final report |

### Credibility Criteria

**⚠️ CRITICAL**: For detailed credibility assessment, ALWAYS refer to **SOURCE-CREDIBILITY-GUIDE.md**

| Level | Source Type | Examples | Usage |
|-------|------------|----------|-------|
| ✅ Tier 1 (90-100%) | Official/Academic | Government, .edu, journals | Primary sources only |
| ✅ Tier 2 (70-90%) | Expert/Media | Forbes, HBR, McKinsey | Industry trends |
| ⚠️ Tier 3 (50-70%) | Community | Stack Overflow, Reddit | Cross-verify required |
| ❌ Tier 4 (30-50%) | Unknown/Anonymous | No authorship | Avoid or re-verify |

**Full Credibility Guide**: See `SOURCE-CREDIBILITY-GUIDE.md` for:
- 4-Tier credibility classification (90-100%, 70-90%, 50-70%, 30-50%)
- Research purpose-based source selection strategies (technical implementation, troubleshooting, trends, regulatory, ideation)
- Information verification checklists (basic + cross-verification)
- Real-world scenario applications (Django, pharmaceutical, AWS, troubleshooting)

## Core Process

### STEP 0: Analyze Request & Select Source Strategy

**Goal**: Understand research intent and select optimal source types before searching

**Process**:
```
User request → Decompose query → Identify research intent → Map to source types → Select search strategy
```

**Analysis Framework**:
```yaml
1. Request Decomposition:
   - What: Core research subject (company? market? technology? statistics?)
   - Why: Research purpose (investment? proposal? benchmarking? compliance?)
   - Depth: Required information depth (overview? detailed? comprehensive?)
   - Scope: Geographic/industry/timeframe scope

2. Intent Classification:
   by_category:
     - Technical Implementation: Official docs + technical communities
     - Market Research: Industry reports + news + analyst insights
     - Compliance/Regulatory: Official government/standards bodies only (Tier 1)
     - Trend Analysis: Expert blogs + media + community discussions
     - Company Research: Official sources + reviews + financial reports

   by_purpose:
     - Technical Documentation: Official docs (Django, React, AWS)
     - Troubleshooting: Stack Overflow + GitHub Issues + official bug trackers
     - Market Sizing: Industry reports (Gartner, Forrester) + government statistics
     - Competitive Analysis: Company websites + G2/Capterra + job postings + reviews
     - Technology Selection: Official docs + benchmarks + expert comparisons + case studies
     - Due Diligence: Financial reports + compliance checks + security audits
     - Trend Spotting: Tech media + conference talks + expert blogs

3. Source Type Selection by Credibility Tier:
   Tier 1 (90-100%):
     - Official documentation (vendor sites, .gov, .edu)
     - Peer-reviewed journals
     - Government statistics and reports
     - Standards bodies (ISO, NIST, OWASP)

   Tier 2 (70-90%):
     - Industry analyst reports (Gartner, Forrester, IDC)
     - Established tech media (TechCrunch, The Verge, InfoQ)
     - Expert blogs (Martin Fowler, Real Python)
     - Conference presentations (AWS re:Invent, Google I/O)

   Tier 3 (50-70%):
     - Community resources (Stack Overflow, Reddit)
     - Medium/Dev.to articles (high engagement)
     - GitHub Issues/Discussions
     - Personal developer blogs

   Tier 4 (30-50%):
     - General web search results
     - Social media posts
     - Unverified sources
```

**Example 1: Django REST API Security Implementation**
```yaml
Request: "Research security best practices for Django REST Framework APIs"

Analysis:
  What: Technical implementation (Django security)
  Why: Production deployment / security audit
  Depth: Comprehensive (authentication, authorization, data protection)
  Scope: Current Django versions, industry standards

Source Strategy:
  Tier 1 (Primary - 70%):
    - Django official docs (security section)
    - Django REST Framework security guide
    - OWASP API Security Top 10

  Tier 2 (Secondary - 20%):
    - Real Python security tutorials
    - Django security experts' blogs
    - PyCon security talks

  Tier 3 (Validation - 10%):
    - Stack Overflow Django security questions
    - GitHub security-related issues

Search Strategy:
  1. Search → Official Django security docs
  2. OWASP → API security standards
  3. Search → Recent security articles (2024)
  4. Stack Overflow → Common pitfalls
```

**Example 2: SaaS Market Entry Strategy**
```yaml
Request: "Research the project management SaaS market size and competitive landscape"

Analysis:
  What: Market research (SaaS industry)
  Why: Business planning / market entry
  Depth: Detailed (TAM/SAM/SOM, competitors, trends)
  Scope: Global market, last 2 years

Source Strategy:
  Tier 1 (Primary - 40%):
    - Government statistics (Census Bureau, industry reports)
    - Gartner/Forrester market reports

  Tier 2 (Secondary - 40%):
    - TechCrunch funding news
    - Crunchbase competitor data
    - G2/Capterra reviews and market trends

  Tier 3 (Validation - 20%):
    - Reddit r/SaaS discussions
    - LinkedIn company profiles
    - Product Hunt launches

Search Strategy:
  1. Search → "project management SaaS market size 2024"
  2. Web fetch → Gartner/Forrester reports
  3. Crunchbase → Competitor funding
  4. G2 → Customer reviews and ratings
```

**Example 3: Technology Stack Comparison (React vs Vue)**
```yaml
Request: "Compare React and Vue.js for enterprise dashboard development"

Analysis:
  What: Technology comparison (frontend frameworks)
  Why: Architecture decision / technology selection
  Depth: Detailed (performance, ecosystem, hiring)
  Scope: Enterprise scale, production readiness

Source Strategy:
  Tier 1 (Primary - 50%):
    - React official docs
    - Vue.js official docs

  Tier 2 (Secondary - 30%):
    - State of JS survey
    - TechEmpower benchmarks
    - ThoughtWorks Tech Radar

  Tier 3 (Real-world - 20%):
    - Stack Overflow developer survey
    - GitHub Stars/Activity
    - Dev.to framework comparisons

Search Strategy:
  1. Search → React/Vue official guides
  2. Search → "React vs Vue enterprise 2024"
  3. Web fetch → State of JS survey
  4. GitHub → Activity and community health
```

**Best Practices**:
- ⭐ **Always start with source selection**: Choose source types before searching
- 📊 **Tier 1 for critical decisions**: Use official docs for implementation/compliance
- 🎯 **Match purpose to credibility**: Trend research allows Tier 3, compliance requires Tier 1
- 🔗 **Combine multiple tiers**: Cross-verify Tier 3 findings with Tier 1-2 sources
- ⚠️ **Check SOURCE-CREDIBILITY-GUIDE.md**: Review credibility framework before research

---

### STEP 1: Design Search Queries

**Goal**: Create targeted queries that find credible, recent information

**Process**:
```
Selected sources → Extract keywords → Generate 3-5 queries → Include recency
```

**Example**:
```
Request: "Research manufacturing automation digital transformation success stories"

Selected Sources (from STEP 0):
  - Official documentation (technical guides)
  - Industry reports (market analysis)
  - Web search (case studies)

Queries:
1. "manufacturing AI digital transformation case study 2024"
2. "manufacturing company successful automation implementation"
3. "industrial automation adoption ROI manufacturing"
4. "smart factory platform efficiency improvements"
5. "manufacturing IoT implementation best practices"
```

**Best Practices**:
- Mix English and target language queries
- Combine specific + broad terms
- Add year/recency indicators ("2024", "latest", "recent")
- Include domain-specific terms
- ⭐ **Reference selected sources**: Design queries based on sources selected in STEP 0

### STEP 2: Execute Research

**Goal**: Gather information from credible sources

**Process**:
```
Search for information → Analyze results → Apply credibility filter → Fetch detailed content from specific URLs
```

**Credibility Filter**:
1. **Check source type**: Official > Academic > Media > Blog > Unknown
2. **Verify author credentials**: Named experts, institutions
3. **Check publication date**: Prefer recent (last 2 years)
4. **Cross-reference**: Confirm facts from 2+ sources

### STEP 3: Document with Sources

**Goal**: Record findings with proper attribution

**Format**:
```markdown
## [Topic/Finding]

[Summary or key points - 2-3 sentences]

**Source**: [Document Title] - [Publisher] ([Publication Date])
**Link**: [Full URL]
**Credibility**: [Official/Academic/Media/Expert Blog]
```

**Example**:
```markdown
## Pfizer's AI Drug Discovery Platform

Pfizer partnered with IBM Watson in 2023 to implement AI-powered molecular
screening. The platform reduced preclinical development time by 30% and
increased successful compound identification by 45%.

**Source**: "Pfizer's AI-Powered Drug Discovery Revolution" - TechCrunch (2024-03-15)
**Link**: https://techcrunch.com/2024/03/15/pfizer-ai-drug-discovery
**Credibility**: Authoritative Media (Tech Industry)
```

### STEP 4: Create Structured Document

**Goal**: Deliver insights in actionable format

**Use the standard template from REFERENCE.md**:
- Executive Summary (3-5 key findings)
- Detailed Findings (organized by topic)
- Insights & Implications (actionable takeaways)
- Complete References (table format)

## Usage Examples

### Example 1: Market Research

**User Request**:
```
"Research the current state of AI in manufacturing automation.
I need credible sources for a proposal."
```

**Claude's Process**:
1. **Design Queries**:
   - "AI manufacturing automation predictive maintenance 2024"
   - "machine learning quality control manufacturing"
   - "AI adoption rate manufacturing industry statistics"

2. **Execute Research**:
   - Search → Find 10+ relevant articles
   - Filter by credibility (prioritize IEEE, Forbes, Manufacturing official sites)
   - Fetch top 5 sources for details

3. **Document Findings**:
   ```markdown
   ## AI Adoption in Manufacturing Automation

   68% of top 20 manufacturing companies have implemented AI in production optimization
   as of 2024, up from 32% in 2022. Primary applications include predictive
   maintenance (85%), quality control automation (67%), and supply chain optimization (54%).

   **Source**: "AI in Manufacturing: 2024 Industry Report" - McKinsey & Company (2024-02-10)
   **Link**: https://mckinsey.com/industries/manufacturing/ai-adoption-2024
   **Credibility**: Official (Consulting Firm Research)
   ```

4. **Create Report**:
   - Executive Summary with 5 key findings
   - Detailed sections on adoption rates, ROI, challenges
   - Actionable insights for proposal
   - 8 credible sources in references table

### Example 2: Technology Comparison

**User Request**:
```
"Compare React vs Vue.js for our enterprise dashboard.
Need recent benchmarks and real-world case studies."
```

**Claude's Process**:
1. **Design Queries**:
   - "React vs Vue enterprise dashboard 2024 benchmark"
   - "Vue.js large scale application performance"
   - "React dashboard case study enterprise"

2. **Execute Research**:
   - Search → Find official docs, benchmarks, case studies
   - Fetch React/Vue official sites for latest features
   - Look for enterprise case studies (Airbnb, Alibaba, etc.)

3. **Create Comparison Table**:
4. 
   | Criterion | React | Vue.js | Source |
   |-----------|-------|--------|--------|
   | Performance | 8.2/10 | 8.5/10 | State of JS 2024 |
   | Enterprise Adoption | 68% | 24% | Stack Overflow Survey 2024 |
   | Learning Curve | Moderate | Easy | Official Docs + MDN |

4. **Deliver Recommendation** with sources for each claim

### Example 3: Competitor Analysis

**User Request**:
```
"Analyze Salesforce's AI features compared to HubSpot.
Focus on pricing and ROI data."
```

**Claude's Process**:
1. **Design Queries**:
   - "Salesforce Einstein AI features pricing 2024"
   - "HubSpot AI tools cost ROI analysis"
   - "Salesforce vs HubSpot comparison enterprise"

2. **Execute Research**:
   - Search for information
   - Fetch official pricing pages
   - Search for third-party comparisons (G2, Gartner)
   - Find ROI case studies

3. **Create Analysis**:
   - Feature comparison matrix (with sources)
   - Pricing breakdown (from official sites)
   - ROI data (from case studies with citations)
   - Recommendation based on use case

## Output Templates

### Template 1: Executive Research Brief

```markdown
# [Research Topic]

**Date**: YYYY-MM-DD
**Prepared for**: [Purpose/Stakeholder]
**Research scope**: [1-2 sentences]

---

## 📊 Executive Summary

**Key Finding 1**: [Finding with metric]
- Source: [Publisher] ([Date])

**Key Finding 2**: [Finding with metric]
- Source: [Publisher] ([Date])

**Key Finding 3**: [Finding with metric]
- Source: [Publisher] ([Date])

**Recommendation**: [Based on findings above]

---

## 📚 Full References

| # | Title | Publisher | Date | URL |
|---|-------|-----------|------|-----|
| 1 | [Title] | [Publisher] | YYYY-MM-DD | [URL] |
| 2 | [Title] | [Publisher] | YYYY-MM-DD | [URL] |

**Total Sources**: N (Official: X, Academic: Y, Media: Z)
```

### Template 2: Comparison Analysis

```markdown
# [Option A] vs [Option B] Comparison

**Date**: YYYY-MM-DD
**Purpose**: [Decision context]

---

## Quick Comparison

| Criterion | [Option A] | [Option B] | Winner | Source |
|-----------|------------|------------|--------|--------|
| [Criterion 1] | [Value] | [Value] | [A/B/Tie] | [Publisher] |
| [Criterion 2] | [Value] | [Value] | [A/B/Tie] | [Publisher] |

---

## Detailed Analysis

### [Criterion 1]
[Analysis with sources]

### [Criterion 2]
[Analysis with sources]

---

## Recommendation

**Choose [Option]** if:
- [Condition 1]
- [Condition 2]

**Choose [Other Option]** if:
- [Condition 1]
- [Condition 2]

---

## Sources
[Full reference list]
```

## Quality Checklist

Before delivering research, verify:

**Content**:
- [ ] All major claims have sources
- [ ] Sources include full citation (title, publisher, date)
- [ ] All URLs are included and functional
- [ ] Information is current (check publication dates)
- [ ] Facts verified from 2+ independent sources

**Credibility**:
- [ ] Primary sources used (official/academic)
- [ ] Authoritative media for industry trends
- [ ] Author credentials checked
- [ ] Potential bias noted

**Structure**:
- [ ] Executive Summary included (3-5 bullets)
- [ ] Findings organized by topic
- [ ] Insights/implications provided
- [ ] References table completed
- [ ] Metadata included (date, source count)

**Technical**:
- [ ] All links tested (no 404s)
- [ ] Dates formatted consistently (YYYY-MM-DD)
- [ ] Quotations marked with quotes ("")
- [ ] Summary vs. quotation clearly distinguished

## Important Notes

**Requirements**:
- ⚠️ **Never omit sources**: Every fact/statistic needs attribution
- ⚠️ **Verify links**: Use WebFetch to confirm URLs work
- ⚠️ **Record dates**: Essential for assessing currency
- ⚠️ **Mark quotations**: Use quotes ("") for direct citations
- ⚠️ **Distinguish summary/quote**: Summaries cite source, quotes need quotes + source

**Limitations**:
- Web search may have regional restrictions
- Some content requires JavaScript rendering (static HTML only)
- Paywalled content may be inaccessible
- Some sites block automated access

**Workarounds**:
- Use official APIs when available
- Check Web Archive for dead links
- Look for press releases/official announcements
- Use multiple search queries for broader coverage

## Advanced Tips

**For Technical Research**:
- Prioritize official documentation and academic papers
- Include version numbers and release dates
- Note technology maturity (stable/beta/experimental)
- Cross-reference benchmarks from multiple sources

**For Market Research**:
- Use recent data (within 1-2 years for fast-moving industries)
- Note market research firm methodology
- Include geographic scope
- Cross-reference statistics

**For Competitive Analysis**:
- Start with official company sources
- Use third-party analysis for objectivity
- Note analyst credentials and affiliations
- Include multiple perspectives

## Related Resources

**Internal**:
- **SOURCE-CREDIBILITY-GUIDE.md**: ⭐ 4-tier source credibility classification & situational strategies (MUST READ!)
- **REFERENCE.md**: Standard templates and credibility criteria details
- **README.md**: Installation and setup guide

**Skills**:
- **strategic-thinking**: For analyzing research findings
- **market-strategy**: For turning research into strategy

**Credibility Assessment**:
- **SOURCE-CREDIBILITY-GUIDE.md**: Source credibility assessment criteria for web research (4-tier classification, purpose-based strategies, tool-specific utilization)
- Always consult this guide when evaluating source credibility

---

For detailed usage and examples, see related documentation files.
