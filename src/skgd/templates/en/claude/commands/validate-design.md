# /validate-design - Cross-Pillar Coherence Check

You are Opus, performing a comprehensive coherence analysis across all design pillars.

## Model

**MANDATORY: opus** - Cross-pillar analysis requires deep understanding of game design interdependencies.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Purpose

This command:
- Checks coherence between all completed pillars
- Identifies contradictions and tensions
- Finds gaps in the design
- Suggests adjustments for alignment
- Validates against the game vision

**READ-ONLY ANALYSIS** - Does not modify files, only reports findings.

---

## Step 1: Load All Design Documents

Read:
- `docs/game-brief.md` - Core vision (SOURCE OF TRUTH)
- `docs/pillars/_index.md` - Pillar status
- All `docs/pillars/*.md` - All pillars (stubs and complete)

---

## Step 2: Categorize Pillars

```
Pillar Inventory:

✅ Complete ([N]):
- [pillar-1]
- [pillar-2]

⬜ Stub ([N]):
- [pillar-3]
- [pillar-4]

Not Started ([N]):
- [optional-1] (not generated)
```

**Minimum for validation:** At least 2 complete pillars.

If fewer than 2 complete:
```
Not enough pillars for meaningful validation.

Complete: [N] pillars
Required: 2+ pillars

Run /deep-dive [pillar] to develop more pillars first.
```

---

## Step 3: Vision Alignment Check

For EACH complete pillar, check alignment with game-brief:

### 3.1 Core Vision Match

```
Vision Alignment Check

Game Soul: "[Core vision statement from game-brief]"

Pillar Alignment:
✓ [pillar-1]: Directly supports through [mechanism]
✓ [pillar-2]: Supports through [mechanism]
⚠ [pillar-3]: Weak connection - [issue]
✗ [pillar-4]: Potential misalignment - [conflict]
```

### 3.2 Core Experience Match

```
Core Experience: "[Target experience from game-brief]"

Pillar Contributions:
[pillar-1] → [How it creates the experience]
[pillar-2] → [How it creates the experience]

Gaps:
- [Missing element that would enhance experience]
```

---

## Step 4: Cross-Pillar Coherence

Analyze pairs of complete pillars for:

### 4.1 Contradictions

Things that directly conflict:

```
Contradiction Analysis

✗ CONFLICT: [pillar-A] vs [pillar-B]
  - [pillar-A] says: "[statement/decision]"
  - [pillar-B] says: "[contradicting statement]"
  - Impact: [What breaks if both are true]
  - Resolution options:
    A) Adjust [pillar-A]: [how]
    B) Adjust [pillar-B]: [how]
    C) Both can coexist if: [condition]
```

### 4.2 Tensions

Things that pull in different directions:

```
Tension Analysis

⚠ TENSION: [pillar-A] vs [pillar-B]
  - [pillar-A] pushes toward: [direction]
  - [pillar-B] pushes toward: [different direction]
  - This creates: [player experience tension]
  - Severity: Low/Medium/High
  - Recommendation: [How to resolve or embrace]
```

### 4.3 Synergies

Positive reinforcement between pillars:

```
Synergy Analysis

✓ SYNERGY: [pillar-A] + [pillar-B]
  - [pillar-A]'s [element] enhances [pillar-B]'s [element]
  - Combined effect: [Emergent benefit]
  - Opportunity: [How to lean into this more]
```

---

## Step 5: Gap Analysis

### 5.1 Missing Connections

```
Gap Analysis

Pillars that should interact but don't:

⬜ [pillar-A] → [pillar-B]
   Expected: [What connection should exist]
   Current: No explicit connection defined
   Risk: [What could go wrong]
   Action: Address in /deep-dive [pillar]

⬜ [pillar-B] → [pillar-C]
   Expected: [Connection]
   Current: Missing
   Action: [What to do]
```

### 5.2 Undefined Areas

```
Design Blind Spots

Areas that affect multiple pillars but aren't addressed:

1. [Blind spot 1]
   Affects: [pillar-A], [pillar-B]
   Suggest: Add to [pillar] or create new pillar

2. [Blind spot 2]
   Affects: [list]
   Suggest: [Action]
```

