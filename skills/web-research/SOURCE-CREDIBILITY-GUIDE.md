# 📚 Source Credibility Guide

**Version**: 1.0.0
**Created**: 2025-01-04
**Purpose**: Source credibility assessment criteria and situation-specific utilization strategies for web research

---

## 🎯 4-Tier Credibility Classification

### Tier 1: Highest Credibility (90-100%)

**Source Types**: Official documentation, academic resources, government agencies

**Appropriate Situations**:
- Technical implementation guides
- Regulatory/compliance requirements
- Official API references
- Academic claims and evidence

**Source Examples**:
- 📘 Official technical documentation: AWS Docs, Django Docs, React Official
- 🎓 Academic journals/papers: IEEE, ACM, Nature, ScienceDirect
- 🏛️ Government/public agencies: FDA, NIST, official health authorities
- 📊 Standards documentation: ISO, NIST, OWASP
- 🏢 Major company official blogs: Google Cloud Blog, AWS Blog

**Usage Guide**:
```yaml
when_to_use:
  - AWS architecture design
  - Django ORM optimization
  - GxP compliance
  - Security standards implementation

verification:
  - Verify official website directly
  - Check version/date information
  - Access original documents directly

tools:
  - Web fetch (official PDF/pages)
```

---

### Tier 2: High Credibility (70-90%)

**Source Types**: Expert blogs, verified media, industry reports

**Appropriate Situations**:
- Technology trend research
- Best practice references
- Industry trend analysis
- Market research data

**Source Examples**:
- 💼 Industry specialist media: TechCrunch, The Verge, InfoWorld
- 👨‍💻 Verified developer blogs: Martin Fowler, Kent Beck, Real Python
- 📰 Tech specialist publications: InfoQ, DZone, Hacker News (top posts)
- 🎯 Market research firms: Gartner, Forrester, IDC, McKinsey
- 🏆 Conference presentations: Google I/O, AWS re:Invent, PyCon

**Usage Guide**:
```yaml
when_to_use:
  - Technology stack selection
  - Architecture pattern reference
  - Market trend analysis
  - Best practice research

verification:
  - Verify author credentials
  - Check publisher credibility
  - Check publication date (within 1 year recommended)
  - Cross-verify with other sources

tools:
  - Web search (latest information)
```

---

### Tier 3: Medium Credibility (50-70%)

**Source Types**: Community, personal blogs, Q&A sites

**Appropriate Situations**:
- Practical experience reference
- Troubleshooting
- Diverse perspective collection
- Community opinions

**Source Examples**:
- 💬 Stack Overflow (high-voted answers)
- 📝 Medium, Dev.to (high views/recommendations)
- 🐙 GitHub Issues/Discussions (verified projects)
- 🗣️ Reddit (r/programming, r/webdev)
- 👥 Individual developer blogs (verifiable credentials)

**Usage Guide**:
```yaml
when_to_use:
  - Error message resolution
  - Practical tips/tricks
  - Comparing various approaches
  - Community opinion gathering

verification:
  - ⚠️ Multiple source cross-verification mandatory
  - Check upvotes/recommendation count
  - Check publication date (within 1 year recommended)
  - Review comments/reactions
  - Re-verify with Tier 1-2 mandatory

caution:
  - Never use alone
  - Not for critical decisions
  - Not for regulatory/compliance
```

---

### Tier 4: Low Credibility (30-50%)

**Source Types**: Anonymous communities, unverified individuals, marketing materials

**Appropriate Situations**:
- Initial idea collection
- Hypothesis formation
- Broad exploration
- Brainstorming

**Source Examples**:
- 🌐 Personal blogs (unknown identity)
- 💭 Q&A sites (low-voted answers)
- 📱 Social media (Twitter/X, Facebook)
- 🗨️ Anonymous communities (anonymous forums)
- 📢 Marketing materials (vendor promotional content)

**Usage Guide**:
```yaml
when_to_use:
  - Initial brainstorming
  - Problem recognition phase
  - Diverse opinion collection
  - "Interesting approach" level only

critical_rules:
  - ❌ Never use alone (absolute prohibition)
  - ❌ Never use instead of official docs
  - ❌ Never use as decision-making basis
  - ⚠️ Re-verify with Tier 1-2 mandatory
  - ⚠️ Distinguish facts vs opinions
  - ⚠️ Recognize bias

```

