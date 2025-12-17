# RPG Game Template

> Specific guidance for RPG game development

## Genre Characteristics
- Character progression (stats, abilities)
- Story/narrative elements
- Combat system
- Inventory/equipment
- Often includes exploration

## Core Systems Priority

### 1. Character Stats System (Critical)
**Core Stats:**
| Stat | Purpose | Typical Range |
|------|---------|---------------|
| Health | Survivability | 10-1000+ |
| Attack | Damage output | 1-100+ |
| Defense | Damage reduction | 0-50+ |
| Speed | Turn order/movement | 1-100 |

**Derived Stats:**
- Damage = Attack - Defense (clamped)
- Crit Chance = (Luck / 100)
- Dodge = Speed / 200

### 2. Combat System
**Turn-based:**
- Action selection
- Turn order calculation
- Action execution
- State management

**Real-time:**
- Input handling
- Cooldown management
- Target acquisition
- Damage calculation

### 3. Progression System
- Experience points
- Level up
- Stat increases
- Ability unlocks

### 4. Inventory System
- Item storage
- Equipment slots
- Item effects
- Stack management

## Recommended Roadmap Order

```
1. Character Stats (data structure)
2. Basic Combat (one enemy, basic attack)
3. Health/Damage System
4. Level Up System
5. Simple Inventory
6. Equipment Effects
7. Multiple Abilities
8. Enemy Variety
9. Loot/Rewards
10. Save System
```

## Unity Implementation Tips

### ScriptableObject Data Pattern
```csharp
[CreateAssetMenu(menuName = "RPG/Character Stats")]
public class CharacterStats : ScriptableObject
{
    public int baseHealth;
    public int baseAttack;
    public int baseDefense;
    public AnimationCurve levelCurve;
}

[CreateAssetMenu(menuName = "RPG/Item")]
public class ItemData : ScriptableObject
{
    public string itemName;
    public Sprite icon;
    public ItemType type;
    public StatModifier[] modifiers;
}
```

### Recommended Architecture
```
Managers/
├── GameManager (singleton)
├── CombatManager
├── InventoryManager
└── SaveManager

Data/
├── ScriptableObjects/
│   ├── Characters/
│   ├── Items/
│   ├── Abilities/
│   └── Enemies/

Runtime/
├── Character.cs
├── Inventory.cs
├── CombatState.cs
└── Stats.cs
```

### Common Pitfalls
- Hardcoding stats instead of data-driven
- Not separating data from logic
- Complex inheritance hierarchies
- Not planning save system early

## Reference Games
- Final Fantasy (classic turn-based)
- Diablo (action RPG, loot)
- Undertale (simple but effective)
- Stardew Valley (lite RPG elements)

## GDD Sections to Emphasize
- Stat system design
- Combat flow
- Progression curve
- Economy balance
- Narrative structure

## Playtest Focus Areas
- [ ] Is stat progression satisfying?
- [ ] Is combat engaging?
- [ ] Are rewards meaningful?
- [ ] Is difficulty curve appropriate?
- [ ] Do choices feel impactful?
