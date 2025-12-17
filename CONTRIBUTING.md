# Contributing to Spec Kit Game Dev

Thank you for considering contributing to SKGD! This document provides guidelines and information for contributors.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Development Workflow](#development-workflow)
- [Contribution Types](#contribution-types)
- [Pull Request Process](#pull-request-process)
- [Design Principles](#design-principles)
- [Testing](#testing)

---

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Maintain a positive environment

---

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- Claude Code CLI (for testing)
- Unity or Godot (for integration testing)

### Development Setup

```bash
# 1. Fork and clone
git clone https://github.com/YOUR-USERNAME/spec-kit-game-dev.git
cd spec-kit-game-dev

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# 3. Install in development mode
pip install -e .

# 4. Test installation
skgd --version
```

### Testing Your Changes

```bash
# Create test project
mkdir test-project && cd test-project
skgd init --engine unity

# Start Claude Code and test commands
claude
/init
/brainstorm
```

---

## Project Structure

```
spec-kit-game-dev/
├── src/skgd/
│   ├── cli.py              # Main CLI entry point
│   └── templates/          # Template files
│       ├── en/             # English templates
│       │   ├── claude/commands/   # Slash commands
│       │   │   ├── brainstorm.md
│       │   │   ├── implement.md
│       │   │   ├── _scout.md      # Internal helpers (_prefix)
│       │   │   └── ...
│       │   ├── skgd/              # Config & memory templates
│       │   │   ├── config.yaml
│       │   │   ├── state.yaml
│       │   │   └── memory/
│       │   │       ├── constitution.md
│       │   │       └── ...
│       │   └── docs/              # Document templates
│       └── fr/             # French templates (mirror structure)
├── docs/
│   ├── tutorial/           # User tutorial
│   └── diagrams/           # DOT visualization files
├── CLAUDE.md               # Dev context (not distributed)
├── README.md               # User documentation
└── pyproject.toml          # Package config
```

### Key Directories

| Directory | Purpose | Distributed to Users? |
|-----------|---------|----------------------|
| `src/skgd/templates/` | Template source of truth | Yes (via `skgd init`) |
| `.claude/commands/` | Dev testing only | No |
| `docs/tutorial/` | User documentation | Yes |
| `CLAUDE.md` | Dev context | No |

---

## Development Workflow

### 1. Branch Naming

```
feature/command-name     # New commands
fix/issue-description    # Bug fixes
docs/section-name        # Documentation
refactor/area            # Code improvements
```

### 2. Making Changes to Commands

Commands are in `src/skgd/templates/{lang}/claude/commands/`.

**Important:**
- **Always update both EN and FR** versions
- Use `_` prefix for internal helpers (e.g., `_scout.md`)
- Follow existing patterns (Scout-First for context-heavy commands)

### 3. Testing Locally

```bash
# Test command changes
cd /path/to/test-project
skgd upgrade  # Copies new templates

# Then test in Claude Code
claude
/your-command
```

---

## Contribution Types

### 1. New Commands

**When adding a new command:**

1. Create `src/skgd/templates/en/claude/commands/your-command.md`
2. Create `src/skgd/templates/fr/claude/commands/your-command.md`
3. Follow the command template pattern:

```markdown
# /your-command - Description

You are Opus, [role description].

## Model

**MANDATORY: opus|sonnet|haiku** - [Justification]

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Phase 0: Scout Context (if needed)

[Scout pattern for context gathering]

## Step 1: [Action]

[Implementation]

## Step N: Summary

[Output format]
```

4. Add to command table in README.md
5. Add to tutorial if significant
6. Update CLAUDE.md command reference

### 2. Bug Fixes

1. Create issue describing the bug
2. Reference issue in PR
3. Add test case if applicable

### 3. Documentation

- Keep language simple and direct
- Include practical examples
- Update both README and tutorial if needed

### 4. Templates

Templates in `src/skgd/templates/{lang}/skgd/templates/`:

- Keep templates minimal
- Use placeholders: `[placeholder]`
- Document template purpose in comments

---

## Pull Request Process

### 1. Before Submitting

- [ ] Tested with real Claude Code session
- [ ] Both EN and FR versions updated (if applicable)
- [ ] README.md updated (if adding feature)
- [ ] No debug/test artifacts left

### 2. PR Description

```markdown
## Summary
[Brief description of changes]

## Type
- [ ] New command
- [ ] Bug fix
- [ ] Documentation
- [ ] Refactor

## Testing
[How you tested the changes]

## Related Issues
Fixes #[issue number]
```

### 3. Review Criteria

- **Context efficiency**: Does it stay in the Smart Zone (~5k tokens)?
- **Pattern consistency**: Does it follow established patterns?
- **User value**: Does it solve a real problem?
- **Simplicity**: Is it the simplest solution?

---

## Design Principles

When contributing, keep these principles in mind:

### 1. Context is King

```
BAD:  Load all files, then work
GOOD: Scout pattern - Haiku gathers, Opus creates
```

Keep loaded context under ~5k tokens. Use Scout-First pattern for context-heavy commands.

### 2. Dialogue Over Delegation

```
BAD:  Auto-generate everything without user input
GOOD: Opus discusses, proposes options, gets user decisions
```

Commands should be collaborative, not automated.

### 3. Quality Over Speed

```
BAD:  Use Haiku for creative work (cheaper/faster)
GOOD: Use Opus for creative work, Haiku only for scouting
```

### 4. One Thing Well

```
BAD:  /super-command that does spec+plan+tasks+implement
GOOD: /spec, /plan, /tasks, /implement as separate commands
```

Each command should do one thing excellently.

### 5. User Agency

```
BAD:  "Running /implement automatically..."
GOOD: "Ready to implement. Options: [A] MVP [B] Full [C] Range?"
```

Always give users control over significant actions.

---

## Testing

### Manual Testing Checklist

For command changes:

- [ ] Command executes without errors
- [ ] Output matches expected format
- [ ] State files updated correctly
- [ ] Works with both Unity and Godot (if applicable)
- [ ] Works in both EN and FR

### Integration Testing

```bash
# Full workflow test
skgd init test-game --engine unity
cd test-game
claude

# Test sequence
/init
/brainstorm
/pillars
/deep-dive game-loop
/validate-design
/gdd
/roadmap
/architecture
/spec player-movement
/plan player-movement
/tasks player-movement
# /implement (requires MCP)
```

---

## Questions?

- Open an issue for questions
- Check existing issues before posting
- Be specific about what you're trying to do

---

## Recognition

Contributors will be acknowledged in release notes. Significant contributions may be highlighted in the README.

---

Thank you for contributing to SKGD!
