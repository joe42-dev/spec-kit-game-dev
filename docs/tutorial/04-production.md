# SKGD Tutorial - Part 4: Production Cycle

## Overview

The Production Cycle is repeated for each feature:

```
/spec [feature] → /plan [feature] → /tasks [feature] → /implement → /playtest
```

## Step 1: Create Specification

Run:
```
/spec player-movement
```

### Prerequisites
- Feature must exist in `roadmap.yaml`
- Dependencies must be completed

### What It Asks
- Clarification on requirements
- Edge cases to handle
- Performance targets
- Feel/quality goals

### Output: spec.md

```markdown
# Player Movement Specification

## Why This Feature
[Connection to core vision]

## Overview
[What this feature is]

## Player Experience

### User Stories
- As a player, I want to move fluidly so that I feel in control
- As a player, I want responsive jumps so that platforming feels fair

### Target Feel
Like [Reference Game] - responsive but weighty

## Requirements

### Functional
- [ ] FR-1: Player moves left/right with input
- [ ] FR-2: Player jumps with variable height
- [ ] FR-3: Player has coyote time (0.1s)

### Non-Functional
- [ ] NFR-1: Input latency < 1 frame
- [ ] NFR-2: No physics jitter at 60fps

## Mechanics Detail

### Core Behavior
[Detailed explanation]

### Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Move speed | 8 m/s | [Why] |
| Jump force | 12 | [Why] |
| Gravity | 30 | [Why] |
| Coyote time | 0.1s | Industry standard |

### States
[State diagram if applicable]

## Edge Cases
1. **Wall collision**: [Behavior]
2. **Jump at edge**: Coyote time applies

## Dependencies
- [x] None (first feature)

## Acceptance Criteria
- [ ] AC-1: Player moves at specified speed
- [ ] AC-2: Jump height is consistent
- [ ] AC-3: Coyote time works correctly
- [ ] AC-4: No physics glitches

## Implementation Hints
### Suggested Structure
```
Assets/Scripts/Player/
├── PlayerController.cs
├── PlayerInput.cs
└── PlayerPhysics.cs
```

### Key Considerations
[From learnings-core.md patterns]
```

## Step 2: Generate Plan

Run:
```
/plan player-movement
```

### Prerequisites
- `spec.md` must exist

### What It Produces

```markdown
# Player Movement - Implementation Plan

## Technical Approach

### Strategy
Use Unity's CharacterController with custom physics layer
for precise control and predictable behavior.

### Patterns Used
| Pattern | Why |
|---------|-----|
| State Machine | Clean state transitions |
| Component | Separate concerns |

### Key Decisions
| Decision | Choice | Rationale |
|----------|--------|-----------|
| Physics | CharacterController | More control than Rigidbody |
| Input | New Input System | Rebinding support |

## Component Architecture

### Scripts to Create
1. `PlayerController.cs` - Main coordinator
2. `PlayerInput.cs` - Input handling
3. `PlayerMovement.cs` - Movement logic
4. `PlayerJump.cs` - Jump mechanics

### Dependencies
[Component diagram]

## Implementation Phases

### Phase 1: Foundation
**Goal:** Basic input and movement

**Steps:**
1. Create PlayerInput.cs with Input System
2. Create PlayerMovement.cs with basic move
3. Hook up to CharacterController

**Verification:** Player moves left/right

### Phase 2: Jump Mechanics
**Goal:** Variable jump with coyote time

**Steps:**
1. Add jump input detection
2. Implement variable jump height
3. Add coyote time buffer
4. Add jump buffer

**Verification:** Jump feels responsive

### Phase 3: Polish
**Goal:** Edge cases and feel

**Steps:**
1. Wall collision handling
2. Ground detection tuning
3. Animation hooks (events)

**Verification:** All AC pass

## Risk Assessment
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Physics jitter | Medium | High | Fixed timestep |

## Testing Strategy
### Automated
- EditMode: Parameter validation
- PlayMode: Movement speed check

### Manual
- Feel test on gamepad
- Edge collision check
```

## Step 3: Generate Tasks

Run:
```
/tasks player-movement
```

### Prerequisites
- `spec.md` AND `plan.md` must exist

### Output: tasks.md

