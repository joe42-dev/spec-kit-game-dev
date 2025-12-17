# SKGD Tutorial - Part 6: Utilities

## Overview

Utility commands support the main workflow:

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/continue` | Smart session router | Between sessions |
| `/pivot` | Major direction change | Vision/scope change |
| `/snapshot [v]` | Save milestone | Before risky changes |
| `/project-status` | Dashboard | Anytime |
| `/analyze [feature]` | Cross-artifact check | Before implement |
| `/assets` | Asset pipeline | When creating art |

## /continue - Smart Router

### Usage
```
/continue
```

### What It Does

1. **Reads state.yaml** - Determines current phase/step
2. **Checks session-context.md** - Recalls last session
3. **Routes to next action** - With context

### Decision Logic

```
IF phase == "concept":
    IF brainstorm_done == false → /brainstorm
    ELSE → /roadmap

ELSE IF phase == "production":
    IF current_spec == null → /roadmap
    ELSE:
        SWITCH current_step:
            "spec" → verify complete, suggest /plan
            "plan" → /plan [spec]
            "tasks" → /tasks [spec]
            "implement" → /implement (with resume detection)
            "playtest" → /playtest
```

### Session Context

On session end, updates `session-context.md`:
```markdown
## Last Session
Date: 2024-01-15T14:00:00Z
Duration: ~45min
Commands: /implement, /playtest

## Decisions Made
- Chose CharacterController over Rigidbody

## Open Threads
- [ ] Revisit jump curve after enemy implementation

## Momentum
Level: high
Next should: Continue with next feature

## Quick Context
Player movement complete. Ready for basic-combat feature.
```

### Resuming Work

```
/continue
```

Output:
```
Picking up where we left off...

Last session: 2024-01-15
- You were: Production (implementing basic-combat)
- Key decision: Using state machine for enemy AI
- Momentum: high

Next: Continue implementing basic-combat (T015-T025)

Options:
  [A] Continue with /implement (recommended)
  [B] Review first (/project-status)
  [C] Something else?
```

## /pivot - Direction Change

### When to Use
- Core mechanic isn't fun
- Scope needs to change
- New inspiration strikes
- Market/feedback requires shift

### Usage
```
/pivot
```

### Process

1. **Understand the Pivot**
   - What's changing? (mechanic, genre, scope, audience)
   - Why? (feedback, limitation, evolution)
   - New direction?

2. **Auto-Create Pre-Pivot Snapshot**
   - Runs `/snapshot` automatically

3. **Impact Analysis**
   - What work is invalidated?
   - What can be preserved?
   - New work required?
   - Risks?

4. **Generate Pivot Analysis Document**

```markdown
# Pivot Analysis #1

## Trigger
Combat feels too slow - switching to action-focused

## Change Summary
**From:** Turn-based tactical combat
**To:** Real-time action combat

## Impact Analysis

### Invalidated (needs rewrite)
| Document | Reason | Effort |
|----------|--------|--------|
| combat-system.md | Core mechanic changed | High |
| enemy-design.md | Behavior model changed | Medium |

### Preserved
| Document | Notes |
|----------|-------|
| player-movement | Still valid |
| art-direction | Style unchanged |

### New Required
- docs/pillars/action-combat.md
- docs/specs/attack-system/

### Code Impact
- Remove: TurnManager.cs
- Modify: PlayerController (add attack)
- Keep: PlayerMovement, UI systems

## Recommendation
Proceed - Core loop improvement worth the cost
```

5. **Get Confirmation**
   - Proceed with pivot
   - Modify scope
   - Abort

6. **Execute (if proceeding)**
   - Update constitution.md
   - Archive deprecated specs
   - Regenerate roadmap

### After Pivot

```
🔄 Pivot Complete

Change: Turn-based → Real-time combat

Actions Taken:
- Pre-pivot snapshot: v0.3-pre-pivot
- Updated constitution
- Archived 2 specs
- Regenerated roadmap

To undo: git checkout v0.3-pre-pivot
```

## /snapshot [version] - Save Milestone

### Usage
```
/snapshot v0.5
```
Or auto-increment:
```
/snapshot
```

### What It Creates

```
.skgd/snapshots/v0.5/
├── state.yaml          # Full state copy
├── game-brief.md       # Vision snapshot
├── architecture.md     # Tech snapshot
└── specs/              # All current specs
```

### When to Snapshot
- Before risky changes
- At milestone completion
- Before `/pivot`
- After major feature done

### Restoring

```bash
# View snapshot
cat .skgd/snapshots/v0.5/state.yaml

