"""Spec Kit Game Dev CLI - Initialize game development projects."""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from typing import Optional

import click
import questionary
import yaml

from . import __version__


MODELS = {
    "opus": "Highest quality, recommended for creative and complex tasks",
    "sonnet": "Balanced quality and speed, good for most tasks",
    "haiku": "Fast and economical, good for simple tasks",
}

SHELLS = {
    "bash": "Linux/macOS",
    "powershell": "Windows",
}

LANGUAGES = {
    "en": "English",
    "fr": "Français",
}

ENGINES = {
    "unity": "Unity (Unity MCP)",
    "godot": "Godot (GDAI MCP)",
}

GAME_TYPES = [
    "platformer",
    "rpg",
    "puzzle",
    "shooter",
    "roguelike",
    "simulation",
    "strategy",
    "action-adventure",
]

ART_STYLES = {
    "pixel-2d": "Pixel Art (2D retro style)",
    "stylized-2d": "Hand-drawn / Stylized (2D)",
    "realistic-3d": "Realistic (3D)",
    "stylized-3d": "Low-poly / Stylized (3D)",
    "mixed": "Mixed / Undecided",
}

ASSET_MCPS = {
    "blender": {
        "name": "Blender MCP",
        "description": "3D modeling, materials, animations",
        "install": "claude mcp add blender-mcp -- uvx blender-mcp",
        "detector": "blender",
    },
    "pixellab": {
        "name": "PixelLab MCP",
        "description": "AI sprite generation, animations, tilesets",
        "install": "claude mcp add pixellab -- npx pixellab-mcp",
        "detector": None,
    },
}


SKGD_VERSION = "3.6"


def get_template_dir() -> Path:
    """Get the path to the templates directory."""
    return Path(__file__).parent / "templates"


def detect_existing_project(dest: Path) -> dict:
    """Detect existing Spec Kit project and its version.

    Returns dict with:
        - exists: bool
        - version: str or None
        - has_game_brief: bool
        - specs_count: int
        - has_learnings: bool
        - has_v2_templates: bool
    """
    skgd_dir = dest / ".skgd"

    if not skgd_dir.exists():
        return {"exists": False}

    info = {
        "exists": True,
        "version": None,
        "has_game_brief": (dest / "docs" / "game-brief.md").exists(),
        "specs_count": 0,
        "has_learnings": (skgd_dir / "memory" / "learnings.md").exists(),
        "has_constitution": (skgd_dir / "memory" / "constitution.md").exists(),
        "has_v2_templates": False,
        "has_v3_templates": False,
        "has_i18n": (skgd_dir / "i18n").exists(),
        "has_session_context": (skgd_dir / "memory" / "session-context.md").exists(),
        "has_learnings_core": (skgd_dir / "templates" / "learnings-core.md").exists() or
                             (skgd_dir / "memory" / "learnings-core.md").exists(),
        "has_assets_catalog": (skgd_dir / "memory" / "assets-catalog.md").exists(),
        "has_assets_config": False,
    }

    # Count specs
    specs_dir = dest / "docs" / "specs"
    if specs_dir.exists():
        info["specs_count"] = len([d for d in specs_dir.iterdir() if d.is_dir()])

    # Try to get version from config
    config_path = skgd_dir / "config.yaml"
    if config_path.exists():
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f) or {}
                info["version"] = config.get("version", "1.x")
                # Check for v3.0 assets config
                mcp_config = config.get("mcp", {})
                info["has_assets_config"] = "assets" in mcp_config
        except Exception:
            info["version"] = "1.x"
    else:
        info["version"] = "1.x"

    # Check for v2.0 markers
    info["has_v2_templates"] = info["has_i18n"] and info["has_session_context"]

    # Check for v3.0 markers (v2 + assets pipeline)
    info["has_v3_templates"] = (info["has_v2_templates"] and
                                info["has_assets_catalog"] and
                                info["has_assets_config"])

    return info