### 5.3 Stub Impact Assessment

```
Stub Risk Assessment

These incomplete pillars may create issues:

⚠ [stub-pillar] (stub)
   Blocked decisions in:
   - [pillar-A]: [What can't be finalized]
   - [pillar-B]: [What can't be finalized]
   Priority: Complete this stub next
```

---

## Step 6: Player Experience Simulation

Walk through the player experience using all pillars:

```
Player Journey Coherence

First Session (0-30 min):
1. Player encounters: [from pillar-X]
2. Player feels: [from player-experience]
3. Player does: [from game-loop]
→ Coherent? [Yes/Issues]

Core Loop (typical session):
1. [Step from game-loop]
2. [Interaction from combat/puzzle/etc]
3. [Progression from progression pillar]
→ Coherent? [Yes/Issues]

Long-term (10+ hours):
1. [Meta progression]
2. [Content variety from level-design/enemy-design]
3. [Maintained engagement from game-loop]
→ Coherent? [Yes/Issues]
```

---

## Step 7: Generate Report

```markdown
# Design Validation Report

*Game: [Name]*
*Date: [timestamp]*
*Pillars Analyzed: [N] complete, [N] stubs*

## Summary

| Aspect | Status | Issues |
|--------|--------|--------|
| Vision Alignment | ✓/⚠/✗ | [count] |
| Cross-Pillar Coherence | ✓/⚠/✗ | [count] |
| Gap Coverage | ✓/⚠/✗ | [count] |
| Player Journey | ✓/⚠/✗ | [count] |

**Overall Health:** [Good/Needs Attention/Critical Issues]

## Critical Issues ([N])

### Issue 1: [Title]
**Type:** Contradiction/Gap/Misalignment
**Severity:** Critical
**Pillars:** [list]
**Problem:** [Description]
**Recommendation:** [Action]

### Issue 2: [Title]
...

## Warnings ([N])

### Warning 1: [Title]
**Type:** Tension/Minor Gap
**Severity:** Medium
**Recommendation:** [Action]

## Strengths ([N])

### Strength 1: [Title]
[What's working well]

### Strength 2: [Title]
[Synergy or strong alignment]

## Recommended Actions

Priority order:

1. **[Action 1]** - Fixes [issue]
   Command: /deep-dive [pillar]

2. **[Action 2]** - Addresses [warning]
   Command: [command]

3. **[Action 3]**
   ...

## Next Pillar to Complete

Based on analysis, prioritize: **[pillar-name]**
Reason: [Why this pillar next]

---
*Report generated by /validate-design*
```

---

## Step 8: Output Summary

```
Design Validation Complete

Health: [Good/Needs Attention/Critical]

  ✗ [N] Critical issues
  ⚠ [N] Warnings
  ✓ [N] Strengths/synergies

Top Issues:
1. [Issue] → /deep-dive [pillar]
2. [Issue] → [action]

Recommended next steps:
  /deep-dive [pillar] - Address [issue]
  /brainstorm         - Get fresh perspective on [tension]

Full report displayed above.
```

---

## Validation Heuristics

### Common Contradictions to Check

| Pillar A | Pillar B | Common Conflict |
|----------|----------|-----------------|
| game-loop | progression | Pacing mismatch |
| combat | difficulty-curve | Power curve vs challenge |
| player-experience | game-loop | Emotion vs mechanics |
| level-design | progression | Content gating |
| art-direction | player-experience | Mood mismatch |

### Common Gaps to Check

| Area | Usually Defined In | Check For |
|------|-------------------|-----------|
| Onboarding | game-loop, level-design | First hour experience |
| Difficulty | combat, progression, enemy-design | Consistent philosophy |
| Feedback | player-experience, UI | Clear communication |
| Pacing | game-loop, level-design | Variety and rhythm |

---

## Remember

- **Vision is truth** - game-brief.md is the source of truth
- **Tensions aren't always bad** - Some create interesting design
- **Gaps are normal** - Flag for future attention
- **Actionable output** - Every issue needs a suggested fix
- **Read-only** - Never modify files, only analyze
