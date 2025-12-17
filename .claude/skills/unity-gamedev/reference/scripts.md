# Unity C# Scripting Patterns

> **Token estimate:** ~250 tokens | **Last updated:** 2025-12

## Table of Contents
- [Creating Scripts](#creating-scripts) - MonoBehaviour templates, create_script usage
- [Modifying Scripts](#modifying-scripts) - apply_text_edits, script_apply_edits (safer)
- [Validation Flow](#validation-flow) - Compile check loop, validate_script
- [Common Patterns](#common-patterns) - SerializeField, Events, Singleton
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid) - What NOT to do

---

## Creating Scripts

### Basic MonoBehaviour
```csharp
// Path: Assets/Scripts/[Feature]/[Name].cs
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField] private float moveSpeed = 5f;

    private void Update()
    {
        // Implementation
    }
}
```

### Tool Usage: create_script
```python
mcp__UnityMCP__create_script(
    path="Assets/Scripts/Player/PlayerController.cs",
    contents=script_content  # Base64 encoded
)
```

## Modifying Scripts

### Tool Usage: apply_text_edits
```python
mcp__UnityMCP__apply_text_edits(
    uri="Assets/Scripts/Player/PlayerController.cs",
    edits=[{
        "startLine": 10,
        "startCol": 1,
        "endLine": 15,
        "endCol": 1,
        "newText": "new code here"
    }]
)
```

### Safer: script_apply_edits (structured)
```python
mcp__UnityMCP__script_apply_edits(
    name="PlayerController",
    path="Assets/Scripts/Player",
    edits=[{
        "op": "replace_method",
        "className": "PlayerController",
        "methodName": "Update",
        "replacement": "private void Update() { /* new impl */ }"
    }]
)
```

## Validation Flow

### After Every Script Change
```
1. read_console(types=["error", "warning"])
2. IF errors:
   - Parse error message
   - Locate line/column
   - apply_text_edits to fix
   - GOTO 1
3. ELSE: proceed
```

### Validation Script Check
```python
mcp__UnityMCP__validate_script(
    uri="Assets/Scripts/Player/PlayerController.cs",
    level="standard",
    include_diagnostics=True
)
```

## Common Patterns

### SerializeField with Validation
```csharp
[SerializeField, Range(0f, 100f)]
private float health = 100f;

[SerializeField, Min(0f)]
private float damage = 10f;
```

### Event-Based Communication
```csharp
public event System.Action<float> OnHealthChanged;

private void TakeDamage(float amount)
{
    health -= amount;
    OnHealthChanged?.Invoke(health);
}
```

### Singleton Pattern (Simple)
```csharp
public static GameManager Instance { get; private set; }

private void Awake()
{
    if (Instance != null && Instance != this)
    {
        Destroy(gameObject);
        return;
    }
    Instance = this;
}
```

## Anti-Patterns to Avoid

- `public` fields instead of `[SerializeField] private`
- Magic numbers without constants or SerializeField
- Update() polling when events would work
- GetComponent() in Update() (cache in Awake/Start)
- Hardcoded paths/tags (use constants or ScriptableObjects)