def upgrade_project(dest: Path, lang: str, engine: str) -> dict:
    """Upgrade existing project to v2.0.

    Returns dict with upgrade stats:
        - commands_updated: int
        - templates_added: list
        - preserved: list
    """
    template_dir = get_template_dir() / lang
    skgd_dest = dest / ".skgd"
    commands_dest = dest / ".claude" / "commands"

    stats = {
        "commands_updated": 0,
        "templates_added": [],
        "preserved": [],
        "to_version": SKGD_VERSION,
    }

    # 1. Update commands (always overwrite - these are the workflow)
    commands_src = template_dir / "claude" / "commands"
    if commands_src.exists():
        for cmd_file in commands_src.glob("*.md"):
            shutil.copy2(cmd_file, commands_dest / cmd_file.name)
            stats["commands_updated"] += 1

    # 2. Add new v2.0 templates (don't overwrite existing)

    # i18n directory
    i18n_dest = skgd_dest / "i18n"
    if not i18n_dest.exists():
        i18n_src = template_dir / "skgd" / "i18n"
        if i18n_src.exists():
            shutil.copytree(i18n_src, i18n_dest)
            stats["templates_added"].append("i18n/messages.yaml")

    # learnings-core.md template
    learnings_core_template = skgd_dest / "templates" / "learnings-core.md"
    if not learnings_core_template.exists():
        src = template_dir / "skgd" / "templates" / "learnings-core.md"
        if src.exists():
            shutil.copy2(src, learnings_core_template)
            stats["templates_added"].append("templates/learnings-core.md")

    # session-context.md template
    session_context_template = skgd_dest / "templates" / "session-context.md"
    if not session_context_template.exists():
        src = template_dir / "skgd" / "templates" / "session-context.md"
        if src.exists():
            shutil.copy2(src, session_context_template)
            stats["templates_added"].append("templates/session-context.md")

    # Create empty memory files for v2.0 Living Memory System
    memory_dir = skgd_dest / "memory"
    memory_dir.mkdir(exist_ok=True)

    # Empty learnings-core.md (for crystallized learnings)
    learnings_core_memory = memory_dir / "learnings-core.md"
    if not learnings_core_memory.exists():
        learnings_core_src = template_dir / "skgd" / "templates" / "learnings-core.md"
        if learnings_core_src.exists():
            shutil.copy2(learnings_core_src, learnings_core_memory)
            stats["templates_added"].append("memory/learnings-core.md")

    # Empty session-context.md
    session_context_memory = memory_dir / "session-context.md"
    if not session_context_memory.exists():
        session_context_src = template_dir / "skgd" / "templates" / "session-context.md"
        if session_context_src.exists():
            shutil.copy2(session_context_src, session_context_memory)
            stats["templates_added"].append("memory/session-context.md")

    # 2.5 Copy/update skills (always overwrite for latest patterns)
    skills_dest = dest / ".claude" / "skills"
    skills_src = get_template_dir() / "common" / "skills"
    if skills_src.exists():
        skills_dest.mkdir(parents=True, exist_ok=True)
        for skill_dir in skills_src.iterdir():
            if skill_dir.is_dir():
                skill_dest = skills_dest / skill_dir.name
                if skill_dest.exists():
                    shutil.rmtree(skill_dest)
                shutil.copytree(skill_dir, skill_dest)
        stats["skills_updated"] = len(list(skills_src.iterdir()))

    # 3. Track preserved files
    if (dest / "docs" / "game-brief.md").exists():
        stats["preserved"].append("docs/game-brief.md")

    specs_dir = dest / "docs" / "specs"
    if specs_dir.exists():
        spec_count = len([d for d in specs_dir.iterdir() if d.is_dir()])
        if spec_count > 0:
            stats["preserved"].append(f"docs/specs/ ({spec_count} features)")

    if (memory_dir / "learnings.md").exists():
        stats["preserved"].append(".skgd/memory/learnings.md")

    if (memory_dir / "constitution.md").exists():
        stats["preserved"].append(".skgd/memory/constitution.md")

    if (skgd_dest / "state.yaml").exists():
        stats["preserved"].append(".skgd/state.yaml")

    if (skgd_dest / "roadmap.yaml").exists():
        stats["preserved"].append(".skgd/roadmap.yaml")

    # 4. Update config.yaml with new fields
    config_path = skgd_dest / "config.yaml"
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
    else:
        config = {}

    # Add version
    config["version"] = SKGD_VERSION

    # Add/update user.language if missing
    if "user" not in config:
        config["user"] = {}
    if "language" not in config["user"]:
        config["user"]["language"] = lang

    # Update MCP section for engine choice
    if "mcp" not in config:
        config["mcp"] = {}

    if engine == "unity":
        config["mcp"]["unity"] = config["mcp"].get("unity", {"required": True, "status": "unchecked"})
        config["mcp"]["gdai"] = {"required": False, "status": "unchecked"}
    else:  # godot
        config["mcp"]["unity"] = {"required": False, "status": "unchecked"}
        config["mcp"]["gdai"] = config["mcp"].get("gdai", {"required": True, "status": "unchecked"})

    # Add engine field
    config["engine"] = engine

    with open(config_path, "w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)

    return stats


def upgrade_v2_to_v3(dest: Path, lang: str, art_style: Optional[str] = None, asset_mcps: Optional[list] = None) -> dict:
    """Upgrade existing v2.0 project to v3.0.

    Adds:
        - Asset pipeline support (mcp.assets config)
        - assets-catalog.md
        - check-asset-mcps scripts
        - Updated commands with asset support

    Returns dict with upgrade stats.
    """
    template_dir = get_template_dir() / lang
    skgd_dest = dest / ".skgd"
    commands_dest = dest / ".claude" / "commands"
    memory_dir = skgd_dest / "memory"
    scripts_dir = skgd_dest / "scripts"

    stats = {
        "commands_updated": 0,
        "templates_added": [],
        "preserved": [],
        "from_version": "2.0",
        "to_version": SKGD_VERSION,
    }

    # 1. Update commands (always overwrite - these are the workflow)
    commands_src = template_dir / "claude" / "commands"
    if commands_src.exists():
        for cmd_file in commands_src.glob("*.md"):
            shutil.copy2(cmd_file, commands_dest / cmd_file.name)
            stats["commands_updated"] += 1

    # 1.5 Copy/update skills (always overwrite for latest patterns)
    skills_dest = dest / ".claude" / "skills"
    skills_src = get_template_dir() / "common" / "skills"
    if skills_src.exists():
        skills_dest.mkdir(parents=True, exist_ok=True)
        for skill_dir in skills_src.iterdir():
            if skill_dir.is_dir():
                skill_dest_dir = skills_dest / skill_dir.name
                if skill_dest_dir.exists():
                    shutil.rmtree(skill_dest_dir)
                shutil.copytree(skill_dir, skill_dest_dir)
        stats["skills_updated"] = len(list(skills_src.iterdir()))

    # 1.6 Copy/update data folder (always overwrite for latest reference data)
    data_dest = dest / ".claude" / "data"
    data_src = template_dir / "claude" / "data"
    if data_src.exists():
        data_dest.mkdir(parents=True, exist_ok=True)
        for data_file in data_src.glob("*.md"):
            shutil.copy2(data_file, data_dest / data_file.name)
        stats["data_updated"] = len(list(data_src.glob("*.md")))

    # 2. Add assets-catalog.md if not exists
    memory_dir.mkdir(exist_ok=True)
    assets_catalog_dest = memory_dir / "assets-catalog.md"
    if not assets_catalog_dest.exists():
        assets_catalog_src = template_dir / "skgd" / "memory" / "assets-catalog.md"
        if assets_catalog_src.exists():
            shutil.copy2(assets_catalog_src, assets_catalog_dest)
            stats["templates_added"].append("memory/assets-catalog.md")

    # 3. Add check-asset-mcps scripts
    scripts_dir.mkdir(exist_ok=True)
    scripts_src = template_dir / "skgd" / "scripts"
    if scripts_src.exists():
        for script_file in scripts_src.glob("check-asset-mcps.*"):
            script_dest = scripts_dir / script_file.name
            if not script_dest.exists():
                shutil.copy2(script_file, script_dest)
                # Make shell scripts executable
                if script_file.suffix == ".sh":
                    script_dest.chmod(script_dest.stat().st_mode | 0o755)
                stats["templates_added"].append(f"scripts/{script_file.name}")

    # 4. Update agents with asset MCP references
    agents_src = template_dir / "skgd" / "agents"
    agents_dest = skgd_dest / "agents"
    if agents_src.exists() and agents_dest.exists():
        for agent_file in agents_src.glob("*.md"):
            shutil.copy2(agent_file, agents_dest / agent_file.name)

    # 5. Update config.yaml with mcp.assets section
    config_path = skgd_dest / "config.yaml"
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
    else:
        config = {}

    # Update version
    config["version"] = SKGD_VERSION

    # Add mcp.assets section if missing
    if "mcp" not in config:
        config["mcp"] = {}

    if "assets" not in config["mcp"]:
        asset_mcps = asset_mcps or []
        config["mcp"]["assets"] = {
            "profile": art_style,
            "blender": {
                "enabled": "blender" in asset_mcps,
                "status": "unchecked",
                "export_format": "fbx"
            },
            "pixellab": {
                "enabled": "pixellab" in asset_mcps,
                "status": "unchecked"
            }
        }
        stats["templates_added"].append("config.yaml (mcp.assets section)")

    with open(config_path, "w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)

    # 6. Update state.yaml with assets section
    state_path = skgd_dest / "state.yaml"
    if state_path.exists():
        with open(state_path, "r", encoding="utf-8") as f:
            state = yaml.safe_load(f) or {}

        if "assets" not in state:
            state["assets"] = {
                "queue": [],
                "generated": [],
                "placeholders": []
            }
            stats["templates_added"].append("state.yaml (assets section)")

            with open(state_path, "w", encoding="utf-8") as f:
                yaml.dump(state, f, default_flow_style=False, sort_keys=False)

    # 7. Track preserved files
    if (dest / "docs" / "game-brief.md").exists():
        stats["preserved"].append("docs/game-brief.md")

    specs_dir = dest / "docs" / "specs"
    if specs_dir.exists():
        spec_count = len([d for d in specs_dir.iterdir() if d.is_dir()])
        if spec_count > 0:
            stats["preserved"].append(f"docs/specs/ ({spec_count} features)")

    if (memory_dir / "learnings.md").exists():
        stats["preserved"].append(".skgd/memory/learnings.md")

    if (memory_dir / "learnings-core.md").exists():
        stats["preserved"].append(".skgd/memory/learnings-core.md")

    if (memory_dir / "constitution.md").exists():
        stats["preserved"].append(".skgd/memory/constitution.md")

    if (skgd_dest / "roadmap.yaml").exists():
        stats["preserved"].append(".skgd/roadmap.yaml")

    return stats


def print_upgrade_success(stats: dict, lang: str = "en") -> None:
    """Print upgrade success message."""
    # Detect version from stats
    to_version = stats.get("to_version", "2.0")
    is_v3_upgrade = to_version.startswith("3.")

    click.echo()
    click.secho("  ╔═══════════════════════════════════════════════════════════════╗", fg="green")
    click.secho("  ║                                                               ║", fg="green")
    if lang == "fr":
        click.secho(f"  ║   ✓  PROJET MIS A JOUR VERS v{to_version} !                           ║", fg="green")
    else:
        click.secho(f"  ║   ✓  PROJECT UPGRADED TO v{to_version}!                                ║", fg="green")
    click.secho("  ║                                                               ║", fg="green")
    click.secho("  ╚═══════════════════════════════════════════════════════════════╝", fg="green")
    click.echo()

    # What was updated
    if lang == "fr":
        click.secho("  📦 Modifications:", fg="cyan", bold=True)
    else:
        click.secho("  📦 Changes:", fg="cyan", bold=True)
    click.echo()
    click.secho(f"     ✓ Commands updated ({stats['commands_updated']} files)", fg="green")

    if stats.get("skills_updated"):
        click.secho(f"     ✓ Skills added/updated ({stats['skills_updated']} skills)", fg="green")

    if stats.get("data_updated"):
        click.secho(f"     ✓ Reference data updated ({stats['data_updated']} files)", fg="green")

    if stats["templates_added"]:
        click.secho("     ✓ New templates added:", fg="green")
        for t in stats["templates_added"]:
            click.echo(f"        └─ {t}")

    if is_v3_upgrade:
        click.secho("     ✓ Asset pipeline added", fg="green")
    else:
        click.secho("     ✓ i18n support added", fg="green")
        click.secho("     ✓ Living Memory structure created", fg="green")
    click.echo()

    # What was preserved
    if stats["preserved"]:
        if lang == "fr":
            click.secho("  🔒 Preserve:", fg="yellow", bold=True)
        else:
            click.secho("  🔒 Preserved:", fg="yellow", bold=True)
        click.echo()
        for p in stats["preserved"]:
            click.echo(f"     └─ {p}")
        click.echo()

    # New features
    click.secho("  ┌─────────────────────────────────────────────────────────────┐", fg="cyan")
    if lang == "fr":
        click.secho("  │  🆕  Nouvelles fonctionnalites:                             │", fg="cyan")
    else:
        click.secho("  │  🆕  New features available:                                │", fg="cyan")
    click.secho("  │                                                             │", fg="cyan")

    # Detect minor version upgrades (e.g., 3.5 -> 3.6)
    from_version = stats.get("from_version", "")
    is_v36_upgrade = to_version == "3.6" and from_version.startswith("3.")

    if is_v36_upgrade:
        click.secho("  │    /next        - Zero-friction continue (auto-execute)     │", fg="cyan")
        click.secho("  │    /assets      - Asset pipeline with PixelLab MCP          │", fg="cyan")
        click.secho("  │    Auto-Suggest - Post-command suggestions                  │", fg="cyan")
        click.secho("  │    Quality Gates- Validation checkpoints in /implement      │", fg="cyan")
    elif is_v3_upgrade:
        click.secho("  │    /implement   - Unified Unity/Godot (auto-detect)         │", fg="cyan")
        click.secho("  │    Scout-First  - Context gathering via Haiku               │", fg="cyan")
        click.secho("  │    /deep-dive   - Pillar development with Scout             │", fg="cyan")
    else:
        click.secho("  │    /crystallize - Compress your learnings                   │", fg="cyan")
        click.secho("  │    /brainstorm  - Now with spark mode                       │", fg="cyan")
        click.secho("  │    /continue    - Flow preservation                         │", fg="cyan")
    click.secho("  └─────────────────────────────────────────────────────────────┘", fg="cyan")
    click.echo()

    if lang == "fr":
        click.echo(f"  Executez {click.style('/continue', fg='cyan')} pour reprendre votre projet.")
    else:
        click.echo(f"  Run {click.style('/continue', fg='cyan')} to resume your project.")
    click.echo()


def copy_templates(dest: Path, shell: str, model: str, lang: str = "en", engine: str = "unity") -> None:
    """Copy all template files to destination."""
    template_dir = get_template_dir() / lang

    # Copy .claude/commands
    commands_src = template_dir / "claude" / "commands"
    commands_dest = dest / ".claude" / "commands"
    if commands_src.exists():
        shutil.copytree(commands_src, commands_dest, dirs_exist_ok=True)

    # Copy .skgd
    skgd_src = template_dir / "skgd"
    skgd_dest = dest / ".skgd"
    if skgd_src.exists():
        shutil.copytree(skgd_src, skgd_dest, dirs_exist_ok=True)

    # Copy docs structure
    docs_dest = dest / "docs"
    docs_dest.mkdir(parents=True, exist_ok=True)
    (docs_dest / "specs").mkdir(exist_ok=True)

    # Create snapshots directory
    (skgd_dest / "snapshots").mkdir(exist_ok=True)

    # Create memory directory with v2.0 structure
    memory_dir = skgd_dest / "memory"
    memory_dir.mkdir(exist_ok=True)


def update_config(
    dest: Path,
    project_name: str,
    model: str,
    shell: str,
    lang: str = "en",
    engine: str = "unity",
    art_style: Optional[str] = None,
    asset_mcps: Optional[list] = None
) -> None:
    """Update config.yaml with user preferences."""
    config_path = dest / ".skgd" / "config.yaml"

    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
    else:
        config = {}

    # Add version
    config["version"] = SKGD_VERSION

    config["project"] = config.get("project", {})
    config["project"]["name"] = project_name

    # Engine selection
    config["engine"] = engine

    config["models"] = config.get("models", {})
    config["models"]["default"] = model

    config["shell"] = shell

    config["user"] = config.get("user", {})
    config["user"]["language"] = lang

    # MCP configuration - restructured with engine and assets sections
    config["mcp"] = config.get("mcp", {})

    # Engine MCPs
    config["mcp"]["engine"] = config["mcp"].get("engine", {})
    config["mcp"]["engine"]["active"] = engine
    if engine == "unity":
        config["mcp"]["engine"]["unity"] = {"required": True, "status": "unchecked"}
        config["mcp"]["engine"]["gdai"] = {"required": False, "status": "unchecked"}
    else:  # godot
        config["mcp"]["engine"]["unity"] = {"required": False, "status": "unchecked"}
        config["mcp"]["engine"]["gdai"] = {"required": True, "status": "unchecked"}

    # Asset MCPs
    config["mcp"]["assets"] = config["mcp"].get("assets", {})
    config["mcp"]["assets"]["profile"] = art_style

    # Configure selected asset MCPs
    asset_mcps = asset_mcps or []
    config["mcp"]["assets"]["blender"] = {
        "enabled": "blender" in asset_mcps,
        "status": "unchecked",
        "export_format": "fbx"
    }
    config["mcp"]["assets"]["pixellab"] = {
        "enabled": "pixellab" in asset_mcps,
        "status": "unchecked"
    }

    with open(config_path, "w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)


def get_readme_content(project_name: str, engine: str, lang: str) -> str:
    """Generate README content based on language and engine."""
    engine_name = "Unity" if engine == "unity" else "Godot"
    mcp_name = "Unity MCP" if engine == "unity" else "GDAI MCP"

    if lang == "fr":
        return f"""# {project_name}

Un projet de jeu utilisant le workflow **Spec Kit Game Dev** avec {engine_name}.

## Pour commencer

1. Ouvrez l'editeur {engine_name} dans ce dossier
2. Lancez `claude` pour demarrer Claude Code
3. Executez `/init` pour initialiser le workflow

## Commandes

| Commande | Description |
|----------|-------------|
| `/init` | Initialiser le projet |
| `/brainstorm` | Ideation creative |
| `/roadmap` | Feuille de route |
| `/spec [feature]` | Creer une specification |
| `/plan [feature]` | Plan d'implementation |
| `/implement` | Executer via {mcp_name} |
| `/playtest` | Tester et valider |
| `/project-status` | Etat actuel |
| `/continue` | Auto-router l'action suivante |
| `/crystallize` | Cristalliser les apprentissages |

## Workflow

```
/init -> /brainstorm -> /roadmap -> [/spec -> /plan -> /implement -> /playtest] (repeter)
```
"""
    else:  # English (default)
        return f"""# {project_name}

A game project using **Spec Kit Game Dev** workflow with {engine_name}.

## Getting Started

1. Open {engine_name} Editor in this folder
2. Run `claude` to start Claude Code
3. Run `/init` to initialize the workflow

## Commands

| Command | Description |
|---------|-------------|
| `/init` | Initialize project |
| `/brainstorm` | Creative ideation |
| `/roadmap` | Development path |
| `/spec [feature]` | Create specification |
| `/plan [feature]` | Implementation plan |
| `/implement` | Execute via {mcp_name} |
| `/playtest` | Test and validate |
| `/project-status` | Current state |
| `/continue` | Auto-route next action |
| `/crystallize` | Compress learnings |

## Workflow

```
/init -> /brainstorm -> /roadmap -> [/spec -> /plan -> /implement -> /playtest] (repeat)
```
"""


def print_banner() -> None:
    """Print the welcome banner."""
    click.echo()
    click.secho("  ╔═══════════════════════════════════════════════════════════════╗", fg="cyan")
    click.secho("  ║                                                               ║", fg="cyan")
    click.secho("  ║   ███████╗██████╗ ███████╗ ██████╗    ██╗  ██╗██╗████████╗    ║", fg="cyan")
    click.secho("  ║   ██╔════╝██╔══██╗██╔════╝██╔════╝    ██║ ██╔╝██║╚══██╔══╝    ║", fg="cyan")
    click.secho("  ║   ███████╗██████╔╝█████╗  ██║         █████╔╝ ██║   ██║       ║", fg="cyan")
    click.secho("  ║   ╚════██║██╔═══╝ ██╔══╝  ██║         ██╔═██╗ ██║   ██║       ║", fg="cyan")
    click.secho("  ║   ███████║██║     ███████╗╚██████╗    ██║  ██╗██║   ██║       ║", fg="cyan")
    click.secho("  ║   ╚══════╝╚═╝     ╚══════╝ ╚═════╝    ╚═╝  ╚═╝╚═╝   ╚═╝       ║", fg="cyan")
    click.secho("  ║                                                               ║", fg="cyan")
    click.secho("  ║            G A M E   D E V   W O R K F L O W                  ║", fg="cyan")
    click.secho("  ║                      v" + SKGD_VERSION + "                                     ║", fg="cyan")
    click.secho("  ╚═══════════════════════════════════════════════════════════════╝", fg="cyan")
    click.echo()


def print_success(project_name: str, dest: Path, engine: str = "unity", lang: str = "en") -> None:
    """Print success message."""
    engine_name = "Unity" if engine == "unity" else "Godot"

    click.echo()
    click.secho("  ╔═══════════════════════════════════════════════════════════════╗", fg="green")
    click.secho("  ║                                                               ║", fg="green")
    if lang == "fr":
        click.secho("  ║   ✓  PROJET CREE AVEC SUCCES !                               ║", fg="green")
    else:
        click.secho("  ║   ✓  PROJECT CREATED SUCCESSFULLY!                            ║", fg="green")
    click.secho("  ║                                                               ║", fg="green")
    click.secho("  ╚═══════════════════════════════════════════════════════════════╝", fg="green")
    click.echo()

    # Project info box
    click.secho("  ┌─────────────────────────────────────────────────────────────┐", fg="white")
    click.echo(f"  │  Project: {click.style(project_name, fg='cyan', bold=True):<50}│")
    click.echo(f"  │  Engine:  {click.style(engine_name, fg='yellow'):<50}│")
    click.echo(f"  │  Path:    {click.style(str(dest)[:48], fg='white'):<50}│")
    click.secho("  └─────────────────────────────────────────────────────────────┘", fg="white")
    click.echo()

    if lang == "fr":
        click.secho("  📋 Prochaines etapes:", fg="yellow", bold=True)
        click.echo()
        click.echo(f"     1. cd {project_name}")
        click.echo(f"     2. Ouvrez votre projet {engine_name} ici (ou creez-en un)")
        click.echo(f"     3. Lancez Claude Code: {click.style('claude', fg='cyan')}")
        click.echo(f"     4. Executez: {click.style('/init', fg='cyan')}")
    else:
        click.secho("  📋 Next steps:", fg="yellow", bold=True)
        click.echo()
        click.echo(f"     1. cd {project_name}")
        click.echo(f"     2. Open your {engine_name} project here (or create new)")
        click.echo(f"     3. Start Claude Code: {click.style('claude', fg='cyan')}")
        click.echo(f"     4. Run: {click.style('/init', fg='cyan')}")
    click.echo()


def check_mcp_command() -> bool:
    """Check if Claude CLI is installed."""
    try:
        result = subprocess.run(
            ["claude", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def detect_blender() -> bool:
    """Check if Blender is installed locally."""
    try:
        result = subprocess.run(
            ["blender", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def recommend_asset_mcps(art_style: str, has_blender: bool) -> list:
    """Recommend asset MCPs based on art style and detected tools."""
    recommendations = []

    if art_style in ["realistic-3d", "stylized-3d", "mixed"]:
        if has_blender:
            recommendations.append("blender")

    if art_style in ["pixel-2d", "stylized-2d", "mixed"]:
        recommendations.append("pixellab")

    return recommendations


@click.group()
@click.version_option(version=__version__, prog_name="skgd")
def main():
    """Spec Kit Game Dev - AI-first workflow for game development."""
    pass


@main.command()
@click.argument("project_name", required=False)
@click.option(
    "--model", "-m",
    type=click.Choice(list(MODELS.keys())),
    help="Default LLM model to use"
)
@click.option(
    "--shell", "-s",
    type=click.Choice(list(SHELLS.keys())),
    help="Shell type (bash or powershell)"
)
@click.option(
    "--no-interactive", "-y",
    is_flag=True,
    help="Skip interactive prompts, use defaults"
)
@click.option(
    "--here", "-H",
    is_flag=True,
    help="Initialize in current directory (for existing projects)"
)
@click.option(
    "--lang", "-l",
    type=click.Choice(list(LANGUAGES.keys())),
    help="Language for workflow templates (en or fr)"
)
@click.option(
    "--engine", "-e",
    type=click.Choice(list(ENGINES.keys())),
    help="Game engine (unity or godot)"
)
def init(project_name: Optional[str], model: Optional[str], shell: Optional[str], no_interactive: bool, here: bool, lang: Optional[str], engine: Optional[str]):
    """Initialize a new Spec Kit Game Dev project.

    Creates a new directory with the complete workflow structure
    for AI-assisted game development with Unity or Godot.

    Examples:
        skgd init my-awesome-game           # Create new project folder
        skgd init --here                    # Initialize in current folder
        skgd init --here --engine godot     # Upgrade existing project for Godot
        skgd init -H -e unity               # Short form
    """
    print_banner()

    # Determine destination
    if here:
        dest = Path.cwd()
        project_name = project_name or dest.name

        # Check for existing Spec Kit project - offer upgrade instead of error
        existing = detect_existing_project(dest)
        if existing["exists"]:
            current_version = existing.get("version", "1.x")
            click.secho(f"Detected existing Spec Kit Game Dev project (v{current_version})", fg="yellow")
            click.echo()

            # Check if already at latest version
            if existing["has_v3_templates"] and current_version == SKGD_VERSION:
                click.secho(f"Project is already at v{SKGD_VERSION}. Nothing to upgrade.", fg="green")
                click.echo("Use --force to re-initialize (will overwrite commands).")
                sys.exit(0)

            # Determine upgrade path
            is_v1_to_v2 = not existing["has_v2_templates"]
            is_v2_to_v3 = existing["has_v2_templates"] and not existing["has_v3_templates"]

            # Show what will be preserved
            click.echo("  Will preserve:")
            if existing["has_game_brief"]:
                click.echo("    - docs/game-brief.md")
            if existing["specs_count"] > 0:
                click.echo(f"    - docs/specs/ ({existing['specs_count']} features)")
            if existing["has_learnings"]:
                click.echo("    - .skgd/memory/learnings.md")
            if existing["has_constitution"]:
                click.echo("    - .skgd/memory/constitution.md")
            if is_v2_to_v3 and existing.get("has_learnings_core"):
                click.echo("    - .skgd/memory/learnings-core.md")
            click.echo()

            # Ask for upgrade confirmation in interactive mode
            if not no_interactive:
                upgrade_msg = f"Upgrade to v{SKGD_VERSION}?"
                if not questionary.confirm(upgrade_msg, default=True).ask():
                    click.echo("Upgrade cancelled.")
                    sys.exit(0)

            # Get missing options for upgrade
            art_style = None
            asset_mcps = []

            if not no_interactive:
                if lang is None:
                    lang = questionary.select(
                        "Select language / Choisir la langue:",
                        choices=[
                            questionary.Choice(f"{desc}", value=key)
                            for key, desc in LANGUAGES.items()
                        ],
                        default="en"
                    ).ask()
                    if lang is None:  # User cancelled
                        sys.exit(0)

                if engine is None:
                    engine = questionary.select(
                        "Select game engine:",
                        choices=[
                            questionary.Choice(f"{key} - {desc}", value=key)
                            for key, desc in ENGINES.items()
                        ],
                        default="unity"
                    ).ask()
                    if engine is None:
                        sys.exit(0)

                # For v2→v3 upgrade, ask about art style and asset MCPs
                if is_v2_to_v3:
                    click.echo("v3.0 adds an asset pipeline. Let's configure it:")
                    click.echo()

                    # Art style selection
                    art_style = questionary.select(
                        "Select art style (for asset pipeline):",
                        choices=[
                            questionary.Choice(f"{key} - {desc}", value=key)
                            for key, desc in ART_STYLES.items()
                        ],
                        default="mixed"
                    ).ask()
                    if art_style is None:
                        sys.exit(0)

                    # Detect tools and recommend MCPs
                    click.echo("  +-- Detecting asset tools...")
                    has_blender = detect_blender()
                    if has_blender:
                        click.secho("      [OK] Blender detected", fg="green")
                    else:
                        click.secho("      [--] Blender not found", fg="yellow")

                    recommended_mcps = recommend_asset_mcps(art_style, has_blender)
                    if recommended_mcps:
                        click.echo()
                        click.echo("Recommended asset MCPs for your art style:")
                        for mcp_key in recommended_mcps:
                            mcp_info = ASSET_MCPS[mcp_key]
                            click.echo(f"  - {click.style(mcp_info['name'], fg='cyan')}: {mcp_info['description']}")
                        if questionary.confirm("Enable recommended asset MCPs?", default=True).ask():
                            asset_mcps = recommended_mcps
            else:
                lang = lang or "en"
                engine = engine or "unity"

            # Perform upgrade
            click.secho(f"Upgrading to v{SKGD_VERSION}...", fg="cyan")
            click.echo()

            try:
                if is_v1_to_v2:
                    # First upgrade v1→v2
                    stats = upgrade_project(dest, lang, engine)
                    print_upgrade_success(stats, lang)
                    click.echo()
                    click.secho("Now upgrading v2.0→v3.0...", fg="cyan")
                    click.echo()

                    # Then upgrade v2→v3
                    stats = upgrade_v2_to_v3(dest, lang, art_style, asset_mcps)
                    print_upgrade_success(stats, lang)
                elif is_v2_to_v3:
                    # Direct v2→v3 upgrade
                    stats = upgrade_v2_to_v3(dest, lang, art_style, asset_mcps)
                    print_upgrade_success(stats, lang)
                else:
                    # Fallback to v1→v2 upgrade
                    stats = upgrade_project(dest, lang, engine)
                    print_upgrade_success(stats, lang)
            except Exception as e:
                click.secho(f"Error during upgrade: {e}", fg="red")
                sys.exit(1)

            return  # Exit after upgrade

        # New project in existing directory
        click.secho(f"Initializing workflow in existing project: {dest.name}", fg="yellow")
        click.echo()
    else:
        if not project_name:
            click.secho("Error: Please provide a project name or use --here for current directory.", fg="red")
            click.echo("       Example: skgd init my-game")
            click.echo("       Example: skgd init --here")
            sys.exit(1)

        dest = Path.cwd() / project_name
        if dest.exists():
            click.secho(f"Error: Directory '{project_name}' already exists.", fg="red")
            click.echo("       Use --here to initialize in an existing directory.")
            sys.exit(1)

    # Interactive prompts if not provided
    if not no_interactive:
        if model is None:
            model = questionary.select(
                "Select default LLM model:",
                choices=[
                    questionary.Choice(f"{key} - {desc}", value=key)
                    for key, desc in MODELS.items()
                ],
                default="opus"
            ).ask()
            if model is None:
                sys.exit(0)

        if shell is None:
            default_shell = "powershell" if os.name == "nt" else "bash"
            shell = questionary.select(
                "Select your shell:",
                choices=[
                    questionary.Choice(f"{key} - {desc}", value=key)
                    for key, desc in SHELLS.items()
                ],
                default=default_shell
            ).ask()
            if shell is None:
                sys.exit(0)

        if lang is None:
            lang = questionary.select(
                "Select language / Choisir la langue:",
                choices=[
                    questionary.Choice(f"{desc}", value=key)
                    for key, desc in LANGUAGES.items()
                ],
                default="en"
            ).ask()
            if lang is None:
                sys.exit(0)

        if engine is None:
            engine = questionary.select(
                "Select game engine:",
                choices=[
                    questionary.Choice(f"{key} - {desc}", value=key)
                    for key, desc in ENGINES.items()
                ],
                default="unity"
            ).ask()
            if engine is None:
                sys.exit(0)

        # Art style selection (optional but recommended)
        art_style = questionary.select(
            "Select art style (for asset pipeline):",
            choices=[
                questionary.Choice(f"{key} - {desc}", value=key)
                for key, desc in ART_STYLES.items()
            ],
            default="mixed"
        ).ask()
        if art_style is None:
            sys.exit(0)

        # Detect available tools and recommend MCPs
        click.echo("  +-- Detecting asset tools...")
        has_blender = detect_blender()
        if has_blender:
            click.secho("      [OK] Blender detected", fg="green")
        else:
            click.secho("      [--] Blender not found", fg="yellow")

        # Get recommendations based on art style
        recommended_mcps = recommend_asset_mcps(art_style, has_blender)

        # Ask about asset MCPs
        asset_mcps = []
        if recommended_mcps:
            click.echo()
            click.echo("Recommended asset MCPs for your art style:")
            for mcp_key in recommended_mcps:
                mcp_info = ASSET_MCPS[mcp_key]
                click.echo(f"  - {click.style(mcp_info['name'], fg='cyan')}: {mcp_info['description']}")

            if questionary.confirm("Enable recommended asset MCPs?", default=True).ask():
                asset_mcps = recommended_mcps
    else:
        # Defaults for non-interactive
        model = model or "sonnet"
        shell = shell or ("powershell" if os.name == "nt" else "bash")
        lang = lang or "en"
        engine = engine or "unity"
        art_style = None
        asset_mcps = []

    # Create project
    if here:
        click.echo(f"Adding workflow to '{project_name}'...")
    else:
        click.echo(f"Creating project '{project_name}'...")
    click.echo()

    try:
        # Only create directory for new projects
        if not here:
            dest.mkdir(parents=True, exist_ok=True)

        # Copy templates
        click.echo("  +-- Copying workflow templates...")
        copy_templates(dest, shell, model, lang, engine)
        click.secho("  |   [OK] .claude/commands/", fg="green")
        click.secho("  |   [OK] .skgd/", fg="green")
        click.secho("  |   [OK] docs/", fg="green")

        # Update config
        click.echo("  +-- Configuring project...")
        update_config(dest, project_name, model, shell, lang, engine, art_style, asset_mcps)
        click.secho("  |   [OK] config.yaml updated", fg="green")

        # Show asset MCP status if configured
        if asset_mcps:
            click.echo("  +-- Asset MCPs configured:")
            for mcp_key in asset_mcps:
                mcp_info = ASSET_MCPS[mcp_key]
                click.secho(f"  |   [OK] {mcp_info['name']} enabled", fg="green")

        # Create or skip README
        readme_path = dest / "README.md"
        if readme_path.exists() and here:
            # Don't overwrite existing README for existing projects
            click.secho("  |   [--] README.md exists, skipped", fg="yellow")
        else:
            readme_content = get_readme_content(project_name, engine, lang)
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(readme_content)
            click.secho("  |   [OK] README.md created", fg="green")

        # Check Claude CLI
        click.echo("  +-- Checking prerequisites...")
        if check_mcp_command():
            click.secho("      [OK] Claude CLI detected", fg="green")
        else:
            click.secho("      [!!] Claude CLI not found", fg="yellow")
            click.echo("           Install: npm install -g @anthropic-ai/claude-code")

        print_success(project_name, dest, engine, lang)

    except Exception as e:
        click.secho(f"Error creating project: {e}", fg="red")
        # Cleanup on failure
        if dest.exists():
            shutil.rmtree(dest)
        sys.exit(1)


@main.command("check-mcp")
def check_mcp():
    """Check MCP installation status.

    Verifies that Claude CLI and Unity MCP are properly configured.
    """
    print_banner()

    click.echo("Checking MCP setup...")
    click.echo()

    # Check Claude CLI
    click.echo("1. Claude Code CLI")
    if check_mcp_command():
        click.secho("   [OK] Installed", fg="green")
    else:
        click.secho("   [X] Not found", fg="red")
        click.echo("       Install: npm install -g @anthropic-ai/claude-code")

    click.echo()
    click.echo("2. Unity MCP")
    click.echo("   Run this in Claude Code to check:")
    click.secho("   mcp__UnityMCP__manage_editor with action: \"get_state\"", fg="cyan")
    click.echo()
    click.echo("   If not installed:")
    click.secho("   claude mcp add unity-mcp -- uvx --from git+https://github.com/SirLorrence/unity-mcp unity-mcp", fg="cyan")
    click.echo()


@main.command()
def version():
    """Show version information."""
    click.echo(f"Spec Kit Game Dev v{__version__}")


@main.command("check-assets")
def check_assets():
    """Check asset MCP installation status.

    Verifies that asset creation tools (Blender, PixelLab) are available.
    """
    print_banner()

    click.echo("Checking Asset Pipeline Setup...")
    click.echo()

    # Check local tools
    click.secho("1. Local Tools", bold=True)
    click.echo()

    has_blender = detect_blender()
    if has_blender:
        click.secho("   [OK] Blender installed", fg="green")
    else:
        click.secho("   [--] Blender not found", fg="yellow")
        click.echo("        Install from: https://www.blender.org/download/")
    click.echo()

    # Check MCPs
    click.secho("2. Asset MCPs", bold=True)
    click.echo()

    for mcp_key, mcp_info in ASSET_MCPS.items():
        click.echo(f"   {mcp_info['name']}:")
        click.echo(f"        {mcp_info['description']}")
        click.echo(f"        Install: {click.style(mcp_info['install'], fg='cyan')}")
        click.echo()

    # Recommendations
    click.secho("3. Recommendations by Art Style", bold=True)
    click.echo()
    click.echo("   Pixel Art (2D):     PixelLab MCP")
    click.echo("   Stylized (2D):      PixelLab MCP")
    click.echo("   3D (any):           Blender MCP (requires Blender)")
    click.echo("   Mixed:              Both recommended")
    click.echo()


@main.command("list-templates")
def list_templates():
    """List available game type templates."""
    print_banner()

    click.echo("Available game type templates:")
    click.echo()

    templates = {
        "platformer": "Movement, levels, precision jumping",
        "rpg": "Stats, combat, dialogue, progression",
        "puzzle": "Rules, solutions, difficulty curves",
        "shooter": "Weapons, enemies, action mechanics",
        "roguelike": "Procedural generation, permadeath, meta-progression",
        "simulation": "Systems, time management, emergence",
        "strategy": "Units, resources, tactical decisions",
        "action-adventure": "Exploration, combat, abilities",
    }

    for name, desc in templates.items():
        click.echo(f"  - {click.style(name, fg='cyan')}: {desc}")

    click.echo()
    click.echo("Template is selected during /init command in Claude Code.")


@main.command()
@click.option(
    "--lang", "-l",
    type=click.Choice(list(LANGUAGES.keys())),
    help="Language for workflow templates (en or fr)"
)
@click.option(
    "--no-interactive", "-y",
    is_flag=True,
    help="Skip interactive prompts, use defaults"
)
def upgrade(lang: Optional[str], no_interactive: bool):
    """Upgrade existing project to latest SKGD version.

    Updates slash commands, adds new skills, and preserves your
    existing game-brief, specs, and learnings.

    Must be run from within an existing SKGD project directory.

    Examples:
        skgd upgrade              # Interactive upgrade
        skgd upgrade -y           # Non-interactive, use defaults
        skgd upgrade --lang fr    # Upgrade with French templates
    """
    print_banner()

    dest = Path.cwd()

    # Detect existing project
    existing = detect_existing_project(dest)
    if not existing["exists"]:
        click.secho("Error: No SKGD project found in current directory.", fg="red")
        click.echo()
        click.echo("To create a new project:")
        click.echo("  skgd init my-game")
        click.echo()
        click.echo("To initialize in current directory:")
        click.echo("  skgd init --here")
        sys.exit(1)

    current_version = existing.get("version", "1.x")

    # Detect language and engine from existing config first
    detected_lang = "en"
    detected_engine = "unity"
    config_path = dest / ".skgd" / "config.yaml"
    if config_path.exists():
        try:
            import yaml
            with open(config_path) as f:
                config = yaml.safe_load(f)
            detected_lang = config.get("user", {}).get("language", "en")
            detected_engine = config.get("engine", "unity")
        except Exception:
            pass

    # Use provided lang or detected
    if lang is None:
        lang = detected_lang
    engine = detected_engine

    # Display detected configuration
    click.secho(f"Detected SKGD project (v{current_version})", fg="yellow")
    click.echo(f"  Engine:   {click.style(engine, fg='cyan')}")
    click.echo(f"  Language: {click.style(lang, fg='cyan')}")
    click.echo()

    # Check if already at latest version
    if existing["has_v3_templates"] and current_version == SKGD_VERSION:
        click.secho(f"Project is already at v{SKGD_VERSION}. Nothing to upgrade.", fg="green")
        sys.exit(0)

    # Show what will be preserved
    click.echo("Will preserve:")
    if existing["has_game_brief"]:
        click.secho("  - docs/game-brief.md", fg="green")
    if existing["specs_count"] > 0:
        click.secho(f"  - docs/specs/ ({existing['specs_count']} features)", fg="green")
    if existing["has_learnings"]:
        click.secho("  - .skgd/memory/learnings.md", fg="green")
    if existing["has_constitution"]:
        click.secho("  - .skgd/memory/constitution.md", fg="green")
    if existing.get("has_learnings_core"):
        click.secho("  - .skgd/memory/learnings-core.md", fg="green")
    click.echo()

    # Confirm upgrade
    if not no_interactive:
        if not questionary.confirm(f"Upgrade to v{SKGD_VERSION}?", default=True).ask():
            click.echo("Upgrade cancelled.")
            sys.exit(0)

    # Perform upgrade
    click.echo()
    click.echo("Upgrading...")

    try:
        # Determine upgrade path
        if existing["has_v3_templates"]:
            # v3.x to v3.y (minor/patch upgrade) - still use v2_to_v3 as it updates commands/skills
            stats = upgrade_v2_to_v3(dest, lang)
            stats["from_version"] = current_version
        elif existing["has_v2_templates"]:
            # v2 to v3
            stats = upgrade_v2_to_v3(dest, lang)
        else:
            # v1 to v2+
            stats = upgrade_project(dest, lang, engine)
            # Then upgrade to v3
            stats = upgrade_v2_to_v3(dest, lang)

        print_upgrade_success(stats, lang)

    except Exception as e:
        click.secho(f"Error during upgrade: {e}", fg="red")
        sys.exit(1)


if __name__ == "__main__":
    main()
