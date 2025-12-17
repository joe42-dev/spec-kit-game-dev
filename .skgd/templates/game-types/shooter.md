# Shooter Game Template

> Specific guidance for shooter game development (FPS/TPS/Top-down)

## Genre Characteristics
- Projectile/hitscan weapons
- Enemy AI
- Health/damage systems
- Often fast-paced
- Aiming precision

## Sub-genres
| Type | Camera | Controls |
|------|--------|----------|
| FPS | First-person | WASD + Mouse |
| TPS | Third-person | WASD + Mouse |
| Top-down | Overhead | WASD or arrows + Mouse aim |
| Twin-stick | Overhead | Left stick move, right stick aim |

## Core Systems Priority

### 1. Shooting Mechanic (Critical)
**Key Parameters:**
| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| Fire Rate | Shots per second | 1-20 |
| Damage | Per projectile | 5-100 |
| Spread | Accuracy cone | 0-15 degrees |
| Recoil | Camera/aim kick | 0-10 degrees |
| Reload Time | Seconds | 1-3s |

**Projectile vs Hitscan:**
- Projectile: Physical bullet, travel time
- Hitscan: Instant raycast, immediate hit

### 2. Player Controller
- Movement (WASD or sticks)
- Aiming (mouse or right stick)
- Camera control
- Strafing

### 3. Enemy AI
- Detection (sight, sound)
- Pathfinding
- Combat behavior
- Death handling

### 4. Weapon System
- Multiple weapon types
- Ammo management
- Weapon switching
- Upgrades (optional)

## Recommended Roadmap Order

```
1. Player Movement
2. Camera Control
3. Basic Shooting (raycast/projectile)
4. Target Dummy (no AI)
5. Health/Damage System
6. Basic Enemy (moves, shoots)
7. Enemy AI (patrol, chase, attack)
8. Multiple Weapons
9. Ammo/Reload
10. Level with Cover
```

## Unity Implementation Tips

### Shooting System (Raycast)
```csharp
public class Weapon : MonoBehaviour
{
    [SerializeField] private float damage = 10f;
    [SerializeField] private float range = 100f;
    [SerializeField] private float fireRate = 10f;
    [SerializeField] private LayerMask hitLayers;

    private float nextFireTime;

    public void TryShoot()
    {
        if (Time.time < nextFireTime) return;
        nextFireTime = Time.time + 1f / fireRate;

        Ray ray = Camera.main.ViewportPointToRay(new Vector3(0.5f, 0.5f, 0));
        if (Physics.Raycast(ray, out RaycastHit hit, range, hitLayers))
        {
            hit.collider.GetComponent<IDamageable>()?.TakeDamage(damage);
        }
    }
}
```

### Projectile Pattern
```csharp
public class Projectile : MonoBehaviour
{
    [SerializeField] private float speed = 20f;
    [SerializeField] private float damage = 10f;
    [SerializeField] private float lifetime = 5f;

    private void Start()
    {
        Destroy(gameObject, lifetime);
    }

    private void Update()
    {
        transform.Translate(Vector3.forward * speed * Time.deltaTime);
    }

    private void OnTriggerEnter(Collider other)
    {
        other.GetComponent<IDamageable>()?.TakeDamage(damage);
        Destroy(gameObject);
    }
}
```

### Common Pitfalls
- Ignoring feel (screenshake, muzzle flash)
- Enemies too accurate
- No hit feedback
- Boring weapon variety
- Poor level design (no cover)

## Reference Games
- DOOM (feel, speed)
- Halo (combat sandbox)
- Hotline Miami (top-down, brutal)
- Enter the Gungeon (twin-stick)

## GDD Sections to Emphasize
- Weapon stats and feel
- Enemy types and behaviors
- Level design (cover, flow)
- Difficulty balancing
- Audio/visual feedback

## Playtest Focus Areas
- [ ] Does shooting feel impactful?
- [ ] Is aiming responsive?
- [ ] Are enemies fair but challenging?
- [ ] Is feedback clear (hit markers, etc)?
- [ ] Does movement feel good during combat?
