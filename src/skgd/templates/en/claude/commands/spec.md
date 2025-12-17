# /spec [feature-name] - Create Feature Specification

You are creating a detailed specification for a game feature.

**Argument:** `$ARGUMENTS` (feature name, e.g., "player-movement", "enemy-ai")

## Your Task

### Step 1: Validate Feature

Read `.skgd/roadmap.yaml` to verify:
- Feature exists in roadmap
- Dependencies are met (blocking features completed)
- Feature is appropriate for current phase

If no argument provided, read roadmap and suggest next feature.

### Step 2: Load Context

Read these files:
- `docs/game-brief.md` - Core vision
- `docs/gdd.md` - If exists, relevant sections
- `.skgd/templates/spec.md` - Spec template
- `.skgd/templates/game-types/[type].md` - Type-specific guidance
- `.skgd/memory/constitution.md` - Constraints
- `.skgd/memory/learnings.md` - Past learnings
- `.skgd/config.yaml` - Get `mcp.assets.profile` for art style guidance
- `.skgd/memory/assets-catalog.md` - Existing assets and style guide

For dependencies, also read:
- `docs/specs/[dependency]/spec.md` - Each dependency spec

### Step 3: Delegate to Designer Agent

Use Task tool with **sonnet** model:

```
Task: Create feature specification

Agent: designer
Model: sonnet

Feature: [feature-name]
Context: [loaded context summary - keep minimal]

Create specification following template structure:
1. Overview - What and why
2. User Stories - As a player, I want...
3. Requirements - Functional and non-functional
4. Mechanics Detail - How it works
5. Edge Cases - What could go wrong
6. Dependencies - What this needs
7. Acceptance Criteria - How we know it's done
8. Asset Requirements - Visual/audio assets needed (IMPORTANT: be specific about sizes, styles)
9. Unity Implementation Hints - Components, scripts suggested

IMPORTANT: Always fill the Asset Requirements section based on art style from config.
Reference `.skgd/memory/assets-catalog.md` for existing assets and style guide.
```

### Step 4: Create Spec File

Create `docs/specs/[feature-name]/spec.md`:

```markdown
# [Feature Name] Specification

## Overview
[What this feature is and why it matters to the game]

## User Stories

### Primary
- As a player, I want to [action] so that [benefit]

### Secondary
- As a player, I want to [action] so that [benefit]

## Requirements

### Functional
- [ ] FR-1: [Requirement]
- [ ] FR-2: [Requirement]

### Non-Functional
- [ ] NFR-1: Performance - [target]
- [ ] NFR-2: Feel - [quality target]

## Mechanics Detail

### Core Behavior
[Detailed description of how the mechanic works]

### Parameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| [param] | [value] | [why] |

### State Machine (if applicable)
```
[State A] --[trigger]--> [State B]
```

## Edge Cases
1. **[Case]**: [How to handle]
2. **[Case]**: [How to handle]

## Dependencies
- [x] [Completed dependency]
- [ ] [Pending dependency] - Blocked

## Acceptance Criteria
- [ ] AC-1: [Testable criterion]
- [ ] AC-2: [Testable criterion]
- [ ] AC-3: [Testable criterion]

## Asset Requirements

### Visual Assets
| ID | Name | Type | Size | Description | Priority |
|----|------|------|------|-------------|----------|
| SPR-1 | [asset_name] | sprite | [WxH] | [What it shows] | Must |

### 3D Models (if applicable)
| ID | Name | Poly Budget | Description | Priority |
|----|------|-------------|-------------|----------|

### Audio Assets
| ID | Name | Type | Duration | Description | Priority |
|----|------|------|----------|-------------|----------|
| SFX-1 | [asset_name] | sfx | [length] | [What it sounds like] | Must |

### Style Notes
- **Art style reference:** [From config or specific to this feature]
- **Color palette:** [From assets-catalog or feature-specific]
- **Size constraints:** [Platform-specific requirements]

## Unity Implementation Hints

### Suggested Components
- `[ComponentName]` - [purpose]

### Suggested Scripts
- `[ScriptName].cs` - [responsibility]

### Scene Setup
- [GameObject structure suggestion]

---
*Created: [timestamp]*
*Status: Draft*
*Dependencies: [list]*
```

### Step 5: Update State

Update `.skgd/state.yaml`:
```yaml
production:
  current_spec: [feature-name]
  current_step: spec

specs:
  total: [increment]
  in_progress: [feature-name]

assets:
  queue:
    - feature: [feature-name]
      pending_assets: [count from Asset Requirements section]
```

Update `.skgd/roadmap.yaml`:
- Mark feature as `in_progress`

If assets were defined, also count them:
```yaml
assets:
  total_defined: [increment by assets count]
```

### Step 6: Git Commit

```bash
git add docs/specs/[feature-name]/
git commit -m "docs: add [feature-name] specification"
```

### Step 7: Next Steps

Display this message and **STOP**:
```
📋 Specification Created: [feature-name]

Location: docs/specs/[feature-name]/spec.md

Spec Summary:
- [N] User stories
- [N] Requirements
- [N] Acceptance criteria
- [N] Assets defined

Next steps (for user to decide):
  → /plan [feature-name] - Generate implementation plan
  → /assets list [feature-name] - Review required assets
  → /spec [other-feature] - Spec another feature
  → /continue - Auto-route to planning
```

If assets were defined and MCPs are configured, add:
```
💡 Tip: Run /assets generate [feature-name] before /implement to prepare assets.
```

## Auto-Suggest

After displaying the summary, show the auto-suggest prompt:

```
───────────────────────────────────────
Next: Create implementation plan
[Enter] /plan [feature] | [S] stop
───────────────────────────────────────
```

- If user presses **Enter** or says "yes"/"continue": Execute `/plan [feature-name]`
- If user says **"stop"**, **"s"**, or anything else: Exit and let user control pace

## IMPORTANT: Wait for User Response

**Do NOT automatically proceed** - show the auto-suggest prompt and wait.

This gives user control while reducing friction for the common path.

## Model
Use: **sonnet** (structured documentation task)
