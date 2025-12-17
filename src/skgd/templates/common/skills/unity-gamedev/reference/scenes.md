# Unity Scene Management Patterns

## Scene Operations

### Get Current Scene Info
```python
mcp__UnityMCP__manage_scene(action="get_active")
# Returns: name, path, isDirty, rootCount
```

### Get Scene Hierarchy
```python
mcp__UnityMCP__manage_scene(action="get_hierarchy")
# Returns full tree of GameObjects
```

### Save Current Scene
```python
mcp__UnityMCP__manage_scene(action="save")
```

### Create New Scene
```python
mcp__UnityMCP__manage_scene(
    action="create",
    name="Level_01"
)
```

### Load Scene
```python
mcp__UnityMCP__manage_scene(
    action="load",
    path="Assets/Scenes/Level_01.unity"
)

# Or by build index
mcp__UnityMCP__manage_scene(
    action="load",
    build_index=1
)
```

### Get Build Settings
```python
mcp__UnityMCP__manage_scene(action="get_build_settings")
# Returns list of scenes in build
```

## Essential Scene Setup

### Minimum Scene Requirements
Every playable scene needs:
1. **Main Camera** (tag: MainCamera)
2. **Directional Light** (Sun)
3. **EventSystem** (for UI)

### Basic Scene Setup Pattern
```python
# 1. Create new scene
mcp__UnityMCP__manage_scene(action="create", name="GameScene")

# 2. Add Camera
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="Main Camera",
    tag="MainCamera",
    components_to_add=["Camera", "AudioListener"],
    position=[0, 5, -10],
    rotation=[30, 0, 0]
)

# 3. Add Directional Light
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="Directional Light",
    components_to_add=["Light"],
    rotation=[50, -30, 0]
)
mcp__UnityMCP__manage_gameobject(
    action="set_component_property",
    target="Directional Light",
    component_properties={
        "Light": {"type": 1}  # Directional
    }
)

# 4. Add EventSystem (for UI)
mcp__UnityMCP__manage_gameobject(
    action="create",
    name="EventSystem",
    components_to_add=["EventSystem", "StandaloneInputModule"]
)

# 5. Save
mcp__UnityMCP__manage_scene(action="save")
```

## Scene Organization

### Recommended Hierarchy Structure
```
Scene Root
├── --- ENVIRONMENT ---
├── Ground
├── Props
│   └── [prop objects]
├── --- GAMEPLAY ---
├── Player
├── Enemies
│   └── [enemy instances]
├── Spawners
│   └── [spawn points]
├── --- SYSTEMS ---
├── GameManager
├── AudioManager
├── --- UI ---
├── Canvas
│   └── [UI elements]
└── EventSystem
```

### Using Empty GameObjects as Organizers
```python
# Create organization objects
for category in ["--- ENVIRONMENT ---", "--- GAMEPLAY ---", "--- SYSTEMS ---", "--- UI ---"]:
    mcp__UnityMCP__manage_gameobject(
        action="create",
        name=category
    )
```

## Scene Workflow Patterns

### Pattern 1: Safe Scene Work
```
1. manage_scene(get_active) → verify correct scene
2. [make changes]
3. manage_scene(save) → persist
4. read_console → check for issues
```

### Pattern 2: Scene Setup from Scratch
```
1. manage_scene(create, name="NewScene")
2. Add essential objects (camera, light, eventsystem)
3. Add gameplay objects
4. manage_scene(save)
5. Verify with manage_scene(get_hierarchy)
```

### Pattern 3: Scene Modification
```
1. manage_scene(load, path="...")
2. manage_scene(get_hierarchy) → understand structure
3. [modify objects]
4. manage_scene(save)
```

## Multi-Scene Patterns

### Scene Types
- **Persistent Scene**: Managers, audio, UI (never unloaded)
- **Level Scenes**: Gameplay content (loaded/unloaded)
- **Additive Loading**: Multiple scenes active simultaneously

### Folder Structure
```
Assets/
└── Scenes/
    ├── _Boot.unity          # Entry point, loads persistent
    ├── _Persistent.unity    # Managers (additive)
    ├── Menus/
    │   ├── MainMenu.unity
    │   └── PauseMenu.unity
    └── Levels/
        ├── Level_01.unity
        ├── Level_02.unity
        └── Level_Debug.unity
```

## Save Frequency Guidelines

**ALWAYS save after:**
- Creating/deleting GameObjects
- Adding/removing components
- Modifying transform significantly
- Before testing in Play mode
- After successful compilation check

**Pattern:**
```python
# After any significant operation
mcp__UnityMCP__manage_scene(action="save")
mcp__UnityMCP__read_console(types=["error"])  # Verify clean
```

## Anti-Patterns

- Not saving before Play mode (changes lost)
- Disorganized hierarchy (use separators/folders)
- Scene-specific scripts with hardcoded references
- Missing essential objects (camera, light, eventsystem)
- Not checking scene state before operations
