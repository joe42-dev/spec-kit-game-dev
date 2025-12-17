# /implement - Execute Implementation (Engine Router)

You are Opus, implementing a feature using the appropriate engine MCP.

**Argument:** `$ARGUMENTS` (optional: "continue", scope like "T001-T015", or "mvp")

## Model

**MANDATORY: opus**

## Step 0: Intelligent Session Detection

**Always read first:**
- `.skgd/state.yaml` → `implementation` block + `production.current_spec`
- `docs/specs/[feature]/tasks.md` → Session Tracking header (if exists)

### Parse Arguments

| Argument | Behavior |
|----------|----------|
| *(none)* | Auto-detect state, ask if needed |
| `continue` | Force resume from last checkpoint (no questions) |
| `mvp` | Scope to MVP tasks only (Phase 1-3) |
| `T001-T015` | Scope to specific task range |
| `Phase 2` | Scope to specific phase |

### Decision Logic

```
READ state.yaml → implementation

IF $ARGUMENTS == "continue":
    → GOTO Resume Flow (skip questions)

ELSE IF implementation.active == true:
    # Session was interrupted (crash, timeout, etc.)
    → Show: "Resuming interrupted session..."
    → GOTO Resume Flow

ELSE IF implementation.completed_tasks > 0 AND < total_tasks:
    # Previous session ended normally but feature incomplete
    → GOTO Incomplete Session Flow

ELSE IF implementation.completed_tasks == 0 OR implementation.feature != current_spec:
    # Fresh start
    → GOTO New Session Flow

ELSE IF implementation.completed_tasks == total_tasks:
    # Feature already complete
    → Show: "Feature [X] already implemented. Run /playtest?"
```

---

### Resume Flow (Continue from checkpoint)

**Triggered by:** `/implement continue` OR `implementation.active == true`

```
Resuming: [feature]

Progress: [completed]/[total] tasks ([percentage]%)
Last: [last_completed] - "[title]"
Next: [next_task] - "[title]"

Continuing from [next_task]...
```

→ **Skip to Step 1** (Engine detection)
→ **In engine file:** Start implementation loop at [next_task], not T001

---

### Incomplete Session Flow (Previous session saved)

**Triggered by:** `completed_tasks > 0 AND < total_tasks AND active == false`

```
Previous session: [feature]

Progress: [completed]/[total] tasks ([percentage]%)
Last checkpoint: [last_checkpoint timestamp]
Stopped at: [last_completed] - "[title]"

Options:
  [A] Continue from [next_task] (recommended)
  [B] Restart from T001 (lose progress)
  [C] Change scope (e.g., finish current phase only)
```

→ On [A]: Set `active: true`, continue from [next_task]
→ On [B]: Reset implementation state, start fresh
→ On [C]: Ask for new scope, then continue

---

### New Session Flow (Fresh start)

**Triggered by:** No implementation state OR different feature

```
Starting: [feature]

Tasks: [total] | MVP: [mvp_count] | Phases: [phase_count]

Session scope:
  [A] MVP (Setup + Foundation + US1) - recommended first run
  [B] Full feature (all [total] tasks)
  [C] Specific range (e.g., T001-T020)
  [D] Single phase (e.g., "Phase 2: Foundation")
```

→ On selection, initialize `state.yaml`:
```yaml
implementation:
  active: true
  feature: [feature]
  total_tasks: [N]
  completed_tasks: 0
  last_completed: null
  next_task: "T001"
  session_scope: "[selection]"
  sessions:
    count: 1
    history:
      - date: [today]
        started_at: "T001"
  last_checkpoint: null
```

---

### Scope Argument Handling

If user provides scope directly (`/implement T001-T015`):

```
Starting: [feature]
Scope: T001-T015 ([count] tasks)

Proceeding with specified scope...
```

→ Initialize state with provided scope, skip selection prompt

## Step 1: Detect Engine

Read `.skgd/config.yaml` and check `mcp.engine.active`:

```yaml
mcp:
  engine:
    active: unity  # or "godot"
```

## Step 2: Route to Engine-Specific Implementation

### If `active: unity`

Follow the instructions in `.claude/commands/implement-unity.md`

**Key tools:** `mcp__UnityMCP__*`
- `manage_editor`, `create_script`, `manage_gameobject`, `manage_scene`, `read_console`

**Paths:** `Assets/Scripts/`, `Assets/Scenes/`

---

### If `active: godot`

Follow the instructions in `.claude/commands/implement-godot.md`

**Key tools:** `mcp__gdai__*`
- `get_project_info`, `create_script`, `add_node`, `create_scene`, `get_godot_errors`

**Paths:** `res://scripts/`, `res://scenes/`

---

## Quick Reference: Tool Mapping

| Action | Unity MCP | GDAI MCP |
|--------|-----------|----------|
| Check connection | `manage_editor(get_state)` | `get_project_info` |
| Play | `manage_editor(play)` | `play_scene` |
| Stop | `manage_editor(stop)` | `stop_running_scene` |
| Create script | `create_script` | `create_script` |
| Create node/object | `manage_gameobject(create)` | `add_node` |
| Modify properties | `manage_gameobject(set_component_property)` | `update_property` |
| Delete node/object | `manage_gameobject(delete)` | `delete_node` |
| Create scene | `manage_scene(create)` | `create_scene` |
| Open scene | `manage_scene(load)` | `open_scene` |
| Save scene | `manage_scene(save)` | *(auto-saved)* |
| Check errors | `read_console` | `get_godot_errors` |
| Screenshot | *(N/A)* | `get_running_scene_screenshot` |

## If Engine Not Configured

If `mcp.engine.active` is not set or unclear:

```
Engine not configured.

Please run: skgd init --engine [unity|godot]
Or manually set in .skgd/config.yaml:
  mcp:
    engine:
      active: unity  # or godot
```
