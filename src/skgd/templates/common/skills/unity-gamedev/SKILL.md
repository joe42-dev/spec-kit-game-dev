---
name: unity-gamedev
description: Unity game development patterns and Unity MCP tool usage. Provides C# scripting templates, GameObject management, prefab workflows, scene operations, and testing patterns. Use when working with Unity, creating MonoBehaviours, managing GameObjects, prefabs, scenes, or running Unity tests.
---

# Unity Game Development Skill

## Quick Reference - Unity MCP Tools

### Script Operations
```
mcp__UnityMCP__create_script     → Create new C# scripts
mcp__UnityMCP__apply_text_edits  → Modify existing scripts
mcp__UnityMCP__validate_script   → Check for errors
mcp__UnityMCP__read_console      → Check compilation status
```

### GameObject Operations
```
mcp__UnityMCP__manage_gameobject → Create, modify, delete, find GameObjects
                                   add_component, remove_component
                                   set_component_property
```

### Scene & Prefab Operations
```
mcp__UnityMCP__manage_scene      → Create, load, save, get_hierarchy
mcp__UnityMCP__manage_prefabs    → Create, modify, delete prefabs
mcp__UnityMCP__manage_asset      → Asset CRUD operations
```

### Editor Control
```
mcp__UnityMCP__manage_editor     → play, pause, stop, get_state
mcp__UnityMCP__run_tests         → EditMode, PlayMode tests
```

## Implementation Patterns

### Pattern 1: Safe Script Creation
```
1. create_script → new script
2. read_console → check compilation
3. IF errors → fix with apply_text_edits
4. REPEAT until clean
```

### Pattern 2: GameObject with Components
```
1. manage_gameobject(create) → base object
2. manage_gameobject(add_component) → add components
3. manage_gameobject(set_component_property) → configure
4. manage_scene(save) → persist changes
```

### Pattern 3: Prefab Workflow
```
1. Create and configure GameObject
2. manage_prefabs(create, target=path) → save as prefab
3. For instances: manage_gameobject(create, prefab_path=...)
```

## Essential Anti-Patterns

- **NEVER** accumulate multiple scripts without checking console
- **NEVER** skip `manage_scene(save)` after significant changes
- **NEVER** assume compilation success without `read_console`
- **ALWAYS** check `manage_editor(get_state)` before operations

## Detailed References

For in-depth patterns, see:
- [reference/scripts.md](reference/scripts.md) - C# scripting patterns
- [reference/gameobjects.md](reference/gameobjects.md) - GameObject management
- [reference/prefabs.md](reference/prefabs.md) - Prefab workflows
- [reference/scenes.md](reference/scenes.md) - Scene operations
- [reference/testing.md](reference/testing.md) - Testing patterns

## Pre-Implementation Checklist

Before implementing:
- [ ] Verify Unity MCP connection: `manage_editor(get_state)`
- [ ] Check current scene: `manage_scene(get_active)`
- [ ] Clear console baseline: `read_console`

After each script:
- [ ] `read_console` - No compilation errors
- [ ] `manage_scene(save)` - Changes persisted
