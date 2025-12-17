# Action-Adventure Game Template

> Specific guidance for action-adventure game development

## Genre Characteristics
- Exploration and discovery
- Combat encounters
- Story/narrative elements
- Ability/item progression
- Mix of action and puzzle elements

## Sub-genres
| Type | Focus | Example |
|------|-------|---------|
| Metroidvania | Exploration, ability gates | Hollow Knight, Metroid |
| Zelda-like | Dungeons, items, puzzles | Zelda, Tunic |
| Character Action | Combat depth, combos | Devil May Cry, Bayonetta |
| Soulslike | Difficult combat, exploration | Dark Souls, Elden Ring |
| Open World | Freedom, discovery | Breath of the Wild |

## Core Systems Priority

### 1. Player Controller (Critical)
**Movement:**
- Walk/run
- Jump (if applicable)
- Dodge/roll
- Climbing/swimming (if applicable)

**Combat:**
- Basic attack
- Dodge/block
- Special abilities
- Lock-on (3D)

### 2. Exploration System
- Interconnected areas
- Shortcuts/fast travel
- Secrets and collectibles
- Map/navigation

### 3. Progression System
- Health/stamina upgrades
- New abilities
- Equipment upgrades
- Story progression

### 4. Enemy Encounters
- Enemy variety
- Attack patterns
- Telegraphed attacks
- Boss encounters

## Recommended Roadmap Order

```
1. Player Movement
2. Basic Combat (attack, dodge)
3. Health System
4. Basic Enemy (one type)
5. First Area (small, complete)
6. Ability Unlock System
7. Area Transitions
8. More Enemies
9. First Boss
10. Progression Items
```

## Unity Implementation Tips

### Player State Machine
```csharp
public class PlayerController : MonoBehaviour
{
    private enum State { Idle, Moving, Attacking, Dodging, Hit }
    private State currentState = State.Idle;

    [Header("Movement")]
    [SerializeField] private float moveSpeed = 5f;
    [SerializeField] private float dodgeSpeed = 10f;
    [SerializeField] private float dodgeDuration = 0.3f;

    [Header("Combat")]
    [SerializeField] private float attackDuration = 0.4f;
    [SerializeField] private float attackDamage = 10f;

    private void Update()
    {
        switch (currentState)
        {
            case State.Idle:
            case State.Moving:
                HandleMovement();
                HandleCombatInput();
                break;
            case State.Attacking:
                // Locked until animation complete
                break;
            case State.Dodging:
                // I-frames active
                break;
        }
    }
}
```

### Area/Room Management
```csharp
public class AreaManager : MonoBehaviour
{
    [SerializeField] private Transform[] spawnPoints;
    [SerializeField] private Enemy[] enemyPrefabs;

    private List<Enemy> activeEnemies = new();
    private bool isCleared;

    public event Action OnAreaCleared;

    public void OnPlayerEnter()
    {
        SpawnEnemies();
    }

    private void OnEnemyDeath(Enemy enemy)
    {
        activeEnemies.Remove(enemy);
        if (activeEnemies.Count == 0)
        {
            isCleared = true;
            OnAreaCleared?.Invoke();
        }
    }
}
```

### Ability Gate System
```csharp
public class AbilityGate : MonoBehaviour
{
    [SerializeField] private AbilityType requiredAbility;
    [SerializeField] private GameObject blockedVisual;
    [SerializeField] private GameObject unlockedVisual;

    private void Start()
    {
        bool hasAbility = PlayerAbilities.Instance.HasAbility(requiredAbility);
        blockedVisual.SetActive(!hasAbility);
        unlockedVisual.SetActive(hasAbility);
        GetComponent<Collider>().enabled = !hasAbility;
    }
}
```

### Common Pitfalls
- Movement doesn't feel good
- Combat lacks impact
- Empty exploration
- Unclear progression
- Backtracking tedium
- Save point frustration

## Reference Games
- Hollow Knight (metroidvania, feel)
- Dark Souls (combat, exploration)
- Zelda: BotW (freedom, discovery)
- Hyper Light Drifter (feel, style)
- Tunic (mystery, design)

## GDD Sections to Emphasize
- Movement and combat feel
- World structure (map)
- Ability progression
- Enemy design
- Boss encounters

## Playtest Focus Areas
- [ ] Does movement feel good?
- [ ] Is combat satisfying?
- [ ] Is exploration rewarding?
- [ ] Are ability gates clear?
- [ ] Are bosses challenging but fair?
- [ ] Is getting lost fun or frustrating?
