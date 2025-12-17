# /roadmap - Intelligent Development Roadmap

You are generating or displaying the prioritized development roadmap.

## Your Task

### Step 1: Load Context

Read these files:
- `.skgd/state.yaml` - Current state
- `.skgd/config.yaml` - Project config (especially game_type)
- `.skgd/roadmap.yaml` - Existing roadmap if any
- `docs/game-brief.md` - If exists
- `docs/gdd.md` - If exists
- `.skgd/memory/constitution.md` - Core principles

### Step 2: Determine Roadmap Mode

**If no roadmap exists or major state change:**
→ Generate new roadmap (use Opus)

**If roadmap exists and state matches:**
→ Display current roadmap with progress (use Haiku)

### Step 3: Generate Roadmap (if needed)

Use the Task tool to delegate to the **Architect agent** with opus model:

```
Analyze the project and generate a prioritized roadmap.

Context:
- Game type: [from config]
- Current phase: [from state]
- Completed specs: [list]
- Game brief: [content if exists]
- GDD: [content if exists]

Generate roadmap following these principles:
1. Core loop first (playable minimum)
2. Dependencies respected (what blocks what)
3. Complexity progression (simple → complex)
4. Game-type specific priorities (load template)

Output format for .skgd/roadmap.yaml
```

### Step 4: Roadmap YAML Structure

```yaml
# .skgd/roadmap.yaml
generated: "[timestamp]"
game_type: "[type]"
current_phase: "[phase]"

phases:
  concept:
    status: completed|in_progress|pending
    items:
      - brainstorm
      - game-brief

  design:
    status: completed|in_progress|pending
    items:
      - core-mechanics
      - progression-system
      - [game-type specific]

  architecture:
    status: completed|in_progress|pending
    items:
      - technical-architecture
      - unity-project-structure

  production:
    status: completed|in_progress|pending
    cycles:
      - cycle: 1
        milestone: "Playable Core Loop"
        features:
          - id: player-movement
            priority: critical
            complexity: low
            dependencies: []
            status: pending|in_progress|completed
          - id: basic-level
            priority: critical
            complexity: low
            dependencies: [player-movement]
            status: pending
          # ... more features

next_recommended:
  feature: "[feature-id]"
  reason: "[why this is next]"
  command: "/spec [feature-id]"

blocked:
  - feature: "[feature-id]"
    blocked_by: "[dependency]"
```

### Step 5: Display Roadmap

Format output:

```
🗺️ DEVELOPMENT ROADMAP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE: CONCEPT [✓ Complete]
  ✓ Brainstorm session
  ✓ Game brief

PHASE: DESIGN [○ In Progress]
  ✓ Core mechanics spec
  ○ Progression system      ← Current
  · Level design
  · Enemy system

PHASE: ARCHITECTURE [· Pending]
  · Technical architecture
  · Unity project structure

PHASE: PRODUCTION [· Pending]
  Cycle 1: "Playable Core Loop"
  ┌─────────────────────────────────────────────────────────┐
  │  · player-movement [Critical] [Low complexity]          │
  │  · basic-level [Critical] [Low] ← depends: player-mov   │
  │  · game-camera [High] [Low]                             │
  └─────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏭️  NEXT: /spec progression-system
    Reason: Required for core loop definition
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 6: Update State

After generating/displaying roadmap, update `.skgd/state.yaml`:
```yaml
last_action:
  command: roadmap
  timestamp: [now]
  result: success
```

## Model Selection
- **Generating new roadmap**: opus (complex analysis)
- **Displaying existing roadmap**: haiku (simple read)
