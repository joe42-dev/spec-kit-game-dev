# Godot GDScript Patterns

## Creating Scripts

### Tool Usage: create_script
```python
mcp__gdai__create_script(
    path="res://scripts/player/player_controller.gd",
    content=script_content
)
```

### Basic Node Script
```gdscript
# res://scripts/player/player_controller.gd
extends CharacterBody2D

@export var move_speed: float = 200.0

func _physics_process(delta: float) -> void:
    var direction = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = direction * move_speed
    move_and_slide()
```

### Class Name Declaration
```gdscript
class_name PlayerController
extends CharacterBody2D
```

## Script Structure

### Standard Template
```gdscript
class_name MyClass
extends Node

# Signals
signal health_changed(new_value: float)

# Exports (Inspector-configurable)
@export var max_health: float = 100.0
@export_range(0, 100) var damage: float = 10.0

# Onready (cached references)
@onready var sprite: Sprite2D = $Sprite2D
@onready var collision: CollisionShape2D = $CollisionShape2D

# Private variables
var _current_health: float

# Lifecycle
func _ready() -> void:
    _current_health = max_health

func _process(delta: float) -> void:
    pass

func _physics_process(delta: float) -> void:
    pass

# Public methods
func take_damage(amount: float) -> void:
    _current_health = maxf(0, _current_health - amount)
    health_changed.emit(_current_health)

# Private methods
func _on_something() -> void:
    pass
```

## Attaching Scripts

### To Existing Node
```python
mcp__gdai__attach_script(
    node_path="/root/Player",
    script_path="res://scripts/player/player_controller.gd"
)
```

## Export Patterns

### Basic Exports
```gdscript
@export var health: float = 100.0
@export var player_name: String = "Player"
@export var is_active: bool = true
```

### Ranged Values
```gdscript
@export_range(0, 100, 1) var percentage: int = 50
@export_range(0.0, 10.0, 0.1) var speed: float = 5.0
```

### Enums
```gdscript
enum State { IDLE, WALK, RUN, JUMP }
@export var current_state: State = State.IDLE
```

### Resources
```gdscript
@export var weapon_stats: Resource
@export var character_data: CharacterData  # Custom resource
```

### Node References
```gdscript
@export var target_node: Node2D
@export var spawn_points: Array[Marker2D]
```

## Common Patterns

### State Machine (Simple)
```gdscript
enum State { IDLE, MOVE, ATTACK, DEAD }
var _state: State = State.IDLE

func _physics_process(delta: float) -> void:
    match _state:
        State.IDLE:
            _process_idle(delta)
        State.MOVE:
            _process_move(delta)
        State.ATTACK:
            _process_attack(delta)
        State.DEAD:
            pass

func change_state(new_state: State) -> void:
    _state = new_state
```

### Singleton/Autoload Pattern
```gdscript
# res://autoload/game_manager.gd
extends Node

var score: int = 0
var is_paused: bool = false

func add_score(amount: int) -> void:
    score += amount

func pause_game() -> void:
    is_paused = true
    get_tree().paused = true
```

### Resource-Based Data
```gdscript
# res://resources/weapon_data.gd
class_name WeaponData
extends Resource

@export var weapon_name: String
@export var damage: float
@export var fire_rate: float
@export var icon: Texture2D
```

## Error Checking

### After Script Creation
```python
mcp__gdai__get_godot_errors()
# Check for parsing/syntax errors
```

### Common Errors
- Missing `extends` declaration
- Typo in node paths (@onready)
- Missing type hints causing runtime issues
- Signal not defined before emit

## Anti-Patterns to Avoid

- Using `$` paths without `@onready` caching
- Public variables instead of `@export`
- Hardcoded magic numbers (use exports)
- Long `_process` functions (delegate to methods)
- Not using type hints (hurts autocomplete & safety)
