# [Feature Name] Specification

> Template for feature specifications

## Overview

### What
[One paragraph describing what this feature is]

### Why
[Why this feature matters to the game/player experience]

### Scope
[What's included and explicitly excluded]

## User Stories

### Primary
- As a player, I want to [action] so that [benefit]
- As a player, I want to [action] so that [benefit]

### Secondary
- As a player, I want to [action] so that [benefit]

## Requirements

### Functional Requirements
| ID | Requirement | Priority |
|----|-------------|----------|
| FR-1 | [Requirement description] | Must |
| FR-2 | [Requirement description] | Must |
| FR-3 | [Requirement description] | Should |
| FR-4 | [Requirement description] | Could |

### Non-Functional Requirements
| ID | Requirement | Target |
|----|-------------|--------|
| NFR-1 | Performance | [specific metric] |
| NFR-2 | Responsiveness | [input latency target] |
| NFR-3 | Visual quality | [quality target] |

## Mechanics Detail

### Core Behavior
[Detailed description of how the mechanic works]

### Parameters
| Parameter | Default | Range | Notes |
|-----------|---------|-------|-------|
| [param] | [value] | [min-max] | [why this value] |

### State Machine (if applicable)
```
[Idle] --[input]--> [Active] --[complete]--> [Cooldown] --[timer]--> [Idle]
```

### Interactions
- With [System A]: [how they interact]
- With [System B]: [how they interact]

## Edge Cases

| Case | Trigger | Expected Behavior |
|------|---------|-------------------|
| [Case 1] | [How it occurs] | [What should happen] |
| [Case 2] | [How it occurs] | [What should happen] |
| [Case 3] | [How it occurs] | [What should happen] |

## Dependencies

### Requires (Blocking)
- [ ] [Feature/System that must exist first]

### Enhanced By (Non-blocking)
- [ ] [Feature that would improve this, but not required]

## Acceptance Criteria

| ID | Criterion | Verification |
|----|-----------|--------------|
| AC-1 | [Specific, testable criterion] | [How to verify] |
| AC-2 | [Specific, testable criterion] | [How to verify] |
| AC-3 | [Specific, testable criterion] | [How to verify] |

## Asset Requirements

> Define all visual and audio assets needed for this feature.
> These will be tracked and can be generated via /assets generate

### Visual Assets
| ID | Name | Type | Size | Description | Priority |
|----|------|------|------|-------------|----------|
| SPR-1 | [asset_name] | sprite | [WxH] | [What it shows] | Must |
| SPR-2 | [asset_name] | animation | [frames] | [What it animates] | Should |
| TEX-1 | [asset_name] | texture | [resolution] | [What it's for] | Could |

### 3D Models (if applicable)
| ID | Name | Poly Budget | Description | Priority |
|----|------|-------------|-------------|----------|
| MDL-1 | [model_name] | low/med/high | [What it is] | Must |

### Audio Assets
| ID | Name | Type | Duration | Description | Priority |
|----|------|------|----------|-------------|----------|
| SFX-1 | [sound_name] | sfx | [Xs] | [When it plays] | Should |
| MUS-1 | [music_name] | music | [Xm] | [When it plays] | Could |

### Style Notes
- **Art style reference:** [Game/image reference or description]
- **Color palette:** [Primary colors or link to palette]
- **Size constraints:** [e.g., 32x32 pixel sprites, 2K textures max]

### Asset Dependencies
- Shares assets with: [other features]
- Requires assets from: [other features]

## Unity Implementation Hints

### Suggested Components
| Component | GameObject | Purpose |
|-----------|------------|---------|
| [Script] | [Target] | [What it does] |

### Scene Setup
```
[Parent Object]
├── [Child 1] (Components: X, Y)
└── [Child 2] (Components: Z)
```

### Key Unity APIs
- `[API]` - for [purpose]
- `[API]` - for [purpose]

## Open Questions

- [ ] [Question that needs clarification]
- [ ] [Decision that needs to be made]

---

*Created: [timestamp]*
*Status: Draft*
*Author: Designer Agent*
