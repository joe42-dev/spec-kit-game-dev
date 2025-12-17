# Pre-Implementation Checklist for Godot

## Before Starting Any Implementation

### Environment Verification
- [ ] GDAI MCP connection active
  ```python
  mcp__gdai__get_project_info()
  # Expect: project name, path, version info
  ```

- [ ] Check for existing errors
  ```python
  mcp__gdai__get_godot_errors()
  # Document any pre-existing errors
  ```

- [ ] No scene currently running
  ```python
  mcp__gdai__stop_running_scene()  # Safe to call even if nothing running
  ```

### Documentation Check
- [ ] Spec exists and is reviewed (`docs/specs/[feature]/spec.md`)
- [ ] Plan exists and is reviewed (`docs/specs/[feature]/plan.md`)
- [ ] Tasks are clear (`docs/specs/[feature]/tasks.md`)

## During Implementation

### After Each Script Creation
- [ ] Check for parse errors
  ```python
  mcp__gdai__get_godot_errors()
  ```
- [ ] Fix any errors before proceeding
- [ ] Attach to node if applicable

### After Adding Nodes
- [ ] Verify node hierarchy
  ```python
  mcp__gdai__open_scene(scene_path="...")
  # Visual verification in editor
  ```
- [ ] Configure required properties
  ```python
  mcp__gdai__update_property(...)
  ```

### After Scene Changes
- [ ] Test with play_scene
  ```python
  mcp__gdai__play_scene(scene_path="...")
  ```
- [ ] Visual check
  ```python
  mcp__gdai__get_running_scene_screenshot()
  ```
- [ ] Stop scene
  ```python
  mcp__gdai__stop_running_scene()
  ```
- [ ] Check runtime errors
  ```python
  mcp__gdai__get_godot_errors()
  ```

## Before Marking Task Complete

### Validation Steps
- [ ] No parse errors
- [ ] No runtime errors (play test)
- [ ] Scene runs without crashes
- [ ] All tasks in tasks.md checked

### Quick Test
```python
# 1. Check errors baseline
mcp__gdai__get_godot_errors()

# 2. Run scene
mcp__gdai__play_scene(scene_path="res://scenes/test_scene.tscn")

# 3. Visual check
mcp__gdai__get_running_scene_screenshot()

# 4. Stop
mcp__gdai__stop_running_scene()

# 5. Check for runtime errors
mcp__gdai__get_godot_errors()
```

## Common Issues to Watch For

### Parse Errors
- Missing colons after function declarations
- Incorrect indentation (GDScript is whitespace-sensitive)
- Missing type hints (not errors but warnings)
- Typos in node paths

### Runtime Errors
- Node not found (invalid path)
- Null reference (node not ready yet)
- Signal not connected properly
- Missing exports not set in editor

### Scene Issues
- Missing collision shapes on physics bodies
- Incorrect collision layers/masks
- Script not attached to node
- Node paths hardcoded and broken

## Godot-Specific Considerations

### Scene Dependencies
- [ ] All instanced scenes exist
- [ ] All preload() paths are valid
- [ ] Autoloads are configured in Project Settings

### Resources
- [ ] All @export resources have defaults or are set
- [ ] PackedScene exports point to valid .tscn files
- [ ] Texture/Audio resources exist at specified paths

### Groups & Layers
- [ ] Collision layers match design (player=1, enemies=2, etc.)
- [ ] Nodes added to correct groups ("player", "enemies", etc.)
