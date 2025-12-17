# Platformer Game Template

> Specific guidance for platformer game development

## Genre Characteristics
- Precise movement and jumping
- Level-based progression
- Obstacle navigation
- Often includes collectibles
- Focus on timing and spatial awareness

## Core Systems Priority

### 1. Movement System (Critical)
**Feel Targets:**
- Responsive (< 50ms input latency feel)
- Controllable air movement
- Coyote time (0.1-0.15s)
- Jump buffering (0.1s)

**Key Parameters:**
| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Move Speed | 5-10 units/s | Feel fast but controllable |
| Jump Height | 2-4 units | Affects level design |
| Gravity Scale | 2-4 | Higher = snappier jumps |
| Air Control | 0.5-1.0 | How much control in air |

### 2. Collision System
- Precise hitboxes (often smaller than sprite)
- One-way platforms
- Moving platforms
- Slopes handling (if applicable)

### 3. Camera System
- Follow player smoothly
- Look-ahead
- Vertical dead zones
- Level boundaries

### 4. Level Design Framework
- Introduce mechanics one at a time
- Safe spaces to practice
- Increasing complexity
- Checkpoints for longer levels

## Recommended Roadmap Order

```
1. Player Movement (walk, jump)
2. Basic Collision (ground, walls)
3. Camera Follow
4. Simple Level (platforms only)
5. Hazards (spikes, pits)
6. Collectibles
7. Enemies (basic)
8. Advanced Movement (wall jump, dash)
9. Level Progression
10. Polish (particles, screenshake)
```

## Unity Implementation Tips

### Player Controller Pattern
```csharp
public class PlayerController : MonoBehaviour
{
    [Header("Movement")]
    [SerializeField] private float moveSpeed = 7f;
    [SerializeField] private float jumpForce = 12f;

    [Header("Ground Check")]
    [SerializeField] private Transform groundCheck;
    [SerializeField] private LayerMask groundLayer;

    private Rigidbody2D rb;
    private bool isGrounded;
    private float coyoteTimeCounter;
    private float jumpBufferCounter;
}
```

### Recommended Components
- Rigidbody2D (Dynamic, Freeze Rotation Z)
- BoxCollider2D or CapsuleCollider2D
- Custom PlayerController script
- Separate GroundCheck child object

### Common Pitfalls
- Using transform.Translate instead of Rigidbody
- Not using FixedUpdate for physics
- Checking ground in Update instead of FixedUpdate
- Too large hitboxes

## Reference Games
- Celeste (tight controls, forgiving mechanics)
- Super Meat Boy (precision, speed)
- Hollow Knight (combat + platforming)
- Mario (feel, momentum)

## GDD Sections to Emphasize
- Movement feel targets
- Jump parameters
- Level structure
- Difficulty progression
- Collectible purpose

## Playtest Focus Areas
- [ ] Does jumping feel good?
- [ ] Is coyote time noticeable but fair?
- [ ] Can player land precisely?
- [ ] Are hitboxes forgiving enough?
- [ ] Is air control intuitive?
