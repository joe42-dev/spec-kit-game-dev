# /architecture - Generate Project Architecture

You are Opus, creating a technical architecture document for the game project.

**No argument required** - This is a project-level document, not per-feature.

## Model

**MANDATORY: opus** - Architecture requires deep technical analysis and cross-cutting decisions.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## When to Use

Run `/architecture` AFTER:
- `/brainstorm` (game-brief.md exists)
- `/roadmap` (roadmap.yaml exists)

Run `/architecture` BEFORE:
- `/spec` (features need architecture context)

## Philosophy

**DO NOT delegate to a sub-agent.** You create the architecture directly, making foundational decisions with full context.

Use Task(Sonnet) ONLY for:
- Exploring existing Unity/Godot project structure
- Reading multiple codebase files
- Finding existing patterns in the project

## Step 1: Validate Prerequisites

Check these exist:
- `docs/game-brief.md` - Core game concept
- `.skgd/roadmap.yaml` - Feature priorities
- `.skgd/config.yaml` - Engine detection (unity/godot)

If missing, inform user which prerequisite command to run first.

## Step 2: Load Context

**Always read:**
- `docs/game-brief.md` - Game concept, pillars, core loop
- `.skgd/roadmap.yaml` - Features to architect for
- `.skgd/memory/constitution.md` - Project constraints
- `.skgd/memory/learnings-core.md` - Validated patterns

**Engine-specific exploration (Task Sonnet):**
- Unity: Explore `Assets/` structure, existing scripts, packages
- Godot: Explore project structure, existing scenes, autoloads

## Step 3: Architectural Decisions

Before writing, decide on these categories:

### Core Systems
- **Game Loop**: How does the main loop work?
- **State Management**: How are game states handled?
- **Scene Flow**: How do scenes/levels transition?
- **Data Persistence**: Save system, player prefs, cloud saves?

