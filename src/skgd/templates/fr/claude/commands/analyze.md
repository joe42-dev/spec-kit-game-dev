# /analyze [feature-name] - Cross-Artifact Validation

You are Opus, performing a non-destructive analysis of project artifacts.

**Argument:** `$ARGUMENTS` (feature name, defaults to current_spec from state)

## Model

**MANDATORY: opus** - Cross-artifact analysis requires deep reasoning.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Philosophy

**STRICTLY READ-ONLY**: Do **not** modify any files. Output a structured analysis report only.

## Step 1: Load Artifacts

Read `.skgd/state.yaml` to get current feature (if no argument provided).

**Required files:**
- `docs/specs/[feature]/spec.md` - Requirements
- `docs/specs/[feature]/plan.md` - Implementation plan
- `docs/specs/[feature]/tasks.md` - Task checklist

**Context files:**
- `.skgd/memory/constitution.md` - Project constraints
- `.skgd/memory/learnings-core.md` - Validated patterns

If any required file is missing, report which prerequisite command to run first.

## Step 2: Build Semantic Models

Create internal representations (do not output these):

- **Requirements inventory**: Each requirement with a key slug (e.g., "player-can-move" → `player-can-move`)
- **Task coverage mapping**: Map each task to requirements
- **Constitution rules**: MUST/SHOULD normative statements

## Step 3: Detection Passes

Focus on high-signal findings. Limit to 30 findings max.

### A. Duplication Detection
- Near-duplicate requirements across spec/plan/tasks
- Redundant tasks doing the same thing

### B. Ambiguity Detection
- Vague terms without measurable criteria (fast, scalable, smooth)
- Unresolved placeholders (TODO, TBD, ???)

### C. Underspecification
- Requirements missing acceptance criteria
- Tasks referencing undefined components/scripts
- Missing edge case handling

### D. Constitution Alignment
- Violations of MUST principles from constitution.md
- Missing quality gates

### E. Coverage Gaps
- Requirements with zero associated tasks
- Tasks with no mapped requirement
- Non-functional requirements not reflected in tasks

### F. Inconsistency
- Terminology drift (same concept named differently)
- Task ordering contradictions
- Conflicting requirements

## Step 4: Severity Assignment

| Severity | Criteria |
|----------|----------|
| CRITICAL | Constitution violation, zero coverage for core requirement |
| HIGH | Conflicting requirements, untestable criteria |
| MEDIUM | Terminology drift, missing edge cases |
| LOW | Style improvements, minor redundancy |

## Step 5: Output Report

Generate a Markdown report (to console, no file writes):

```markdown
# Analysis Report: [feature-name]

## Issues Found

| ID | Category | Severity | Location | Summary | Recommendation |
|----|----------|----------|----------|---------|----------------|
| D1 | Duplication | MEDIUM | spec.md:L12, tasks.md:L8 | Similar requirement | Consolidate |
| A1 | Ambiguity | HIGH | spec.md:L25 | "smooth movement" undefined | Add metrics |

## Coverage Summary

| Requirement | Has Tasks? | Task IDs | Notes |
|-------------|-----------|----------|-------|
| player-movement | Yes | T1, T2 | - |
| enemy-ai | No | - | Missing implementation tasks |

## Constitution Alignment

- [x] Pattern X followed
- [ ] Quality gate Y missing (CRITICAL)

## Metrics

- Total Requirements: N
- Total Tasks: N
- Coverage: N%
- Critical Issues: N
- High Issues: N
```

## Step 6: Next Actions

Based on findings:

**If CRITICAL issues:**
```
CRITICAL issues found. Resolve before /implement:
- [List critical issues]

Suggested:
  /spec [feature] - Refine requirements
  /plan [feature] - Adjust architecture
```

**If only LOW/MEDIUM:**
```
Analysis complete. Minor improvements recommended.

Safe to proceed:
  /implement - Execute implementation
```

## Step 7: Offer Remediation

Ask: "Would you like me to suggest specific fixes for the top issues?"

**Do NOT apply fixes automatically** - this command is READ-ONLY.

## Remember

- **Never modify files** - analysis only
- **Constitution is non-negotiable** - violations are always CRITICAL
- **Be specific** - cite exact locations (file:line)
- **Actionable recommendations** - tell user exactly what to fix
- **Zero issues is valid** - report success with coverage stats
