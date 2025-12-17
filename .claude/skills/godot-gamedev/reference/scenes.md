# Godot Scene Management Patterns

> **Token estimate:** ~450 tokens | **Last updated:** 2025-12

## Table of Contents
- [Scene Operations](#scene-operations) - create_scene, open_scene, play/stop, screenshot
- [Scene Types](#scene-types) - Root node selection, Common scene structures
- [Scene Workflow](#scene-workflow) - Creating complete levels step-by-step
- [Scene Instancing](#scene-instancing) - Runtime instantiation in GDScript
- [Folder Structure](#folder-structure) - Recommended project organization
- [Scene Testing Cycle](#scene-testing-cycle) - Standard test flow
- [Main Scene Setup](#main-scene-setup) - Boot scene pattern
- [Anti-Patterns](#anti-patterns) - What NOT to do

---

## Scene Operations

### Create New Scene
```python
mcp__gdai__create_scene(
    scene_path="res://scenes/levels/level_01.tscn",
    root_type="Node2D",
    root_name="Level01"
)
```

### Open Existing Scene
```python
mcp__gdai__open_scene(
    scene_path="res://scenes/levels/level_01.tscn"
)
```

### Run Scene
```python
mcp__gdai__play_scene(
    scene_path="res://scenes/levels/level_01.tscn"
)
# Or run current scene
mcp__gdai__play_scene()
```

### Stop Running Scene
```python
mcp__gdai__stop_running_scene()
```

### Visual Check
```python
mcp__gdai__get_running_scene_screenshot()
# Returns screenshot of running game
```

## Scene Types

### Root Node Selection Guide

**2D Games:**
- `Node2D` - Generic 2D scene (levels, UI screens)
- `CharacterBody2D` - Player/enemy scenes
- `Control` - Pure UI scenes

**3D Games:**
- `Node3D` - Generic 3D scene
- `CharacterBody3D` - Player/enemy scenes

### Common Scene Types

**Player Scene (player.tscn):**
```
Player (CharacterBody2D)
├── Sprite2D
├── CollisionShape2D
├── AnimationPlayer
└── [script: player_controller.gd]
```

**Enemy Scene (enemy.tscn):**
```
Enemy (CharacterBody2D)
├── Sprite2D
├── CollisionShape2D
├── DetectionArea (Area2D)
│   └── CollisionShape2D
└── [script: enemy_ai.gd]
```

**Level Scene (level_01.tscn):**
```
Level01 (Node2D)
├── TileMap
├── Player [instance of player.tscn]
├── Enemies (Node2D)
│   └── [enemy instances]
├── SpawnPoints (Node2D)
└── [script: level_manager.gd]
```

**UI Scene (hud.tscn):**
```
HUD (CanvasLayer)
├── MarginContainer
│   ├── HealthBar (ProgressBar)
│   └── ScoreLabel (Label)
└── [script: hud.gd]
```

## Scene Workflow

### Creating a Complete Level
```python
# 1. Create scene
mcp__gdai__create_scene(
    scene_path="res://scenes/levels/level_01.tscn",
    root_type="Node2D",
    root_name="Level01"
)

# 2. Add TileMap
mcp__gdai__add_node(
    parent_path="/root/Level01",
    node_type="TileMap",
    node_name="TileMap"
)

# 3. Add container for entities
mcp__gdai__add_node(
    parent_path="/root/Level01",
    node_type="Node2D",
    node_name="Entities"
)

# 4. Add spawn points container
mcp__gdai__add_node(
    parent_path="/root/Level01",
    node_type="Node2D",
    node_name="SpawnPoints"
)

# 5. Add spawn point markers
mcp__gdai__add_node(
    parent_path="/root/Level01/SpawnPoints",
    node_type="Marker2D",
    node_name="PlayerSpawn"
)

# 6. Test
mcp__gdai__play_scene(
    scene_path="res://scenes/levels/level_01.tscn"
)
```

## Scene Instancing

### In GDScript
```gdscript
# Load and instance a scene
var enemy_scene = preload("res://scenes/enemies/enemy.tscn")
var enemy_instance = enemy_scene.instantiate()
add_child(enemy_instance)
enemy_instance.position = spawn_point.position

# Or with PackedScene export
@export var enemy_scene: PackedScene

func spawn_enemy(pos: Vector2) -> void:
    var enemy = enemy_scene.instantiate()
    add_child(enemy)
    enemy.position = pos
```

## Folder Structure

### Recommended Organization
```
res://
├── scenes/
│   ├── levels/
│   │   ├── level_01.tscn
│   │   └── level_02.tscn
│   ├── characters/
│   │   ├── player.tscn
│   │   └── enemies/
│   │       ├── enemy_base.tscn
│   │       └── enemy_variants/
│   ├── ui/
│   │   ├── main_menu.tscn
│   │   ├── hud.tscn
│   │   └── pause_menu.tscn
│   └── pickups/
│       └── coin.tscn
├── scripts/
│   ├── player/
│   ├── enemies/
│   ├── systems/
│   └── ui/
├── resources/
│   └── data/
├── assets/
│   ├── sprites/
│   ├── audio/
│   └── fonts/
└── autoload/
    ├── game_manager.gd
    └── audio_manager.gd
```

## Scene Testing Cycle

### Standard Test Flow
```python
# 1. Open scene
mcp__gdai__open_scene(scene_path="res://scenes/levels/level_01.tscn")

# 2. Check for errors
mcp__gdai__get_godot_errors()

# 3. Run scene
mcp__gdai__play_scene()

# 4. Visual check
mcp__gdai__get_running_scene_screenshot()

# 5. Stop
mcp__gdai__stop_running_scene()

# 6. Check runtime errors
mcp__gdai__get_godot_errors()
```

## Main Scene Setup

### Project Settings
The main scene is set in Project Settings → Application → Run → Main Scene

### Boot Scene Pattern
```
main.tscn (Node)
├── GameManager (autoload handles this)
└── [immediately changes to menu or level]

# In game_manager.gd autoload:
func _ready():
    get_tree().change_scene_to_file("res://scenes/ui/main_menu.tscn")
```

## Anti-Patterns

- Single massive scene (split into instanced sub-scenes)
- Circular scene dependencies
- Not using CanvasLayer for UI
- Hardcoded scene paths (use @export PackedScene)
- Not organizing nodes in containers
