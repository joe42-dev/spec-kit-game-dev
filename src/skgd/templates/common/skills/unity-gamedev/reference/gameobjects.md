# Unity GameObject Management Patterns

## Creating GameObjects

### Empty GameObject
```python
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="Player",
    position=[0, 0, 0],
    rotation=[0, 0, 0],
    scale=[1, 1, 1]
)
```

### Primitive GameObject
```python
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="Ground",
    primitive_type="Cube",
    position=[0, -1, 0],
    scale=[10, 1, 10]
)
```
**Primitive types**: Cube, Sphere, Capsule, Cylinder, Plane, Quad

### With Parent
```python
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="Weapon",
    parent="Player/Hand"  # Path in hierarchy
)
```

## Adding Components

### Single Component
```python
mcp__UnityMCP__manage_gameobject(
    action="add_component",
    target="Player",
    component_name="Rigidbody"
)
```

### Multiple Components at Creation
```python
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="Player",
    components_to_add=["CharacterController", "AudioSource"]
)
```

## Configuring Components

### Set Component Property
```python
mcp__UnityMCP__manage_gameobject(
    action="set_component_property",
    target="Player",
    component_properties={
        "Rigidbody": {
            "mass": 2.0,
            "useGravity": True,
            "isKinematic": False
        }
    }
)
```

### Common Component Configurations

**CharacterController**:
```python
component_properties={
    "CharacterController": {
        "height": 2.0,
        "radius": 0.5,
        "center": [0, 1, 0]
    }
}
```

**BoxCollider**:
```python
component_properties={
    "BoxCollider": {
        "isTrigger": True,
        "size": [2, 2, 2],
        "center": [0, 1, 0]
    }
}
```

## Finding GameObjects

### By Name
```python
mcp__UnityMCP__manage_gameobject(
    action="find",
    search_method="by_name",
    search_term="Player"
)
```

### By Tag
```python
mcp__UnityMCP__manage_gameobject(
    action="find",
    search_method="by_tag",
    search_term="Enemy",
    find_all=True  # Find all with this tag
)
```

### By Component
```python
mcp__UnityMCP__manage_gameobject(
    action="find",
    search_method="by_component",
    search_term="PlayerController"
)
```

### Search Options
- `find_all`: Return all matches (default: first only)
- `search_inactive`: Include inactive GameObjects
- `search_in_children`: Search in children of target

## Modifying GameObjects

### Transform
```python
mcp__UnityMCP__manage_gameobject(
    action="modify",
    target="Player",
    position=[5, 0, 3],
    rotation=[0, 90, 0]
)
```

### Active State
```python
mcp__UnityMCP__manage_gameobject(
    action="modify",
    target="Enemy",
    set_active=False
)
```

### Tags and Layers
```python
mcp__UnityMCP__manage_gameobject(
    action="modify",
    target="Player",
    tag="Player",
    layer="Characters"
)
```

## Getting Component Info

```python
mcp__UnityMCP__manage_gameobject(
    action="get_components",
    target="Player",
    includeNonPublicSerialized=True
)
```

## Hierarchy Patterns

### Standard Player Setup
```
Player (CharacterController, PlayerController)
├── CameraTarget (empty, camera follows this)
├── Model (mesh, animator)
│   └── Weapon (weapon mesh)
└── GroundCheck (trigger collider)
```

### Standard Enemy Setup
```
Enemy (NavMeshAgent, EnemyAI)
├── Model (mesh, animator)
├── DetectionZone (SphereCollider trigger)
└── AttackPoint (empty, spawn point for attacks)
```

## Anti-Patterns

- Creating GameObjects without proper naming
- Deep nesting (prefer flat hierarchies)
- Mixing gameplay and visual objects at same level
- Not setting tags/layers for objects that need them
