# Godot Signal Patterns

## Signal Basics

### Declaring Signals
```gdscript
# Simple signal
signal died

# Signal with parameters
signal health_changed(new_health: float)
signal damage_taken(amount: float, source: Node)
```

### Emitting Signals
```gdscript
# Simple emit
died.emit()

# With parameters
health_changed.emit(current_health)
damage_taken.emit(10.0, attacker)
```

### Connecting Signals

**In Code (Recommended):**
```gdscript
func _ready() -> void:
    # Connect to own signal
    health_changed.connect(_on_health_changed)

    # Connect to child's signal
    $Button.pressed.connect(_on_button_pressed)

    # Connect to another node's signal
    player.died.connect(_on_player_died)

func _on_health_changed(new_health: float) -> void:
    print("Health is now: ", new_health)
```

**With Callable:**
```gdscript
# One-shot connection (auto-disconnects after first call)
enemy.died.connect(_on_enemy_died, CONNECT_ONE_SHOT)

# Deferred (called at end of frame)
button.pressed.connect(_on_button_pressed, CONNECT_DEFERRED)
```

## Common Signal Patterns

### Health System
```gdscript
class_name HealthComponent
extends Node

signal health_changed(current: float, maximum: float)
signal damaged(amount: float)
signal healed(amount: float)
signal died

@export var max_health: float = 100.0
var _current_health: float

func _ready() -> void:
    _current_health = max_health

func take_damage(amount: float) -> void:
    var actual_damage = minf(amount, _current_health)
    _current_health -= actual_damage
    damaged.emit(actual_damage)
    health_changed.emit(_current_health, max_health)

    if _current_health <= 0:
        died.emit()

func heal(amount: float) -> void:
    var actual_heal = minf(amount, max_health - _current_health)
    _current_health += actual_heal
    healed.emit(actual_heal)
    health_changed.emit(_current_health, max_health)
```

### State Machine Events
```gdscript
class_name StateMachine
extends Node

signal state_changed(old_state: String, new_state: String)

var _current_state: String = ""

func change_state(new_state: String) -> void:
    var old_state = _current_state
    _current_state = new_state
    state_changed.emit(old_state, new_state)
```

### UI Binding
```gdscript
# In Player script
signal score_changed(new_score: int)

func add_score(amount: int) -> void:
    score += amount
    score_changed.emit(score)

# In HUD script
func _ready() -> void:
    var player = get_tree().get_first_node_in_group("player")
    player.score_changed.connect(_on_score_changed)

func _on_score_changed(new_score: int) -> void:
    $ScoreLabel.text = "Score: %d" % new_score
```

### Event Bus (Global Signals)

**Autoload Pattern:**
```gdscript
# res://autoload/events.gd
extends Node

# Game flow
signal game_started
signal game_paused
signal game_over

# Player events
signal player_spawned(player: Node)
signal player_died

# UI events
signal show_dialog(text: String)
signal close_all_menus
```

**Usage:**
```gdscript
# Emitting global event
Events.player_died.emit()

# Listening to global event
func _ready() -> void:
    Events.player_died.connect(_on_player_died)
```

## Built-in Signals

### Common Node Signals

**Area2D:**
```gdscript
area_entered.connect(_on_area_entered)      # Area2D enters
area_exited.connect(_on_area_exited)        # Area2D exits
body_entered.connect(_on_body_entered)      # PhysicsBody enters
body_exited.connect(_on_body_exited)        # PhysicsBody exits
```

**Button:**
```gdscript
pressed.connect(_on_pressed)
button_down.connect(_on_button_down)
button_up.connect(_on_button_up)
```

**Timer:**
```gdscript
timeout.connect(_on_timeout)
```

**AnimationPlayer:**
```gdscript
animation_finished.connect(_on_animation_finished)
```

**Visibility:**
```gdscript
visibility_changed.connect(_on_visibility_changed)
```

## Connection Patterns

### Dynamic Connections
```gdscript
# Connect when spawning
func spawn_enemy(enemy: Node) -> void:
    add_child(enemy)
    enemy.died.connect(_on_enemy_died.bind(enemy))

func _on_enemy_died(enemy: Node) -> void:
    enemies_killed += 1
    enemy.queue_free()
```

### Disconnecting
```gdscript
# Manual disconnect
player.health_changed.disconnect(_on_health_changed)

# Check if connected
if player.health_changed.is_connected(_on_health_changed):
    player.health_changed.disconnect(_on_health_changed)
```

### Lambda/Anonymous Functions
```gdscript
# Quick one-liner
button.pressed.connect(func(): print("Button pressed!"))

# With cleanup
timer.timeout.connect(func():
    spawn_wave()
    timer.queue_free()
)
```

## Signal vs Direct Call

### Use Signals When:
- Sender doesn't need to know about receivers
- Multiple listeners possible
- Loose coupling desired
- Event-driven communication

### Use Direct Calls When:
- Direct parent-child relationship
- Performance critical (signals have slight overhead)
- Need return value
- Single known receiver

## Anti-Patterns

- Overusing signals for simple parent-child communication
- Not disconnecting signals when nodes are freed (memory leaks)
- Circular signal dependencies
- Using signals for synchronous operations that need return values
- Not using typed parameters in signal declarations
