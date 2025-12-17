# Strategy Game Template

> Specific guidance for strategy game development

## Genre Characteristics
- Decision-making focused
- Resource management
- Unit/asset control
- Planning and execution
- Often competitive (vs AI or players)

## Sub-genres
| Type | Timing | Example |
|------|--------|---------|
| Turn-based | Sequential turns | Civilization, XCOM |
| Real-time (RTS) | Continuous | StarCraft, Age of Empires |
| 4X | Explore, Expand, Exploit, Exterminate | Stellaris, Endless Legend |
| Tower Defense | Wave-based | BTD, Kingdom Rush |
| Auto-battler | Preparation + auto-combat | Teamfight Tactics |

## Core Systems Priority

### 1. Unit Control (Critical)
**Turn-based:**
- Selection
- Movement range
- Action points
- Turn order

**Real-time:**
- Selection (click, box)
- Commands (move, attack, stop)
- Formation
- Pathfinding

### 2. Resource System
- Income sources
- Resource types
- Spending (units, buildings, upgrades)
- Economy balance

### 3. Combat Resolution
**Turn-based:**
- Hit calculation
- Damage formula
- Cover/terrain modifiers
- Special abilities

**Real-time:**
- DPS calculations
- Range/targeting
- Unit counters
- Micro potential

### 4. AI Opponent
- Decision making
- Difficulty scaling
- Cheating vs playing fair
- Readable behavior

## Recommended Roadmap Order

```
1. Map/Grid System
2. Unit Placement
3. Unit Selection
4. Movement System
5. Basic Combat
6. Win/Lose Condition
7. Resources
8. Unit Production
9. AI Opponent (basic)
10. Balance Pass
```

## Unity Implementation Tips

### Grid System
```csharp
public class GridManager : MonoBehaviour
{
    [SerializeField] private int width = 10;
    [SerializeField] private int height = 10;
    [SerializeField] private float cellSize = 1f;

    private Cell[,] grid;

    public Cell GetCell(Vector3 worldPosition)
    {
        int x = Mathf.FloorToInt(worldPosition.x / cellSize);
        int y = Mathf.FloorToInt(worldPosition.z / cellSize);
        return grid[x, y];
    }

    public Vector3 GetWorldPosition(int x, int y)
    {
        return new Vector3(x * cellSize + cellSize/2, 0, y * cellSize + cellSize/2);
    }
}
```

### Unit Selection (RTS)
```csharp
public class SelectionManager : MonoBehaviour
{
    private List<Unit> selectedUnits = new();
    private Vector3 dragStart;
    private bool isDragging;

    private void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            dragStart = Input.mousePosition;
            isDragging = true;
        }

        if (Input.GetMouseButtonUp(0))
        {
            if (isDragging)
            {
                SelectUnitsInBox(dragStart, Input.mousePosition);
            }
            isDragging = false;
        }
    }
}
```

### Turn Manager
```csharp
public class TurnManager : MonoBehaviour
{
    public enum Phase { PlayerTurn, EnemyTurn }

    public Phase currentPhase;
    public int turnNumber = 1;

    public event Action<Phase> OnPhaseChanged;

    public void EndTurn()
    {
        currentPhase = currentPhase == Phase.PlayerTurn
            ? Phase.EnemyTurn
            : Phase.PlayerTurn;

        if (currentPhase == Phase.PlayerTurn)
            turnNumber++;

        OnPhaseChanged?.Invoke(currentPhase);
    }
}
```

### Common Pitfalls
- Pathfinding performance
- Unit stacking issues
- AI too easy or unfair
- Information overload
- Slow pacing
- Snowball effects

## Reference Games
- Into the Breach (turn-based, elegant)
- StarCraft (RTS, competitive)
- XCOM (turn-based, tactics)
- Civilization (4X, depth)
- Slay the Spire (strategy + roguelike)

## GDD Sections to Emphasize
- Unit roster and stats
- Resource economy
- Tech tree (if applicable)
- Victory conditions
- AI behavior rules

## Playtest Focus Areas
- [ ] Are decisions meaningful?
- [ ] Is information readable?
- [ ] Is AI challenging but fair?
- [ ] Is pacing appropriate?
- [ ] Are there viable strategies?
- [ ] Is snowballing controlled?
