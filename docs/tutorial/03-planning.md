# SKGD Tutorial - Part 3: Planning Phase

## Overview

The Planning Phase prioritizes work and establishes technical foundations:

```
/roadmap → /architecture
```

## Step 1: Generate Roadmap

Run:
```
/roadmap
```

### First Time: Generation Mode

Creates `.skgd/roadmap.yaml` with:

**Prioritization Principles:**
1. Core loop first (minimum playable)
2. Dependencies respected
3. Complexity progression (simple → complex)
4. Risk early (fail fast)
5. Game-type aware

### Roadmap Structure

```yaml
generated: "2024-01-15T10:30:00Z"
game_type: roguelike
version: 1

phases:
  concept:
    status: completed
  design:
    status: completed
  production:
    cycles:
      - cycle: 1
        milestone: "Playable Core Loop"
        features:
          - id: player-movement
            priority: critical
            complexity: low
            dependencies: []
            status: pending
          - id: basic-combat
            priority: critical
            complexity: medium
            dependencies: [player-movement]
            status: pending

      - cycle: 2
        milestone: "Vertical Slice"
        features:
          - id: enemy-ai
            priority: high
            complexity: high
            dependencies: [basic-combat]
            status: pending

next_recommended:
  feature: player-movement
  reason: "No dependencies, critical priority"
  command: "/spec player-movement"
```

### Subsequent Runs: Display Mode

Shows current progress and updates statuses:
```
ROADMAP - [Game Name]

Phase: Production (Cycle 1)
Milestone: "Playable Core Loop"

Features:
  [✓] player-movement (completed)
  [→] basic-combat (in progress)
  [ ] level-generation
  [ ] basic-ui

Recommended Next: basic-combat
Run: /continue
```

## Step 2: Design Architecture

Run:
```
/architecture
```

### Prerequisites
- `game-brief.md` must exist
- `roadmap.yaml` must exist

### What It Covers

1. **Core Systems**
   - Game Loop (state flow diagram)
   - State Management (state table)
   - Scene Management (folder structure)
   - Data Persistence (save/load approach)

2. **Engine Patterns**

   **Unity:**
   - MonoBehaviour vs pure classes
   - ScriptableObjects for data
   - Event systems (UnityEvents, C# events)
   - Dependency injection approach

   **Godot:**
   - Node hierarchy design
   - Signal Bus pattern
   - Autoloads for globals
   - Resources for data

3. **Technical Decisions**
   - Input system design
   - UI framework choice
   - Audio architecture
   - Physics setup

### Output: architecture.md

```markdown
# [Game Name] - Technical Architecture

## Overview
### Technical Vision
[High-level approach]

### Architecture Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]

## Core Systems

### Game Loop
[State diagram]

### State Management
| State | Entry Condition | Exit Condition |
|-------|-----------------|----------------|

### Scene Management
```
Assets/Scenes/
├── Main/
├── Gameplay/
└── UI/
```

## System Architecture

### Core Managers
| Manager | Responsibility | Lifetime |
|---------|----------------|----------|

### Event System
[Pattern + diagram]

### Dependency Graph
[Component relationships]

## Feature System Patterns
[Per-feature from roadmap]

## Input Architecture
| Action | Input | Context |
|--------|-------|---------|

## UI Architecture
[Screen flow tree]

## Audio Architecture
| Category | Bus | Example |
|----------|-----|---------|

## Performance Considerations
| Metric | Target |
|--------|--------|

## Testing Strategy
- EditMode: [What]
- PlayMode: [What]
- Manual: [What]

## Extension Points
[For planned features]

## Appendix: Folder Structure
[Complete layout]
```

## Manual Edits Allowed

Both `roadmap.yaml` and `architecture.md` can be manually edited:

### Roadmap Reordering
```yaml
# Change priority manually
features:
  - id: enemy-ai
    priority: critical  # Was: high
```

### Architecture Updates
Add sections as you learn:
- New patterns discovered
- Performance findings
- Integration notes

## Reusing Commands

### Re-run /roadmap
- **Display mode** if `roadmap.yaml` exists
- Asks to regenerate if you want fresh prioritization
- Updates feature statuses from completed specs

### Re-run /architecture
- **Overwrites** `architecture.md`
- Useful after major design changes
- Consider using `/pivot` for major changes

## Validation

Before moving to Production:

```
/analyze
```

This checks:
- All critical features are in roadmap
- Architecture covers roadmap features
- No orphaned dependencies

## Common Issues

### "Architecture doesn't match my engine"
- Specify engine explicitly in `/init`
- Re-run `/architecture` after fixing config

### "Roadmap priorities feel wrong"
- Edit `roadmap.yaml` manually
- Or use `/pivot` for major restructuring

### "Too many features in Cycle 1"
- Move non-critical to Cycle 2
- Focus on **minimum playable**

## Next: Production Cycle

With roadmap and architecture in place:
- ✅ Features prioritized
- ✅ Technical foundation documented

Continue to **[Part 4: Production Cycle](04-production.md)** to implement your first feature.
