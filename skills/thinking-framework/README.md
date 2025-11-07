# Thinking Framework v2.0

> Systematic problem-solving using 14 proven thinking methodologies

Transform complex problems into structured solutions using battle-tested frameworks like 5 Why, First Principles, SWOT, Design Thinking, and more.

---

## 🚀 Quick Start (5 minutes)

### 1. Start With Problem Definition

**FIRST STEP**: Clarify what the real problem is using [Problem Definition](reference/problem-definition.md)

**Why?** Most problem-solving failures come from solving the wrong problem. Spend 30-60 minutes:
- Understanding if this is the real problem or a symptom
- Uncovering hidden assumptions
- Defining success criteria

### 2. Identify Your Problem Type

**Got a specific problem?** Jump to the [Problem Type Selector](GUIDE.md#problem-type-selector) in the User Guide.

**Common scenarios** (after Problem Definition):
- 🔍 **"Why did this happen?"** → [5 Why](reference/5-why.md) or [Fishbone](reference/fishbone.md)
- 💡 **"How can I innovate?"** → [SCAMPER](reference/scamper.md), [First Principles](reference/first-principles.md), [TRIZ](reference/triz.md)
- 🎯 **"What's my strategy?"** → [SWOT](reference/swot.md) + [GAP Analysis](reference/gap-analysis.md)
- ⚙️ **"How to improve this?"** → [Pareto](reference/pareto.md), [PDCA](reference/pdca.md)

### 3. Apply the Method

Each method guide includes:
- Clear definition
- Step-by-step process
- Real-world examples
- When to use / when to avoid

### 4. Reflect and Iterate

After applying a method:
- What worked well?
- What could be improved?
- Would a different method fit better?

---

## 📚 Documentation Structure

```
thinking-framework/
├── README.md                    # ← You are here (Project overview)
├── GUIDE.md                     # Practical user guide with examples
├── SKILL.md                     # AI execution prompts (technical)
└── reference/                   # Detailed method documentation
    ├── INDEX.md                 # Method catalog and selector
    ├── 5-why.md                 # Individual method guides
    ├── fishbone.md
    ├── first-principles.md
    └── ... (14 methods total)
```

### For Different Audiences

| Your Goal | Start Here |
|-----------|------------|
| **Learn how to use** | [GUIDE.md](GUIDE.md) - Practical guide with real examples |
| **Choose a method** | [reference/INDEX.md](reference/INDEX.md) - Method catalog |
| **Deep dive into method** | [reference/](reference/) - Individual method files |
| **AI-assisted analysis** | [SKILL.md](SKILL.md) - Execution prompts |

---

## 🎯 What's Included

### 15 Proven Thinking Methods

**Foundational Method (Start Here)**
- [Problem Definition](reference/problem-definition.md) - Clarify the true problem before solving

**Root Cause Analysis**
- [5 Why](reference/5-why.md) - Drill down causal chains
- [Fishbone Diagram](reference/fishbone.md) - Multi-dimensional analysis

**Innovation & Breakthrough**
- [First Principles](reference/first-principles.md) - Fundamental reconstruction
- [Design Thinking](reference/design-thinking.md) - User-centric innovation
- [TRIZ](reference/triz.md) - Technical contradiction resolution
- [SCAMPER](reference/scamper.md) - Creative modification prompts

**Strategic Planning**
- [SWOT Analysis](reference/swot.md) - Strengths/Weaknesses/Opportunities/Threats
- [GAP Analysis](reference/gap-analysis.md) - Current → Target planning

**Process Improvement**
- [Pareto (80/20)](reference/pareto.md) - Prioritize critical few
- [PDCA Cycle](reference/pdca.md) - Iterative improvement
- [DMAIC](reference/dmaic.md) - Six Sigma quality

**Decision Making**
- [OODA Loop](reference/ooda-loop.md) - Rapid decision cycles
- [Kepner-Tregoe](reference/kepner-tregoe.md) - Systematic analysis

**Synthesis**
- [Dialectic](reference/dialectic.md) - Integrate opposing views

---

## 💡 Key Features

### v2.1 Improvements (NEW!)

**Problem Definition Thinking**: Start EVERY problem-solving effort by clarifying the true problem
- Prevents solving the wrong problem efficiently
- Uncovers hidden assumptions
- Creates clear success criteria
- Saves weeks of wasted effort

### v2.0 Improvements

**Complexity Assessment**: Prevent over/under-engineering with pre-flight checks
- Simple problems (1-2 steps) → Quick methods
- Medium problems (3-5 steps) → Standard methods
- Complex problems (5+ factors) → Advanced methods

**Method-Problem Matching**: Evidence-based recommendations
- Success rates from 20 execution analysis
- Anti-patterns highlighted (e.g., DMAIC for innovation = 0% success)
- Optimal combinations suggested

**Quality Safeguards**
- Pre-flight checks catch mismatches early
- 2x2 priority matrix mandatory for SWOT (fixes 33% failure rate)
- Max 5 sub-problems for Divide & Conquer (prevents over-complexity)

---

## 🎓 Learning Path

### Beginner (Week 1)
1. Read [GUIDE.md](GUIDE.md) "What Is This?" and "Problem Type Selector"
2. Try [5 Why](reference/5-why.md) on a real problem (simplest method)
3. Review [Common Mistakes](GUIDE.md#common-mistakes-and-solutions)

### Intermediate (Week 2-4)
1. Apply [SWOT](reference/swot.md) + [GAP Analysis](reference/gap-analysis.md) to a project
2. Experiment with [Pareto](reference/pareto.md) for prioritization
3. Try [SCAMPER](reference/scamper.md) for quick ideation

### Advanced (Month 2+)
1. Master [First Principles](reference/first-principles.md) for breakthrough thinking
2. Learn method combinations from [INDEX.md](reference/INDEX.md)
3. Use [SKILL.md](SKILL.md) for AI-assisted systematic analysis

---

## 📊 Success Metrics

Based on v1.0 analysis of 20 executions:

| Metric | v1.0 Baseline | v2.0 Target |
|--------|---------------|-------------|
| Overall Success Rate | 70% | 90%+ |
| Complexity Matching | Simple: 50%, Complex: 57% | 85%+ all |
| User Satisfaction | 3.7/5.0 | 4.5+/5.0 |

**High Success Methods** (100% success rate):
- 5 Why, Fishbone (root cause)
- First Principles, TRIZ, SCAMPER, Design Thinking (innovation)
- Pareto, PDCA, GAP (process improvement)
- OODA Loop (decision making)

---

## 🛠️ Use Cases

### For Individuals
- Debug complex technical problems
- Make career decisions
- Plan personal projects
- Learn systematic thinking

### For Teams
- Strategic planning sessions
- Post-mortem analysis
- Innovation workshops
- Process improvement initiatives

### For Organizations
- Product development
- Business strategy
- Quality management
- Organizational change

---

## 📦 Installation

### Option 1: Using prpm (Recommended)

```bash
prpm install thinking-framework
```

### Option 2: Manual Installation

1. **Download or clone this package**
2. **Create ZIP package**:
   ```bash
   zip -r thinking-framework.zip thinking-framework/
   ```
3. **Upload to Claude.ai or Claude Code**:
   - Go to Settings > Capabilities > Skills
   - Upload `thinking-framework.zip`
   - Activate the skill

### Option 3: Direct Copy

Copy the entire `thinking-framework/` directory to your Claude skills directory

---

## 🧪 Testing Your Installation

After installing, try these prompts to verify the skill works:

1. **Test Root Cause**: "Our API response times are slow. What's the root cause?"
2. **Test Innovation**: "How can we improve our user onboarding experience?"
3. **Test Strategy**: "I have limited resources. How do I prioritize?"

If Claude invokes the Thinking Framework and follows structured routines, the skill is working correctly.

---

## 🔧 Customization

You can customize this skill by editing `SKILL.md`:

- **Adjust triggers**: Change when Claude invokes the skill
- **Add domain methods**: Include industry-specific frameworks
- **Modify routines**: Adjust steps to match your workflow
- **Add examples**: Include domain-relevant examples

---

## 🐛 Troubleshooting

**Claude doesn't invoke the skill:**
- Check that the skill is activated in Settings > Capabilities
- Ensure your prompt involves complex problem-solving
- Try being explicit: "Use systematic thinking to solve this"

**Skill invoked but incomplete:**
- Problem may be too simple for advanced routines
- Check SKILL.md formatting (YAML frontmatter required)

**Need more detail:**
- Check [reference/INDEX.md](reference/INDEX.md) for method catalog
- Read individual method files in [reference/](reference/)
- Review [GUIDE.md](GUIDE.md) for practical examples

---

---

For detailed usage and examples, see related documentation files.