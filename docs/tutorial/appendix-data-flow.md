# SKGD Appendix: Complete Data Flow Reference

## Master Command Reference

| Command | Inputs | Creates | Modifies | Model |
|---------|--------|---------|----------|-------|
| `/init` | User Q&A, MCP check | CLAUDE.md | config.yaml, state.yaml | Sonnet |
| `/brainstorm` | config.yaml, (game-brief.md) | game-brief.md | constitution.md, state.yaml | Opus |
| `/pillars` | game-brief.md, game-types.md | pillars/_index.md, pillars/*.md | state.yaml | Sonnet |
| `/deep-dive` | Scout Report | pillars/[name].md | _index.md, state.yaml | Opus |
| `/validate-design` | All pillars, game-brief | *None (read-only)* | - | Opus |
| `/roadmap` | game-brief, pillars | roadmap.yaml | state.yaml | Sonnet |
| `/architecture` | game-brief, roadmap, constitution | architecture.md | state.yaml | Opus |
| `/spec` | roadmap, constitution, learnings-core | specs/[f]/spec.md | state.yaml | Opus |
| `/plan` | spec.md, constitution, learnings-core | specs/[f]/plan.md | state.yaml | Sonnet |
| `/tasks` | spec.md, plan.md, architecture | specs/[f]/tasks.md | state.yaml | Sonnet |
| `/implement` | Scout Report, tasks.md, plan.md | Code/Scenes | tasks.md, state.yaml | Opus |
| `/playtest` | spec.md, tasks.md | specs/[f]/playtest.md | learnings.md, state.yaml, roadmap.yaml | Sonnet |
| `/crystallize` | learnings.md, learnings-core.md | learnings-core.md, archive | learnings.md (reset) | Haiku |
| `/continue` | state.yaml, session-context.md | *Routes to command* | session-context.md | Haiku |
| `/pivot` | All docs | pivot-analysis.md, archive | constitution.md, state.yaml, roadmap.yaml | Opus |
| `/snapshot` | state.yaml, docs | snapshots/[v]/ | state.yaml | Haiku |
| `/analyze` | spec.md, plan.md, tasks.md | *None (read-only)* | - | Sonnet |
| `/project-status` | state.yaml, config.yaml | *None (read-only)* | - | Haiku |
| `/assets` | config.yaml, state.yaml, specs | varies | state.yaml, assets-catalog.md | Sonnet |

## File Dependency Graph

```
                    ┌─────────────────────────────────────┐
                    │           /init                      │
                    │  Creates: config.yaml, state.yaml   │
                    │           CLAUDE.md, constitution   │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────▼───────────────────┐
                    │          /brainstorm                 │
                    │  Reads:  config.yaml                 │
                    │  Creates: game-brief.md              │
                    │  Updates: constitution.md            │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────▼───────────────────┐
                    │           /pillars                   │
                    │  Reads:  game-brief.md              │
                    │          game-types.md               │
                    │  Creates: pillars/_index.md          │
                    │           pillars/[stub].md          │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────▼───────────────────┐
                    │        /deep-dive [pillar]          │
                    │  Reads:  Scout (pillars, brief)     │
                    │  Updates: pillars/[pillar].md       │
                    │           pillars/_index.md          │
                    └─────────────────┬───────────────────┘
                                      │ (repeat per pillar)
                    ┌─────────────────▼───────────────────┐
                    │        /validate-design             │
                    │  Reads:  All pillars, game-brief    │
                    │  Output: Console report only        │
                    └─────────────────┬───────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
┌─────────────────┐      ┌────────────────────┐      ┌─────────────────┐
│    /roadmap      │      │   /architecture    │      │   /crystallize   │
│ Creates:         │      │ Reads: brief,      │      │ (when needed)    │
│  roadmap.yaml    │      │        roadmap     │      │ Updates:         │
└────────┬────────┘      │ Creates:           │      │  learnings-core  │
         │               │  architecture.md    │      └─────────────────┘
         │               └─────────┬──────────┘
         │                         │
         └────────────┬────────────┘
                      │
                      ▼
          ┌───────────────────────────────────────────────────────┐
          │                  PRODUCTION CYCLE                      │
          │                  (repeat per feature)                  │
          │                                                        │
          │  ┌──────────────────────────────────────────────────┐ │
          │  │ /spec [feature]                                   │ │
          │  │ Reads:  roadmap.yaml, constitution, learnings    │ │
          │  │ Creates: specs/[f]/spec.md                        │ │
          │  └─────────────────────┬────────────────────────────┘ │
          │                        │                               │
          │  ┌─────────────────────▼────────────────────────────┐ │
          │  │ /plan [feature]                                   │ │
          │  │ Reads:  spec.md, constitution, learnings          │ │
          │  │ Creates: specs/[f]/plan.md                        │ │
          │  └─────────────────────┬────────────────────────────┘ │
          │                        │                               │
          │  ┌─────────────────────▼────────────────────────────┐ │
          │  │ /tasks [feature]                                  │ │
          │  │ Reads:  spec.md, plan.md, architecture            │ │
          │  │ Creates: specs/[f]/tasks.md                       │ │
          │  └─────────────────────┬────────────────────────────┘ │
          │                        │                               │
          │  ┌─────────────────────▼────────────────────────────┐ │
          │  │ /implement                                        │ │
          │  │ Reads:  Scout (config, state, tasks, plan)       │ │
          │  │ Creates: Code, Scenes, GameObjects                │ │
          │  │ Updates: tasks.md (checkboxes), state.yaml       │ │
          │  │ Commits: Git checkpoints every 5-10 tasks        │ │
          │  └─────────────────────┬────────────────────────────┘ │
          │                        │                               │
          │  ┌─────────────────────▼────────────────────────────┐ │
          │  │ /playtest                                         │ │
          │  │ Reads:  spec.md (AC), tasks.md                    │ │
          │  │ Creates: specs/[f]/playtest.md                    │ │
          │  │ Updates: learnings.md, state.yaml, roadmap.yaml  │ │
          │  └──────────────────────────────────────────────────┘ │
          │                                                        │
          └───────────────────────────────────────────────────────┘
```

## State Machine

```
                              ┌─────────────┐
                              │uninitialized│
                              └──────┬──────┘
                                     │ /init
                              ┌──────▼──────┐
                              │   concept   │
                              └──────┬──────┘
                    /brainstorm done │
                    /pillars done    │
                    /deep-dive done  │
                              ┌──────▼──────┐
                              │   design    │
                              └──────┬──────┘
                        /roadmap     │
                              ┌──────▼──────┐
                              │ architecture│
                              └──────┬──────┘
                    /architecture    │
                              ┌──────▼──────┐
                         ┌────│ production  │◄───────┐
                         │    └─────────────┘        │
                         │                           │
    /spec ─► spec ─► /plan ─► plan ─► /tasks ─► tasks
                                                 │
                                                 │
                                  ┌──────────────▼──────────────┐
                                  │         implement           │
                                  │  (multi-session supported)  │
                                  │                              │
                                  │  checkpoints every 5-10     │
                                  │  resume via /implement      │
                                  └──────────────┬──────────────┘
                                                 │
                                                 ▼
                                            ┌─────────┐
                                            │playtest │
                                            └────┬────┘
                                                 │
                            ┌────────────────────┼────────────────────┐
                            │                    │                    │
                       PASS │           CONDITIONAL            FAIL │
                            │                    │                    │
                            ▼                    ▼                    ▼
                    Next feature          Fix + retest         Back to
                    via /continue         /playtest            /implement
```

## Living Memory System

```
┌─────────────────────────────────────────────────────────────────────┐
│                      CONTEXT BUDGET (~5k tokens)                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  LAYER 1: constitution.md (~500 tokens)                            │
│  ├── Core vision (immutable)                                        │
│  ├── 5 max design principles                                        │
│  └── Technical constraints                                          │
│                                                                     │
│  LAYER 2: learnings-core.md (~1000 tokens)                         │
│  ├── Top 10 validated patterns                                      │
│  ├── Confirmed anti-patterns                                        │
│  └── Key decisions + rationale                                      │
│                                                                     │
│  LAYER 3: session-context.md (~500 tokens)                         │
│  ├── Last session state                                             │
│  ├── Open threads                                                   │
│  └── Quick context                                                  │
│                                                                     │
│  LAYER 4: Active work (~3000 tokens)                               │
│  ├── Current spec/plan/tasks                                        │
│  └── Active pillar (if in concept)                                  │
│                                                                     │
│  LAYER 5: Archive (0 tokens - not loaded)                          │
│  ├── learnings-archive/                                             │
│  ├── Completed specs                                                │
│  └── Old snapshots                                                  │
│                                                                     │
│  Total: ~5k tokens loaded → 75k+ available for Smart Zone          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Scout-First Pattern

Commands that use Phase 0 Scout:

```
┌─────────────────────────────────────────────────────────────────────┐
│  SCOUT PATTERN (Token-Efficient Context Gathering)                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. Opus calls Task(Haiku) with scout prompt                       │
│  2. Haiku reads multiple files                                      │
│  3. Haiku returns Scout Report (≤500 tokens)                       │
│  4. Opus works with compressed context                              │
│                                                                     │
│  Benefits:                                                          │
│  - 52% token cost reduction                                         │
│  - 2.6% solve rate improvement                                      │
│  - Cleaner context = better decisions                               │
│                                                                     │
│  Commands using Scout:                                              │
│  ├── /deep-dive    → pillars, game-brief, constitution             │
│  ├── /implement    → config, state, tasks, plan, learnings         │
│  ├── /validate     → All pillars                                    │
│  └── /crystallize  → learnings.md                                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## MCP Tool Reference

### Unity MCP

| Action | Tool | Key Parameters |
|--------|------|----------------|
| Check connection | `manage_editor` | action: "get_state" |
| Play/Stop | `manage_editor` | action: "play"/"stop" |
| Create script | `create_script` | path, contents |
| Check errors | `read_console` | types: ["error"] |
| Create GameObject | `manage_gameobject` | action: "create", name, components |
| Set property | `manage_gameobject` | action: "set_component_property" |
| Save scene | `manage_scene` | action: "save" |
| Run tests | `run_tests` | mode: "EditMode"/"PlayMode" |

### Godot (GDAI MCP)

| Action | Tool | Key Parameters |
|--------|------|----------------|
| Check connection | `get_project_info` | - |
| Play/Stop | `play_scene`/`stop_running_scene` | scene_path |
| Create script | `create_script` | file_path, content |
| Check errors | `get_godot_errors` | - |
| Add node | `add_node` | parent, type, name |
| Set property | `update_property` | node_path, property, value |
| Attach script | `attach_script` | node_path, script_path |

## File Structure Reference

```
project/
├── CLAUDE.md                          # Project context (generated)
│
├── .claude/
│   ├── commands/                      # Slash commands
│   │   ├── brainstorm.md
│   │   ├── implement.md
│   │   ├── _scout.md                  # Internal helper
│   │   └── ...
│   ├── skills/                        # Engine patterns
│   │   ├── unity-gamedev/
│   │   └── godot-gamedev/
│   └── data/
│       └── game-types.md              # Pillar mappings
│
├── .skgd/
│   ├── config.yaml                    # Project settings
│   ├── state.yaml                     # Workflow state
│   ├── roadmap.yaml                   # Feature priorities
│   ├── memory/
│   │   ├── constitution.md            # Core vision
│   │   ├── learnings.md               # Raw observations
│   │   ├── learnings-core.md          # Crystallized patterns
│   │   ├── session-context.md         # Last session
│   │   └── assets-catalog.md          # Asset inventory
│   ├── snapshots/                     # Milestone backups
│   │   └── v0.X/
│   └── i18n/
│       └── messages.yaml              # Localized strings
│
├── docs/
│   ├── game-brief.md                  # Vision document
│   ├── architecture.md                # Technical blueprint
│   ├── pillars/
│   │   ├── _index.md                  # Pillar overview
│   │   ├── game-loop.md
│   │   ├── player-experience.md
│   │   └── [type-specific].md
│   └── specs/
│       └── [feature]/
│           ├── spec.md                # Requirements
│           ├── plan.md                # Implementation plan
│           ├── tasks.md               # Task checklist
│           └── playtest.md            # Test results
│
└── Assets/ (Unity) or res:// (Godot)
    └── [Generated code and scenes]
```

## Version History

| Version | Key Changes |
|---------|-------------|
| v3.5 | Unified /implement (auto-detect engine), Scout-First pattern |
| v3.4 | Scout-First for /deep-dive, auto-learnings in /playtest |
| v3.3 | Multi-session /implement with checkpoints |
| v3.2 | Design pillars system, /pillars, /deep-dive, /validate-design |
| v3.1 | /architecture command, separate /tasks |
| v3.0 | Asset pipeline, Blender/PixelLab MCP |
| v2.0 | Living Memory, i18n, /crystallize |
| v1.0 | Initial spec-driven workflow |
