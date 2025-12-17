# /project-status - Display Project Status

You are displaying the current state of the Spec Kit Game Dev project.

## Your Task

### Step 1: Read State Files

Read these files:
- `.skgd/state.yaml` - Current workflow state
- `.skgd/config.yaml` - Project configuration
- `.skgd/roadmap.yaml` - If exists, current roadmap

### Step 2: Check Unity MCP Connection

Quick check:
```
mcp__UnityMCP__manage_editor with action: "get_state"
```

### Step 3: Display Status Dashboard

Format output as:

```
╔══════════════════════════════════════════════════════════════╗
║  🎮 SPEC KIT GAME DEV - STATUS                               ║
╠══════════════════════════════════════════════════════════════╣
║  Project: [Name]                                             ║
║  Type: [Game Type]                                           ║
║  Phase: [Current Phase]                                      ║
╠══════════════════════════════════════════════════════════════╣
║  PROGRESS                                                    ║
║  ├─ Concept:      [✓ Done / ○ In Progress / · Pending]      ║
║  ├─ Design:       [✓ / ○ / ·]                               ║
║  ├─ Architecture: [✓ / ○ / ·]                               ║
║  └─ Production:   [Cycle X - Step Y]                        ║
╠══════════════════════════════════════════════════════════════╣
║  SPECS                                                       ║
║  ├─ Completed: [N]                                          ║
║  ├─ In Progress: [Current spec or "None"]                   ║
║  └─ Total: [N]                                              ║
╠══════════════════════════════════════════════════════════════╣
║  CONNECTIONS                                                 ║
║  ├─ Unity MCP: [🟢 Connected / 🔴 Disconnected]             ║
║  └─ Unity Editor: [Running / Not Running]                   ║
╠══════════════════════════════════════════════════════════════╣
║  SNAPSHOTS: [N] | Latest: [version or "None"]               ║
║  PIVOTS: [N]                                                ║
╠══════════════════════════════════════════════════════════════╣
║  NEXT ACTION                                                 ║
║  → [Suggested next command based on state]                  ║
╚══════════════════════════════════════════════════════════════╝
```

### Step 4: Suggest Next Action

Based on state, suggest:
- If `phase: uninitialized` → "Run /init to start"
- If `phase: concept` and no brainstorm → "Run /brainstorm"
- If `phase: concept` and brainstorm done → "Run /roadmap"
- If `phase: design` → "Run /spec [next-feature]"
- If `phase: production` → "Run /continue"

## Model
Use: **haiku** (simple status check)
