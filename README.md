# Agent Hub

> Comprehensive collection of Claude Code skills for productivity, business strategy, research, and development

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRPM Compatible](https://img.shields.io/badge/PRPM-Compatible-blue.svg)](https://prpm.dev)
[![Skills: 8](https://img.shields.io/badge/Skills-8-green.svg)](#-available-skills)

## 🎯 Overview

**Agent Hub** is a multi-package collection of specialized Claude Code skills designed to enhance AI-assisted workflows across various domains including psychology-based analysis, strategic thinking, web research, business strategy, and development patterns.

### Key Features

- 🧠 **Psychology & Persona Analysis** - Research-backed stakeholder analysis using 7 psychological frameworks
- 💡 **Thinking Frameworks** - 14 structured thinking methodologies for problem-solving
- 🔍 **Web Research** - Comprehensive OSINT framework with source credibility assessment
- 📊 **Business Strategy** - Market analysis and ROI evaluation tools
- 📝 **Document Organization** - Intelligent document management and template generation
- 🎨 **Development Patterns** - Toss-style coding patterns and best practices

## 📦 Available Skills

| Skill | Version | Size | Description |
|-------|---------|------|-------------|
| [ai-persona-creator](skills/ai-persona-creator/) | 1.0.0 | 17.32KB | Psychology-based persona analysis using 7 frameworks (Kahneman, Cialdini, Voss, Navarro, Ariely, Evolution, Organization) |
| [thinking-framework](skills/thinking-framework/) | 1.0.0 | 22.28KB | 14 structured thinking methodologies for systematic problem-solving |
| [web-research](skills/web-research/) | 1.0.0 | 24.33KB | OSINT web research framework with source credibility assessment |
| [doc-organizer](skills/doc-organizer/) | 1.0.0 | 4.70KB | Document organization and management tools |
| [template-generator](skills/template-generator/) | 1.0.0 | 7.51KB | Template generation system for various document types |
| [market-strategy](skills/market-strategy/) | 1.0.0 | 8.98KB | Market strategy analysis and planning tools |
| [roi-analyzer](skills/roi-analyzer/) | 1.0.0 | 7.96KB | ROI analysis framework for business decisions |
| [toss-patterns](skills/toss-patterns/) | 1.0.0 | 14.80KB | Toss-style development patterns and best practices |

## 🚀 Installation

### Install Individual Skills

Using PRPM (Prompt Package Manager):

```bash
# Psychology & Persona Analysis
prpm install ai-persona-creator

# Thinking Frameworks
prpm install thinking-framework

# Research & Investigation
prpm install web-research

# Document Management
prpm install doc-organizer
prpm install template-generator

# Business Tools
prpm install market-strategy
prpm install roi-analyzer

# Development Patterns
prpm install toss-patterns
```

### Install All Skills

```bash
# Clone the repository
git clone https://github.com/Tempuss/agent-hub.git
cd agent-hub

# Install all skills
prpm install
```

## 💻 Usage

### Using Skills with Claude Code

Skills are automatically activated based on context and keywords. You can also manually invoke them:

```bash
# Persona analysis for stakeholder negotiations
"Analyze the stakeholder psychology for this proposal"

# Strategic thinking for problem-solving
"Apply systematic thinking frameworks to this problem"

# Web research with credibility assessment
"Research this topic with source verification"

# Business strategy analysis
"Analyze market strategy for this product"
```

### Project Structure

```
agent-hub/
├── skills/                 # 8 Claude Code skills
│   ├── ai-persona-creator/ # Psychology-based persona analysis
│   ├── thinking-framework/ # 14 thinking methodologies
│   ├── web-research/      # OSINT research framework
│   ├── doc-organizer/     # Document management
│   ├── template-generator/# Template generation
│   ├── market-strategy/   # Market analysis
│   ├── roi-analyzer/      # ROI evaluation
│   └── toss-patterns/     # Development patterns
├── hooks/                 # Claude Code hooks
├── mcps/                  # MCP servers
│   ├── docx/             # Document processing
│   └── evolution/        # Pattern evolution
├── orchestrator/         # Agent orchestration system
├── prompts/              # Prompt library and knowledge base
└── scripts/              # Deployment and utility scripts
```

## 🛠️ Development

### Prerequisites

- [PRPM](https://prpm.dev) - Prompt Package Manager
- [Claude Code](https://claude.com/claude-code) - AI coding assistant

### Publishing Skills

```bash
# Verify all skills (dry-run)
./scripts/publish-all-skills.sh --dry-run

# Publish all skills
./scripts/publish-all-skills.sh

# Publish individual skill
./scripts/publish-skill.sh ai-persona-creator
```

See [PUBLISH_GUIDE.md](PUBLISH_GUIDE.md) for detailed publishing instructions.

### Adding New Skills

1. Create skill directory:
   ```bash
   mkdir -p skills/new-skill
   ```

2. Initialize PRPM package:
   ```bash
   cd skills/new-skill
   prpm init
   ```

3. Configure `prpm.json`:
   ```json
   {
     "name": "new-skill",
     "version": "1.0.0",
     "description": "Detailed description (min 100 characters recommended)",
     "author": "Tempuss",
     "license": "MIT",
     "format": "claude",
     "subtype": "skill",
     "tags": ["tag1", "tag2"],
     "files": ["SKILL.md", "README.md"]
   }
   ```

4. Update publish scripts:
   ```bash
   # Add to scripts/publish-all-skills.sh
   # Update prpm.json packages array
   ```

## 📊 Features by Category

### Psychology & Analysis
- **ai-persona-creator**: 7 psychological frameworks for stakeholder analysis
  - Kahneman's behavioral economics
  - Cialdini's influence principles
  - Voss's negotiation tactics
  - Navarro's behavioral analysis
  - Ariely's irrationality patterns
  - Evolutionary psychology
  - Organizational psychology

### Strategic Thinking
- **thinking-framework**: 14 structured methodologies
  - First Principles Thinking
  - Systems Thinking
  - Design Thinking
  - Critical Thinking
  - Creative Thinking
  - And 9 more frameworks...

### Research & Investigation
- **web-research**: Comprehensive OSINT framework
  - Multi-source verification
  - Credibility assessment
  - Structured investigation workflows
  - Source quality scoring

### Business Tools
- **market-strategy**: Market analysis and planning
- **roi-analyzer**: ROI evaluation framework
- **doc-organizer**: Document management
- **template-generator**: Template creation system

### Development
- **toss-patterns**: Toss-style coding patterns
  - Code organization
  - Best practices
  - Style guidelines

## 🔧 Advanced Features

### Hooks
Custom Claude Code hooks for workflow automation and context enhancement.

### MCP Servers
- **docx**: Document processing and generation
- **evolution**: Pattern learning and evolution

### Orchestrator
Agent coordination system for complex multi-agent workflows.

### Prompt Library
Curated collection of prompts and knowledge bases for various domains.

## 📝 Documentation

- [Publishing Guide](PUBLISH_GUIDE.md) - Detailed guide for publishing skills to PRPM
- Individual skill READMEs in `skills/*/README.md`
- Framework references in `skills/*/REFERENCE.md`

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-skill`)
3. Commit your changes (`git commit -m 'Add amazing skill'`)
4. Push to the branch (`git push origin feature/amazing-skill`)
5. Open a Pull Request

### Contribution Standards

- Follow existing skill structure and naming conventions
- Include comprehensive documentation (SKILL.md, README.md, REFERENCE.md)
- Add relevant examples and use cases
- Update PUBLISH_GUIDE.md if adding new skills
- Ensure `author: "Tempuss"` and `license: "MIT"` in all packages
- Test with `--dry-run` before submitting

## 📄 License

This project is licensed under the MIT License - see individual skill directories for details.

## 👤 Author

**Tempuss**

- GitHub: [@Tempuss](https://github.com/Tempuss)
- Repository: [agent-hub](https://github.com/Tempuss/agent-hub)

## 🙏 Acknowledgments

- Built for [Claude Code](https://claude.com/claude-code)
- Packaged with [PRPM](https://prpm.dev)
- Inspired by research in psychology, strategy, and software development

## 📊 Project Status

- ✅ **8/8 skills** ready for deployment
- ✅ All packages tested and verified
- ✅ Published to PRPM registry
- 🔄 Actively maintained and updated

## 🔗 Links

- [PRPM Registry](https://prpm.dev)
- [Claude Code Documentation](https://docs.claude.com)
- [Issue Tracker](https://github.com/Tempuss/agent-hub/issues)
- [Changelog](CHANGELOG.md) _(coming soon)_

---

**Built with ❤️ for the Claude Code community**