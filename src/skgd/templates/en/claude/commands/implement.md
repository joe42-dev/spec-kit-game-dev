# /implement - Execute Implementation

You are Opus, implementing a feature via the configured engine's MCP tools (Unity or Godot).

## Model

**MANDATORY: opus** - MCP operations require precise understanding and complex decision-making.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Philosophy

**DO NOT delegate implementation to a sub-agent.** MCP operations require:
- Understanding context from the plan
- Adapting to unexpected situations
- Real-time decisions on errors
- Maintaining quality standards

Use Task(Sonnet) ONLY for:
- Searching existing code patterns
- Reading multiple reference files
- Finding asset locations

---

## Phase 0: Scout Context

**BEFORE any other step**, use Task tool to gather context:

```yaml
Task:
  subagent_type: 'Explore'
  model: 'haiku'
  prompt: |
    Scout context for implementation. Read and summarize:

    1. `.skgd/config.yaml`:
       - Extract `engine` (unity or godot)
       - Extract `user.language`

    2. `.skgd/state.yaml`:
       - Extract `current_spec`
       - Extract `implementation.checkpoint` if present
       - Extract `implementation.tasks_completed` if present

    3. `docs/specs/[current_spec]/tasks.md`:
       - Count total tasks
       - List ONLY unchecked tasks [ ]
       - Identify [MVP] vs [POLISH] tasks

    4. `docs/specs/[current_spec]/plan.md`:
       - Identify current phase (based on remaining tasks)
       - Extract 2-3 key points for this phase

    5. `.skgd/memory/learnings-core.md`:
       - Extract 3-5 relevant patterns for this feature

    Return Scout Report format (max 500 tokens):

    ## Scout Report: implement
    **Status:** [ready|resume|blocked]
    **Engine:** [unity|godot]
    **Feature:** [feature name]
    **Language:** [en|fr]

    **Session:**
    - State: [new | resume from T0XX]
    - Checkpoint: [timestamp or "none"]

    **Tasks:**
    - Total: [N] | Done: [X] | Remaining: [N-X]
    - MVP remaining: [short list]
    - Polish remaining: [count]

    **Current Phase:** [phase name]
    - [key point 1]
    - [key point 2]

    **Learnings to Apply:**
    - [pattern 1]
    - [pattern 2]
    - [pattern 3]

    **Blockers:** [list or "none"]
```

### Processing Scout Report

**If Status = `blocked`:**
```
Blocked: Implementation blocked

Reason: [from Scout Report]

Required actions:
1. [corrective action]
2. Run /implement again
```

**If Status = `resume`:**
```
Previous session detected

Feature: [name]
Progress: [X]/[N] tasks completed
Last checkpoint: [timestamp]

[A] Resume from T0XX
[B] Start from beginning
[C] View task details
```

**If Status = `ready`:** Continue with Phase 1.

---

## Phase 1: Verify MCP Connection

### If Engine = Unity

```yaml
mcp__UnityMCP__manage_editor:
  action: "get_state"
```

If not connected:
```
Unity connection required.

Please:
1. Open Unity Editor
2. Ensure Unity MCP bridge is running (Window > Unity MCP)
3. Run /implement again
```

### If Engine = Godot

```yaml
mcp__gdai__get_project_info: {}
```

If not connected:
```
GDAI connection required.

Please:
1. Open Godot Editor with your project
2. Ensure GDAI plugin is enabled (Project > Project Settings > Plugins)
3. Ensure GDAI server is running
4. Run /implement again
```

---

## Phase 2: Implementation Flow

For each task from Scout Report (in order):

### Unity - Create Scripts

```yaml
mcp__UnityMCP__create_script:
  path: "Assets/Scripts/[Feature]/[Name].cs"
  contents: |
    using UnityEngine;

    public class [Name] : MonoBehaviour
    {
        // Implementation following learnings-core patterns
    }
```

### Godot - Create Scripts

```yaml
mcp__gdai__create_script:
  file_path: "res://scripts/[feature]/[name].gd"
  content: |
    extends Node
    class_name [ClassName]

    # Implementation following learnings-core patterns
```

### After EACH Script - Check Compilation

**Unity:**
```yaml
mcp__UnityMCP__read_console:
  types: ["error"]
  count: 10
```

**Godot:**
```yaml
mcp__gdai__get_godot_errors: {}
```

**If errors: FIX before proceeding.** Don't accumulate errors.

### Unity - Create GameObjects

```yaml
mcp__UnityMCP__manage_gameobject:
  action: "create"
  name: "[Name]"
  primitive_type: "[Type]"
  position: [x, y, z]
  components_to_add: ["[Script]"]
```

### Godot - Create Nodes

```yaml
mcp__gdai__add_node:
  parent_node_path: "/root/[Parent]"
  node_type: "CharacterBody2D"
  node_name: "[Name]"
```

### Configure Properties

