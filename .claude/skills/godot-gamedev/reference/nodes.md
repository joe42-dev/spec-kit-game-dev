# Godot Node Management Patterns

> **Token estimate:** ~400 tokens | **Last updated:** 2025-12

## Table of Contents
- [Adding Nodes](#adding-nodes) - add_node, Common node types (2D, 3D, UI)
- [Modifying Properties](#modifying-properties) - update_property, Transform, Visibility, Physics
- [Node Hierarchies](#node-hierarchies) - Standard Player, Enemy, Level structures
- [Building Hierarchies](#building-hierarchies) - Step-by-step setup patterns
- [Groups](#groups) - Categorizing nodes, Common group usage
- [Layers & Masks](#layers--masks) - Collision layer configuration
- [Anti-Patterns](#anti-patterns) - What NOT to do

---

## Adding Nodes

### Tool Usage: add_node
```python
mcp__gdai__add_node(
    parent_path="/root/Main",
    node_type="CharacterBody2D",
    node_name="Player"
)
```

### Common Node Types

**2D Physics:**
- `CharacterBody2D` - Player/enemy movement
- `RigidBody2D` - Physics objects
- `StaticBody2D` - Walls, platforms
- `Area2D` - Triggers, hitboxes

**2D Visuals:**
- `Sprite2D` - Static images
- `AnimatedSprite2D` - Frame animations
- `AnimationPlayer` - Complex animations

**3D Equivalents:**
- `CharacterBody3D`, `RigidBody3D`, `StaticBody3D`, `Area3D`
- `MeshInstance3D`, `AnimationPlayer`

**UI:**
- `Control` - Base UI node
- `Button`, `Label`, `TextureRect`
- `VBoxContainer`, `HBoxContainer` - Layouts

**Utility:**
- `Timer` - Delayed/repeated calls
- `AudioStreamPlayer2D` - Sound effects
- `Camera2D` - Following camera

## Modifying Properties

### Tool Usage: update_property
```python
mcp__gdai__update_property(
    node_path="/root/Main/Player",
    property="position",
    value="Vector2(100, 200)"
)
```

### Common Properties

**Transform (2D):**
```python
update_property(node_path, "position", "Vector2(x, y)")
update_property(node_path, "rotation", "1.57")  # radians
update_property(node_path, "scale", "Vector2(2, 2)")
```

**Transform (3D):**
```python
update_property(node_path, "position", "Vector3(x, y, z)")
update_property(node_path, "rotation", "Vector3(0, 1.57, 0)")
```

**Visibility:**
```python
update_property(node_path, "visible", "true")
update_property(node_path, "modulate", "Color(1, 0, 0, 1)")  # RGBA
```

**Physics Bodies:**
```python
update_property(node_path, "collision_layer", "1")
update_property(node_path, "collision_mask", "3")
```

## Node Hierarchies

### Standard Player (2D)
```
Player (CharacterBody2D)
├── Sprite2D (visuals)
├── CollisionShape2D (physics)
├── AnimationPlayer (animations)
├── Camera2D (following camera)
└── HitboxArea (Area2D for combat)
    └── CollisionShape2D
```

### Standard Enemy (2D)
```
Enemy (CharacterBody2D)
├── Sprite2D
├── CollisionShape2D
├── AnimationPlayer
├── NavigationAgent2D (pathfinding)
├── DetectionArea (Area2D)
│   └── CollisionShape2D
└── AttackPoint (Marker2D)
```

### Standard Level
```
Level (Node2D)
├── TileMap (ground, walls)
├── Entities (Node2D)
│   ├── Player
│   └── Enemies (Node2D)
│       └── [enemy instances]
├── Collectibles (Node2D)
│   └── [pickup instances]
├── SpawnPoints (Node2D)
│   └── [Marker2D instances]
└── Camera2D
```

## Building Hierarchies

### Create Player Setup
```python
# 1. Create root
mcp__gdai__add_node(
    parent_path="/root/Main",
    node_type="CharacterBody2D",
    node_name="Player"
)

# 2. Add sprite
mcp__gdai__add_node(
    parent_path="/root/Main/Player",
    node_type="Sprite2D",
    node_name="Sprite2D"
)

# 3. Add collision
mcp__gdai__add_node(
    parent_path="/root/Main/Player",
    node_type="CollisionShape2D",
    node_name="CollisionShape2D"
)

# 4. Configure collision shape (via script or editor)
```

## Groups

Groups are Godot's way to categorize nodes for bulk operations.

### Common Group Usage (in scripts)
```gdscript
# Add to group
add_to_group("enemies")

# Process all in group
for enemy in get_tree().get_nodes_in_group("enemies"):
    enemy.take_damage(10)

# Call method on all
get_tree().call_group("enemies", "alert_player")
```

### Standard Groups
- `"player"` - Player node(s)
- `"enemies"` - All enemies
- `"projectiles"` - Bullets, etc.
- `"pickups"` - Collectibles
- `"interactables"` - Objects player can interact with

## Layers & Masks

### Layer Naming Convention
```
Layer 1: Player
Layer 2: Enemies
Layer 3: World (walls, floors)
Layer 4: Projectiles
Layer 5: Pickups
Layer 6: Triggers
```

### Configuration
```python
# Player: on layer 1, collides with layers 2, 3
update_property("/root/Main/Player", "collision_layer", "1")
update_property("/root/Main/Player", "collision_mask", "6")  # 2 + 4 = 6

# Enemy: on layer 2, collides with layers 1, 3, 4
update_property("/root/Main/Enemy", "collision_layer", "2")
update_property("/root/Main/Enemy", "collision_mask", "13")  # 1 + 4 + 8 = 13
```

## Anti-Patterns

- Deep nesting (prefer flat, use groups instead)
- Hardcoded node paths (use @export NodePath or groups)
- Not setting collision layers (everything collides with everything)
- Missing CollisionShape2D on physics bodies
- Not caching node references (@onready)
