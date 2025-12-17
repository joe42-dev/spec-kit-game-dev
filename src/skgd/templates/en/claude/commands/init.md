# /init - Initialize Spec Kit Game Dev Project

You are initializing a new game development project using **Spec Kit Game Dev** workflow.

## Your Task

Execute these steps in order:

### Step 1: Check Engine MCP Status

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

### Step 1b: Detect Asset Tools

Check for available asset creation tools:

**Blender Detection:**
```bash
blender --version 2>/dev/null || echo "not_found"
```

If Blender is found:
- Note the version for later recommendation
- Blender MCP can provide 3D modeling, materials, and animation support

Store detection results for Step 2b.

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

### Step 2b: Asset Configuration

Based on Step 1b detection results, ask about art style and asset tools:

1. **Art style** - What visual style are you targeting?
   - Pixel Art (2D retro style)
   - Hand-drawn / Stylized (2D)
   - Realistic (3D)
   - Low-poly / Stylized (3D)
   - Mixed / Undecided

2. **Asset tools** - Based on detected tools and art style, recommend appropriate MCPs:

   **If Blender detected + 3D style selected:**
   ```
   Blender MCP recommended for 3D modeling, materials, and animations.
   Install: claude mcp add blender-mcp -- uvx blender-mcp
   ```

   **If 2D/Pixel style selected:**
   ```
   PixelLab MCP recommended for AI sprite generation and animations.
   Install: claude mcp add pixellab -- npx pixellab-mcp
   ```

   **If Mixed style:**
   Offer both options.

3. Ask user which asset MCPs to enable (multi-select allowed):
   - Blender MCP (3D modeling)
   - PixelLab MCP (sprite generation)
   - None for now (can configure later with /assets setup)

### Step 3: Update Configuration Files

Update `.skgd/config.yaml` with gathered information:
- `project.name`, `project.type`, `project.vision`, `project.platform`
- `mcp.assets.profile` with selected art style
- `mcp.assets.blender.enabled` / `mcp.assets.pixellab.enabled` based on user choices

Example asset config update:
```yaml
mcp:
  assets:
    profile: pixel-2d  # or stylized-2d, realistic-3d, stylized-3d, mixed
    blender:
      enabled: true   # if user selected
      status: unchecked
    pixellab:
      enabled: true   # if user selected
      status: unchecked
```

Update `.skgd/state.yaml`:
```yaml
phase: concept
initialization:
  completed: true
  mcp_checked: true
  claude_md_generated: true
assets:
  total_defined: 0
  total_created: 0
  active_mcps: []  # Will be populated after MCP verification
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
| `/assets` | Manage asset pipeline |
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

## Asset Pipeline
Art Style: [From Step 2b]
Configured MCPs: [List enabled MCPs or "None - run /assets setup"]

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
Art Style: [Selected style]
Phase: Concept

Asset Pipeline:
  [✓/✗] Blender MCP - [enabled/disabled]
  [✓/✗] PixelLab MCP - [enabled/disabled]

Next step: Run /brainstorm to start your creative ideation session.
Or run /roadmap to see the full development path.
```

If asset MCPs were enabled, add:
```
Tip: After /spec, use /assets to generate assets before /implement.
```

## Model
Use: **sonnet** (standard initialization task)
