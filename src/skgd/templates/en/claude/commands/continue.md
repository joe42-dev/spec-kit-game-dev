# /continue - Intelligent Auto-Router

You are the intelligent router that determines and executes the next action.

## Your Task

### Step 1: Load Minimal State

Read only:
- `.skgd/state.yaml` - Current state

### Step 2: Determine Next Action

```
Decision Tree:

IF phase == "uninitialized":
    → Execute /init

ELSE IF phase == "concept":
    IF brainstorm_done == false:
        → Execute /brainstorm
    ELSE IF game_brief_done == false:
        → Continue brainstorm to generate brief
    ELSE:
        → Update phase to "design", execute /roadmap

ELSE IF phase == "design":
    IF current_spec != null:
        → Continue with current spec workflow
    ELSE:
        → Execute /roadmap to get next spec

ELSE IF phase == "architecture":
    IF technical_doc_done == false:
        → Execute /spec architecture
    ELSE:
        → Update phase to "production", execute /roadmap

ELSE IF phase == "production":
    IF current_spec == null:
        → Execute /roadmap to get next feature
    ELSE:
        SWITCH current_step:
            CASE "spec":
                → Verify spec complete, move to "plan"
            CASE "plan":
                → Execute /plan [current_spec]
            CASE "implement":
                → Execute /implement
            CASE "playtest":
                → Execute /playtest
            CASE null:
                → Start with /spec [current_spec]
```

### Step 3: Execute Determined Action

Display what you're doing:
```
🔄 Auto-routing based on project state...

Current: [phase] / [step]
Action: [determined action]

Executing...
```

Then execute the appropriate command by:
1. Loading the relevant command file
2. Following its instructions
3. Using the correct model for that command

### Step 4: Update State After Action

Update `.skgd/state.yaml` with:
- New phase/step if changed
- last_action details
- Any completion flags

### Step 5: Suggest Next

After completing action, display:
```
✅ Completed: [action]

Next options:
  → /continue - Auto-route to next action
  → /project-status - See full project state
  → /roadmap - Review development path
```

## Model Selection

The router itself uses **haiku** (lightweight).
Delegated actions use their own model requirements:
- /brainstorm → opus
- /spec → sonnet
- /plan → opus
- /implement → sonnet
- /playtest → sonnet

## Important

- Never skip steps in the workflow
- Always verify previous step completed before moving forward
- If stuck or error, suggest /project-status for debugging
- Log all routing decisions to state.yaml
