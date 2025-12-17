# Simulation Game Template

> Specific guidance for simulation game development

## Genre Characteristics
- Systems-driven gameplay
- Player agency in complex systems
- Often open-ended
- Resource management
- Emergent behavior

## Sub-genres
| Type | Focus | Example |
|------|-------|---------|
| Life Sim | Daily life, relationships | Stardew Valley, Animal Crossing |
| Management | Business/city building | SimCity, Planet Coaster |
| Vehicle | Realistic control | Flight Sim, Euro Truck |
| God Game | World manipulation | Black & White, Populous |
| Sandbox | Creation freedom | Minecraft, Terraria |

## Core Systems Priority

### 1. Core Simulation Loop (Critical)
**Define:**
- What is being simulated?
- What rules govern it?
- What can player influence?
- What emerges from systems?

### 2. Time System
- Day/night cycle
- Seasons (if applicable)
- Time scaling
- Scheduled events

### 3. Resource Management
- Resource types
- Production/consumption
- Storage limits
- Trade/conversion

### 4. AI Agents (if applicable)
- NPC behaviors
- Needs systems
- Relationships
- Routines

## Recommended Roadmap Order

```
1. Core System Loop (single system working)
2. Time Progression
3. Basic Resources
4. Player Interaction
5. UI for Information
6. Second System (interactions)
7. Save/Load
8. Goals/Objectives
9. Emergent Events
10. Content Expansion
```

## Unity Implementation Tips

### Time Manager
```csharp
public class TimeManager : MonoBehaviour
{
    public static TimeManager Instance;

    [SerializeField] private float minutesPerRealSecond = 1f;

    public int day = 1;
    public int hour = 6;
    public int minute = 0;

    public event Action<int> OnHourChanged;
    public event Action<int> OnDayChanged;

    private void Update()
    {
        minute += Mathf.RoundToInt(minutesPerRealSecond * Time.deltaTime);

        if (minute >= 60)
        {
            minute = 0;
            hour++;
            OnHourChanged?.Invoke(hour);

            if (hour >= 24)
            {
                hour = 0;
                day++;
                OnDayChanged?.Invoke(day);
            }
        }
    }
}
```

### Resource System
```csharp
public class ResourceManager : MonoBehaviour
{
    private Dictionary<ResourceType, float> resources = new();

    public event Action<ResourceType, float> OnResourceChanged;

    public void AddResource(ResourceType type, float amount)
    {
        if (!resources.ContainsKey(type))
            resources[type] = 0;

        resources[type] += amount;
        OnResourceChanged?.Invoke(type, resources[type]);
    }

    public bool TryConsume(ResourceType type, float amount)
    {
        if (!resources.ContainsKey(type) || resources[type] < amount)
            return false;

        resources[type] -= amount;
        OnResourceChanged?.Invoke(type, resources[type]);
        return true;
    }
}
```

### Agent Needs System
```csharp
public class NeedsSystem : MonoBehaviour
{
    [System.Serializable]
    public class Need
    {
        public string name;
        [Range(0, 100)] public float value = 50f;
        public float decayRate = 1f; // per hour
    }

    public Need[] needs;

    private void OnEnable()
    {
        TimeManager.Instance.OnHourChanged += UpdateNeeds;
    }

    private void UpdateNeeds(int hour)
    {
        foreach (var need in needs)
        {
            need.value -= need.decayRate;
            need.value = Mathf.Clamp(need.value, 0, 100);
        }
    }
}
```

### Common Pitfalls
- Systems too opaque (player can't understand)
- Not enough feedback
- Micromanagement tedium
- No clear goals or direction
- Save system bugs (complex state)

## Reference Games
- Stardew Valley (life sim, polish)
- Dwarf Fortress (emergence, complexity)
- Cities: Skylines (management, scale)
- RimWorld (storytelling, AI)
- Factorio (systems, optimization)

## GDD Sections to Emphasize
- System interactions diagram
- Time/pacing design
- Resource flow
- Player feedback loops
- Win conditions (if any)

## Playtest Focus Areas
- [ ] Are systems understandable?
- [ ] Is feedback clear and timely?
- [ ] Is pacing engaging (not tedious)?
- [ ] Do interesting situations emerge?
- [ ] Is information accessible?
- [ ] Does saving/loading work reliably?