# Checkout via git
git checkout v0.5

# Compare with current
git diff v0.5..HEAD -- docs/
```

## /project-status - Dashboard

### Usage
```
/project-status
```

### Output

```
╔═══════════════════════════════════════════════════════════════╗
║  🎮 SPEC KIT GAME DEV - STATUS                                ║
╠═══════════════════════════════════════════════════════════════╣
║  Project: Dungeon Crawler                                     ║
║  Type: Roguelike                                              ║
║  Phase: production                                            ║
╠═══════════════════════════════════════════════════════════════╣
║  PROGRESS                                                     ║
║  ├─ Concept:      ✓ Done                                     ║
║  ├─ Design:       ✓ Done                                     ║
║  ├─ Architecture: ✓ Done                                     ║
║  └─ Production:   Cycle 1 - implement                        ║
╠═══════════════════════════════════════════════════════════════╣
║  SPECS                                                        ║
║  ├─ Completed: 2                                              ║
║  ├─ In Progress: basic-combat                                ║
║  └─ Total: 8                                                  ║
╠═══════════════════════════════════════════════════════════════╣
║  CONNECTIONS                                                  ║
║  ├─ Unity MCP: 🟢 Connected                                  ║
║  └─ Blender MCP: ⚪ Not configured                           ║
╠═══════════════════════════════════════════════════════════════╣
║  SNAPSHOTS: 3 | Latest: v0.3                                 ║
║  PIVOTS: 0                                                    ║
╠═══════════════════════════════════════════════════════════════╣
║  NEXT ACTION                                                  ║
║  → /implement to continue basic-combat                       ║
╚═══════════════════════════════════════════════════════════════╝
```

### Read-Only
Does not modify any files.

## /analyze [feature] - Cross-Artifact Validation

### Usage
```
/analyze basic-combat
```

### Prerequisites
- spec.md, plan.md, tasks.md all exist

### What It Checks

1. **Duplication** - Similar requirements
2. **Ambiguity** - Vague terms, placeholders
3. **Underspecification** - Missing details
4. **Constitution Alignment** - Principle violations
5. **Coverage** - Requirements → Tasks mapping
6. **Inconsistency** - Conflicting statements

### Report Format

```markdown
# Analysis Report: basic-combat

## Issues Found
| ID | Category | Severity | Location | Summary |
|----|----------|----------|----------|---------|
| A1 | Coverage | HIGH | FR-3 | No task for damage calculation |
| A2 | Ambiguity | MEDIUM | spec:L45 | "fast" undefined |

## Coverage Summary
| Requirement | Has Tasks? | Task IDs |
|-------------|------------|----------|
| FR-1 | ✅ | T012, T013 |
| FR-2 | ✅ | T014-T016 |
| FR-3 | ❌ | None |

## Recommendation
Fix HIGH issues before /implement
```

### Read-Only
Does not modify files - you must act on recommendations.

## /assets - Asset Pipeline

### Usage
```
/assets              # Status overview
/assets setup        # Configure MCPs
/assets list [feat]  # List assets for feature
/assets generate [f] # Generate via MCP
```

### Status Overview
```
🎨 ASSET PIPELINE STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Art Profile: pixel-2d

📦 Configured MCPs:
  ✓ PixelLab MCP - connected
  ✗ Blender MCP - not configured

📊 Asset Progress:
  Sprites:    [####......] 4/10 (40%)
  Animations: [##........] 2/8 (25%)

🎯 Features Needing Assets:
  → basic-combat (3 sprites, 2 animations)
```

### Asset Generation

```
/assets generate basic-combat
```

Reads spec's "Asset Requirements" section and generates via appropriate MCP.

## Best Practices

### Daily Workflow
1. Start with `/continue` - Get oriented
2. Work on current task
3. End with `/snapshot` if milestone reached

### Weekly Workflow
1. `/project-status` - Review progress
2. `/crystallize` - If learnings accumulated
3. Adjust roadmap if needed

### Before Major Changes
1. `/snapshot` - Safety save
2. `/analyze` - Check consistency
3. Then proceed

## Next: Troubleshooting

Continue to **[Part 7: Troubleshooting](07-troubleshooting.md)** for common issues and solutions.
