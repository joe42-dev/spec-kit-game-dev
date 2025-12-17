# Unity Prefab Workflow Patterns

## Creating Prefabs

### From Existing GameObject
```python
# First create and configure the GameObject
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="EnemyBase",
    components_to_add=["Rigidbody", "CapsuleCollider"]
)

# Then save as prefab
mcp__UnityMCP__manage_prefabs(
    action="create",
    target="EnemyBase",
    prefab_path="Assets/Prefabs/Enemies/EnemyBase.prefab"
)
```

### With Overwrite Protection
```python
mcp__UnityMCP__manage_prefabs(
    action="create",
    target="Player",
    prefab_path="Assets/Prefabs/Player.prefab",
    allow_overwrite=False  # Fail if exists
)
```

## Instantiating Prefabs

### Create Instance in Scene
```python
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="Enemy_01",
    prefab_path="Assets/Prefabs/Enemies/EnemyBase.prefab",
    position=[10, 0, 5]
)
```

### Multiple Instances
```python
for i, pos in enumerate(spawn_positions):
    mcp__UnityMCP__manage_gameobject(
        action="create",
        name=f"Enemy_{i:02d}",
        prefab_path="Assets/Prefabs/Enemies/EnemyBase.prefab",
        position=pos
    )
```

## Modifying Prefabs

### Edit Prefab Asset
```python
mcp__UnityMCP__manage_prefabs(
    action="modify",
    prefab_path="Assets/Prefabs/Player.prefab",
    component_properties='{"Rigidbody": {"mass": 3.0}}'
)
```

### Get Prefab Components
```python
mcp__UnityMCP__manage_prefabs(
    action="get_components",
    prefab_path="Assets/Prefabs/Player.prefab"
)
```

## Prefab Organization

### Recommended Folder Structure
```
Assets/
└── Prefabs/
    ├── Characters/
    │   ├── Player.prefab
    │   └── NPCs/
    │       ├── Villager.prefab
    │       └── Merchant.prefab
    ├── Enemies/
    │   ├── EnemyBase.prefab
    │   └── Variants/
    │       ├── FastEnemy.prefab
    │       └── TankEnemy.prefab
    ├── Environment/
    │   ├── Props/
    │   ├── Obstacles/
    │   └── Interactables/
    ├── VFX/
    │   └── Particles/
    └── UI/
        └── Widgets/
```

## Prefab Variants Pattern

### Base Prefab
```python
# Create base enemy
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="EnemyBase",
    components_to_add=["EnemyAI", "Health"]
)

mcp__UnityMCP__manage_prefabs(
    action="create",
    target="EnemyBase",
    prefab_path="Assets/Prefabs/Enemies/EnemyBase.prefab"
)
```

### Variant (Manual for now)
Create variant by:
1. Instantiate base prefab
2. Modify properties
3. Save as new prefab with reference to base

## Complete Workflow Example

### Creating a Player Prefab
```python
# Step 1: Create base GameObject
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="Player",
    primitive_type="Capsule",
    position=[0, 1, 0]
)

# Step 2: Add components
mcp__UnityMCP__manage_gameobject(
    action="add_component",
    target="Player",
    component_name="CharacterController"
)

# Step 3: Configure components
mcp__UnityMCP__manage_gameobject(
    action="set_component_property",
    target="Player",
    component_properties={
        "CharacterController": {
            "height": 2.0,
            "radius": 0.5
        }
    }
)

# Step 4: Add child objects
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="CameraTarget",
    parent="Player",
    position=[0, 1.5, 0]
)

# Step 5: Save as prefab
mcp__UnityMCP__manage_prefabs(
    action="create",
    target="Player",
    prefab_path="Assets/Prefabs/Characters/Player.prefab"
)

# Step 6: Verify
mcp__UnityMCP__manage_prefabs(
    action="get_components",
    prefab_path="Assets/Prefabs/Characters/Player.prefab"
)
```

## Anti-Patterns

- Prefabs with scene-specific references (use interfaces/events)
- Overly deep prefab hierarchies
- Not using prefab variants for similar objects
- Hardcoded values instead of SerializeField
