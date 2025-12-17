# /playtest - Run Tests and Validation

You are running automated tests and generating a manual playtest checklist.

## Your Task

### Step 1: Load Context

Read:
- `.skgd/state.yaml` - Current feature
- `docs/specs/[feature]/spec.md` - Acceptance criteria
- `docs/specs/[feature]/tasks.md` - Implementation status
- `.skgd/templates/playtest-checklist.md` - Checklist template

### Step 2: Run Unity Automated Tests

#### EditMode Tests
```yaml
mcp__UnityMCP__run_tests:
  mode: "EditMode"
  timeout_seconds: 60
```

#### PlayMode Tests
```yaml
mcp__UnityMCP__run_tests:
  mode: "PlayMode"
  timeout_seconds: 120
```

### Step 3: Check Console State

```yaml
mcp__UnityMCP__read_console:
  types: ["error", "warning"]
  count: 50
```

Categorize issues:
- **Blockers**: Errors that prevent gameplay
- **Warnings**: Non-critical issues to track
- **Info**: Informational messages

### Step 4: Generate Playtest Checklist

Create/update `docs/specs/[feature]/playtest.md`:

```markdown
# [Feature Name] - Playtest Checklist

## Automated Test Results
- EditMode: [✓ Passed / ✗ Failed] ([N] tests)
- PlayMode: [✓ Passed / ✗ Failed] ([N] tests)

## Console Status
- Errors: [N]
- Warnings: [N]

### Issues Found
| Type | Message | Severity | Status |
|------|---------|----------|--------|
| [Error/Warning] | [message] | [High/Med/Low] | [Open/Fixed] |

---

## Manual Playtest Checklist

### Core Functionality
Based on acceptance criteria from spec:

- [ ] **AC-1**: [Criterion from spec]
  - Steps: [How to test]
  - Expected: [Expected result]
  - Actual: _____________

- [ ] **AC-2**: [Criterion]
  - Steps: [How to test]
  - Expected: [Expected result]
  - Actual: _____________

### Edge Cases
From spec edge cases:

- [ ] **Edge 1**: [Edge case]
  - Test: [How to trigger]
  - Expected: [Behavior]
  - Actual: _____________

### Feel & Polish
Game-specific quality checks:

- [ ] **Responsiveness**: Input feels immediate
- [ ] **Feedback**: Actions have clear feedback
- [ ] **Consistency**: Behavior is predictable
- [ ] **No Jank**: No visual glitches or stutters

### Performance
- [ ] **Frame Rate**: Stable [target] FPS
- [ ] **No Freezes**: No frame drops during gameplay
- [ ] **Memory**: No obvious memory leaks

---

## Playtest Session

### Tester
Name: _____________
Date: _____________

### Session Notes
[Free-form observations during play]

### Bugs Found
| ID | Description | Severity | Repro Steps |
|----|-------------|----------|-------------|
| B1 | | | |

### Suggestions
[Ideas for improvement that emerged during play]

---

## Summary

### Pass/Fail
- [ ] All acceptance criteria met
- [ ] No blocking bugs
- [ ] Performance acceptable

### Verdict
[ ] **PASS** - Ready for completion
[ ] **FAIL** - Needs fixes (see issues above)

### Next Action
If PASS: `/continue` or mark feature done
If FAIL: Fix issues, then `/playtest` again
```

### Step 5: Interactive Playtest Guide

If user wants to do manual playtest now, guide them:

```
🎮 Starting Playtest Session

I'll put Unity in Play mode. Follow the checklist above.

1. Opening Play mode...
```

```yaml
mcp__UnityMCP__manage_editor:
  action: "play"
```

```
2. Test each checklist item
3. Note results in playtest.md
4. When done, tell me to stop

Commands during playtest:
- "stop" - Exit play mode
- "console" - Check for errors
- "bug [description]" - Log a bug
- "done" - Complete playtest
```

### Step 6: Process Results

After playtest:

1. **If all pass:**
   - Update state to ready for completion
   - Suggest marking feature done

2. **If failures:**
   - List issues to fix
   - Keep state at playtest
   - Suggest fixing then re-running

### Step 7: Extract & Save Learnings (Automatic)

Based on the playtest results, extract and categorize learnings:

#### 7.1 Categorize Findings

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

#### 7.2 Append to learnings.md

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

#### 7.3 Update Metadata

At the bottom of learnings.md, update the metadata:
```markdown
*Entries: [new count]*
*Last updated: [YYYY-MM-DD]*
```

#### 7.4 Check Crystallization Trigger

Count total entries in learnings.md (lines starting with `- ` under subsections).

**If >30 entries:** Display suggestion:
```
Learnings growing ([N] entries). Consider running /crystallize to consolidate patterns.
```

### Step 8: Update State

```yaml
# If passed:
production:
  current_step: null  # Ready for next feature
specs:
  completed: [increment]
  in_progress: null

# If failed:
production:
  current_step: implement  # Back to fix
```

### Step 9: Git Commit

```bash
git add docs/specs/[feature]/playtest.md .skgd/
git commit -m "test([feature]): playtest results

- Automated: [Pass/Fail]
- Manual: [N]/[N] checks passed
- Issues: [N] found"
```

### Step 10: Summary

```
🧪 Playtest Complete: [feature-name]

Automated Tests:
  EditMode: [✓/✗]
  PlayMode: [✓/✗]

Manual Checks: [N]/[N] passed

Verdict: [PASS ✓ / FAIL ✗]
```

### Step 11: Auto-Suggest

After displaying the summary, show context-appropriate prompt:

**If PASS:**
```
───────────────────────────────────────
✓ Feature complete! Next: Select next feature
[Enter] /continue | [S] stop | [M] snapshot milestone
───────────────────────────────────────
```

- **Enter**: Execute `/continue` to select next feature
- **S**: Stop for now
- **M**: Execute `/snapshot` to save milestone

**If FAIL:**
```
───────────────────────────────────────
✗ Issues found. Fix and retest.

Issues to fix:
1. [Issue 1]
2. [Issue 2]

[Enter] retest | [S] stop
───────────────────────────────────────
```

- **Enter**: Execute `/playtest` again after fixes
- **S**: Stop for now (issues tracked in playtest.md)

## Model
Use: **sonnet** (testing and validation task)
