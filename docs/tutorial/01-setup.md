# SKGD Tutorial - Part 1: Setup

## Prerequisites

- **Python 3.8+** installed
- **Claude Code CLI** (`claude`) installed
- **Unity** or **Godot** installed
- **Git** installed

## Step 1: Install SKGD

```bash
pip install skgd
```

Or from source:
```bash
git clone https://github.com/your-repo/spec-kit-game-dev
cd spec-kit-game-dev
pip install -e .
```

## Step 2: Initialize Your Project

Navigate to your game project folder (or create a new one):

```bash
mkdir my-awesome-game
cd my-awesome-game
```

Run the SKGD CLI:

```bash
skgd init
```

You'll be prompted for:
- **Language**: English or French
- **Engine**: Unity or Godot
- **Shell**: Bash or PowerShell

The CLI will:
1. Copy all templates to your project
2. Create `.claude/commands/`, `.skgd/`, `docs/`
3. Set up initial configuration

## Step 3: Install Engine MCP

### For Unity

```bash
claude mcp add unity-mcp -- npx -y @anthropic-ai/unity-mcp
```

Then in Unity:
1. Open your Unity project
2. Install Unity MCP package (via Package Manager)
3. Open Window > Unity MCP to start the bridge

### For Godot

```bash
# GDAI MCP (paid, see gdaimcp.com)
claude mcp add gdai -- npx gdai-mcp
```

Then in Godot:
1. Enable GDAI plugin in Project Settings
2. Start the GDAI server

## Step 4: Run /init in Claude

Start Claude Code in your project:

```bash
claude
```

Then run:
```
/init
```

This command will:
1. **Check MCP connection** - Verifies Unity/Godot is connected
2. **Ask project questions**:
   - Project name
   - Game type (platformer, RPG, roguelike, etc.)
   - Core vision (one sentence)
   - Target platform
   - Unity/Godot version
   - Art style
   - Asset MCPs (optional)
3. **Generate CLAUDE.md** - Project-specific context file
4. **Update config.yaml** - With your answers
5. **Initialize git** - If not already

## Step 5: Verify Setup

Run:
```
/project-status
```

You should see:
```
╔═══════════════════════════════════════════════════════════════╗
║  🎮 SPEC KIT GAME DEV - STATUS                                ║
╠═══════════════════════════════════════════════════════════════╣
║  Project: [Your Project Name]                                  ║
║  Type: [Your Game Type]                                        ║
║  Phase: concept                                                ║
╠═══════════════════════════════════════════════════════════════╣
║  CONNECTIONS                                                   ║
║  ├─ [Unity/Godot] MCP: 🟢 Connected                           ║
╠═══════════════════════════════════════════════════════════════╣
║  NEXT ACTION                                                   ║
║  → Run /brainstorm to start creative ideation                 ║
╚═══════════════════════════════════════════════════════════════╝
```

## Upgrading Existing Projects

If you have an existing SKGD project:

```bash
skgd upgrade
```

This will:
- Update all commands to latest version
- Add new templates (without overwriting your content)
- Preserve your game-brief, specs, learnings

## Files Created

After setup, your project will have:

```
my-awesome-game/
├── CLAUDE.md                    # Generated with your project info
├── .claude/
│   ├── commands/                # 19 slash commands
│   │   ├── brainstorm.md
│   │   ├── implement.md
│   │   └── ...
│   ├── skills/                  # Engine patterns
│   │   ├── unity-gamedev/
│   │   └── godot-gamedev/
│   └── data/
│       └── game-types.md        # Pillar mappings
├── .skgd/
│   ├── config.yaml              # Your project settings
│   ├── state.yaml               # phase: concept
│   ├── memory/
│   │   └── (empty, ready for use)
│   └── i18n/
│       └── messages.yaml        # Localized strings
└── docs/
    └── specs/                   # Empty, ready for features
```

## Common Setup Issues

### "Unity MCP not connected"

1. Ensure Unity Editor is running
2. Check Window > Unity MCP bridge is active
3. Restart Claude Code

### "GDAI not responding"

1. Ensure Godot project is open
2. Check GDAI plugin is enabled
3. Verify GDAI server is running

### "skgd command not found"

```bash
pip install --user skgd
# Add ~/.local/bin to PATH if needed
```

## Next: Concept Phase

Your project is ready! Continue to **[Part 2: Concept Phase](02-concept.md)** to start brainstorming your game.
