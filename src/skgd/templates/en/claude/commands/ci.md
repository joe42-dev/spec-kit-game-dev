# /ci - Setup CI/CD Pipeline (Optional)

You are setting up an optional GitHub Actions CI/CD pipeline for automated testing.

**This command is OPTIONAL.** Only run when the user explicitly wants CI/CD automation.

## Your Task

### Step 1: Load Context

Read `.skgd/config.yaml` to determine:
- Engine: Unity or Godot
- Project name
- Unity/Godot version

### Step 2: Confirm Setup

```
🔧 CI/CD Setup

This will create a GitHub Actions workflow for automated testing.

Engine detected: [Unity/Godot]
Testing framework: [Unity Test Framework / GdUnit4]

This creates:
- .github/workflows/tests.yml

Prerequisites:
- GitHub repository (public or private)
- [Unity License for CI] / [Godot headless builds]

Continue? [Y/N]
```

If user declines, exit gracefully.

### Step 3: Generate Workflow

#### For Unity Projects

Create `.github/workflows/tests.yml`:

```yaml
name: Unity Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    name: Run Unity Tests
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          lfs: true

      - name: Cache Library
        uses: actions/cache@v4
        with:
          path: Library
          key: Library-${{ hashFiles('Assets/**', 'Packages/**', 'ProjectSettings/**') }}
          restore-keys: |
            Library-

      - name: Run EditMode Tests
        uses: game-ci/unity-test-runner@v4
        env:
          UNITY_LICENSE: ${{ secrets.UNITY_LICENSE }}
        with:
          testMode: EditMode
          githubToken: ${{ secrets.GITHUB_TOKEN }}
          checkName: EditMode Tests

      - name: Run PlayMode Tests
        uses: game-ci/unity-test-runner@v4
        env:
          UNITY_LICENSE: ${{ secrets.UNITY_LICENSE }}
        with:
          testMode: PlayMode
          githubToken: ${{ secrets.GITHUB_TOKEN }}
          checkName: PlayMode Tests

      - name: Upload Test Results
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: Test Results
          path: artifacts
```

#### For Godot Projects

Create `.github/workflows/tests.yml`:

```yaml
name: Godot Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    name: Run GdUnit4 Tests
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Godot
        uses: chickensoft-games/setup-godot@v2
        with:
          version: 4.3.0  # Match your project version
          use-dotnet: false

      - name: Verify Godot
        run: godot --version

      - name: Import Project
        run: godot --headless --import
        timeout-minutes: 5

      - name: Run GdUnit4 Tests
        run: |
          godot --headless -s addons/gdUnit4/bin/GdUnitCmdTool.gd \
            --add --continue-on-failure \
            -rd res://test
        timeout-minutes: 10

      - name: Upload Test Results
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-results
          path: |
            reports/
            *.xml
```

### Step 4: Create Setup Instructions

Create `.github/CI_SETUP.md`:

```markdown
# CI/CD Setup Instructions

## For Unity Projects

### 1. Unity License Secret

You need a Unity license for CI. Options:

**Personal License (Free):**
1. Run locally: `unity -batchmode -createManualActivationFile`
2. Upload .alf to https://license.unity3d.com/manual
3. Download .ulf file
4. Add to GitHub Secrets as `UNITY_LICENSE` (paste file contents)

**Pro/Plus License:**
1. Add these secrets to GitHub:
   - `UNITY_EMAIL`: Your Unity account email
   - `UNITY_PASSWORD`: Your Unity account password
   - `UNITY_SERIAL`: Your license serial

### 2. Enable GitHub Actions

1. Go to repo Settings > Actions > General
2. Enable "Allow all actions"
3. Under "Workflow permissions", select "Read and write permissions"

---

## For Godot Projects

### 1. Install GdUnit4

In your Godot project:
1. AssetLib > Search "GdUnit4"
2. Install and enable the addon
3. Create `test/` folder for your tests

### 2. No License Required

Godot is open source - no license secrets needed!

### 3. Test Naming

Place tests in `res://test/` with naming:
- `test_[name].gd` for test scripts
- Extend `GdUnitTestSuite` in test classes

---

## Verify Setup

After pushing:
1. Check Actions tab in GitHub
2. First run may take longer (caching)
3. Subsequent runs use cached dependencies
```

### Step 5: Update State

```yaml
# .skgd/state.yaml
initialization:
  ci_configured: true
  ci_engine: [unity/godot]
  ci_date: [YYYY-MM-DD]
```

### Step 6: Git Commit

```bash
git add .github/
git commit -m "ci: add GitHub Actions test workflow

- Automated [EditMode/PlayMode | GdUnit4] tests
- Runs on push to main/develop
- Runs on PRs to main"
```

### Step 7: Summary

```
✅ CI/CD Pipeline Created

Files created:
- .github/workflows/tests.yml
- .github/CI_SETUP.md

Next steps:
1. Read .github/CI_SETUP.md for license setup
2. Push to GitHub
3. Check Actions tab after first push

The pipeline will:
- Run tests on every push to main/develop
- Run tests on every PR to main
- Report results as GitHub checks

This is OPTIONAL - your /playtest command still works locally!
```

## Notes

- This command is **opt-in only**
- Users without GitHub repos can ignore this
- Local testing via `/playtest` always available
- CI complements but doesn't replace manual playtesting

## Model
Use: **sonnet** (configuration task)
