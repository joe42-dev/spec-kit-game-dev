# PixelLab Map Objects

> **Token estimate:** ~450 tokens | **Last updated:** 2025-12

## Table of Contents
- [create_map_object](#create_map_object) - Parameters, Size guidelines, View options
- [Object Categories & Examples](#object-categories--examples) - Collectibles, Props, Furniture, Nature, Structures
- [Batch Creation Pattern](#batch-creation-pattern) - Complete scene objects workflow
- [Description Best Practices](#description-best-practices) - Good descriptions, Structure, Avoid
- [View Consistency](#view-consistency) - Keep same view for all scene objects
- [Integration Tips](#integration-tips) - Unity and Godot import

---

## create_map_object

Creates pixel art objects with transparent backgrounds.

### Parameters

```python
mcp__pixellab__create_map_object(
    description="detailed object description",
    width=32,
    height=32,
    view="high top-down",  # or "low top-down", "side"
    outline="single",      # none, single, double
    shading="smooth",      # flat, smooth, detailed
    detail="medium",       # low, medium, high
    background_image=None, # Optional: blend with background
    inpainting=False       # Advanced: edit existing image
)
```

### Size Guidelines

| Size | Use Case |
|------|----------|
| 16x16 | Small items (coins, gems) |
| 32x32 | Standard objects (potions, keys) |
| 48x48 | Medium props (chairs, barrels) |
| 64x64 | Large objects (tables, statues) |
| 96x96+ | Big structures (fountains, trees) |

### View Options

- **"high top-down"** - Looking down at ~60° (RTS/strategy)
- **"low top-down"** - Looking down at ~45° (RPG/adventure)
- **"side"** - Side view (platformers)

---

## Object Categories & Examples

### Collectibles (16x16 - 32x32)

```python
collectibles = [
    "golden coin with shine effect",
    "red health potion in glass bottle",
    "blue mana crystal glowing",
    "silver key with ornate handle",
    "green gem emerald cut",
    "treasure chest small closed"
]

for item in collectibles:
    create_map_object(
        description=f"pixel art {item}, game item",
        width=16, height=16,
        view="high top-down",
        outline="single"
    )
```

### Props (32x32 - 64x64)

```python
props = [
    ("wooden barrel with metal bands", 32, 32),
    ("wooden crate box", 32, 32),
    ("torch on wall bracket, flame animation", 16, 32),
    ("wooden sign post with arrow", 32, 48),
    ("campfire with logs and flames", 48, 48),
    ("well with stone rim and bucket", 48, 64)
]

for desc, w, h in props:
    create_map_object(
        description=desc,
        width=w, height=h,
        view="high top-down"
    )
```

### Furniture (48x48 - 96x96)

```python
furniture = [
    ("wooden table rectangular, medieval tavern", 64, 48),
    ("wooden chair simple, matching table", 32, 48),
    ("bed with red blanket and pillow", 64, 96),
    ("bookshelf full of books, wooden", 48, 64),
    ("throne golden with red velvet cushion", 48, 64)
]
```

### Nature Objects

```python
nature = [
    ("oak tree large with full canopy", 96, 128),
    ("bush green rounded", 32, 32),
    ("flowers patch colorful", 32, 16),
    ("rock boulder gray mossy", 48, 32),
    ("mushroom red with white spots", 16, 24),
    ("tree stump old with moss", 32, 24)
]
```

### Buildings & Structures

```python
structures = [
    ("house small cottage stone walls thatched roof", 96, 96),
    ("tower stone medieval with flag", 64, 128),
    ("bridge wooden over water", 96, 48),
    ("fence wooden section", 32, 32),
    ("gate iron ornate closed", 64, 64)
]
```

---

## Batch Creation Pattern

### Complete Scene Objects

```python
# Define all objects for a forest scene
forest_scene = {
    "collectibles": [
        ("coin", "golden coin", 16, 16),
        ("gem", "green emerald", 16, 16),
        ("potion", "red health potion bottle", 16, 24)
    ],
    "props": [
        ("chest_closed", "treasure chest wooden closed", 32, 32),
        ("chest_open", "treasure chest wooden open with gold", 32, 32),
        ("campfire", "campfire with cooking pot", 48, 48)
    ],
    "nature": [
        ("tree_oak", "oak tree large green canopy", 96, 128),
        ("tree_pine", "pine tree tall pointed", 64, 128),
        ("bush", "bush green leafy", 32, 32),
        ("rock", "rock gray boulder mossy", 48, 32),
        ("stump", "tree stump old rings visible", 32, 24)
    ]
}

# Queue all objects
job_ids = {}
for category, objects in forest_scene.items():
    for name, desc, w, h in objects:
        result = create_map_object(
            description=f"pixel art {desc}, game asset",
            width=w, height=h,
            view="high top-down"
        )
        job_ids[name] = result["object_id"]

# Check status later (5-10 min)
for name, obj_id in job_ids.items():
    status = get_map_object(obj_id)
    print(f"{name}: {status['status']}")
```

---

## Description Best Practices

### Good Descriptions

```
"wooden treasure chest medieval style, iron bands, closed lid"
"health potion in round glass bottle, red liquid, cork stopper"
"stone fountain ornate, water flowing, moss on edges"
```

### Structure: [Material] [Object] [Style] [Details] [State]

Examples:
- "wooden barrel old, metal bands rusty, cracked"
- "crystal ball glowing, on silver stand, purple mist inside"
- "iron cage hanging, chains visible, empty"

### Avoid

- "cool item" (vague)
- "potion" (no details)
- "like in Zelda" (copyright)
- Multiple objects in one (create separately)

---

## View Consistency

**Important:** Keep same view for all objects in a scene!

```python
# All RPG objects with same view
view = "low top-down"

for obj in rpg_objects:
    create_map_object(
        description=obj["desc"],
        width=obj["w"],
        height=obj["h"],
        view=view  # Consistent!
    )
```

---

## Integration Tips

### Unity Import
- Download PNG with transparency
- Import as Sprite (2D and UI)
- Set Pixels Per Unit to match (e.g., 32)

### Godot Import
- PNG imports automatically with transparency
- Set as Sprite2D texture
- Enable pixel-perfect rendering in project settings
