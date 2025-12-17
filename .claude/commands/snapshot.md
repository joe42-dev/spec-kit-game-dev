# /snapshot [version] - Save Project State

You are creating a snapshot of the current project state for versioning.

**Argument:** `$ARGUMENTS` (version string, e.g., "v0.1", "v0.2-alpha")

## Your Task

### Step 1: Determine Version

If argument provided, use it.
If not, auto-increment:
- Read `.skgd/state.yaml` for `snapshots.latest`
- Increment (v0.1 → v0.2, etc.)

### Step 2: Gather Current State

Read:
- `.skgd/state.yaml` - Full state
- `.skgd/config.yaml` - Configuration
- `.skgd/roadmap.yaml` - Roadmap progress
- `docs/` - All documentation

List completed specs:
```bash
ls docs/specs/
```

### Step 3: Create Snapshot Directory

```bash
mkdir -p .skgd/snapshots/[version]/specs
```

### Step 4: Copy State Files

Copy current state to snapshot:

```yaml
# .skgd/snapshots/[version]/state.yaml
snapshot:
  version: "[version]"
  created: "[timestamp]"
  git_commit: "[current HEAD hash]"

project_state:
  phase: [current phase]
  specs_completed: [list]
  specs_in_progress: [list]

summary:
  total_specs: [N]
  total_scripts: [N]
  total_gameobjects: [N]

notes: |
  [User can add notes]
```

Copy relevant docs:
```bash
cp docs/game-brief.md .skgd/snapshots/[version]/
cp docs/gdd.md .skgd/snapshots/[version]/ 2>/dev/null || true
cp docs/architecture.md .skgd/snapshots/[version]/ 2>/dev/null || true
cp -r docs/specs/* .skgd/snapshots/[version]/specs/ 2>/dev/null || true
```

### Step 5: Update Main State

Update `.skgd/state.yaml`:
```yaml
snapshots:
  count: [increment]
  latest: "[version]"
```

### Step 6: Git Tag

```bash
git add .skgd/snapshots/[version]/
git commit -m "chore: create snapshot [version]

Phase: [phase]
Specs completed: [N]
Milestone: [description if any]"

git tag -a [version] -m "Snapshot [version]: [brief description]"
```

### Step 7: Summary

Display:
```
📸 Snapshot Created: [version]

Location: .skgd/snapshots/[version]/

Contents:
├── state.yaml (project state)
├── game-brief.md
├── gdd.md (if exists)
├── architecture.md (if exists)
└── specs/
    ├── [spec1]/
    └── [spec2]/

Git tag: [version]

Project Progress:
- Phase: [phase]
- Specs: [completed]/[total]
- Since last snapshot: [changes summary]

To restore this snapshot later:
  git checkout [version]

To compare with current:
  git diff [version]..HEAD

All Snapshots:
[List all versions with dates]
```

### Step 8: Ask for Notes

Use AskUserQuestion:
```
Would you like to add notes to this snapshot?
(e.g., milestone reached, key decisions made, etc.)
```

If yes, update the snapshot state.yaml with notes.

## Restore Snapshot (for reference)

To restore a snapshot (document for user):
```bash
# View snapshot state
cat .skgd/snapshots/[version]/state.yaml

# Checkout git tag
git checkout [version]

# Or diff against current
git diff [version]..HEAD -- docs/
```

## Model
Use: **haiku** (simple file operations)
