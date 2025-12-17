# /next - Zero-Friction Continue

You are executing the SINGLE next action with zero friction. No questions, no options.

**Philosophy:** The user said "next". Just do it.

## Model

**MANDATORY: sonnet** - Quick routing and execution.

## Step 1: Read State (Fast)

Read ONLY `.skgd/state.yaml` - nothing else.

Extract:
- `phase` - Current workflow phase
- `production.current_spec` - Active feature
- `production.current_step` - Current step
- `implementation.active` - Is implementation running?
- `implementation.next_task` - Next task ID

## Step 2: Determine Single Next Action

### Decision Tree (in order):

```
IF implementation.active == true AND next_task exists:
    → Execute that task immediately

ELSE IF production.current_step == "implement":
    → Run /implement continue

ELSE IF production.current_step == "playtest":
    → Run /playtest

ELSE IF production.current_step == "tasks":
    → Run /implement (start implementation)

ELSE IF production.current_step == "plan":
    → Run /tasks

ELSE IF production.current_step == "spec":
    → Run /plan [current_spec]

ELSE IF production.current_spec exists BUT current_step is null:
    → Feature complete! Show completion message

ELSE IF phase == "production" AND no current_spec:
    → Run /continue (to pick next feature)

ELSE IF phase == "architecture":
    → Run /roadmap or /spec (whichever makes sense)

ELSE IF phase == "design":
    → Run /architecture

ELSE IF phase == "concept":
    → Run /pillars or /brainstorm

ELSE:
    → Show: "Not sure what's next. Try /project-status"
```

## Step 3: Execute Immediately

**DO NOT ask confirmation.** Just execute the determined action.

Display brief context:
```
→ [action description]
```

Then execute.

### Examples:

**If next task is T016:**
```
→ Implementing T016: Add coyote time buffer

[Immediately starts working on T016]
```

**If implementation needs to continue:**
```
→ Resuming implementation: movement-system (15/30 tasks)

[Runs /implement continue logic]
```

**If playtest needed:**
```
→ Running playtest for: movement-system

[Runs /playtest logic]
```

**If feature complete:**
```
✓ Feature complete: movement-system

Playtested and verified. Ready for next feature.
Run /continue to select next feature from roadmap.
```

## Step 4: Auto-Suggest (After Execution)

After completing the action, show ONE suggestion:

```
───────────────────────────────────────
Next: [brief description]
[Enter] to continue | [S] stop
───────────────────────────────────────
```

If user presses Enter or says "yes", loop back to Step 1.
If user says "stop" or anything else, exit.

## Anti-Patterns

- **NEVER** show multiple options
- **NEVER** ask clarifying questions
- **NEVER** read files beyond state.yaml for routing
- **NEVER** hesitate - just execute

## Edge Cases

### No Clear Next Action
```
🤔 Not sure what's next.

Current state:
  Phase: [phase]
  Feature: [feature or "none"]
  Step: [step or "none"]

Try:
  /project-status  - See full dashboard
  /continue        - Smart routing with options
```

### Error in Previous Step
If state shows error or blocked status:
```
⚠️ Previous step encountered an issue.

Use /continue for guided recovery.
```

## Summary

`/next` = Read state → Determine action → Execute immediately → Suggest next

**Maximum vibe-coding energy. Zero friction.**
