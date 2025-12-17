# Scout Helper (Internal)

> **Internal documentation for the Scout-First pattern.**
> This file is NOT a callable command. It documents the pattern for other commands to reference.

## Purpose

Sub-agent pattern for context gathering BEFORE creative/analytical commands.
Reduces context pollution in main Opus agent by delegating file reads to Haiku.

## Benefits (Validated by Research)

- **-52% token costs** - Haiku reads files, Opus gets summary
- **+2.6% solve rate** - Cleaner context = better decisions
- **Separation of concerns** - Scout gathers, Opus creates

---

## Usage in Commands

Commands that need context should add a **Phase 0** before their main workflow:

```markdown
## Phase 0: Scout Context

BEFORE any other step, use Task tool:
- subagent_type: 'Explore'
- model: 'haiku'
- prompt: |
    [Command-specific instructions]

    Return Scout Report format (max 500 tokens).
```

### Task Tool Parameters

```yaml
Task:
  subagent_type: 'Explore'
  model: 'haiku'
  prompt: |
    [Specific files to read]
    [What to extract]
    [Return Scout Report format]
```

---

## Scout Report Format Standard

```markdown
## Scout Report: [command-name]

**Status:** ready | blocked | partial
**Key Context:**
- [Bullet point 1 - most important finding]
- [Bullet point 2 - key decision or state]
- [Bullet point 3 - relevant constraint]

**Missing:** [List missing files] or "none"
**Token Estimate:** ~[count] tokens
```

### Status Definitions

| Status | Meaning | Action |
|--------|---------|--------|
| `ready` | All required files found, context complete | Proceed with command |
| `blocked` | Critical files missing | Stop, inform user |
| `partial` | Some files missing, can proceed with caveats | Proceed with warnings |

---

## Rules for Scouts

1. **Max 500 tokens output** - Summarize, don't dump
2. **Read-only** - Never write files
3. **Return summary, not raw content** - Extract insights, not text
4. **Identify gaps** - Report what's missing
5. **Stay focused** - Only gather what the command needs

---

## Commands Using Scout-First

| Command | Scout Target | Key Extractions |
|---------|--------------|-----------------|
| `/deep-dive` | pillars/*.md, game-brief.md | Pillar status, decisions, questions |
| `/validate-design` | All pillars | Cross-pillar coherence data |
| `/crystallize` | learnings.md | Pattern candidates, entry count |
| `/analyze` | specs/*.md, architecture.md | Cross-artifact relationships |

---

## Commands WITHOUT Scout (Already Efficient)

- `/brainstorm` - Minimal context by design (creative freedom)
- `/continue` - Router, not context-heavy
- `/implement-*` - Uses Task tool for exploration already
- `/playtest` - Focused on current spec only

---

## Example: Scout for /deep-dive

```yaml
Task:
  subagent_type: 'Explore'
  model: 'haiku'
  prompt: |
    Scout the pillars system for deep-dive on [pillar-name]:

    1. Read docs/pillars/_index.md - extract pillar list with completion status
    2. For each COMPLETED pillar (marked ✅), extract 2-3 key decisions
    3. Read docs/pillars/[pillar-name].md - get stub questions
    4. Read docs/game-brief.md - extract core vision (3-5 bullets)
    5. Identify potential cross-pillar tensions

    Return Scout Report format (max 500 tokens):

    ## Scout Report: deep-dive [pillar-name]
    **Status:** [ready/blocked/partial]
    **Pillar Progress:** [N]/[M] complete
    **Key Context:** [vision bullets]
    **Completed Decisions:** [from done pillars]
    **Target Questions:** [from stub]
    **Potential Tensions:** [if any]
    **Missing:** [files not found]
```

---

## Anti-Patterns

```
BAD: Scout returns full file contents
GOOD: Scout returns summarized insights

BAD: Scout writes files or modifies state
GOOD: Scout is strictly read-only

BAD: Scout output exceeds 500 tokens
GOOD: Scout prioritizes and truncates

BAD: Main command does inline reads after Scout
GOOD: Main command trusts Scout Report
```

---

*Version: 3.4*
*Pattern validated: MetaGPT, Claude Flow, Google ADK research*
