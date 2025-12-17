# Spec Kit Game Dev

> AI-first workflow for solo game developers using Claude Code with Unity MCP or GDAI (Godot).

A context-optimized system for building video games with AI assistance. Designed for **long-term projects** (months of development) while staying in Claude's optimal performance zone.

**Supported Engines:** Unity (via Unity MCP) | Godot (via [GDAI MCP](https://gdaimcp.com/))

---

## What Makes This Different

| Traditional AI Dev | Spec Kit Game Dev |
|-------------------|-------------------|
| Copy-paste code snippets | Direct Unity control via MCP |
| Lose context between sessions | Living Memory preserves continuity |
| Generic AI responses | Opus dialogue tailored to YOUR game |
| Start fresh each time | Crystallized learnings compound |

---

## Quick Start

### Prerequisites

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code)
- **Unity:** [Unity Editor](https://unity.com/) 2021.3+ with [Unity MCP](https://github.com/SirLorrence/unity-mcp)
- **Godot:** [Godot Engine](https://godotengine.org/) 4.2+ with [GDAI MCP](https://gdaimcp.com/)
- Python 3.8+
- Git

#### macOS Notes

macOS users with zsh as default shell: no worries, all scripts use bash and work fine.

```bash
# Install Python (if needed) via Homebrew
brew install python

# Or via pyenv for version management
brew install pyenv
pyenv install 3.11
pyenv global 3.11

# Install uv (recommended for faster installs)
brew install uv
```

### Installation

#### Option 1: Direct install (recommended)

```bash
# Unity project
uvx --from git+https://github.com/joe42-dev/spec-kit-game-dev.git skgd init my-game

# Godot project
uvx --from git+https://github.com/joe42-dev/spec-kit-game-dev.git skgd init my-game --engine godot
```

#### Option 2: Install globally

```bash
# Install once
pip install git+https://github.com/joe42-dev/spec-kit-game-dev.git

# Then use anywhere
skgd init my-game
skgd init my-game --engine godot
```

#### Start working

```bash
cd my-game
claude
```

### Your First Session (5 minutes)

```bash
# 1. Initialize your project
/init

# 2. Creative brainstorming with Opus
/brainstorm

# 3. See your development roadmap
/roadmap

# 4. Start your first feature
/continue
```

That's it. You're building a game with AI.

---

## Tutorial: Complete Workflow

### Session 1: Vision & Architecture (30-45 min)

**Goal:** Establish your game's core vision and technical foundation.

```
/brainstorm
```

Opus will have a creative dialogue with you (3 modes: Explorer, Creator, Spark):
- What excites you about this game?
- What feeling should players have?
- What's the ONE thing that makes it different?

**Output:** `docs/game-brief.md` - Your game's soul captured.

```
/roadmap
```

Opus analyzes your vision and creates a prioritized development path.

**Output:** `.skgd/roadmap.yaml` - Features ordered by importance.

```
/architecture
```

Opus designs project-wide technical decisions:
- Core systems (game loop, state management)
- Engine patterns (Unity/Godot specific)
- Folder structure
- Data architecture

**Output:** `docs/architecture.md` - Technical foundation for all features.

---

### Session 1.5: Design Pillars

**Goal:** Deep-dive into your game's design decisions with quality focus.

```
/pillars
```

Generates design pillar stubs based on your game type (roguelike, platformer, RPG, etc.):
- `docs/pillars/game-loop.md` - Core gameplay cycle
- `docs/pillars/combat-system.md` - Combat mechanics (if applicable)
- `docs/pillars/progression.md` - Player progression
- And more based on your game type...

```
/deep-dive game-loop
```

Develops ONE pillar in depth through collaborative dialogue:
- Answer key design questions
- Explore options with pros/cons
- Reference successful games
- Check cross-pillar coherence

**Output:** Complete `docs/pillars/[pillar].md` with decisions, rationale, and prototype plan.

```
/validate-design
```

Checks coherence across all completed pillars:
- Finds contradictions and tensions
- Identifies gaps
- Suggests adjustments

**Why this matters:** One pillar at a time = maximum quality. Each deep-dive loads previous pillars for coherence.

---

### Session 2-N: Feature Development (1-2 hours each)

Each feature follows the same cycle:

```
┌───────────────────────────────────────────────────────┐
│                                                       │
│   /spec [feature]    Define WHAT to build (stories)   │
│         ↓                                             │
│   /plan [feature]    Design HOW (architecture)        │
│         ↓                                             │
│   /tasks [feature]   Generate EXECUTION checklist     │
│         ↓                                             │
│   /implement         Build in Unity/Godot via MCP     │
│         ↓                                             │
│   /playtest          Test and capture learnings       │
│         ↓                                             │
│   /continue          Next feature                     │
│                                                       │
└───────────────────────────────────────────────────────┘
```

#### Example: Building Player Movement

```bash
# Define the feature
/spec player-movement
```

Opus creates a detailed specification:
- User stories (what the player experiences)
- Requirements (specific, testable)
- Edge cases (what could go wrong)
- Acceptance criteria (how we know it's done)

```bash
# Plan the implementation
/plan player-movement
```

Opus designs the technical architecture:
- Patterns to use
- Scripts to create
- Component dependencies
- Implementation phases

```bash
# Generate actionable tasks
/tasks player-movement
```

Opus creates an execution checklist:
- Task IDs (T001, T002...) for tracking
- [P] markers for parallelizable tasks
- [US1], [US2] for user story grouping
- Exact file paths for each task

```bash
# Build it in Unity/Godot
/implement
```

Opus executes directly in Unity via MCP:
- Creates C# scripts
- Sets up GameObjects
- Configures components
- Checks for errors

```bash
# Test and validate
/playtest
```

Opus runs tests and guides manual validation:
- Automated Unity tests
- Acceptance criteria checklist
- Game feel assessment
- Auto-captures learnings to `.skgd/memory/learnings.md`

```bash
# Move to next feature
/continue
```

---

### Between Sessions: Flow Preservation

When you return after a break:

```bash
/continue
```

The system remembers:
- Where you left off
- Decisions you made
- Open questions to revisit
- Your momentum level

```
Picking up where we left off...

Last session: 2 days ago
- You were: implementing enemy-ai
- Key decision: Using state machine pattern
- Momentum: high

Next logical step: /playtest enemy-ai

Options:
  [A] Continue with playtest (recommended)
  [B] Review first (/project-status)
  [C] Something else?
```

---

### Periodic: Compress Learnings

Every 5-10 features:

```bash
/crystallize
```

Compresses raw observations into validated patterns:
- What works in YOUR game
- Anti-patterns to avoid
- Technical decisions and WHY

Keeps your knowledge base compact but powerful.

---

### Milestones: Save Your Progress

```bash
/snapshot v0.1
```

Creates a git tag with full state capture. You can always roll back.

---

### Direction Changes: Pivot Safely

```bash
/pivot
```

When you need to change direction:
- Auto-creates safety snapshot
- Analyzes impact on everything
- Guides transition plan
- Preserves what's still valid

---

## Commands Reference

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `/init` | Setup project, verify MCP | Once at start |
| `/brainstorm` | Creative dialogue (3 modes) | Vision phase, or when stuck |
| `/roadmap` | Show/generate development priorities | After brainstorm, periodically |
| `/pillars` | Generate design pillar stubs | After brainstorm |
| `/deep-dive [pillar]` | Develop ONE pillar in depth | After pillars |
| `/validate-design` | Cross-pillar coherence check | After 2+ pillars complete |
| `/architecture` | Project-wide technical design | After roadmap, before features |
| `/spec [feature]` | Define WHAT to build (user stories) | Before building |
| `/plan [feature]` | Design HOW to build (patterns, structure) | After spec |
| `/tasks [feature]` | Generate EXECUTION checklist (IDs, deps) | After plan |
| `/implement` | Build in Unity/Godot via MCP | After tasks |
| `/playtest` | Test and capture learnings | After implement |
| `/crystallize` | Compress learnings into patterns | Every 5-10 features |
| `/continue` | Smart routing to next action | Anytime |
| `/next` | Zero-friction continue (just do it) | Vibe-coding flow |
| `/snapshot [v]` | Save milestone version | At milestones |
| `/pivot` | Handle major direction change | When vision changes |
| `/project-status` | Dashboard of current state | To check progress |
| `/analyze` | Cross-artifact consistency check | Before implement, periodically |
| `/gdd` | Generate formal Game Design Document | After pillars, for stakeholders |
| `/assets` | Asset pipeline management | When creating art |
| `/ci` | Setup GitHub Actions CI/CD (optional) | When you want automated tests |

**All commands use Opus** for maximum quality. Haiku/Sonnet are used only for research sub-tasks (Scout pattern).

---

## The Living Memory System

How the system maintains context over months:

```
┌─────────────────────────────────────────────────┐
│  LAYER 1: Constitution (~500 tokens)            │
│  Your game's immutable core vision              │
│  Only changes via /pivot                        │
├─────────────────────────────────────────────────┤
│  LAYER 2: Learnings Core (~1000 tokens)         │
│  Crystallized, validated patterns               │
│  Updated via /crystallize                       │
├─────────────────────────────────────────────────┤
│  LAYER 3: Session Context (~500 tokens)         │
│  Last session's decisions and momentum          │
│  Auto-updated each session                      │
├─────────────────────────────────────────────────┤
│  LAYER 4: Active Work (~3000 tokens)            │
│  Current spec/plan/tasks                        │
│  Focus of the moment                            │
├─────────────────────────────────────────────────┤
│  LAYER 5: Archive (not loaded)                  │
│  All completed specs, old learnings             │
│  Accessed via sub-agent when needed             │
└─────────────────────────────────────────────────┘

Total loaded: ~5k tokens
Available for conversation: ~75k tokens
```

This keeps you in the **Smart Zone** where Claude performs best.

---

## Project Structure

```
my-game/
├── .claude/commands/       # Workflow commands (don't edit)
├── .skgd/
│   ├── config.yaml         # Your project settings
│   ├── state.yaml          # Current workflow state
│   ├── roadmap.yaml        # Development priorities
│   ├── memory/
│   │   ├── constitution.md    # Core vision (immutable)
│   │   ├── learnings.md       # Raw observations
│   │   ├── learnings-core.md  # Crystallized patterns
│   │   └── session-context.md # Last session memory
│   ├── templates/          # Document templates
│   └── i18n/               # EN/FR messages
├── docs/
│   ├── game-brief.md       # Your game's vision
│   ├── architecture.md     # Project-wide technical design
│   ├── specs/              # Feature specifications
│   │   └── [feature]/
│   │       ├── spec.md     # WHAT to build
│   │       ├── plan.md     # HOW to build
│   │       ├── tasks.md    # Execution checklist
│   │       └── playtest.md # Test results
│   └── pivots/             # Direction change records
├── Assets/                 # Unity project
└── CLAUDE.md               # AI context for your project
```

---

## Engine MCP Setup

Required for `/implement` to work.

### Unity MCP (Free)

#### 1. Add MCP to Claude

```bash
claude mcp add unity-mcp -- uvx --from git+https://github.com/SirLorrence/unity-mcp unity-mcp
```

#### 2. Install in Unity

- Window > Package Manager > + > Add from git URL
- `https://github.com/SirLorrence/unity-mcp.git?path=com.slorrence.unitymcp`

#### 3. Enable

- Window > Unity MCP > Enable

---

### GDAI MCP for Godot ($19 one-time)

#### 1. Purchase and Install

Visit [gdaimcp.com](https://gdaimcp.com/) for installation instructions.

#### 2. Add MCP to Claude

Follow the configuration guide from GDAI documentation.

#### 3. Enable in Godot

Enable the GDAI MCP plugin in your Godot project.

---

### Verify

```bash
/init
```

The init command checks your MCP connection.

---

## Game Types

Templates included for:

| Type | Focus |
|------|-------|
| **Platformer** | Movement, levels, precision |
| **RPG** | Stats, combat, progression |
| **Puzzle** | Rules, solutions, difficulty |
| **Shooter** | Weapons, enemies, action |
| **Roguelike** | Procedural, permadeath, meta |
| **Simulation** | Systems, time, emergence |
| **Strategy** | Units, resources, decisions |
| **Action-Adventure** | Exploration, combat, abilities |

---

## Language Support

The system supports English and French.

```bash
# Set during init
skgd init my-game --lang fr

# Or in config
# .skgd/config.yaml
user:
  language: fr
```

All user-facing outputs adapt to your language.

---

## CLI Options

```bash
# Interactive setup (recommended)
skgd init my-game

# With engine selection
skgd init my-game --engine godot
skgd init my-game --engine unity

# With options
skgd init my-game --lang fr --shell bash --engine godot

# Skip prompts (use defaults)
skgd init my-game -y

# Initialize in existing directory
skgd init --here

# Upgrade existing project to v2.0
skgd init --here --engine godot

# Check MCP status
skgd check-mcp

# List game templates
skgd list-templates
```

### Options

| Option | Short | Description |
|--------|-------|-------------|
| `--engine` | `-e` | Game engine: `unity` or `godot` |
| `--lang` | `-l` | Language: `en` or `fr` |
| `--shell` | `-s` | Shell type: `bash` or `powershell` |
| `--here` | `-H` | Initialize in current directory |
| `--no-interactive` | `-y` | Skip prompts, use defaults |

---

## Tips for Success

### Do

- **Short sessions** - 1-2 hours max, use `/continue` to resume
- **One feature at a time** - Complete the cycle before starting another
- **Capture learnings** - The system learns from your playtests
- **Use `/brainstorm`** - When stuck, it gives fresh perspective
- **Trust the flow** - `/continue` knows what's next

### Don't

- Load all docs at once (context bloat)
- Skip `/playtest` (miss learning opportunities)
- Edit generated files manually (breaks state tracking)
- Rush through specs (vague specs = vague code)

---

## Philosophy

This system treats Claude as a **cognitive partner**, not a code generator.

- **Dialogue > Delegation** - Opus talks WITH you, not AT you
- **Emergence > Templates** - Let ideas emerge, then structure
- **Continuity > Sessions** - Memory persists across months
- **Quality > Speed** - Opus everywhere for best results

For the full philosophy, see `docs/SYSTEM-PHILOSOPHY.md`.

---

## Documentation

| Document | Purpose |
|----------|---------|
| [Tutorial](docs/tutorial/00-overview.md) | Complete step-by-step walkthrough |
| [Workflow Diagram](docs/diagrams/workflow.dot) | Visual command flow (Graphviz) |
| [File Dependencies](docs/diagrams/files.dot) | Data dependencies diagram |
| [Memory System](docs/diagrams/memory.dot) | Living Memory visualization |
| [Troubleshooting](docs/tutorial/07-troubleshooting.md) | Common issues & solutions |
| [Data Flow Reference](docs/tutorial/appendix-data-flow.md) | Complete technical reference |

Render DOT diagrams with:
```bash
dot -Tpng docs/diagrams/workflow.dot -o docs/diagrams/workflow.png
```
Or online: [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/)

---

## Troubleshooting

### Unity MCP not connecting

```bash
# Check MCP status
skgd check-mcp

# Verify Unity MCP is enabled
# In Unity: Window > Unity MCP > should show "Connected"
```

### Lost track of where I am

```bash
/project-status
```

Shows complete dashboard of your project state.

### Want to start over

```bash
# Create safety snapshot first
/snapshot backup

# Then reinitialize
/init
```

---

## Contributing

Contributions welcome! Key principles:

- Keep context minimal
- Prefer simplicity
- Test with real projects
- Document the WHY

### Development Setup

```bash
# Clone the repo
git clone https://github.com/joe42-dev/spec-kit-game-dev.git
cd spec-kit-game-dev

# Install in development mode
pip install -e .

# Test locally
skgd init test-project --engine godot
```

### Project Structure

```
spec-kit-game-dev/
├── src/skgd/
│   ├── cli.py              # Main CLI commands
│   └── templates/          # Project templates
│       ├── en/             # English templates
│       │   ├── claude/commands/  # Workflow commands
│       │   └── skgd/            # Config & memory templates
│       └── fr/             # French templates
├── docs/                   # Documentation
└── pyproject.toml          # Package config
```

---

## License

MIT

---

Built for solo developers who want to build games faster with AI.

*"The best workflow is one you actually use."*

---

## Upgrading Existing Projects

```bash
cd your-existing-project
pip install --upgrade git+https://github.com/joe42-dev/spec-kit-game-dev.git
skgd upgrade
```

This preserves your game-brief, specs, and learnings while updating commands to the latest version.