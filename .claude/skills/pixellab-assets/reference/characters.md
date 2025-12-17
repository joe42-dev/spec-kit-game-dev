# PixelLab Character Creation

> **Token estimate:** ~350 tokens | **Last updated:** 2025-12

## Table of Contents
- [create_character](#create_character) - Full parameters, Proportions, Sizes, Directions, Descriptions
- [animate_character](#animate_character) - Animation actions, Pipeline example
- [get_character](#get_character) - Response fields, Status values
- [Best Practices](#best-practices) - Batch creation, Consistency, Polling

---

## create_character

### Full Parameters
```python
mcp__pixellab__create_character(
    description="detailed character description",
    name="character_name",
    n_directions=8,        # 4 or 8
    proportions="default", # see presets below
    size=32,               # 16-128px
    outline="single",      # none, single, double
    shading="smooth",      # flat, smooth, detailed
    detail="medium",       # low, medium, high
    ai_freedom=0.5,        # 0-1, higher = more creative
    view="front"           # starting view
)
```

### Proportions Presets

| Preset | Best For | Description |
|--------|----------|-------------|
| `default` | General use | Balanced proportions |
| `chibi` | Cute games | Big head, tiny body |
| `cartoon` | Platformers | Exaggerated features |
| `stylized` | Action games | Slightly heroic |
| `realistic_male` | RPGs | Human male proportions |
| `realistic_female` | RPGs | Human female proportions |
| `heroic` | Action/Fantasy | Muscular, imposing |

### Size Guidelines

- **16px** - Classic retro, NES-style
- **32px** - Standard pixel art (recommended)
- **48px** - Detailed sprites
- **64px** - Large characters, bosses
- **128px** - Portraits, detailed assets

**Note:** Canvas is total area; character occupies ~60% of height

### Direction Configurations

**4 Directions:**
- Front, Back, Left, Right
- Faster generation (~2 min)
- Good for top-down RPGs

**8 Directions:**
- Adds diagonals
- Longer generation (~5 min)
- Required for smooth rotation

### Description Tips

**Good descriptions:**
```
"medieval knight in silver armor with blue cape, holding longsword"
"small green goblin with ragged clothes and wooden club"
"female mage in purple robes with glowing staff, white hair"
```

**Avoid:**
```
"cool character" (too vague)
"a guy" (no details)
"character like from [game name]" (copyright issues)
```

## animate_character

### Usage
```python
mcp__pixellab__animate_character(
    character_id="char_xxx",
    template_animation_id=None,  # Use preset or custom
    action_description="walk cycle with bounce",
    animation_name="walk"
)
```

### Common Animation Actions

**Movement:**
- `"idle breathing"` - Subtle chest movement
- `"walk cycle"` - Standard walking
- `"run cycle"` - Fast running
- `"jump"` - Jump and land

**Combat:**
- `"sword swing"` - Melee attack
- `"bow draw and release"` - Ranged attack
- `"cast spell"` - Magic animation
- `"take damage"` - Hit reaction
- `"death"` - Dying animation

**Utility:**
- `"pickup item"` - Bend and grab
- `"open chest"` - Interaction
- `"wave"` - Social gesture

### Animation Pipeline Example

```python
# Create hero character
hero = create_character(
    description="pixel knight with sword",
    name="hero",
    n_directions=8,
    size=32,
    proportions="heroic"
)

# Queue essential animations (all at once!)
animations = [
    ("idle", "idle breathing, subtle movement"),
    ("walk", "walk cycle, arms swinging"),
    ("run", "run cycle, faster pace"),
    ("attack", "horizontal sword slash"),
    ("hurt", "flinch backward, flash"),
    ("death", "fall to ground")
]

for anim_name, action in animations:
    animate_character(
        character_id=hero["character_id"],
        action_description=action,
        animation_name=anim_name
    )

# Check status after 5-10 minutes
get_character(hero["character_id"])
```

## get_character

### Response Fields
```python
{
    "character_id": "char_xxx",
    "name": "hero",
    "status": "completed",  # or "processing"
    "rotations": [...],     # All direction sprites
    "animations": [
        {
            "name": "walk",
            "status": "completed",
            "frames": [...]
        }
    ],
    "pending_jobs": [...],  # Jobs still processing
    "download_url": "https://..."  # ZIP with all assets
}
```

### Status Values
- `completed` - Ready to download
- `processing` - Still generating (check eta_seconds)
- `failed` - Error occurred
- `not_found` - Invalid ID

## Best Practices

1. **Batch create** - Queue all animations immediately after character
2. **Consistent style** - Same size/shading for all game characters
3. **Name clearly** - Use descriptive names for organization
4. **Check periodically** - Don't poll constantly, wait 2-5 min
5. **Download once complete** - ZIP contains all sprites organized
