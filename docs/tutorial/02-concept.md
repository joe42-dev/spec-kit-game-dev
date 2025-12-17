# SKGD Tutorial - Part 2: Concept Phase

## Overview

The Concept Phase establishes your game's creative foundation:

```
/brainstorm → /pillars → /deep-dive × N → /validate-design
```

## Step 1: Brainstorm

Run:
```
/brainstorm
```

### Three Modes Available

**🎲 Explorer Mode** (for uncertain users)
- Guided experience profiling
- 26 game-brain techniques available
- Generates 5 distinct concepts
- Pick, combine, or regenerate

**💡 Creator Mode** (for users with a vision)
- Organic dialogue
- Follows your creative energy
- Synthesizes ideas as you explore
- Crystallizes when ready

**⚡ Spark Mode** (if game-brief.md exists)
- Unblocks stuck projects
- Presents 3 creative interventions:
  - The Weird One (uncomfortable twist)
  - The Pivot (flip an assumption)
  - The Deep Dive (10x an existing idea)

### Output: game-brief.md

```markdown
# [Game Name]

## Elevator Pitch
[One compelling sentence]

## Game Type
[Genre classification]

## Core Experience
[What players should feel]

## Core Loop
[The fundamental gameplay cycle]

## Unique Selling Point
[What makes this game special]

## Reference Games
- [Game 1]: [What to take]
- [Game 2]: [What to avoid]
```

### Also Created: constitution.md

Your core vision is captured in `.skgd/memory/constitution.md`:
- **Immutable** - Only changes via `/pivot`
- **Loaded by all commands** - Ensures consistency

## Step 2: Generate Pillars

Run:
```
/pillars
```

This command:
1. Reads your `game-brief.md`
2. Detects game type
3. Maps to relevant design pillars via `game-types.md`
4. Generates pillar stubs

### Pillar Structure

```
docs/pillars/
├── _index.md              # Overview and status
├── game-loop.md           # Core gameplay cycle (always)
├── player-experience.md   # Target emotions (always)
├── art-direction.md       # Visual style (always)
└── [type-specific]*.md    # Based on game type
```

### Game Type → Pillars Mapping

| Game Type | Key Pillars |
|-----------|-------------|
| **Roguelike** | combat-system, progression, meta-progression, procedural-generation, enemy-design |
| **Platformer** | movement-controls, level-design, difficulty-curve |
| **RPG** | combat-system, character-progression, dialogue-system, quest-design |
| **Puzzle** | puzzle-mechanics, level-design, tutorial-design |

### Stub Format

Each pillar starts as a stub with:
```markdown
# [Pillar Name]

**Status:** 🔲 STUB

## Connection to Vision
> [Quote from game-brief]

## Key Questions
- [ ] Question 1?
- [ ] Question 2?
- [ ] Question 3?

## Design Space
[Empty - to be filled in /deep-dive]

## Dependencies
- Depends on: [other pillars]
- Blocks: [pillars waiting for this]
```

## Step 3: Deep Dive (Repeat Per Pillar)

Run for each pillar (start with highest priority):
```
/deep-dive game-loop
```

### The Deep Dive Process

1. **Phase 0: Scout Context** (Haiku agent)
   - Reads all existing pillars
   - Identifies cross-pillar connections
   - Returns summary to Opus

2. **Collaborative Design Session** (Opus)
   - Reviews each question in the stub
   - Proposes 2-4 options with reference games
   - Discusses trade-offs
   - Documents decisions with rationale

3. **Cross-Pillar Check**
   - Verifies decisions don't conflict with other pillars
   - Notes potential tensions for validation

4. **Complete Document Generation**

### Complete Pillar Format

```markdown
# [Pillar Name]

**Status:** ✅ COMPLETE

## Connection to Vision
> [Quote from game-brief]

## Design Decisions

| Question | Decision | Rationale |
|----------|----------|-----------|
| [Q1] | [Answer] | [Why] |

## Detailed Design

### [Section 1]
[Deep content]

### [Section 2]
[Deep content]

## References
- **[Game A]**: Take [X], Avoid [Y]
- **[Game B]**: Take [Z]

## Risks & Mitigation

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| [Risk] | [H/M/L] | [Strategy] |

## Prototype Plan
- **Minimal Test**: [What to build]
- **Extended Test**: [Follow-up validation]

## Cross-Pillar Impact
- Affects: [pillar] - [how]
- Affected by: [pillar] - [dependency]

## Open Questions
- [Question for later]
```

### Recommended Order

1. `game-loop` (P1) - Everything depends on this
2. Primary mechanic pillar (P1) - e.g., `combat-system` for roguelike
3. `player-experience` (P1) - Validates emotional goals
4. Secondary pillars (P2) - Based on dependencies

## Step 4: Validate Design

After completing 2+ pillars, run:
```
/validate-design
```

### What It Checks

1. **Vision Alignment** - Do pillars match game-brief?
2. **Cross-Pillar Coherence**
   - Contradictions (direct conflicts)
   - Tensions (pulling different directions)
   - Synergies (reinforcing each other)
3. **Gap Analysis**
   - Missing connections
   - Undefined areas
4. **Player Experience Simulation**
   - First session (0-30 min)
   - Core loop (typical session)
   - Long-term (10+ hours)

### Report Format

```
# Design Validation Report

## Summary
| Aspect | Status |
|--------|--------|
| Vision Alignment | ✅ |
| Cross-Coherence | ⚠️ |
| Gaps | ✅ |
| Player Journey | ⚠️ |

## Critical Issues
[None or list]

## Warnings
1. **[Title]**
   - Type: Tension
   - Pillars: [A] ↔ [B]
   - Problem: [Description]
   - Recommendation: [Action]

## Strengths
- [Synergy found]

## Recommended Actions
1. [Priority action]
2. [Secondary action]

## Next Pillar to Complete
→ [pillar-name] because [reason]
```

### READ-ONLY Command

`/validate-design` only produces a report. You must:
- Address critical issues via `/deep-dive`
- Accept tensions as design trade-offs
- Continue when coherence is acceptable

## Reusing Commands

### Re-run /brainstorm
- If `game-brief.md` exists → **Spark Mode**
- Gives fresh perspective without losing work

### Re-run /pillars
- **Overwrites** existing stubs
- Use carefully - completed pillars may be reset

### Re-run /deep-dive [pillar]
- Can re-develop any pillar
- Previous version is replaced
- Useful after significant pivot

## Common Issues

### "Pillar feels incomplete"
- Run `/deep-dive [pillar]` again
- Focus on unanswered questions
- Add more reference games

### "Pillars conflict with each other"
- Run `/validate-design` to identify tensions
- Decide which pillar takes priority
- Update the subordinate pillar

### "Too many pillars"
- Focus on P1 (core) pillars first
- Mark others as "Later" in `_index.md`
- Don't deep-dive everything at once

## Next: Planning Phase

Once you have:
- ✅ `game-brief.md` complete
- ✅ Core pillars (3-5) developed
- ✅ `validate-design` shows acceptable coherence

Continue to **[Part 3: Planning Phase](03-planning.md)** to prioritize features and design architecture.
