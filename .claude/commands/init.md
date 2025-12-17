# /init - Initialize Spec Kit Game Dev Project

You are initializing a new game development project using **Spec Kit Game Dev** workflow.

## Your Task

Execute these steps in order:

### Step 1: Check MCP Status

Run the appropriate MCP check script based on OS:
- Linux: `.skgd/scripts/check-mcp.sh`
- Windows: `.skgd/scripts/check-mcp.ps1`

If Unity MCP is not installed, guide user through installation:
```
claude mcp add unity-mcp -- npx -y @anthropic-ai/unity-mcp
```

Verify Unity Editor is running and MCP is connected by calling:
```
mcp__UnityMCP__manage_editor with action: "get_state"
```

### Step 2: Gather Project Information

Ask the user these questions (use AskUserQuestion tool):

1. **Project name** - What's your game project called?

2. **Game type** - Select from:
   - Platformer
   - RPG
   - Puzzle
   - Shooter
   - Roguelike
   - Simulation
   - Strategy
   - Action-Adventure

3. **Core vision** - In one sentence, what experience do you want players to have?

4. **Target platform** - PC / Mobile / Web / Multi-platform?

5. **Unity version** - Which Unity version are you using?

### Step 3: Update Configuration Files

Update `.skgd/config.yaml` with gathered information.

Update `.skgd/state.yaml`:
```yaml
phase: concept
initialization:
  completed: true
  mcp_checked: true
  claude_md_generated: true
```

### Step 4: Generate CLAUDE.md

Create `CLAUDE.md` at project root with this structure:

```markdown
# [Project Name]

## Project Type
Unity Game - [Game Type]

## Workflow
This project uses **Spec Kit Game Dev** workflow.
- Run `/project-status` to see current state
- Run `/roadmap` for prioritized next steps
- Run `/continue` to auto-route to next action

## Commands
| Command | Description |
|---------|-------------|
| `/init` | Initialize project (done) |
| `/roadmap` | See prioritized features |
| `/brainstorm` | Creative ideation session |
| `/spec [feature]` | Create feature specification |
| `/plan [feature]` | Generate implementation plan |
| `/implement` | Execute in Unity via MCP |
| `/playtest` | Run tests + manual checklist |
| `/snapshot [v]` | Save project state |
| `/pivot` | Handle direction change |
| `/project-status` | Show current state |
| `/continue` | Auto-route next action |

## Constitution
[Insert core vision and principles from init]

## Unity MCP
Status: Connected
Commands available for direct Unity Editor control.

## Current State
Phase: Concept
Next: Run `/brainstorm` to begin ideation
```

### Step 5: Initialize Git (if not already)

If no `.git` folder exists:
```bash
git init
git add .
git commit -m "chore: initialize Spec Kit Game Dev project"
```

If git exists:
```bash
git add .
git commit -m "chore: initialize Spec Kit Game Dev workflow"
```

### Step 6: Welcome Message

Display:
```
🎮 Spec Kit Game Dev initialized!

Project: [Name]
Type: [Game Type]
Phase: Concept

Next step: Run /brainstorm to start your creative ideation session.
Or run /roadmap to see the full development path.
```

## Model
Use: **sonnet** (standard initialization task)
