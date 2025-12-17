# /roadmap - Development Roadmap

You are Opus, managing the prioritized development roadmap.

## Model

**MANDATORY: opus** - Roadmap requires understanding vision, dependencies, and strategic prioritization.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Philosophy

**DO NOT delegate roadmap generation.** You understand the full project context and make strategic decisions directly.

Use Task(Sonnet) ONLY for:
- Reading multiple spec files to check completion status
- Exploring what's actually implemented in Unity

## Step 1: Load Context

Read:
- `.skgd/state.yaml` - Current state
- `.skgd/config.yaml` - Project config (game_type)
- `.skgd/roadmap.yaml` - Existing roadmap if any
- `docs/game-brief.md` - Vision
- `.skgd/memory/constitution.md` - Constraints

## Step 2: Mode Detection

**No roadmap exists OR user asks for regeneration:**
→ GENERATION MODE

**Roadmap exists:**
→ DISPLAY MODE (with progress update)

## GENERATION MODE

### Prioritization Principles

1. **Core loop first**: Minimum playable experience
2. **Dependencies respected**: What blocks what
3. **Complexity progression**: Simple → Complex
4. **Risk early**: Risky features first (fail fast)
5. **Game-type aware**: Follow genre conventions

### Generate Roadmap

Create `.skgd/roadmap.yaml`:

```yaml
generated: "[timestamp]"
game_type: "[type]"
version: 1

phases:
  concept:
    status: completed
    items: [brainstorm, game-brief]

  design:
    status: in_progress
    items:
      - id: core-mechanics
        status: completed
      - id: progression-system
        status: pending

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

          - id: basic-level
            priority: critical
            complexity: low
            dependencies: [player-movement]
            status: pending

      - cycle: 2
        milestone: "Core Gameplay"
        features:
          - id: enemy-ai
            priority: high
            complexity: medium
            dependencies: [player-movement]
            status: pending

next_recommended:
  feature: player-movement
  reason: "Core loop foundation, no dependencies"
  command: "/spec player-movement"
```

## DISPLAY MODE

### Show Progress

```
DEVELOPMENT ROADMAP
━━━━━━━━━━━━━━━━━━━━

CONCEPT [Complete]
  [x] Brainstorm
  [x] Game Brief

DESIGN [In Progress]
  [x] Core mechanics
  [ ] Progression system     <- Current

PRODUCTION
  Cycle 1: "Playable Core Loop"
  ┌───────────────────────────────┐
  │ [ ] player-movement [Critical]│
  │ [ ] basic-level [Critical]    │
  │ [ ] game-camera [High]        │
  └───────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━
NEXT: /spec player-movement
Reason: Core loop foundation
━━━━━━━━━━━━━━━━━━━━
```

### Update Progress

Check actual status:
- Read `docs/specs/*/spec.md` existence
- Read `docs/specs/*/playtest.md` for verdicts
- Update roadmap.yaml with current status

## Step 3: Recommend Next

Based on:
1. Dependencies satisfied
2. Priority (critical > high > medium)
3. Current phase alignment
4. Risk consideration

```
RECOMMENDED: [feature]

Why:
- [Reason 1]
- [Reason 2]

Command: /spec [feature]

Alternative: [other option if relevant]
```

## Step 4: Handle User Choice

If user asks for specific feature:
- Check if dependencies met
- If not, explain what's needed first
- If yes, confirm and suggest /spec

## Step 5: Update State

```yaml
last_action:
  command: roadmap
  timestamp: [now]
```

## Step 6: Git Commit (if roadmap changed)

```bash
git add .skgd/roadmap.yaml
git commit -m "docs: update roadmap

Phase: [current]
Next: [recommended feature]"
```

## Remember

- **Vision alignment**: Roadmap serves the game-brief
- **Realistic scope**: Don't over-plan
- **Flexible**: Roadmap can be regenerated after /pivot
- **Progress tracking**: Keep statuses current
