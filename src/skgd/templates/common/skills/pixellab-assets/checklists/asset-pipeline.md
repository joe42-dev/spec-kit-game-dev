# PixelLab Asset Pipeline Checklist

## Pre-Production Planning

### Before Creating Assets
- [ ] Define art style (size, outline, shading consistency)
- [ ] List all needed assets by category
- [ ] Plan tileset chains (what transitions to what)
- [ ] Choose consistent view angle for all assets

### Style Guide Template
```yaml
style:
  base_size: 32           # 16, 32, 48, 64
  outline: "single"       # none, single, double
  shading: "smooth"       # flat, smooth, detailed
  view: "high top-down"   # high/low top-down, side

character:
  proportions: "stylized" # default, chibi, heroic, etc.
  directions: 8           # 4 or 8
```

---

## Character Production

### New Character Checklist
- [ ] Create character with clear description
- [ ] Note character_id for reference
- [ ] Queue ALL animations immediately:
  - [ ] idle
  - [ ] walk
  - [ ] run (if needed)
  - [ ] attack (if combat)
  - [ ] hurt
  - [ ] death
- [ ] Wait 5-10 minutes
- [ ] Check status: `get_character(id)`
- [ ] Download ZIP when complete
- [ ] Import to engine

### Character Batch Template
```python
characters = [
    {
        "name": "hero",
        "desc": "knight in silver armor",
        "animations": ["idle", "walk", "attack", "hurt", "death"]
    },
    {
        "name": "enemy_goblin",
        "desc": "small green goblin with club",
        "animations": ["idle", "walk", "attack", "death"]
    },
    {
        "name": "npc_villager",
        "desc": "peasant in brown clothes",
        "animations": ["idle", "walk"]
    }
]
```

---

## Tileset Production

### Tileset Chain Planning
```
[ ] Water (base)
    ↓ chain
[ ] Beach
    ↓ chain
[ ] Grass
    ↓ chain
[ ] Forest
    ↓ chain
[ ] Mountain
```

### New Tileset Checklist
- [ ] Plan lower → upper terrain pair
- [ ] Use base_tile_id from previous (if chaining)
- [ ] Set appropriate transition_size
- [ ] Note tileset_id for next chain
- [ ] Wait 3-5 minutes
- [ ] Check status
- [ ] Download when complete
- [ ] Test in engine tilemap

### Tileset Transition Reference
| Transition | Size | Description |
|------------|------|-------------|
| Water ↔ Beach | 0.3 | Foam, wet sand |
| Beach ↔ Grass | 0.25 | Sparse grass on sand |
| Grass ↔ Forest | 0.3 | Undergrowth |
| Grass ↔ Path | 0.15 | Worn edges |
| Cliff edge | 0 | Sharp drop |

---

## Object Production

### Object Category Checklist

**Collectibles (16-32px)**
- [ ] Coins/currency
- [ ] Health items
- [ ] Mana/energy items
- [ ] Keys
- [ ] Gems/crystals
- [ ] Power-ups

**Interactive Props (32-48px)**
- [ ] Chests (open/closed variants)
- [ ] Doors (open/closed)
- [ ] Switches/levers
- [ ] Signs
- [ ] NPCs conversation markers

**Environment (32-96px)**
- [ ] Trees (2-3 variants)
- [ ] Bushes
- [ ] Rocks (small, medium, large)
- [ ] Flowers/grass patches
- [ ] Water features

**Structures (64-128px)**
- [ ] Buildings
- [ ] Bridges
- [ ] Fences/walls
- [ ] Decorative elements

---

## Quality Control

### Before Downloading
- [ ] All jobs show "completed" status
- [ ] No failed jobs (retry if needed)
- [ ] Character has all animations
- [ ] Tileset chain is complete

### After Importing to Engine
- [ ] Transparency preserved
- [ ] Correct pivot points
- [ ] Pixel-perfect rendering enabled
- [ ] Colliders match sprites (if needed)
- [ ] Animations play correctly
- [ ] Tilesets tile seamlessly

---

## Batch Job Management

### Status Tracking Template
```python
jobs = {
    "characters": {
        "hero": {"id": "char_xxx", "status": "processing"},
        "enemy": {"id": "char_yyy", "status": "completed"}
    },
    "tilesets": {
        "water_beach": {"id": "tile_xxx", "status": "completed"},
        "beach_grass": {"id": "tile_yyy", "status": "processing"}
    },
    "objects": {
        "coin": {"id": "obj_xxx", "status": "completed"},
        "chest": {"id": "obj_yyy", "status": "completed"}
    }
}
```

### Polling Strategy
```
Minute 0:   Submit all jobs
Minute 2:   First status check (quick objects may be done)
Minute 5:   Check tilesets, simple characters
Minute 10:  Check complex characters (8-dir + animations)
Minute 15:  Everything should be done, investigate failures
```

---

## Troubleshooting

### Job Failed
- [ ] Check description (too vague? inappropriate?)
- [ ] Retry with clearer description
- [ ] Try different parameters (smaller size, simpler style)

### Inconsistent Style
- [ ] Use same seed for isometric tiles
- [ ] Chain tilesets with base_tile_id
- [ ] Keep outline/shading/detail consistent

### Import Issues
- [ ] Verify PNG has alpha channel
- [ ] Check sprite import settings in engine
- [ ] Ensure pixel-perfect camera/rendering
