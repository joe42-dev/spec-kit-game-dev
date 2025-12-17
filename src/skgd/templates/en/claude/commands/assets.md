# /assets [subcommand] - Asset Pipeline Management

You are managing the asset pipeline for this game project.

**Argument:** `$ARGUMENTS` (optional subcommand: setup, list, generate)

## Model

**MANDATORY: sonnet** - Orchestration task, coordinate between systems.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Philosophy

This command is the **hub** for all asset-related operations.
It orchestrates between multiple MCPs (Blender, PixelLab) and the game engine (Unity/Godot).

## Step 1: Load Context

Read these files:
- `.skgd/config.yaml` → Get `mcp.assets` configuration
- `.skgd/state.yaml` → Get `assets` status
- `.skgd/memory/assets-catalog.md` → Current asset inventory

## Step 2: Route by Subcommand

### No Subcommand → Show Status Overview

Display asset pipeline status:

```
🎨 ASSET PIPELINE STATUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Art Profile: [profile from config or "Not set"]

📦 Configured MCPs:
  [✓/✗] Blender MCP - [status]
  [✓/✗] PixelLab MCP - [status]

📊 Asset Progress:
  Sprites:    [##........] X/Y (Z%)
  Models:     [####......] X/Y (Z%)
  Animations: [#.........] X/Y (Z%)
  Audio:      [..........] X/Y (Z%)

🎯 Features Needing Assets:
  → [feature-name] (N sprites, N animations)
  → [feature-name] (N models)

Commands:
  /assets setup              - Configure asset MCPs
  /assets list [feature]     - List assets for feature
  /assets generate [feature] - Generate assets via MCP
```

### Subcommand: setup

Guide user through MCP configuration:

1. Check current art profile in config
2. Show available asset MCPs:
   - **Blender MCP** - 3D modeling, materials, animations
   - **PixelLab MCP** - AI sprite generation, tilesets

3. For each selected MCP, provide installation instructions:
   ```
   Blender MCP:
     Install: claude mcp add blender-mcp -- uvx blender-mcp
     Requires: Blender installed locally

   PixelLab MCP:
     Install: claude mcp add pixellab -- npx pixellab-mcp
   ```

4. Update `.skgd/config.yaml` → `mcp.assets.[name].enabled = true`

### Subcommand: list [feature]

If feature provided:
1. Read `docs/specs/[feature]/spec.md`
2. Extract "Asset Requirements" section
3. Display assets with status:
   ```
   Assets for: [feature]

   Visual Assets:
   | ID | Name | Type | Status | Path |
   |----|------|------|--------|------|
   | SPR-1 | player_idle | sprite | ready | Assets/Art/Sprites/player_idle.png |
   | SPR-2 | player_walk | animation | pending | - |

   Audio Assets:
   | ID | Name | Type | Status | Path |
   |----|------|------|--------|------|
   | SFX-1 | footstep | sfx | pending | - |
   ```

If no feature:
1. List all features with pending assets from `state.yaml → assets.queue`

### Subcommand: generate [feature]

**IMPORTANT:** Invoke the `pixellab-assets` skill for detailed patterns.

1. **Load spec** - Read `docs/specs/[feature]/spec.md`
2. **Extract assets** - Parse "Asset Requirements" section
3. **Check MCPs** - Verify required MCPs are configured and connected
4. **Queue assets (NON-BLOCKING!):**

   #### Characters (via PixelLab MCP):
   ```python
   # Create character and queue animations immediately
   result = mcp__pixellab__create_character(
       description="detailed character description from spec",
       name="character_name",
       n_directions=8,      # 4 or 8 based on game type
       proportions="heroic", # chibi, default, heroic, realistic
       size=32              # 16, 32, 48, 64
   )
   character_id = result["character_id"]

   # Queue all animations at once (don't wait!)
   for anim in ["idle breathing", "walk cycle", "attack"]:
       mcp__pixellab__animate_character(
           character_id=character_id,
           action_description=anim
       )
   ```

   #### Tilesets (via PixelLab MCP):
   ```python
   # Chain tilesets for terrain consistency
   ocean = mcp__pixellab__create_topdown_tileset(
       lower_description="deep blue ocean water",
       upper_description="shallow water with foam",
       transition_size=0.25,
       tile_size=32
   )

   beach = mcp__pixellab__create_topdown_tileset(
       lower_description="shallow water",
       upper_description="sandy beach",
       base_tile_id=ocean["tileset_id"]  # CHAIN for consistency!
   )
   ```

   #### Map Objects (via PixelLab MCP):
   ```python
   # Batch queue objects
   objects = ["wooden chest", "health potion", "gold coins"]
   for obj in objects:
       mcp__pixellab__create_map_object(
           description=f"pixel art {obj}, game item",
           width=32, height=32,
           view="high top-down"
       )
   ```

   #### 3D Models (via Blender MCP):
   ```python
   # Use Blender MCP for 3D assets
   mcp__blender-mcp__execute_blender_code(
       code="# Python code to create/import 3D model"
   )
   ```

5. **Track generation status:**
   ```python
   # Check status after 5-10 minutes
   mcp__pixellab__get_character(character_id)
   # Status: "completed" | "processing" | "failed"
   ```

6. **Import to engine when ready:**
   - Download from PixelLab URL
   - Import to `Assets/Art/` (Unity) or `res://assets/` (Godot)

7. **Update tracking:**
   - Update `.skgd/state.yaml` → `assets.by_category`
   - Update `.skgd/memory/assets-catalog.md`

#### Asset Generation Checklist:
```
📋 Before generating:
- [ ] Spec has "Asset Requirements" section
- [ ] Art profile defined (pixel art vs 3D)
- [ ] Consistent sizes/proportions documented
- [ ] PixelLab/Blender MCP connected

🔄 During generation (NON-BLOCKING):
- [ ] Queue all characters + animations
- [ ] Chain tilesets with base_tile_id
- [ ] Batch queue map objects
- [ ] Note job IDs for status checking

✓ After generation:
- [ ] Check status after 5-10 min
- [ ] Download completed assets
- [ ] Import to engine
- [ ] Update assets-catalog.md
```

## Step 3: Update State

After any operation:
```yaml
# Update state.yaml
last_action:
  command: assets
  timestamp: [now]
  result: [outcome]
```

## Step 4: Summary

Provide clear summary of what was done and next steps:

```
✓ Asset operation complete

[Summary of actions taken]

Next steps:
  /assets list [feature] - Check asset status
  /implement - Continue with implementation
```

## Error Handling

If MCP not configured:
```
⚠️ [MCP Name] is not configured.

To enable:
  1. Run: /assets setup
  2. Follow installation instructions
  3. Retry: /assets generate [feature]
```

If MCP not connected:
```
⚠️ [MCP Name] is not responding.

Please ensure:
  1. [Application] is running (if required)
  2. MCP server is started
  3. Try: /assets setup to verify connection
```
