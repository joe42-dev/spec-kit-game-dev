# SKGD Tutorial - Part 5: Validation

## Overview

Validation captures what works and what doesn't:

```
/playtest → /crystallize (when learnings accumulate)
```

## Step 1: Run Playtest

After `/implement` completes:
```
/playtest
```

### What It Does

1. **Runs Automated Tests**

   **Unity:**
   ```yaml
   mcp__UnityMCP__run_tests:
     mode: "EditMode"
   mcp__UnityMCP__run_tests:
     mode: "PlayMode"
   ```

   **Godot:**
   ```yaml
   mcp__gdai__run_gut_tests: {}
   ```

2. **Checks Console**
   - Errors (blocking)
   - Warnings (note)

3. **Generates Manual Checklist**
   From spec's Acceptance Criteria

4. **Guides Manual Testing**
   - Enters play mode
   - Walks through each AC
   - Records pass/fail

5. **Captures Game Feel**
   - Responsiveness (1-5)
   - Feedback (1-5)
   - Consistency (1-5)

6. **Auto-Extracts Learnings**
   Appends to `learnings.md`

### Output: playtest.md

```markdown
# Player Movement - Playtest Results

**Date:** 2024-01-15T14:30:00Z
**Build:** abc123

## Automated Tests

### EditMode
- Status: PASS
- Tests: 5
- Failures: 0

### PlayMode
- Status: PASS
- Tests: 3
- Failures: 0

## Manual Validation

| Criterion | Status | Notes |
|-----------|--------|-------|
| AC1: Move at 8 m/s | ✅ PASS | Measured 7.9-8.1 |
| AC2: Responsive | ✅ PASS | Feels good |
| AC3: Variable jump | ✅ PASS | Height varies correctly |
| AC4: Coyote time | ✅ PASS | 0.1s confirmed |

## Edge Cases

| Case | Expected | Actual | Status |
|------|----------|--------|--------|
| Wall collision | Stop | Stop | ✅ |
| Jump at edge | Coyote | Works | ✅ |

## Game Feel Assessment

- **Responsiveness:** 4/5 - Slight delay on direction change
- **Feedback:** 5/5 - Clear visual response
- **Consistency:** 5/5 - Same behavior every time

## Issues Found

| Issue | Severity | Description |
|-------|----------|-------------|
| Direction delay | Low | 1-2 frame delay on turn |

## Learnings

### What Worked
- CharacterController gives precise control
- Input System rebinding is clean
- Coyote time buffer pattern

### What Didn't
- Initial gravity too floaty
- First jump curve was linear (felt bad)

### For Future
- Always test jump feel early
- Gravity curves matter more than values

## Verdict

**PASS**

All AC met, minor polish items noted.
```

### Verdict Outcomes

| Verdict | Meaning | Next Step |
|---------|---------|-----------|
| **PASS** | All AC met | Feature complete → `/continue` |
| **CONDITIONAL** | Minor fixes needed | Fix → re-run `/playtest` |
| **FAIL** | Blocking issues | Back to `/implement` |

## Step 2: Review Learnings

After playtest, check:
```bash
cat .skgd/memory/learnings.md
```

### Learnings Structure

```markdown
# Session Learnings

*Entries: 15*
*Last updated: 2024-01-15*

## Technical Learnings

### Unity Patterns That Work
- [2024-01-15] player-movement: CharacterController better than Rigidbody for platformer

### Unity Patterns to Avoid
- [2024-01-15] player-movement: Don't use Rigidbody.MovePosition for character control

### Performance Insights
- [2024-01-15] player-movement: Ground check via SphereCast more reliable than raycast

## Design Learnings

### Mechanics That Feel Good
- [2024-01-15] player-movement: Coyote time 0.1s feels fair
- [2024-01-15] player-movement: Jump buffer 0.15s prevents missed jumps

### Mechanics That Need Work
- [2024-01-15] player-movement: Linear acceleration feels sluggish

## Process Learnings

### What Speeds Up Development
- [2024-01-15] player-movement: Test feel early, before full implementation

### What Slows Down Development
- [2024-01-15] player-movement: Tuning parameters without reference video
```

## Step 3: Crystallize (Periodic)

When learnings accumulate (50+ lines), run:
```
/crystallize
```

### What It Does

1. **Reads** `learnings.md`
2. **Identifies patterns** (2+ occurrences)
3. **Extracts validated insights** into `learnings-core.md`
4. **Archives** raw learnings to `learnings-archive/[date].md`
5. **Resets** `learnings.md`

### Crystallization Rules

**INCLUDE in learnings-core.md:**
- Patterns observed 2+ times
- Decisions with clear rationale
- Anti-patterns with evidence
- Numbers/values that work

**EXCLUDE (archive only):**
- One-off observations
- Context-specific notes
- Speculation without evidence

### Output: learnings-core.md

```markdown
# Crystallized Learnings

*Last crystallized: 2024-01-20*
*Source sessions: 5*

## Technical Patterns (Validated)

### Unity Architecture
| Pattern | Evidence | Confidence |
|---------|----------|------------|
| CharacterController for platformer | 3 features | HIGH |
| SphereCast for ground check | 2 features | HIGH |

### Performance
- Ground checks every frame is fine for single player
- Pool bullets at 50+ spawns/second

### Code Standards
- One script per behavior
- Events for cross-system communication

## Design Patterns (Validated)

### Mechanics
| Mechanic | Sweet Spot | Evidence |
|----------|------------|----------|
| Coyote time | 0.08-0.12s | 3 playtests |
| Jump buffer | 0.1-0.2s | 2 playtests |
| Attack buffer | 0.2s | 2 playtests |

### Feel
- Acceleration curves > linear
- Visual feedback within 1 frame

## Anti-Patterns (Confirmed)

| Don't Do | Why | Learned From |
|----------|-----|--------------|
| Rigidbody for precise movement | Unpredictable | player-movement |
| Find() in Update() | Performance | enemy-ai |

## Key Decisions & Rationale

| Decision | Choice | Why | Date |
|----------|--------|-----|------|
| Input System | New (not legacy) | Rebinding | 2024-01 |
| Physics | CharacterController | Control | 2024-01 |

## Process Insights

### What Speeds Us Up
- Reference videos before implementation
- Feel tests after each mechanic

### What Slows Us Down
- Tuning without reference
- Skipping edge case handling
```

### Token Budget Impact

Before crystallize:
- `learnings.md`: ~2000 tokens (and growing)

After crystallize:
- `learnings-core.md`: ~1000 tokens (stable)
- `learnings.md`: ~100 tokens (reset)

## Continuing the Cycle

After PASS verdict:

```
/continue
```

Routes to:
- Next feature in roadmap
- Or suggests `/crystallize` if learnings are large

### Feature Completion Flow

```
/playtest → PASS
    ↓
state.yaml updated:
  - production.current_spec: null
  - specs.completed: [feature]
    ↓
roadmap.yaml updated:
  - feature.status: completed
    ↓
/continue → Next feature
```

## Reusing Commands

### Re-run /playtest
- Generates new playtest.md
- Useful after fixing issues
- Previous results overwritten

### Re-run /crystallize
- Only useful when new learnings exist
- Safe to run anytime

## Common Issues

### "All tests pass but feels wrong"
- Game Feel Assessment is key
- Note specific issues
- Consider CONDITIONAL verdict

### "Learnings feel repetitive"
- Time to `/crystallize`
- Extract the patterns

### "Can't reproduce bug in playtest"
- Add to Edge Cases in spec
- Create specific test scenario

## Next: Utilities

Continue to **[Part 6: Utilities](06-utilities.md)** for session management, pivots, and snapshots.
