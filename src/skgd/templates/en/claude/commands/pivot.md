# /pivot - Handle Major Direction Change

You are managing a significant change in game direction or scope.

## Your Task

### Step 1: Understand the Pivot

Ask the user (use AskUserQuestion):

1. **What's changing?**
   - Core mechanic change
   - Genre shift
   - Scope reduction/expansion
   - Target audience change
   - Platform change

2. **Why the pivot?**
   - Playtest feedback
   - Technical limitation
   - Creative evolution
   - Time/resource constraint

3. **What's the new direction?**
   - Free text description

### Step 2: Create Pre-Pivot Snapshot

Automatically create a snapshot before any changes:

```bash
# Auto-snapshot
/snapshot v[X.X]-pre-pivot
```

### Step 3: Load Full Context

Read ALL project documentation:
- `docs/game-brief.md`
- `docs/gdd.md`
- `docs/architecture.md`
- `docs/specs/*/spec.md`
- `.skgd/roadmap.yaml`
- `.skgd/memory/constitution.md`

### Step 4: Delegate Impact Analysis to Architect

Use Task tool with **opus** model:

```
Task: Analyze pivot impact

Agent: architect
Model: opus

Current State:
- Game brief: [summary]
- GDD sections: [list]
- Specs completed: [list]
- Specs in progress: [list]
- Architecture: [summary]

Pivot Description:
[User's description of change]

Analyze:
1. What existing work is invalidated?
2. What existing work can be preserved?
3. What new work is required?
4. What's the impact on timeline/scope?
5. What are the risks of this pivot?
6. Recommended approach for transition?
```

### Step 5: Generate Pivot Analysis Document

Create `docs/pivots/pivot-[N]-[date].md`:

```markdown
# Pivot Analysis #[N]

## Date
[timestamp]

## Trigger
[Why this pivot is happening]

## Change Summary
**From:** [Previous direction]
**To:** [New direction]

## Impact Analysis

### Documentation Impact

#### Invalidated (needs rewrite)
| Document | Reason | Effort |
|----------|--------|--------|
| [doc] | [why invalid] | High/Med/Low |

#### Preserved (still valid)
| Document | Notes |
|----------|-------|
| [doc] | [any minor updates needed] |

#### New Required
| Document | Description | Priority |
|----------|-------------|----------|
| [doc] | [what it covers] | High/Med/Low |

### Specs Impact

#### Keep As-Is
- [spec]: [why still valid]

#### Modify
- [spec]: [what changes needed]

#### Deprecate
- [spec]: [why no longer relevant]

#### New Required
- [spec]: [description]

### Code Impact

#### Keep
- [script/object]: [still needed]

#### Modify
- [script/object]: [changes needed]

#### Remove
- [script/object]: [no longer needed]

### Architecture Impact
[How technical architecture is affected]

## Transition Plan

### Phase 1: Documentation Update
1. Update constitution.md with new principles
2. Revise game-brief.md
3. Update/create relevant GDD sections

### Phase 2: Spec Cleanup
1. Archive deprecated specs
2. Modify affected specs
3. Create new required specs

### Phase 3: Code Cleanup
1. Remove deprecated code
2. Modify existing code
3. Update roadmap

### Phase 4: Resume Development
1. Generate new roadmap
2. Continue with /continue

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [risk] | High/Med/Low | High/Med/Low | [mitigation] |

## Recommendation

[Clear recommendation on how to proceed]

## Decision

[ ] **Proceed** with pivot as analyzed
[ ] **Modify** pivot scope (specify changes)
[ ] **Abort** pivot (keep current direction)

---
*Pre-pivot snapshot: v[X.X]-pre-pivot*
*Analysis by: Architect Agent*
```

### Step 6: Get User Decision

Use AskUserQuestion:
```
Pivot Analysis Complete

Impact Summary:
- [N] docs invalidated
- [N] specs to modify
- [N] new specs needed

Options:
1. Proceed with pivot
2. Modify pivot scope
3. Abort pivot (restore pre-pivot)

Your decision?
```

### Step 7: Execute Based on Decision

#### If Proceed:

1. Update `.skgd/memory/constitution.md` with new principles

2. Update `.skgd/state.yaml`:
```yaml
pivots:
  count: [increment]
  history:
    - version: [N]
      date: [timestamp]
      from: [old direction]
      to: [new direction]
      snapshot: v[X.X]-pre-pivot
```

3. Archive deprecated specs:
```bash
mkdir -p docs/specs/_archived
mv docs/specs/[deprecated] docs/specs/_archived/
```

4. Regenerate roadmap:
```
/roadmap
```

5. Git commit:
```bash
git add .
git commit -m "pivot: [brief description of change]

Impact:
- [N] specs archived
- [N] specs modified
- [N] new specs planned

Pre-pivot snapshot: v[X.X]-pre-pivot"
```

#### If Abort:

1. Delete pivot analysis document
2. Inform user project continues as before
3. No state changes

### Step 8: Summary

```
🔄 Pivot Complete

Change: [from] → [to]

Actions Taken:
- Created pre-pivot snapshot: v[X.X]-pre-pivot
- Updated constitution with new principles
- Archived [N] deprecated specs
- Modified roadmap

New Roadmap:
[Brief summary of new priorities]

Next steps:
  → /roadmap - See updated development path
  → /continue - Resume development with new direction

To undo this pivot:
  git checkout v[X.X]-pre-pivot
```

## Model
Use: **opus** (complex analysis and decision-making)
