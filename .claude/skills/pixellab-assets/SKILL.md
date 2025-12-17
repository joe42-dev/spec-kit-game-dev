---
name: pixellab-assets
description: |
  PixelLab MCP for generating pixel art game assets.

  TRIGGERS: pixel art, sprite, character sprite, tileset, Wang tiles, isometric,
  top-down tiles, sidescroller tiles, map objects, game assets, character animation,
  walk cycle, idle animation, attack animation, PixelLab MCP, create_character,
  animate_character, create_topdown_tileset, create_map_object

  USE WHEN: Generating pixel art characters, creating tilesets for maps, making
  game objects (collectibles, props, furniture), animating characters, building
  consistent visual asset sets, or setting up asset production pipeline.

  TOKEN BUDGET: ~520 tokens (SKILL.md only), ~1800 with references

  NOTE: Non-blocking workflow - queue jobs and check status later (2-5 min processing)
---

# PixelLab Asset Generation Skill

## Key Principle: Non-Blocking Workflow

PixelLab jobs run in background (2-5 minutes). **Never wait** - queue multiple jobs!

```
1. Submit job → get job_id immediately
2. Queue more jobs while processing
3. Check status periodically
4. Download when ready
```

## Quick Reference - PixelLab MCP Tools

### Characters & Animation
```
mcp__pixellab__create_character    → Generate character (4/8 directions)
mcp__pixellab__animate_character   → Add animation to character
mcp__pixellab__get_character       → Check status, get download URL
mcp__pixellab__list_characters     → List all characters
```

### Tilesets
```
mcp__pixellab__create_topdown_tileset      → Wang tileset (16 tiles)
mcp__pixellab__create_sidescroller_tileset → Platformer tiles
mcp__pixellab__create_isometric_tile       → Single isometric tile
mcp__pixellab__get_*_tileset               → Check status
```

### Objects
```
mcp__pixellab__create_map_object   → Objects with transparent bg
mcp__pixellab__get_map_object      → Check status
```

## Workflow Patterns

### Pattern 1: Character + Animation Pipeline
```python
# 1. Create character (returns immediately)
result = create_character(
    description="warrior with sword and shield",
    name="hero",
    n_directions=8,
    proportions="heroic",
    size=32
)
character_id = result["character_id"]

# 2. Queue animations immediately (don't wait!)
animate_character(character_id, action="idle breathing")
animate_character(character_id, action="walk cycle")
animate_character(character_id, action="sword attack")

# 3. Check status after ~5 minutes
get_character(character_id)
```

### Pattern 2: Tileset Chain (Terrain Progression)
```python
# Create cohesive terrain: ocean → beach → grass → forest
ocean = create_topdown_tileset(
    lower="deep blue ocean water",
    upper="shallow water with foam"
)

beach = create_topdown_tileset(
    lower="shallow water",
    upper="sandy beach",
    base_tile_id=ocean["tileset_id"]  # Chain for consistency!
)

grass = create_topdown_tileset(
    lower="sandy beach",
    upper="green grass",
    base_tile_id=beach["tileset_id"]
)
```

### Pattern 3: Batch Object Creation
```python
# Queue all objects at once
objects = ["wooden chest", "health potion", "gold coins", "torch"]
job_ids = []

for obj in objects:
    result = create_map_object(
        description=f"pixel art {obj}, game item",
        width=16, height=16,
        view="high top-down"
    )
    job_ids.append(result["object_id"])

# Check all later
for job_id in job_ids:
    get_map_object(job_id)
```

## Important Parameters

### Character Proportions
- `default` - Standard proportions
- `chibi` - Big head, small body (cute)
- `heroic` - Muscular, imposing
- `realistic_male` / `realistic_female` - Human proportions

### Tileset Transitions
- `transition_size=0` - Sharp edge
- `transition_size=0.25` - Medium blend
- `transition_size=0.5` - Wide gradient

### View Angles
- `"high top-down"` - RTS style (more top visible)
- `"low top-down"` - RPG style (more front visible)
- Side view for sidescrollers

## Detailed References

- [reference/characters.md](reference/characters.md) - Character creation details
- [reference/tilesets.md](reference/tilesets.md) - All tileset types
- [reference/objects.md](reference/objects.md) - Map objects
- [checklists/asset-pipeline.md](checklists/asset-pipeline.md) - Production workflow

## Anti-Patterns

- **NEVER** wait synchronously for jobs (queue and check later)
- **NEVER** forget to chain tilesets (use `base_tile_id`)
- **NEVER** create inconsistent sizes (stick to 16/32/64)
- **ALWAYS** use descriptive names for organization
