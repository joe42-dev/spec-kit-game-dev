# PixelLab Tileset Creation

## Tileset Types Overview

| Type | Use Case | Output |
|------|----------|--------|
| Top-Down | RPG, RTS maps | 16 Wang tiles |
| Sidescroller | Platformers | 16 platform tiles |
| Isometric | Strategy, city builders | Single tiles |

---

## Top-Down Tilesets (Wang)

### create_topdown_tileset

```python
mcp__pixellab__create_topdown_tileset(
    lower_description="deep blue ocean water with waves",
    upper_description="sandy beach with shells",
    transition_description="foam and wet sand",
    transition_size=0.25,  # 0=sharp, 0.25=medium, 0.5=wide
    tile_size=32,
    outline="single",
    shading="smooth",
    detail="medium",
    view="high top-down",  # or "low top-down"
    tile_strength=0.7,
    base_tile_id=None,     # Chain from previous!
    tileset_adherence=0.8,
    text_guidance_scale=7.5
)
```

### Wang Tileset Concept

Wang tiles cover ALL corner combinations for seamless terrain:

```
┌─────────────────────────────────────┐
│  Full    │ Corners │  Edges  │ etc │
│  Lower   │         │         │     │
├──────────┼─────────┼─────────┼─────┤
│ ████████ │ ██░░░░██│ ████████│ ... │
│ ████████ │ ░░░░░░░░│ ░░░░░░░░│     │
│ ████████ │ ██░░░░██│ ████████│     │
└─────────────────────────────────────┘
16 tiles total = All possible transitions
```

### Terrain Chaining Pattern

**Critical:** Use `base_tile_id` to maintain visual consistency!

```python
# Ocean → Beach → Grass → Forest progression

# Step 1: Ocean base
ocean = create_topdown_tileset(
    lower_description="deep blue ocean with subtle waves",
    upper_description="shallow turquoise water",
    transition_description="water depth gradient",
    transition_size=0.5
)

# Step 2: Beach (chain from ocean)
beach = create_topdown_tileset(
    lower_description="shallow turquoise water",
    upper_description="golden sand beach",
    transition_description="wet sand with foam",
    transition_size=0.25,
    base_tile_id=ocean["tileset_id"]  # CHAIN!
)

# Step 3: Grass (chain from beach)
grass = create_topdown_tileset(
    lower_description="golden sand",
    upper_description="green grass with flowers",
    transition_description="sparse grass on sand",
    transition_size=0.25,
    base_tile_id=beach["tileset_id"]  # CHAIN!
)

# Step 4: Forest (chain from grass)
forest = create_topdown_tileset(
    lower_description="green grass",
    upper_description="dark forest floor with leaves",
    transition_description="undergrowth and bushes",
    transition_size=0.3,
    base_tile_id=grass["tileset_id"]  # CHAIN!
)
```

### View Options

- **"high top-down"** - RTS style, see more of top surface
- **"low top-down"** - RPG style, see more vertical detail

---

## Sidescroller Tilesets

### create_sidescroller_tileset

```python
mcp__pixellab__create_sidescroller_tileset(
    lower_description="brown dirt and stone",
    transition_description="green grass with small flowers",
    transition_size=0.2,
    tile_size=32,
    outline="single",
    shading="smooth",
    detail="medium",
    tile_strength=0.7,
    base_tile_id=None,
    tileset_adherence=0.8,
    text_guidance_scale=7.5,
    seed=None  # Set for reproducibility
)
```

### Sidescroller Features

- **Transparent backgrounds** - Layer over parallax
- **Flat top surfaces** - For character walking
- **Platform edges** - Left, right, corners

### Platform Types Example

```python
# Grass platforms
grass_platform = create_sidescroller_tileset(
    lower_description="brown soil with roots",
    transition_description="green grass tuft on top"
)

# Stone platforms (chain for consistency)
stone_platform = create_sidescroller_tileset(
    lower_description="gray cobblestone bricks",
    transition_description="moss and cracks on top",
    base_tile_id=grass_platform["tileset_id"]
)

# Ice platforms
ice_platform = create_sidescroller_tileset(
    lower_description="solid blue ice block",
    transition_description="snow and frost on top",
    base_tile_id=grass_platform["tileset_id"]
)
```

---

## Isometric Tiles

### create_isometric_tile

```python
mcp__pixellab__create_isometric_tile(
    description="grass tile with small flowers",
    size=32,  # 32px recommended
    tile_shape="thin",  # thin, thick, block
    outline="single",   # lineless, single
    shading="smooth",
    detail="medium",
    text_guidance_scale=7.5,
    seed=12345  # Same seed = consistent style
)
```

### Tile Shapes

| Shape | Thickness | Use Case |
|-------|-----------|----------|
| `thin` | ~10% | Flat terrain |
| `thick` | ~25% | Raised platforms |
| `block` | ~50% | Walls, buildings |

### Isometric Set Example

```python
# Create consistent terrain set
base_seed = 42

tiles = [
    ("grass", "green grass with small daisies"),
    ("dirt", "brown packed dirt path"),
    ("stone", "gray cobblestone road"),
    ("water", "shallow blue water with ripples")
]

for name, desc in tiles:
    create_isometric_tile(
        description=desc,
        size=32,
        tile_shape="thin",
        seed=base_seed  # Consistent style!
    )
```

---

## Transition Size Guide

| Value | Effect | Best For |
|-------|--------|----------|
| `0` | Sharp edge | Cliffs, water edge |
| `0.15` | Tight blend | Path edges |
| `0.25` | Medium blend | Most terrain (default) |
| `0.4` | Wide gradient | Soft transitions |
| `0.5` | Very wide | Fog, atmosphere |

---

## Tileset Workflow

### Complete Map Tileset Pipeline

```python
# 1. Plan terrain types
terrains = [
    ("water", "deep", "shallow"),
    ("beach", "shallow water", "sand"),
    ("grass", "sand", "grass"),
    ("forest", "grass", "forest floor")
]

# 2. Create chain
previous_id = None
tilesets = {}

for name, lower, upper in terrains:
    result = create_topdown_tileset(
        lower_description=f"{lower} terrain",
        upper_description=f"{upper} terrain",
        base_tile_id=previous_id
    )
    tilesets[name] = result["tileset_id"]
    previous_id = result["tileset_id"]

# 3. Check all status after ~10 minutes
for name, tileset_id in tilesets.items():
    status = get_topdown_tileset(tileset_id)
    print(f"{name}: {status['status']}")
```
