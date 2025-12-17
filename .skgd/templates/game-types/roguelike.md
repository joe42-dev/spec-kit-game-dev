# Roguelike Game Template

> Specific guidance for roguelike/roguelite development

## Genre Characteristics
- Procedural generation
- Permadeath (or soft permadeath)
- Run-based structure
- High replayability
- Often includes meta-progression

## Roguelike vs Roguelite
| Feature | Roguelike | Roguelite |
|---------|-----------|-----------|
| Death | Full reset | Some persistence |
| Progression | Within run only | Meta-progression |
| Example | Nethack, DCSS | Hades, Dead Cells |

## Core Systems Priority

### 1. Procedural Generation (Critical)
**Approaches:**
| Method | Complexity | Control |
|--------|------------|---------|
| Random placement | Low | Low |
| Templated rooms | Medium | High |
| Wave Function Collapse | High | Medium |
| BSP dungeons | Medium | Medium |

**Key Decisions:**
- What is generated? (levels, enemies, items)
- Seed-based or pure random?
- How much handcrafted content?

### 2. Permadeath System
- Clear death state
- Run summary
- Immediate restart
- Meta-progression hooks

### 3. Item/Power-up System
- Random item drops
- Synergies between items
- Build variety
- Risk/reward choices

### 4. Meta-Progression (Roguelite)
- Persistent currency
- Permanent unlocks
- Starting options
- Narrative hooks

## Recommended Roadmap Order

```
1. Core Gameplay Loop (combat or action)
2. Simple Room Generation
3. Health/Death System
4. Basic Items/Power-ups
5. Room Transitions
6. Enemy Variety
7. Boss Encounter
8. Run Structure (floors)
9. Meta-Progression
10. Item Synergies
```

## Unity Implementation Tips

### Simple Room Generation
```csharp
public class DungeonGenerator : MonoBehaviour
{
    [SerializeField] private GameObject[] roomPrefabs;
    [SerializeField] private int roomCount = 10;

    private List<Room> rooms = new List<Room>();

    public void Generate(int seed)
    {
        Random.InitState(seed);
        // Generate room layout
        // Connect rooms
        // Place enemies
        // Place items
    }
}
```

### Run Manager Pattern
```csharp
public class RunManager : MonoBehaviour
{
    public static RunManager Instance;

    public int currentFloor;
    public int gold;
    public List<Item> collectedItems;
    public float runTime;

    public void StartNewRun()
    {
        currentFloor = 1;
        gold = 0;
        collectedItems.Clear();
        runTime = 0;
    }

    public void EndRun(bool victory)
    {
        // Save meta-progression
        // Show run summary
        // Return to hub
    }
}
```

### Item System
```csharp
[CreateAssetMenu(menuName = "Roguelike/Item")]
public class ItemData : ScriptableObject
{
    public string itemName;
    public Sprite icon;
    public Rarity rarity;
    public ItemEffect[] effects;
    public string[] synergizesWith;
}
```

### Common Pitfalls
- Too random (no control)
- Boring builds (no synergies)
- Runs too long or too short
- Unfair deaths
- Slow meta-progression

## Reference Games
- Hades (meta-progression, narrative)
- Slay the Spire (deckbuilding roguelite)
- Dead Cells (action roguelite)
- Spelunky (pure roguelike, level gen)
- Risk of Rain (item stacking)

## GDD Sections to Emphasize
- Generation algorithm
- Item pool design
- Synergy system
- Meta-progression curve
- Run structure

## Playtest Focus Areas
- [ ] Is each run different enough?
- [ ] Are item choices interesting?
- [ ] Is death frustrating or motivating?
- [ ] Is meta-progression satisfying?
- [ ] Are synergies discoverable?
- [ ] Is run length appropriate?

## Balance Considerations
- Item drop rates by rarity
- Power curve through run
- Meta-progression pacing
- Boss difficulty scaling
- Starting vs unlocked power