### Engine Patterns
**Unity:**
- MonoBehaviour vs pure C# classes
- ScriptableObjects for data
- Event systems (UnityEvents, C# events, custom)
- Dependency injection approach

**Godot:**
- Node hierarchy patterns
- Signal bus architecture
- Autoload services
- Resource-based data

### Technical Decisions
- **Input**: System choice, rebinding support
- **UI**: Framework (UI Toolkit, UGUI, Control nodes)
- **Audio**: Manager pattern, spatial audio
- **Physics**: Layer setup, collision matrix

If unclear about any decision, ASK the user for preferences.

## Step 4: Create Architecture Document

Create `docs/architecture.md`:

```markdown
# [Game Name] - Technical Architecture

*Engine: [Unity/Godot] | Version: [version]*
*Created: [timestamp]*

## Overview

### Technical Vision
[2-3 sentences on the technical approach aligned with game pillars]

### Architecture Principles
1. [Principle 1] - [Why]
2. [Principle 2] - [Why]
3. [Principle 3] - [Why]

## Core Systems

### Game Loop
```
[Visual diagram of main loop]
MainMenu → Loading → Gameplay ↔ Pause → Results
                ↓
            Save/Load
```

**Implementation:**
- [How the loop is implemented]
- [Key scripts/scenes involved]

### State Management
| State | Entry Condition | Exit Condition | Responsible System |
|-------|-----------------|----------------|-------------------|
| [State] | [Condition] | [Condition] | [System] |

**Pattern:** [State machine type, implementation approach]

### Scene Management
```
Scenes/
├── _Bootstrap.unity     # Initialization, persistent managers
├── MainMenu.unity       # UI-only scene
├── Gameplay/
│   ├── Level_01.unity
│   └── Level_02.unity
└── _Loading.unity       # Transition scene
```

**Loading Strategy:** [Additive, single, addressables?]

## Data Architecture

### Runtime Data Flow
```
[Input] → [Systems] → [State] → [Rendering]
              ↓
         [Events]
```

### Persistent Data
| Data Type | Storage | Format | Location |
|-----------|---------|--------|----------|
| Settings | PlayerPrefs/ConfigFile | Key-Value | Local |
| Save Data | JSON/Binary | Serialized | [Path] |
| Analytics | [Service] | Events | Cloud |

### Data Containers (Unity: ScriptableObjects / Godot: Resources)
```
Data/
├── Config/
│   ├── GameSettings.asset
│   └── DifficultyLevels.asset
├── Items/
│   └── [ItemData].asset
└── Characters/
    └── [CharacterData].asset
```

## System Architecture

### Core Managers
| Manager | Responsibility | Lifecycle | Access Pattern |
|---------|---------------|-----------|----------------|
| GameManager | Game state, flow | Persistent | Singleton |
| AudioManager | SFX, Music | Persistent | Singleton |
| UIManager | Screen flow | Persistent | Singleton |
| [Custom] | [Desc] | [Lifecycle] | [Pattern] |

### Event System
**Pattern:** [Choice and rationale]

```
[Event flow diagram]
Player Input → InputEvents → GameplaySystem
                    ↓
              UI Listeners
```

**Key Events:**
- `OnGameStateChanged(GameState newState)`
- `OnPlayerAction(ActionType action)`
- `[Custom events for this game]`

### Dependency Graph
```
[Core Systems]
     ↓
[Feature Systems] → [Data Layer]
     ↓
[UI/Presentation]
```

## Feature System Patterns

### [Primary Feature from Roadmap]
**Pattern:** [Pattern name]
**Rationale:** [Why this pattern]

```
[Component diagram]
```

### [Secondary Feature]
**Pattern:** [Pattern name]
**Rationale:** [Why]

## Input Architecture

### Input Map
| Action | Keyboard | Gamepad | Touch |
|--------|----------|---------|-------|
| Move | WASD | Left Stick | Virtual Joystick |
| Jump | Space | A/Cross | Tap |
| [Action] | [Key] | [Button] | [Gesture] |

**System:** [Unity InputSystem / Godot Input / Custom]
**Rebinding:** [Yes/No, approach]

## UI Architecture

### Screen Flow
```
MainMenu
├── Play → LevelSelect → Gameplay
├── Settings → [Tabs]
└── Credits
```

### UI Framework
- **System:** [UI Toolkit / UGUI / Godot Control]
- **Pattern:** [MVC, MVP, MVVM?]
- **Theming:** [Approach]

## Audio Architecture

### Audio Categories
| Category | Bus | Volume Control | Spatial |
|----------|-----|----------------|---------|
| Music | Music | Settings | No |
| SFX | SFX | Settings | Optional |
| UI | UI | Settings | No |
| Voice | Voice | Settings | Yes |

### Audio Manager Pattern
[Brief description of approach]

## Performance Considerations

### Target Specs
| Platform | Target FPS | Resolution | Memory Budget |
|----------|------------|------------|---------------|
| [Platform] | [FPS] | [Res] | [MB] |

### Optimization Strategies
- **Object Pooling:** [What to pool]
- **LOD:** [Approach]
- **Async Loading:** [Strategy]

## Testing Strategy

### Automated Tests
- **Unit:** [Core systems to unit test]
- **Integration:** [What to integration test]
- **PlayMode:** [Gameplay scenarios]

### Manual Testing
- [Critical paths to manually verify]

## Extension Points

### Planned Features (from Roadmap)
| Feature | Affected Systems | Preparation |
|---------|-----------------|-------------|
| [P1 Feature] | [Systems] | [Hooks/interfaces to add] |
| [P2 Feature] | [Systems] | [Preparation needed] |

### Mod Support (if applicable)
[Approach to extensibility]

---

## Appendix: Folder Structure

```
[Project Root]/
├── Assets/ (Unity) or project/ (Godot)
│   ├── Scripts/
│   │   ├── Core/           # Managers, base classes
│   │   ├── Systems/        # Feature systems
│   │   ├── Data/           # Data containers
│   │   ├── UI/             # UI controllers
│   │   └── Utils/          # Helpers
│   ├── Scenes/
│   ├── Prefabs/ (or Scenes/ for Godot)
│   ├── Data/               # ScriptableObjects/Resources
│   ├── Art/
│   ├── Audio/
│   └── UI/
├── docs/
│   ├── game-brief.md
│   ├── architecture.md     # This document
│   └── specs/
└── .skgd/
```

---
*Architecture Version: 1.0*
*Last Updated: [timestamp]*
*Next Review: After [milestone]*
```

## Step 5: Update State

Update `.skgd/state.yaml`:
```yaml
concept:
  architecture_complete: true
```

## Step 6: Git Commit

```bash
git add docs/architecture.md
git commit -m "docs: project architecture

Engine: [engine]
Key patterns: [list main patterns]
Systems: [count] core systems defined"
```

## Step 7: Summary

```
Architecture created: docs/architecture.md

Summary:
- Engine: [Unity/Godot]
- Core systems: [count]
- Key patterns: [list]
- Extension points: [count] features prepared

The architecture provides:
- Foundation for all feature specs
- Consistent patterns across features
- Clear system boundaries

Next:
  /spec [feature] - Create feature specification
  /continue - Auto-route to next step
```

## Remember

- **Game-First**: Architecture serves the game, not the reverse
- **Extensible**: Prepare hooks for roadmap features
- **Engine-Native**: Use engine patterns, don't fight the framework
- **Simple Start**: Document the MVP architecture, evolve with the project
