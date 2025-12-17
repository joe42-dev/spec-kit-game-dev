# /tasks [feature-name] - Generate Actionable Task List

You are Opus, generating an actionable, dependency-ordered task list for implementation.

**Argument:** `$ARGUMENTS` (feature name, defaults to current_spec from state)

## Model

**MANDATORY: opus** - Task decomposition requires understanding architecture, dependencies, and execution order.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Philosophy

**SEPARATION OF CONCERNS:**
- `/plan` = HOW to architect (technical decisions, patterns, structure)
- `/tasks` = WHAT to execute (ordered checklist, dependencies, parallelization)

**DO NOT delegate to a sub-agent.** You create tasks directly from design artifacts.

## Step 1: Validate Prerequisites

Check these exist in `docs/specs/[feature]/`:
- `spec.md` - **REQUIRED** (user stories, acceptance criteria)
- `plan.md` - **REQUIRED** (technical approach, phases, scripts)

If missing, inform user:
```
Missing prerequisites for /tasks:
- [ ] spec.md - Run /spec [feature] first
- [ ] plan.md - Run /plan [feature] first
```

## Step 2: Load Design Artifacts

**Always read:**
- `docs/specs/[feature]/spec.md` - User stories with priorities (P1, P2, P3)
- `docs/specs/[feature]/plan.md` - Technical phases, scripts to create
- `docs/architecture.md` - Project-wide patterns (if exists)

**Extract from spec.md:**
- User stories (US1, US2, US3...)
- Priority labels (P1, P2, P3)
- Acceptance criteria per story

**Extract from plan.md:**
- Implementation phases
- Scripts/files to create
- Dependencies between components
- Verification criteria

## Step 3: Map Stories to Tasks

For each user story from spec.md:

1. **Identify components needed** (from plan.md):
   - Scripts to create
   - GameObjects/Nodes to set up
   - Data assets to create
   - UI elements

2. **Order within story:**
   ```
   Setup → Data/Models → Logic/Systems → Integration → Verification
   ```

3. **Mark parallelizable tasks:**
   - Different files with no shared dependencies = [P]
   - Same file or dependent = sequential

## Step 4: Generate tasks.md

Create `docs/specs/[feature-name]/tasks.md`:

```markdown
# [Feature Name] - Tasks

*Generated from: spec.md + plan.md*
*Total tasks: [N] | Stories: [N] | Parallel opportunities: [N]*

## Task Format Legend
- `T###` - Task ID (execution order)
- `[P]` - Parallelizable (can run with other [P] tasks)
- `[US#]` - User Story reference
- All tasks include target file path

---

## Phase 1: Setup
*Goal: Project structure and dependencies ready*

- [ ] T001 Create folder structure per plan.md
- [ ] T002 [P] Create [DataType].cs in Assets/Scripts/Data/
- [ ] T003 [P] Create [ManagerBase].cs in Assets/Scripts/Core/

**Verification:** Folders exist, base scripts compile

---

## Phase 2: Foundation
*Goal: Shared systems that all stories depend on*
*MUST complete before any user story phase*

- [ ] T004 Implement [CoreSystem] in Assets/Scripts/Core/[System].cs
- [ ] T005 Create [SharedPrefab] in Assets/Prefabs/
- [ ] T006 [P] Set up [ScriptableObject] in Assets/Data/

**Verification:** Core systems functional, no console errors

**Dependencies:**
```
T004 (CoreSystem)
  ↓
T005 (Prefab uses CoreSystem)
  ↓
[User Story Phases]
```

---

## Phase 3: User Story 1 - [Story Title from spec.md]
*Priority: P1*
*Goal: [User story goal]*

### Acceptance Criteria (from spec.md)
- [ ] AC1: [Criterion]
- [ ] AC2: [Criterion]

### Tasks
- [ ] T007 [US1] Create [Model].cs in Assets/Scripts/[Feature]/
- [ ] T008 [US1] Implement [Logic] in Assets/Scripts/[Feature]/[Script].cs
- [ ] T009 [P] [US1] Create [Prefab] in Assets/Prefabs/[Feature]/
- [ ] T010 [P] [US1] Set up [UI] in Assets/UI/[Feature]/
- [ ] T011 [US1] Integrate [Component] with [System]

