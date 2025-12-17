# Game Types → Design Pillars Mapping

This reference maps game types to their relevant design pillars for `/pillars` command.

## Game Type Detection

Detect from `docs/game-brief.md` → `## Game Type` field, or infer from:
- Keywords in description
- Core mechanics mentioned
- Reference games cited

---

## Type Mappings

### Roguelike / Roguelite

**Keywords:** permadeath, runs, procedural, meta-progression, random

**Core Pillars:**
- `game-loop.md` - Run structure, death cycle
- `combat-system.md` - Combat mechanics
- `progression.md` - In-run progression
- `meta-progression.md` - Between-run unlocks
- `procedural-generation.md` - Level/content generation
- `enemy-design.md` - Enemy variety, patterns
- `boss-design.md` - Boss encounters
- `items-equipment.md` - Loot, builds
- `difficulty-curve.md` - Challenge scaling

**Optional:**
- `character-design.md` - If multiple playable characters
- `synergies.md` - If build/combo focused

---

### Action Platformer

**Keywords:** jump, platform, movement, precision, levels

**Core Pillars:**
- `game-loop.md` - Level progression
- `movement-controls.md` - Jump, dash, physics
- `level-design.md` - Level structure, obstacles
- `difficulty-curve.md` - Challenge progression
- `enemy-design.md` - Enemy placement, patterns

**Optional:**
- `combat-system.md` - If combat-heavy
- `boss-design.md` - If boss fights
- `progression.md` - If abilities unlock
- `collectibles.md` - If collection focused

---

### Metroidvania

**Keywords:** exploration, abilities, backtracking, interconnected

**Core Pillars:**
- `game-loop.md` - Exploration loop
- `movement-controls.md` - Movement abilities
- `level-design.md` - World structure, gates
- `progression.md` - Ability unlocks
- `combat-system.md` - Combat mechanics
- `world-building.md` - Lore, atmosphere
- `boss-design.md` - Boss encounters

**Optional:**
- `items-equipment.md` - If gear system
- `map-design.md` - If complex navigation

---

### RPG (Role-Playing Game)

**Keywords:** stats, leveling, quests, party, inventory, dialogue

**Core Pillars:**
- `game-loop.md` - Core gameplay cycle
- `combat-system.md` - Battle system
- `character-progression.md` - Stats, skills, classes
- `story-structure.md` - Main narrative
- `character-arcs.md` - Party/NPC development
- `dialogue-system.md` - Conversation mechanics
- `world-building.md` - Lore, factions
- `items-equipment.md` - Gear, inventory
- `quest-design.md` - Quest structure

**Optional:**
- `economy-resources.md` - If complex economy
- `crafting-system.md` - If crafting exists

---

### Action RPG (ARPG)

**Keywords:** real-time combat, loot, builds, dungeon

**Core Pillars:**
- `game-loop.md` - Combat/loot cycle
- `combat-system.md` - Real-time combat
- `character-progression.md` - Builds, skills
- `items-equipment.md` - Loot system
- `enemy-design.md` - Enemy variety
- `boss-design.md` - Boss fights
- `level-design.md` - Dungeon structure

**Optional:**
- `multiplayer-design.md` - If co-op/online
- `economy-resources.md` - If trading exists

---

### Turn-Based Tactics

**Keywords:** grid, tactics, positioning, turn-based, strategy

**Core Pillars:**
- `game-loop.md` - Mission structure
- `combat-system.md` - Tactical combat
- `character-progression.md` - Unit development
- `level-design.md` - Map design
- `enemy-design.md` - Enemy types, AI
- `difficulty-curve.md` - Challenge scaling

**Optional:**
- `story-structure.md` - If narrative-driven
- `permadeath-system.md` - If XCOM-style

---

### Puzzle Game

**Keywords:** puzzle, logic, solve, brain, mechanics

**Core Pillars:**
- `game-loop.md` - Puzzle flow
- `puzzle-mechanics.md` - Core puzzle rules
- `level-design.md` - Puzzle progression
- `difficulty-curve.md` - Complexity curve
- `tutorial-design.md` - Teaching mechanics

**Optional:**
- `story-structure.md` - If narrative wrapper
- `art-direction.md` - Visual language for puzzles

---

### Survival

**Keywords:** survival, crafting, resources, hunger, base

