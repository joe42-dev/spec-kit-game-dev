---
name: godot-gamedev
description: |
  Godot game development patterns and GDAI MCP tool usage.

  TRIGGERS: Godot, GDScript, Node2D, Node3D, CharacterBody2D, CharacterBody3D,
  @export, @onready, signal, emit, Area2D, CollisionShape2D, TileMap, .gd file,
  .tscn file, GDAI MCP, create_script, add_node, play_scene, get_godot_errors

  USE WHEN: Creating GDScript files, managing Godot nodes, setting up scenes,
  connecting signals, building player/enemy hierarchies, configuring collision
  layers, or debugging Godot parsing errors.

  TOKEN BUDGET: ~470 tokens (SKILL.md only), ~1400 with references
---

# Godot Game Development Skill

## Quick Reference - GDAI MCP Tools

### Project & Editor
```
mcp__gdai__get_project_info      → Check connection, project details
mcp__gdai__get_godot_errors      → Check for errors
```

### Script Operations
```
mcp__gdai__create_script         → Create new GDScript files
mcp__gdai__attach_script         → Attach script to node
```

### Scene Operations
```
mcp__gdai__create_scene          → Create new scene
mcp__gdai__open_scene            → Load existing scene
mcp__gdai__play_scene            → Run scene
mcp__gdai__stop_running_scene    → Stop playback
mcp__gdai__get_running_scene_screenshot → Visual check
```

### Node Operations
```
mcp__gdai__add_node              → Add node to scene
mcp__gdai__update_property       → Modify node properties
```

## Implementation Patterns

### Pattern 1: Safe Script Creation
```
1. create_script → new GDScript
2. get_godot_errors → check parsing
3. IF errors → fix and recreate
4. attach_script → connect to node
```

### Pattern 2: Node Setup
```
1. create_scene → new scene with root
2. add_node → add children
3. update_property → configure nodes
4. attach_script → add behavior
```

### Pattern 3: Test Cycle
```
1. open_scene → load scene
2. play_scene → run
3. get_running_scene_screenshot → visual check
4. stop_running_scene → end test
5. get_godot_errors → check runtime errors
```

## Essential Anti-Patterns

- **NEVER** skip `get_godot_errors` after script changes
- **NEVER** forget to `stop_running_scene` after testing
- **NEVER** hardcode node paths (use exports, groups, signals)
- **ALWAYS** check connection with `get_project_info` first

## Detailed References

For in-depth patterns, see:
- [reference/scripts.md](reference/scripts.md) - GDScript patterns
- [reference/nodes.md](reference/nodes.md) - Node management
- [reference/scenes.md](reference/scenes.md) - Scene structure
- [reference/signals.md](reference/signals.md) - Signal patterns

## Pre-Implementation Checklist

Before implementing:
- [ ] Verify GDAI connection: `get_project_info`
- [ ] Check for existing errors: `get_godot_errors`
- [ ] Know target scene structure

After each script:
- [ ] `get_godot_errors` - No parsing errors
- [ ] Test with `play_scene` if behavioral
