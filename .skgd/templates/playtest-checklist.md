# Playtest Checklist Template

> Base template for feature playtesting

## Test Session Info
- **Feature:** [Feature name]
- **Tester:** [Name]
- **Date:** [Date]
- **Build:** [Version/Commit]

---

## Automated Tests

### EditMode Tests
- [ ] All tests pass
- **Result:** [ ] Pass [ ] Fail
- **Details:** _____________

### PlayMode Tests
- [ ] All tests pass
- **Result:** [ ] Pass [ ] Fail
- **Details:** _____________

---

## Console Status

### Before Play
- [ ] Console cleared
- [ ] No existing errors

### After Play
| Type | Count | Critical? |
|------|-------|-----------|
| Errors | | [ ] Yes [ ] No |
| Warnings | | [ ] Yes [ ] No |

### Issues Found
| Message | Severity | Action |
|---------|----------|--------|
| | | |

---

## Acceptance Criteria

> From spec - each must pass

### AC-1: [Criterion from spec]
- **Test Steps:**
  1. [Step]
  2. [Step]
- **Expected:** [Result]
- **Actual:** _____________
- **Result:** [ ] Pass [ ] Fail

### AC-2: [Criterion]
- **Test Steps:**
  1. [Step]
  2. [Step]
- **Expected:** [Result]
- **Actual:** _____________
- **Result:** [ ] Pass [ ] Fail

### AC-3: [Criterion]
- **Test Steps:**
  1. [Step]
  2. [Step]
- **Expected:** [Result]
- **Actual:** _____________
- **Result:** [ ] Pass [ ] Fail

---

## Edge Cases

> From spec edge cases

### Edge 1: [Edge case]
- **Trigger:** [How to cause]
- **Expected:** [Behavior]
- **Actual:** _____________
- **Result:** [ ] Pass [ ] Fail

### Edge 2: [Edge case]
- **Trigger:** [How to cause]
- **Expected:** [Behavior]
- **Actual:** _____________
- **Result:** [ ] Pass [ ] Fail

---

## Game Feel Assessment

### Responsiveness
- [ ] Input feels immediate (< 100ms perceived)
- [ ] No input lag
- [ ] No dropped inputs
- **Notes:** _____________

### Feedback
- [ ] Actions have clear visual feedback
- [ ] Sound feedback present (or noted as TODO)
- [ ] State changes are obvious
- **Notes:** _____________

### Consistency
- [ ] Same input = same result
- [ ] Behavior predictable
- [ ] No unexpected edge cases
- **Notes:** _____________

### Polish
- [ ] No visual glitches
- [ ] No animation pops
- [ ] Smooth transitions
- **Notes:** _____________

---

## Performance

### Frame Rate
- [ ] Stable at target FPS
- [ ] No significant drops
- **Measured:** _____ FPS (avg)

### Responsiveness
- [ ] No freezes
- [ ] No stuttering
- [ ] Scene loads quickly

### Memory
- [ ] No obvious leaks (play 5 min)
- [ ] Memory stable

---

## Free-Form Observations

### What Works Well
-
-

### What Needs Improvement
-
-

### Unexpected Behaviors
-
-

### Ideas/Suggestions
-
-

---

## Bugs Found

| ID | Description | Severity | Repro Steps | Status |
|----|-------------|----------|-------------|--------|
| B1 | | [ ] Blocker [ ] Critical [ ] Major [ ] Minor | | [ ] Open |
| B2 | | | | |
| B3 | | | | |

---

## Summary

### Criteria Met
- Acceptance: [X]/[Total]
- Edge Cases: [X]/[Total]
- Game Feel: [X]/[Total]

### Overall Verdict
[ ] **PASS** - All criteria met, ready to proceed
[ ] **CONDITIONAL** - Minor issues, can proceed with noted items
[ ] **FAIL** - Blocking issues, needs fixes

### Blocking Issues
1. [If any]

### Next Actions
- [ ] [Action needed]
- [ ] [Action needed]

---

*Tested by: Tester Agent*
*Template version: 1.0*