---

## 🎯 Source Selection Strategy by Research Purpose

### 1. Technical Documentation/Implementation Guide

**Purpose**: Accurate implementation, verify official recommendations

**Source Selection**:
```yaml
primary: Tier 1 (90%+)
  - Official documentation priority

secondary: Tier 2 (10%)
  - Verified tutorials

avoid: Tier 3-4
  - Risk of outdated information
```

**Examples**:
- Django REST Framework → Django official docs
- AWS architecture → AWS Well-Architected Framework
- React Hooks → React official documentation

---

### 2. Troubleshooting/Error Resolution

**Purpose**: Quick problem solving, utilize practical experience

**Source Selection**:
```yaml
primary: Tier 3 (60%)
  - Stack Overflow
  - GitHub Issues

secondary: Tier 1 (30%)
  - Official issue tracker

validation: Tier 2 (10%)
  - Expert blogs

strategy:
  - Multiple source cross-verification
  - Prioritize recent answers (within 1 year)
  - Check upvotes + comments
```

**Examples**:
- "Django ORM N+1 problem" → Stack Overflow + Django official docs
- AWS Lambda timeout → GitHub Issues + AWS Forums

---

### 3. Technology Trends/Market Research

**Purpose**: Understand latest trends, collect decision-making evidence

**Source Selection**:
```yaml
primary: Tier 2 (50%)
  - Specialist media

secondary: Tier 1 (30%)
  - Market research reports

tertiary: Tier 3 (20%)
  - Community opinions

strategy:
  - Collect diverse perspectives
  - Recognize bias
  - Cite only Tier 1-2 for statistics
```

**Examples**:
- "AI healthcare market trends" → Gartner + TechCrunch + Reddit discussions
- "React vs Vue 2024" → State of JS + Dev.to + HN

---

### 4. Regulatory/Compliance

**Purpose**: Verify legal/regulatory requirements

**Source Selection**:
```yaml
primary: Tier 1 (100%)
  - Official regulatory documents only

secondary: Tier 2 (reference only)
  - Expert interpretations

critical_rules:
  - ❌ Never use Tier 3-4 (absolute prohibition)
  - ❌ Legal risk possible
```

**Examples**:
- HIPAA compliance → HHS official documentation only
- GxP compliance → FDA 21 CFR Part 11 only
- GDPR → EU official guidelines only

---

### 5. Idea Collection/Brainstorming

**Purpose**: Broad perspective, creative approaches

**Source Selection**:
```yaml
primary: Tier 3 (40%)
  - Community

secondary: Tier 2 (30%)
  - Expert blogs

tertiary: Tier 4 (30%)
  - Social media/anonymous communities

strategy:
  - Quantitative collection (many opinions)
  - Lower bias tolerance OK
  - Verify with Tier 1-2 afterward
```

**Examples**:
- "Healthcare AI application ideas" → Reddit + Medium + Twitter
- "Progressive disclosure patterns" → HN + Dev.to + personal blogs

---

## ✅ Information Verification Checklist

### Basic Verification (All Sources)

```yaml
author_identity:
  □ Real name? Anonymous?
  □ Verifiable expertise?
  □ Organization credibility?

publication_date:
  □ Within 1 year? (technical docs)
  □ Latest version for regulations?
  □ Newer information available?

source_citation:
  □ References available?
  □ Statistics/numbers traceable to source?
  □ Secondary citation vs primary source?

bias:
  □ Specific vendor promotion?
  □ Objective evidence vs subjective opinion?
  □ Opposing views presented?
```

---

### Cross-Verification (Mandatory for Tier 3-4)

```yaml
multiple_sources:
  □ Minimum 3 sources
  □ Different Tier combinations
  □ Contradictory information checked

official_doc_reverification:
  □ Tier 3-4 → Re-verify with Tier 1-2
  □ Query latest documentation

experiment_test:
  □ Code examples executed directly
  □ Concepts validated with simple PoC
```

---

## 📋 Real-World Scenario Applications

### Scenario 1: Django REST API Implementation

```yaml
step_1_official_docs:
  tier: Tier 1
  time: 10 minutes

step_2_best_practices:
  tier: Tier 2
  domain_filter: ["realpython.com", "testdriven.io"]
  time: 15 minutes

step_3_troubleshooting:
  tier: Tier 3
  query: "Django REST Framework {error}"
  time: 5 minutes

validation:
  - All code re-verified with official docs
  - Stack Overflow answers cross-verified with 2+ sources
```