**Core Pillars:**
- `game-loop.md` - Survival cycle
- `crafting-system.md` - Crafting mechanics
- `economy-resources.md` - Resource management
- `building-system.md` - Base building
- `world-building.md` - Environment, threats
- `enemy-design.md` - Hostile creatures
- `difficulty-curve.md` - Survival pressure

**Optional:**
- `multiplayer-design.md` - If multiplayer
- `procedural-generation.md` - If procedural world

---

### Horror

**Keywords:** horror, fear, tension, atmosphere, survival horror

**Core Pillars:**
- `game-loop.md` - Tension/release cycle
- `atmosphere-design.md` - Fear building
- `enemy-design.md` - Monster design
- `level-design.md` - Environment, pacing
- `sound-design.md` - Audio atmosphere
- `story-structure.md` - Narrative horror

**Optional:**
- `combat-system.md` - If combat exists
- `puzzle-mechanics.md` - If puzzle elements
- `stealth-system.md` - If stealth focused

---

### Simulation

**Keywords:** simulation, management, systems, sandbox

**Core Pillars:**
- `game-loop.md` - Core simulation loop
- `systems-design.md` - Interacting systems
- `economy-resources.md` - Resource flow
- `progression.md` - Unlock/growth
- `ui-design.md` - Information display

**Optional:**
- `building-system.md` - If construction
- `npc-design.md` - If characters involved

---

### Visual Novel

**Keywords:** story, choices, narrative, dialogue, branching

**Core Pillars:**
- `story-structure.md` - Narrative architecture
- `character-arcs.md` - Character development
- `dialogue-system.md` - Choice mechanics
- `branching-design.md` - Path structure
- `art-direction.md` - Visual presentation

**Optional:**
- `puzzle-mechanics.md` - If puzzle elements
- `relationship-system.md` - If dating sim elements

---

### Fighting Game

**Keywords:** fighting, combo, versus, competitive, moves

**Core Pillars:**
- `game-loop.md` - Match structure
- `combat-system.md` - Fighting mechanics
- `character-design.md` - Fighter roster
- `move-design.md` - Movesets, combos
- `balance-design.md` - Competitive balance

**Optional:**
- `story-structure.md` - If story mode
- `multiplayer-design.md` - Online features

---

### Racing

**Keywords:** racing, speed, vehicles, tracks, driving

**Core Pillars:**
- `game-loop.md` - Race structure
- `vehicle-design.md` - Car/vehicle handling
- `track-design.md` - Level/track design
- `progression.md` - Unlock system
- `difficulty-curve.md` - AI/challenge

**Optional:**
- `multiplayer-design.md` - If multiplayer
- `customization.md` - If vehicle customization

---

### Card Game / Deckbuilder

**Keywords:** cards, deck, draw, hand, synergy

**Core Pillars:**
- `game-loop.md` - Match/run structure
- `card-design.md` - Card mechanics
- `deck-building.md` - Collection, builds
- `synergies.md` - Card combos
- `enemy-design.md` - Opponents/AI
- `balance-design.md` - Card balance

**Optional:**
- `meta-progression.md` - If roguelike
- `multiplayer-design.md` - If PvP

---

### Tower Defense

**Keywords:** tower, defense, waves, enemies, placement

**Core Pillars:**
- `game-loop.md` - Wave structure
- `tower-design.md` - Tower types, upgrades
- `enemy-design.md` - Enemy waves, types
- `level-design.md` - Map design
- `economy-resources.md` - Resource management
- `difficulty-curve.md` - Wave progression

**Optional:**
- `hero-design.md` - If hero units
- `meta-progression.md` - If permanent upgrades

---

## Universal Pillars

**Always generated for all game types:**

| Pillar | Purpose |
|--------|---------|
| `_index.md` | Overview, completion status, order |
| `game-loop.md` | Core gameplay cycle |
| `player-experience.md` | Target emotions, fantasy |
| `art-direction.md` | Visual style, mood |

---

## Pillar Template Structure

Each pillar stub contains:

```markdown
# [Pillar Name] - [Game Name]

## Connection to Vision
How this pillar serves the game's core pillars from game-brief.

## Key Questions

### [Question Category 1]
- [ ] Question 1?
- [ ] Question 2?

### [Question Category 2]
- [ ] Question 3?
- [ ] Question 4?

## Design Space
[Empty - filled during /deep-dive]

## References
[Empty - filled during /deep-dive]

## Dependencies
- **Requires:** [pillar] to be complete first
- **Impacts:** [pillar] decisions

---
*Status: STUB*
*Complete with: /deep-dive [pillar-name]*
```
