# /playtest - Validate Implementation

You are Opus, validating a feature implementation through testing.

## Model

**MANDATORY: opus** - Testing requires understanding acceptance criteria, analyzing results, and making quality judgments.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Philosophy

**DO NOT delegate to a sub-agent.** Testing requires:
- Understanding spec requirements deeply
- Interpreting test results intelligently
- Making judgment calls on edge cases
- Extracting learnings for crystallization

## Step 1: Load Context

Read:
- `.skgd/state.yaml` - Current spec
- `docs/specs/[feature]/spec.md` - Acceptance criteria
- `docs/specs/[feature]/tasks.md` - Implementation status
- `.skgd/memory/learnings-core.md` - Known patterns/issues

## Step 2: Run Automated Tests

### EditMode Tests
```yaml
mcp__UnityMCP__run_tests:
  mode: "EditMode"
```

### PlayMode Tests
```yaml
mcp__UnityMCP__run_tests:
  mode: "PlayMode"
```

### Console Check
```yaml
mcp__UnityMCP__read_console:
  types: ["error", "warning"]
  count: 20
```

## Step 3: Generate Manual Test Checklist

From spec acceptance criteria:

```markdown
## Manual Validation

### Acceptance Criteria
- [ ] AC-1: [Criterion] - How to verify: [steps]
- [ ] AC-2: [Criterion] - How to verify: [steps]

### Edge Cases
- [ ] [Edge case 1]: Expected [behavior]
- [ ] [Edge case 2]: Expected [behavior]

### Game Feel
- [ ] Responsiveness - Does input feel immediate?
- [ ] Feedback - Are actions clearly communicated?
- [ ] Consistency - Is behavior predictable?

### Integration
- [ ] Works with [related system]
- [ ] No conflicts with [other feature]
```

## Step 4: Facilitate Manual Testing

Enter play mode:
```yaml
mcp__UnityMCP__manage_editor:
  action: "play"
```

Guide user:
```
Entering Play Mode...

Please test:

1. [First test]
   Expected: [what should happen]

2. [Second test]
   Expected: [what should happen]

Report:
- What worked
- What didn't
- Anything that felt "off"
```

After testing:
```yaml
mcp__UnityMCP__manage_editor:
  action: "stop"
```

## Step 5: Document Results

Create `docs/specs/[feature]/playtest.md`:

```markdown
# [Feature] - Playtest Results

**Date:** [timestamp]
**Build:** [git commit]

## Automated Tests

### EditMode
- Status: [PASS/FAIL]
- Tests: [N]
- Failures: [list if any]

### PlayMode
- Status: [PASS/FAIL]
- Tests: [N]
- Failures: [list if any]

## Manual Validation

| Criterion | Status | Notes |
|-----------|--------|-------|
| AC-1 | [PASS/FAIL] | [observation] |
| AC-2 | [PASS/FAIL] | [observation] |

## Game Feel Assessment

- **Responsiveness:** [1-5] - [notes]
- **Feedback:** [1-5] - [notes]
- **Consistency:** [1-5] - [notes]

## Issues Found

| Issue | Severity | Description |
|-------|----------|-------------|
| [Issue] | [Blocker/Major/Minor] | [Details] |

## Learnings

### What Worked
- [Pattern that worked well]

### What Didn't
- [Pattern that caused issues]

### For Future
- [Insight to crystallize]

## Verdict

**[PASS / CONDITIONAL PASS / FAIL]**

Rationale: [Why]

[If CONDITIONAL:] Required fixes:
1. [Fix]

[If FAIL:] Blocking issues:
1. [Issue]
```

## Step 6: Extract & Save Learnings (Automatic)

Based on the playtest results above, extract and categorize learnings:

### 6.1 Categorize Findings

For each significant observation from the playtest, categorize into:

**Technical Learnings:**
- Unity Patterns That Work: [patterns that succeeded]
- Unity Patterns to Avoid: [patterns that caused issues]
- Performance Insights: [performance observations]

**Design Learnings:**
- Mechanics That Feel Good: [what felt right]
- Mechanics That Need Work: [what needs improvement]
- Player Feedback Themes: [recurring feedback patterns]

**Process Learnings:**
- What Speeds Up Development: [efficient practices discovered]
- What Slows Down Development: [bottlenecks identified]

**Bug Patterns:**
- Common Issues: [recurring bugs encountered]
- Solutions Found: [fixes that worked]

### 6.2 Append to learnings.md

Read `.skgd/memory/learnings.md` then APPEND findings under the appropriate subsection headers.

**Format for each finding:**
```markdown
- [YYYY-MM-DD] [feature]: [observation]
```

**Example appends:**
```markdown
### Unity Patterns That Work
<!-- Auto-populated -->
- 2024-01-15 player-movement: ScriptableObject events for input decoupling

### Mechanics That Feel Good
<!-- Auto-populated -->
- 2024-01-15 player-movement: Coyote time (0.15s) feels responsive
```

**Important:**
- Append under EXISTING subsection headers (don't create new sections)
- Keep `<!-- Auto-populated -->` comments in place
- One line per finding, prefixed with date and feature name

### 6.3 Update Metadata

At the bottom of learnings.md, update the metadata:
```markdown
*Entries: [new count]*
*Last updated: [YYYY-MM-DD]*
```

### 6.4 Check Crystallization Trigger

Count total entries in learnings.md (lines starting with `- ` under subsections).

**If >30 entries:** Display suggestion:
```
Learnings growing ([N] entries). Consider running /crystallize to consolidate patterns.
```

## Step 7: Update State

### If PASS:
```yaml
production:
  current_spec: null
  current_step: null

specs:
  completed: [increment]
  in_progress: null
```
Update roadmap: mark feature `completed`

### If CONDITIONAL PASS:
Keep state, list required fixes

### If FAIL:
```yaml
production:
  current_step: implement  # Back to fix
```

## Step 8: Git Commit

```bash
git add docs/specs/[feature]/playtest.md .skgd/
git commit -m "test([feature]): playtest - [VERDICT]

AC: [N]/[total] passed
Issues: [count]"
```

## Step 9: Summary

### If PASS:
```
PLAYTEST PASSED: [feature]

All acceptance criteria met.

Learnings captured.
[If > 50 lines: Consider /crystallize]

Next:
  /continue - Next feature
  /roadmap - Review progress
```

### If CONDITIONAL:
```
CONDITIONAL PASS: [feature]

Needs:
1. [Fix]

Fix, then /playtest again.
```

### If FAIL:
```
PLAYTEST FAILED: [feature]

Blocking:
1. [Issue]

/implement to fix.
```

## Remember

- **Be thorough**: Test ALL acceptance criteria
- **Be honest**: FAIL is better than broken feature
- **Capture learnings**: Every test teaches something
- **Game feel matters**: Technical pass =/= good experience