**Unity:**
```yaml
mcp__UnityMCP__manage_gameobject:
  action: "set_component_property"
  target: "[GameObject]"
  component_name: "[Component]"
  component_properties:
    "[Property]": "[Value]"
```

**Godot:**
```yaml
mcp__gdai__update_property:
  node_path: "/root/[Node]"
  property_name: "position"
  property_value: "Vector2(100, 200)"
```

### Save (after each major step)

**Unity:**
```yaml
mcp__UnityMCP__manage_scene:
  action: "save"
```

**Godot:** Auto-save via GDAI.

---

## Phase 3: Checkpoints & Quality Gates

Every **5 tasks**, perform checkpoint WITH quality validation:

### 3.1 Quality Gate Check

**BEFORE saving checkpoint, validate:**

```
═══════════════════════════════════════════════════
QUALITY GATE: T001-T005
═══════════════════════════════════════════════════

Console Status:
  Errors: [count] [✓ if 0, ✗ if >0]
  Warnings: [count] [⚠️ if >5]

Compilation: [✓ All scripts compile]

Quick Validation:
  [✓/✗] Created objects exist in hierarchy
  [✓/✗] Scripts attached correctly
  [✓/✗] No obvious issues
```

**If errors > 0:** STOP and fix before continuing.
**If warnings > 5:** Review and acknowledge before continuing.

### 3.2 User Checkpoint Prompt

After quality gate passes:

```
───────────────────────────────────────────────────
Checkpoint: T001-T005 complete (5/20 tasks)
Quality gate: ✓ PASSED

[Enter] Continue to T006-T010
[P] Pause & review code
[T] Run tests now
[S] Stop for today
───────────────────────────────────────────────────
```

- **Enter/Y** → Continue to next batch
- **P** → Pause, show created files for review
- **T** → Run tests via `/playtest` logic
- **S/stop** → Save checkpoint and exit

### 3.3 Save Checkpoint

1. **Update tasks.md** - Mark completed tasks [x]

2. **Save checkpoint** to `.skgd/state.yaml`:
```yaml
implementation:
  feature: [name]
  checkpoint: [ISO timestamp]
  tasks_completed: ["T001", "T002", ...]
  last_task: "T0XX"
  quality_gates_passed: 1  # Increment
```

3. **Continue or Exit based on user choice**

---

## Phase 4: Final Verification

After all tasks completed:

### Console Check

**Unity:**
```yaml
mcp__UnityMCP__read_console:
  types: ["error", "warning"]
```

**Godot:**
```yaml
mcp__gdai__get_godot_errors: {}
```

### Quick Play Test

**Unity:**
```yaml
mcp__UnityMCP__manage_editor:
  action: "play"
  wait_for_completion: false

# Observe briefly, then:
mcp__UnityMCP__manage_editor:
  action: "stop"
```

**Godot:**
```yaml
mcp__gdai__play_scene:
  scene_path: "res://scenes/[current].tscn"

# Observe briefly, then:
mcp__gdai__stop_running_scene: {}
```

---

## Phase 5: Finalization

### Update State

```yaml
# .skgd/state.yaml
production:
  current_step: playtest

implementation:
  feature: [name]
  status: completed
  completed_at: [timestamp]
```

### Git Commit

```bash
git add Assets/ docs/specs/[feature]/tasks.md .skgd/state.yaml
# or for Godot: git add res://scenes/ res://scripts/ ...

git commit -m "feat([feature]): implement [feature-name]

Scripts: [list]
[GameObjects|Nodes]: [list]
Console: [clean/warnings]"
```

### Summary

```
Implementation complete: [feature-name]

Created:
  Scripts: [list with paths]
  [GameObjects|Nodes]: [list]

Console: [status]
Tasks: [N]/[N] completed

Next:
  /playtest - Validate implementation
```

---

## Error Handling

### Compilation Errors
1. Read full error
2. Identify script and line
3. Fix immediately
4. Recheck compilation
5. Continue only when clean

### Runtime Errors
1. Stop play mode
2. Read error details
3. Analyze root cause
4. Fix and retest

### MCP Connection Lost
1. Save checkpoint immediately
2. Inform user
3. Resume with `/implement` after reconnection

---

## Quality Standards

### Unity (C#)
- One responsibility per script
- Composition over inheritance
- `[SerializeField]` for inspector values
- Cache references in `Awake()`
- Avoid `Find*` in `Update()`

### Godot (GDScript)
- One responsibility per script
- Composition via nodes
- `@export` for inspector values
- `@onready` for node references
- Signal Bus for global events

---

## Optional Arguments

- `/implement` - Auto-detect (new or resume)
- `/implement continue` - Force resume without prompt
- `/implement mvp` - MVP scope only
- `/implement T001-T020` - Specific task range

---

## Remember

- **Compile after each script** - Don't accumulate errors
- **Save frequently** - Scene changes can be lost
- **Check console constantly** - Warnings often become errors
- **Follow the plan** - But adapt if issues discovered
- **Quality over speed** - Better to fix now than debug later