---

### Scenario 2: Healthcare AI Security Assessment

```yaml
step_1_regulations:
  tier: Tier 1 only
  sources:
    - FDA 21 CFR Part 11
    - HIPAA Security Rule
    - ISO 27001
  time: 30 minutes

step_2_case_studies:
  tier: Tier 2
  sources:
    - Gartner healthcare AI reports
    - Major healthcare provider press releases
    - Academic case studies
  time: 20 minutes

step_3_community:
  tier: Tier 3 (reference only)
  sources:
    - Reddit r/healthIT
    - LinkedIn healthcare professionals
  time: 10 minutes
  note: "No citation, idea collection only"

validation:
  - Proposals cite only Tier 1-2
  - Statistics with source attribution
  - Tier 3 for internal reference only
```

---

### Scenario 3: AWS Architecture Trends

```yaml
step_1_official:
  tier: Tier 1
  sources:
    - AWS re:Invent presentations
    - AWS Architecture Blog
  time: 20 minutes

step_2_expert:
  tier: Tier 2
  sources:
    - ThoughtWorks Tech Radar
    - Martin Fowler blog
    - InfoQ
  domain_filter: ["thoughtworks.com", "martinfowler.com", "infoq.com"]
  time: 30 minutes

step_3_community:
  tier: Tier 3
  sources:
    - Hacker News
    - Reddit r/aws
    - Dev.to
  time: 20 minutes

synthesis:
  task: "Synthesize Tier 1-2-3 + resolve contradictions"
```

---

### Scenario 4: Error Troubleshooting

```yaml
step_1_stack_overflow:
  tier: Tier 3
  tool: WebSearch
  query: "exact error message"
  filter: upvotes 10+
  time: 5 minutes

step_2_official_issues:
  tier: Tier 1
  tool: WebFetch
  target: GitHub Issues (official repo)
  time: 10 minutes

step_3_validation:
  - Verify 2+ Stack Overflow answers
  - Re-verify with official docs
  - Test directly before applying
```

---

## ⚠️ Cautions & Best Practices

### 🚫 Never Do

```yaml
never_do:
  - Use Tier 4 alone (especially regulatory/compliance)
  - Use technical docs older than 1 year without verification
  - Cite marketing materials as technical evidence
  - Cite anonymous communities like official docs
  - Use unattributed statistics/numbers
```

---

### ✅ Always Do

```yaml
always_do:
  - Check publication date (especially technical docs)
  - Specify source & credibility Tier
  - Re-verify Tier 3-4 with Tier 1-2
  - Use only Tier 1-2 for critical decisions
  - Use Tier 1 only for regulatory/legal
```

---

### 📊 Recommended Citation Ratios by Credibility

```yaml
technical_documentation:
  Tier1: 80-90%
  Tier2: 10-20%
  Tier3: 0% (reference only)

trend_analysis:
  Tier1: 40%
  Tier2: 40%
  Tier3: 20%

troubleshooting:
  Tier1: 30%
  Tier2: 20%
  Tier3: 50% (cross-verification mandatory)

compliance:
  Tier1: 100%
  Tier2-4: 0% (absolute prohibition)
```

---

## 🎓 Summary: Quick Selection Guide by Situation

| Situation | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|----------|--------|--------|--------|--------|
| **Technical Implementation** | 90% ✅ | 10% | - | - |
| **Trend Research** | 40% | 40% ✅ | 20% | - |
| **Troubleshooting** | 30% | 20% | 50% ✅ | - |
| **Regulatory/Legal** | 100% ✅ | - | - | ❌ |
| **Idea Collection** | 30% | 30% | 30% ✅ | 10% |
| **Decision Evidence** | 70% ✅ | 30% | - | - |

---

## 📚 Related Resources

### Internal Documentation
- **SKILL.md**: Detailed 4-step research process
- **REFERENCE.md**: Templates & real examples
- **README.md**: Installation & usage

### Skills
- **market-strategy**: Develop market strategy

---

---

**💡 Quick Tip**:
- Official implementation → Use Tier 1 sources only
- Latest trends → Tier 2-3 sources acceptable
- Comprehensive research → Combine all Tiers systematically
- Regulatory/legal → Tier 1 only ⚠️