**Verification:** [How to verify this story works independently]

**Story Test Scenario:**
```
1. [Step to test]
2. [Expected result]
3. [Edge case to verify]
```

---

## Phase 4: User Story 2 - [Story Title]
*Priority: P2*
*Goal: [User story goal]*
*Depends on: [US1 if applicable, or "Independent"]*

### Acceptance Criteria
- [ ] AC1: [Criterion]

### Tasks
- [ ] T012 [US2] [Task with file path]
- [ ] T013 [P] [US2] [Parallel task with file path]

**Verification:** [How to verify]

---

## Phase N: Polish & Cross-Cutting
*Goal: Quality, performance, edge cases*

- [ ] T0XX Optimize [specific system]
- [ ] T0XX Add error handling to [component]
- [ ] T0XX Clean up console warnings

**Verification:** Console clean, performance acceptable

---

## Dependency Graph

```
[Setup]
   ↓
[Foundation]
   ↓
[US1: P1] ←──────────┐
   ↓                 │ (if dependent)
[US2: P2] ───────────┘
   ↓
[Polish]
```

## Parallel Execution Map

**Can run simultaneously:**
- T002, T003 (different base files)
- T009, T010 (prefab + UI, no shared deps)

**Must be sequential:**
- T004 → T005 (prefab depends on system)
- T007 → T008 (logic depends on model)

## Implementation Strategy

**MVP (Minimum Viable):** Complete Phase 1-3 (Setup + Foundation + US1)
**Full Feature:** All phases including Polish

**Estimated task breakdown:**
- Setup: [N] tasks
- Foundation: [N] tasks
- User Stories: [N] tasks ([N] per story average)
- Polish: [N] tasks

---

*Created: [timestamp]*
*Source: docs/specs/[feature]/spec.md, plan.md*
*Ready for: /implement*
```

## Step 5: Validate Task Quality

Before saving, verify:

1. **Format compliance:**
   - [ ] Every task has checkbox `- [ ]`
   - [ ] Every task has ID (T001, T002...)
   - [ ] Story phase tasks have [US#] label
   - [ ] Every task has file path
   - [ ] [P] markers only on truly parallelizable tasks

2. **Coverage:**
   - [ ] All scripts from plan.md have creation tasks
   - [ ] All acceptance criteria have verification tasks
   - [ ] Each user story is independently testable

3. **Dependencies:**
   - [ ] Foundation tasks block story tasks
   - [ ] No circular dependencies
   - [ ] Dependency graph is accurate

## Step 6: Update State

```yaml
production:
  current_step: implement
  tasks_generated: true
```

## Step 7: Git Commit

```bash
git add docs/specs/[feature-name]/tasks.md
git commit -m "docs: tasks [feature-name]

Tasks: [total count]
Stories: [story count]
Parallel opportunities: [count]
MVP scope: Phase 1-3"
```

## Step 8: Summary

```
Tasks generated: [feature-name]

Location: docs/specs/[feature-name]/tasks.md

Summary:
- Total tasks: [N]
- User stories: [N]
- Parallel opportunities: [N]
- MVP scope: [phases]

Task breakdown:
- Setup: [N] tasks
- Foundation: [N] tasks
- [US1]: [N] tasks
- [US2]: [N] tasks
- Polish: [N] tasks

Ready for implementation:
  /implement - Execute tasks via Unity/Godot MCP
  /continue - Auto-route
```

## Task ID Reference

| ID Range | Phase |
|----------|-------|
| T001-T010 | Setup |
| T011-T020 | Foundation |
| T021-T0XX | User Stories |
| T0XX+ | Polish |

Adjust ranges based on actual task counts.

## Remember

- **User Story Focus**: Tasks serve stories, not technical layers
- **Independent Stories**: Each US should be testable alone when possible
- **Explicit Dependencies**: Never assume - always document what blocks what
- **Parallel = Speed**: Maximize [P] markers where safe
- **File Paths**: Always include exact path - no ambiguity for /implement