```markdown
# Player Movement - Tasks

*Total tasks: 25 | Stories: 3 | Parallel opportunities: 5*

---
## Session Tracking
```yaml
last_updated: null
total_tasks: 25
completed_tasks: 0
last_completed: null
next_task: T001
sessions: []
```
---

## Phase 1: Setup
*Goal: Project structure ready*

- [ ] T001 Create folder Assets/Scripts/Player/
- [ ] T002 [P] Create PlayerInput.cs (empty)
- [ ] T003 [P] Create PlayerMovement.cs (empty)
- [ ] T004 Create Input Actions asset

**Verification:** Files compile without errors

---

## Phase 2: Foundation
*MUST complete before user stories*

- [ ] T005 [US1] Implement input reading in PlayerInput
- [ ] T006 [US1] Add CharacterController to Player prefab
- [ ] T007 [US1] Implement basic horizontal movement

**Verification:** Player moves with input

---

## Phase 3: User Story 1 - Basic Movement
*Priority: P1*

### Acceptance Criteria
- [ ] AC1: Player moves at 8 m/s
- [ ] AC2: Movement feels responsive

### Tasks
- [ ] T008 [US1] Add speed parameter (SerializeField)
- [ ] T009 [US1] Implement acceleration curve
- [ ] T010 [P] [US1] Create Player prefab in scene

**Verification:** Speed matches spec
**Test Scenario:** Move left, verify speed with debug

---

## Phase 4: User Story 2 - Jump
*Priority: P1*

### Acceptance Criteria
- [ ] AC3: Variable jump height works
- [ ] AC4: Coyote time of 0.1s

### Tasks
- [ ] T011 [US2] Create PlayerJump.cs
- [ ] T012 [US2] Implement ground detection
- [ ] T013 [US2] Add basic jump
- [ ] T014 [US2] Add variable jump (release early = lower)
- [ ] T015 [US2] Add coyote time buffer
- [ ] T016 [US2] Add jump buffer (0.15s)

**Verification:** Jump feels like reference

---

## Phase 5: Polish
*Goal: Edge cases and quality*

- [ ] T020 Handle wall collisions
- [ ] T021 Tune gravity curve
- [ ] T022 Add animation event hooks
- [ ] T023 Final parameter tuning

**Verification:** All AC pass, console clean

---

## Dependency Graph
```
T001 ─┬─> T002 ─┬─> T005 ─> T007 ─> T008
      └─> T003 ─┘           │
      └─> T004 ─────────────┘
                            ↓
                    T011 ─> T012 ─> T013 ─> T014 ─> T015
```

## Parallel Execution Map
- Can run together: T002, T003 (different files)
- Sequential: T005 → T007 (dependency)
```

## Step 4: Implement

Run:
```
/implement
```

### Session Options
```
Starting: player-movement
Tasks: 25 | MVP: 16 | Phases: 5

Session scope:
  [A] MVP (Setup + Foundation + US1-2)
  [B] Full feature (all tasks)
  [C] Specific range (e.g., T001-T010)
  [D] Single phase
```

### Multi-Session Support

If you stop mid-implementation:
```
/implement
```

Will detect incomplete session:
```
Previous session: player-movement
Progress: 10/25 tasks
Stopped at: T010

Options:
  [A] Continue from T011 (recommended)
  [B] Restart from T001
  [C] Change scope
```

Or force resume:
```
/implement continue
```

### Checkpoints

Every 5-10 tasks, SKGD saves:
- Updates `tasks.md` checkboxes
- Updates `state.yaml` with progress
- Git commit: `checkpoint(player-movement): T001-T010`

### Implementation Flow

For each task:
1. **Create/modify code** via MCP
2. **Check compilation** immediately
3. **Fix errors** before next task
4. **Mark complete** in tasks.md

### Unity Example
```yaml
mcp__UnityMCP__create_script:
  path: "Assets/Scripts/Player/PlayerInput.cs"
  contents: |
    using UnityEngine;
    using UnityEngine.InputSystem;

    public class PlayerInput : MonoBehaviour
    {
        public Vector2 MoveInput { get; private set; }

        public void OnMove(InputValue value)
        {
            MoveInput = value.Get<Vector2>();
        }
    }
```

### Godot Example
```yaml
mcp__gdai__create_script:
  file_path: "res://scripts/player/player_input.gd"
  content: |
    extends Node
    class_name PlayerInput

    var move_input: Vector2 = Vector2.ZERO

    func _process(_delta: float) -> void:
        move_input = Input.get_vector("move_left", "move_right", "move_up", "move_down")
```

## Step 5: Playtest

After implementation completes:
```
/playtest
```

See **[Part 5: Validation](05-validation.md)** for details.

## Reusing Production Commands

### Re-run /spec
- Overwrites existing spec
- Use for major requirement changes

### Re-run /plan
- Overwrites plan with new approach
- Tasks will need regeneration

### Re-run /tasks
- **Loses implementation progress!**
- Only use if plan changed significantly

### Re-run /implement
- Safe - detects existing progress
- Can scope to specific tasks

## Common Issues

### "Task seems too big"
- Break into subtasks manually in tasks.md
- Each task should be < 30 min work

### "Compilation errors accumulating"
- **Stop and fix** before continuing
- Never skip to next task with errors

### "Lost my progress"
- Check git history for checkpoints
- `git log --oneline` to find checkpoint commits

### "MCP disconnected"
- Checkpoint is auto-saved
- Reconnect and run `/implement` to resume

## Next: Validation

Continue to **[Part 5: Validation](05-validation.md)** to test and capture learnings.
