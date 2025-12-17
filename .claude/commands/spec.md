# /spec [feature-name] - Create Feature Specification

You are Opus, creating a detailed specification for a game feature.

**Argument:** `$ARGUMENTS` (feature name, e.g., "player-movement", "enemy-ai")

## Model

**MANDATORY: opus** - Specifications require deep understanding of game design and technical implications.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Philosophy

**DO NOT delegate to a sub-agent.** You create the spec directly, using your understanding of the game's vision and technical requirements.

Use Task(Sonnet) ONLY for:
- Exploring existing codebase structure
- Reading multiple files for context
- Searching for patterns in implemented code

## Step 1: Validate Feature

Read `.skgd/roadmap.yaml`:
- Feature exists in roadmap
- Dependencies are met
- Appropriate for current phase

If no argument, suggest next feature from roadmap.

## Step 2: Load Context (Minimal)

**Always read:**
- `docs/game-brief.md` - Core vision
- `.skgd/memory/constitution.md` - Constraints
- `.skgd/memory/learnings-core.md` - Validated patterns

**Read if relevant:**
- `docs/specs/[dependency]/spec.md` - Dependency specs

**Use Task(Sonnet) for:**
- Exploring Unity project structure if needed
- Finding existing similar implementations

## Step 3: Understand Before Writing

Before writing the spec, ensure you understand:
- How this feature serves the core loop
- What makes it feel right for THIS game
- Technical constraints from learnings
- How it connects to existing features

If unclear, ASK the user. Don't guess.

## Step 4: Create Spec

Create `docs/specs/[feature-name]/spec.md`:

```markdown
# [Feature Name] Specification

## Why This Feature

[1-2 sentences connecting to core vision - why this matters for the game]

## Overview

[What this feature is and how it fits the game]

## Player Experience

### User Stories
- As a player, I want to [action] so that [feeling/benefit]

### Target Feel
[What should this feel like? Reference similar games if helpful]

## Requirements

### Functional
- [ ] FR-1: [Specific, testable requirement]
- [ ] FR-2: [Specific requirement]

### Non-Functional
- [ ] NFR-1: Performance - [target, e.g., "< 1ms per frame"]
- [ ] NFR-2: Feel - [quality target]

## Mechanics Detail

### Core Behavior
[How the mechanic works - be specific]

### Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| [param] | [value] | [why this value] |

### States (if applicable)
```
[State A] --[trigger]--> [State B]
```

## Edge Cases

1. **[Case]**: [How to handle]
2. **[Case]**: [How to handle]

## Dependencies

- [x] [Completed dependency]
- [ ] [Required before this]

## Acceptance Criteria

- [ ] AC-1: [Testable - how to verify]
- [ ] AC-2: [Testable - how to verify]

## Unity Implementation Hints

### Suggested Structure
```
Assets/Scripts/[Feature]/
├── [Component].cs
└── [System].cs
```

### Key Considerations
- [Unity-specific consideration from learnings]

---
*Created: [timestamp]*
*Vision alignment: [brief note on how this serves the core loop]*
```

## Step 5: Quality Check

Before saving, verify:
- [ ] Every requirement is testable
- [ ] Parameters have rationale (not magic numbers)
- [ ] Edge cases considered
- [ ] Aligns with constitution/vision
- [ ] Uses patterns from learnings-core.md

## Step 6: Update State

Update `.skgd/state.yaml`:
```yaml
production:
  current_spec: [feature-name]
  current_step: spec

specs:
  total: [increment]
  in_progress: [feature-name]
```

Update `.skgd/roadmap.yaml`:
- Mark feature as `in_progress`

## Step 7: Git Commit

```bash
git add docs/specs/[feature-name]/
git commit -m "docs: add [feature-name] specification

Connects to: [core loop element]
Dependencies: [list]"
```

## Step 8: Summary

```
Spec created: [feature-name]

Location: docs/specs/[feature-name]/spec.md

Summary:
- [N] Requirements
- [N] Acceptance criteria
- Key mechanic: [brief]

Next:
  /plan [feature-name] - Generate implementation plan
  /continue - Auto-route to planning
```

## Remember

- **Vision first**: Every spec should serve the core loop
- **Be specific**: Vague specs create vague implementations
- **Rationale matters**: Document WHY, not just WHAT
- **Use learnings**: Apply validated patterns
