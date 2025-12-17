# Unity Testing Patterns

## Running Tests

### EditMode Tests
```python
mcp__UnityMCP__run_tests(mode="EditMode")
```
- Run without entering Play mode
- Fast, for pure logic tests
- No MonoBehaviour lifecycle

### PlayMode Tests
```python
mcp__UnityMCP__run_tests(mode="PlayMode")
```
- Run in Play mode context
- Test MonoBehaviour lifecycle
- Can test coroutines, physics

### With Timeout
```python
mcp__UnityMCP__run_tests(
    mode="EditMode",
    timeout_seconds=30
)
```

## Console Monitoring

### Check for Errors
```python
mcp__UnityMCP__read_console(types=["error"])
```

### Check All Messages
```python
mcp__UnityMCP__read_console(
    types=["error", "warning", "log"],
    count=20
)
```

### With Stacktrace
```python
mcp__UnityMCP__read_console(
    types=["error"],
    include_stacktrace=True
)
```

### Detailed Format
```python
mcp__UnityMCP__read_console(
    format="detailed",
    types=["error", "warning"]
)
```

### Clear Console
```python
mcp__UnityMCP__read_console(action="clear")
```

## Editor Play Control

### Enter Play Mode
```python
mcp__UnityMCP__manage_editor(action="play")
```

### Pause
```python
mcp__UnityMCP__manage_editor(action="pause")
```

### Stop Play Mode
```python
mcp__UnityMCP__manage_editor(action="stop")
```

### Get Editor State
```python
mcp__UnityMCP__manage_editor(action="get_state")
# Returns: isPlaying, isPaused, isCompiling
```

## Test-Implement Cycle

### Standard Validation Flow
```python
# After script changes:

# 1. Clear console baseline
mcp__UnityMCP__read_console(action="clear")

# 2. Wait for compilation (check state)
mcp__UnityMCP__manage_editor(action="get_state")
# Check: isCompiling == False

# 3. Check compilation result
errors = mcp__UnityMCP__read_console(types=["error"])

# 4. If clean, run tests
if not errors:
    mcp__UnityMCP__run_tests(mode="EditMode")
```

### Quick Play Test
```python
# 1. Save scene first
mcp__UnityMCP__manage_scene(action="save")

# 2. Enter play mode
mcp__UnityMCP__manage_editor(action="play")

# 3. Wait and check console
import time
time.sleep(2)  # Let game run briefly
mcp__UnityMCP__read_console(types=["error", "warning"])

# 4. Stop
mcp__UnityMCP__manage_editor(action="stop")
```

## Writing Test Scripts

### EditMode Test Template
```csharp
using NUnit.Framework;

public class PlayerTests
{
    [Test]
    public void Health_TakeDamage_ReducesHealth()
    {
        // Arrange
        var health = new HealthSystem(100f);

        // Act
        health.TakeDamage(30f);

        // Assert
        Assert.AreEqual(70f, health.CurrentHealth);
    }

    [Test]
    public void Health_TakeDamage_NeverGoesBelowZero()
    {
        var health = new HealthSystem(50f);

        health.TakeDamage(100f);

        Assert.AreEqual(0f, health.CurrentHealth);
    }
}
```

### PlayMode Test Template
```csharp
using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class PlayerMovementTests
{
    [UnityTest]
    public IEnumerator Player_Move_ChangesPosition()
    {
        // Arrange
        var playerGO = new GameObject("Player");
        var controller = playerGO.AddComponent<PlayerController>();
        var startPos = playerGO.transform.position;

        // Act
        controller.Move(Vector3.forward);
        yield return new WaitForSeconds(0.1f);

        // Assert
        Assert.AreNotEqual(startPos, playerGO.transform.position);

        // Cleanup
        Object.Destroy(playerGO);
    }
}
```

## Test Organization

### Folder Structure
```
Assets/
└── Tests/
    ├── EditMode/
    │   ├── EditMode.asmdef
    │   ├── HealthTests.cs
    │   └── InventoryTests.cs
    └── PlayMode/
        ├── PlayMode.asmdef
        ├── PlayerMovementTests.cs
        └── EnemyAITests.cs
```

### Assembly Definition (EditMode.asmdef)
```json
{
    "name": "EditModeTests",
    "references": ["UnityEngine.TestRunner", "UnityEditor.TestRunner"],
    "includePlatforms": ["Editor"],
    "optionalUnityReferences": ["TestAssemblies"]
}
```

## Debugging Patterns

### Console Error Analysis
```python
# Get detailed error info
errors = mcp__UnityMCP__read_console(
    types=["error"],
    include_stacktrace=True,
    format="detailed"
)

# Parse and locate issue
for error in errors:
    # error contains: message, stacktrace, timestamp
    pass
```

### Runtime State Check
```python
# During play mode
mcp__UnityMCP__manage_gameobject(
    action="find",
    search_method="by_name",
    search_term="Player"
)

mcp__UnityMCP__manage_gameobject(
    action="get_components",
    target="Player"
)
```

## Validation Checklist

### Before Marking Feature Complete
- [ ] No compilation errors (`read_console`)
- [ ] EditMode tests pass (`run_tests EditMode`)
- [ ] PlayMode tests pass (`run_tests PlayMode`)
- [ ] No runtime errors in console
- [ ] No warnings that indicate bugs
- [ ] Scene saved (`manage_scene save`)

## Anti-Patterns

- Skipping console check after script changes
- Not writing tests for game logic
- Testing in Play mode without saving scene first
- Ignoring warnings (they often indicate real issues)
- Not clearing console before testing (old errors confuse)
