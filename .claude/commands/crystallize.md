# /crystallize - Compress & Distill Project Learnings

You are Opus, compressing accumulated knowledge into actionable patterns.

## Model

**MANDATORY: opus** - Pattern recognition and synthesis requires deep analysis.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Purpose

Over time, `learnings.md` accumulates raw observations. This command **crystallizes** them into high-signal patterns, keeping the knowledge base compact and powerful.

Inspired by compound engineering: extract patterns, not just text.

## Model

**MANDATORY: opus** - Pattern recognition and synthesis requires deep analysis.

## When to Use

- `learnings.md` exceeds 50 lines
- End of a major milestone
- Before a `/pivot`
- Periodically (every 5-10 features)

## The Living Memory Architecture

```
LAYER 1: constitution.md (~500 tokens)
├── Immutable core vision
├── 5 max design principles
└── Technical constraints
    NEVER modified except by /pivot

LAYER 2: learnings-core.md (~1000 tokens) ← OUTPUT OF THIS COMMAND
├── Top 10 validated patterns
├── Anti-patterns confirmed
└── Key architectural decisions + WHY

LAYER 3: learnings.md (unlimited, raw)
├── Session observations
├── Playtest notes
└── Technical discoveries
    Gets compressed → learnings-core.md
```

## Step 1: Load Raw Learnings

Read:
- `.skgd/memory/learnings.md` - Raw accumulated learnings
- `.skgd/memory/learnings-core.md` - If exists, current crystallized patterns
- `.skgd/memory/constitution.md` - Core principles for alignment check

## Step 2: Pattern Extraction

Analyze learnings for:

### Technical Patterns
- What Unity patterns work well?
- What approaches caused problems?
- Performance insights?
- Architecture decisions that paid off?

### Design Patterns
- What mechanics feel good?
- What player feedback themes emerge?
- What scope decisions were right/wrong?

### Process Patterns
- What speeds up development?
- What slows it down?
- Common bugs and their root causes?

## Step 3: Crystallization Rules

**INCLUDE in learnings-core.md:**
- Patterns observed 2+ times
- Decisions with clear rationale
- Anti-patterns with evidence
- Numbers/values that work (e.g., "0.1s buffer feels right")

**EXCLUDE (keep in learnings.md archive):**
- One-off observations
- Context-specific notes
- Speculation without evidence
- Redundant entries

## Step 4: Generate learnings-core.md

Create/update `.skgd/memory/learnings-core.md`:

```markdown
# Crystallized Learnings

*Last crystallized: [date]*
*Source sessions: [count]*

## Technical Patterns (Validated)

### Unity Architecture
| Pattern | Evidence | Confidence |
|---------|----------|------------|
| [Pattern] | [Where validated] | HIGH/MED |

### Performance
- [Validated insight with numbers]

### Code Standards
- [Validated practice]

## Design Patterns (Validated)

### Mechanics
| Mechanic | Sweet Spot | Evidence |
|----------|------------|----------|
| [e.g., Jump buffer] | 0.1s | 3 playtests |

### Feel
- [What makes the game feel good]

## Anti-Patterns (Confirmed)

| Don't Do | Why | Learned From |
|----------|-----|--------------|
| [Anti-pattern] | [Consequence] | [Feature/session] |

## Key Decisions & Rationale

| Decision | Choice | Why | Date |
|----------|--------|-----|------|
| [Decision] | [What we chose] | [Rationale] | [When] |

## Process Insights

### What Speeds Us Up
- [Practice]

### What Slows Us Down
- [Practice to avoid]

---
*Confidence levels: HIGH (3+ validations), MED (2 validations)*
*Review at next milestone or /crystallize*
```

## Step 5: Archive Raw Learnings

Move processed content from `learnings.md` to archive:

Create `.skgd/memory/learnings-archive/[date].md`:
```markdown
# Learnings Archive - [date]

*Crystallized into learnings-core.md*

[Original content from learnings.md]
```

Then reset `learnings.md`:
```markdown
# Session Learnings

*Active observations - crystallize periodically with /crystallize*

## Recent Sessions

[Empty - ready for new observations]
```

## Step 6: Validation

Present summary:
```
## Crystallization Complete

Processed: [N] raw observations
Extracted: [N] validated patterns

New patterns added:
- [Pattern 1]
- [Pattern 2]

Patterns strengthened (more evidence):
- [Pattern with increased confidence]

Archive created: .skgd/memory/learnings-archive/[date].md

learnings.md reset and ready for new observations.
```

## Step 7: Git Commit

```bash
git add .skgd/memory/
git commit -m "chore: crystallize learnings into validated patterns

Processed [N] observations into [N] patterns
Archive: learnings-archive/[date].md"
```

## Context Budget Impact

**Before crystallization:**
- learnings.md: ~2000+ tokens (growing)
- Constitution: ~500 tokens
- Total memory load: 2500+ tokens

**After crystallization:**
- learnings-core.md: ~1000 tokens (fixed)
- Constitution: ~500 tokens
- learnings.md: ~100 tokens (reset)
- Total memory load: ~1600 tokens (stable)

## Auto-Trigger Suggestion

Add to `/playtest` end:
```
IF learnings.md > 50 lines:
    Suggest: "Learnings are accumulating. Consider /crystallize"
```

## Remember

- **Patterns > Observations**: Extract the WHY, not just the WHAT
- **Evidence matters**: Only crystallize validated insights
- **Keep it compact**: learnings-core.md should stay under 1000 tokens
- **Archive, don't delete**: Raw learnings preserved for reference
