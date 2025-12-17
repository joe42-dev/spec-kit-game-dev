# SKGD Tutorial - Part 0: Overview

## What is Spec Kit Game Dev?

**SKGD** is a spec-driven game development workflow that uses Claude as a cognitive partner. It provides:

- **Structured phases** from concept to production
- **Living documentation** that evolves with your project
- **MCP integration** for direct engine control (Unity/Godot)
- **Context engineering** to keep Claude in the "Smart Zone"

## The Philosophy

```
Documentation is the source of truth
    → Code follows specs, never the inverse
    → Every decision is traceable
```

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 0: SETUP                                                 │
│  skgd init → /init                                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: CONCEPT                                               │
│  /brainstorm → /pillars → /deep-dive × N → /validate-design     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 2: PLANNING                                              │
│  /roadmap → /architecture                                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 3: PRODUCTION (repeat per feature)                       │
│  /spec → /plan → /tasks → /implement → /playtest                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  UTILITIES (anytime)                                            │
│  /continue, /crystallize, /pivot, /snapshot, /project-status    │
└─────────────────────────────────────────────────────────────────┘
```

## Command Quick Reference

| Command | Phase | Purpose |
|---------|-------|---------|
| `/init` | Setup | Initialize project |
| `/brainstorm` | Concept | Creative ideation (3 modes) |
| `/pillars` | Concept | Generate design pillar structure |
| `/deep-dive [pillar]` | Concept | Develop one pillar in depth |
| `/validate-design` | Concept | Check cross-pillar coherence |
| `/roadmap` | Planning | Prioritize features |
| `/architecture` | Planning | Technical blueprint |
| `/spec [feature]` | Production | Feature specification |
| `/plan [feature]` | Production | Implementation plan |
| `/tasks [feature]` | Production | Actionable task list |
| `/implement` | Production | Execute via MCP |
| `/playtest` | Production | Validate + capture learnings |
| `/continue` | Utility | Smart session router |
| `/crystallize` | Utility | Compress learnings |
| `/pivot` | Utility | Handle direction change |
| `/snapshot [v]` | Utility | Save project milestone |
| `/project-status` | Utility | Dashboard view |
| `/analyze [feature]` | Utility | Cross-artifact validation |
| `/assets` | Utility | Asset pipeline management |

## File Structure After Init

```
your-game-project/
├── CLAUDE.md                    # Project context for Claude
├── .claude/
│   ├── commands/                # Slash commands
│   ├── skills/                  # Engine-specific patterns
│   └── data/                    # Reference data
├── .skgd/
│   ├── config.yaml              # Project settings
│   ├── state.yaml               # Workflow state
│   ├── roadmap.yaml             # Feature priorities (generated)
│   └── memory/
│       ├── constitution.md      # Core vision (immutable)
│       ├── learnings.md         # Raw observations
│       ├── learnings-core.md    # Crystallized patterns
│       └── session-context.md   # Last session state
└── docs/
    ├── game-brief.md            # Vision document
    ├── architecture.md          # Technical blueprint
    ├── pillars/                  # Design pillars
    │   ├── _index.md
    │   └── [pillar].md
    └── specs/
        └── [feature]/
            ├── spec.md
            ├── plan.md
            ├── tasks.md
            └── playtest.md
```

## Next Steps

1. **[Part 1: Setup](01-setup.md)** - Installation and initialization
2. **[Part 2: Concept Phase](02-concept.md)** - Brainstorm to design pillars
3. **[Part 3: Planning Phase](03-planning.md)** - Roadmap and architecture
4. **[Part 4: Production Cycle](04-production.md)** - Spec to implementation
5. **[Part 5: Validation](05-validation.md)** - Playtest and learnings
6. **[Part 6: Utilities](06-utilities.md)** - Continue, pivot, snapshot
7. **[Part 7: Troubleshooting](07-troubleshooting.md)** - Common issues
8. **[Appendix: Data Flow](appendix-data-flow.md)** - Complete reference
