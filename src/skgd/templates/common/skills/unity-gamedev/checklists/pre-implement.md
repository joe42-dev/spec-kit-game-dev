# Pre-Implementation Checklist for Unity

## Before Starting Any Implementation

### Environment Verification
- [ ] Unity MCP connection active
  ```python
  mcp__UnityMCP__manage_editor(action="get_state")
  # Expect: successful response with isPlaying, isCompiling
  ```

- [ ] Correct scene loaded
  ```python
  mcp__UnityMCP__manage_scene(action="get_active")
  # Verify name matches expected scene
  ```

- [ ] Console is clean (or note existing issues)
  ```python
  mcp__UnityMCP__read_console(types=["error"])
  # Document any pre-existing errors
  ```

- [ ] Not in Play mode
  ```python
  # Check get_state response: isPlaying should be False
  ```

### Documentation Check
- [ ] Spec exists and is reviewed (`docs/specs/[feature]/spec.md`)
- [ ] Plan exists and is reviewed (`docs/specs/[feature]/plan.md`)
- [ ] Tasks are clear (`docs/specs/[feature]/tasks.md`)

### Folder Verification
- [ ] Target script folder exists
  ```python
  mcp__UnityMCP__manage_asset(
      action="search",
      path="Assets/Scripts",
      search_pattern="*"
  )
  ```

- [ ] Prefab folder exists (if creating prefabs)
  ```python
  mcp__UnityMCP__manage_asset(
      action="get_info",
      path="Assets/Prefabs"
  )
  ```

## During Implementation

### After Each Script Creation
- [ ] Check compilation
  ```python
  mcp__UnityMCP__read_console(types=["error", "warning"])
  ```
- [ ] Fix any errors before proceeding
- [ ] Save scene if GameObject changes made

### After Adding Components
- [ ] Verify component added
  ```python
  mcp__UnityMCP__manage_gameobject(
      action="get_components",
      target="ObjectName"
  )
  ```
- [ ] Configure required properties
- [ ] Save scene

### After Prefab Operations
- [ ] Verify prefab created/modified
  ```python
  mcp__UnityMCP__manage_prefabs(
      action="get_components",
      prefab_path="Assets/Prefabs/..."
  )
  ```

## Before Marking Task Complete

### Validation Steps
- [ ] No compilation errors
- [ ] No runtime errors (quick play test)
- [ ] Scene saved
- [ ] All tasks in tasks.md checked

### Quick Test
```python
# 1. Save scene
mcp__UnityMCP__manage_scene(action="save")

# 2. Clear console
mcp__UnityMCP__read_console(action="clear")

# 3. Play briefly
mcp__UnityMCP__manage_editor(action="play")

# 4. Wait ~2 seconds, then check
mcp__UnityMCP__read_console(types=["error"])

# 5. Stop
mcp__UnityMCP__manage_editor(action="stop")
```

## Common Issues to Watch For

### Compilation Errors
- Missing `using` statements
- Typos in component/class names
- Incorrect access modifiers
- Missing semicolons

### Runtime Errors
- NullReferenceException (check GetComponent calls)
- Missing component dependencies
- Unassigned SerializeField references

### Scene Issues
- Unsaved changes
- Missing essential objects (camera, light)
- Incorrect layer/tag assignments
