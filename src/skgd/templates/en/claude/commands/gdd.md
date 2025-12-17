# /gdd - Generate Game Design Document

You are Opus, generating a formal Game Design Document that synthesizes all project design work.

## Model

**MANDATORY: opus** - Document synthesis requires comprehensive understanding and creative organization.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Purpose

Generate a formal, shareable GDD that synthesizes:
- Vision from `game-brief.md`
- Design decisions from `pillars/*.md`
- Technical approach from `architecture.md`
- Implementation scope from `roadmap.yaml`

**Output:** `docs/gdd.md`

---

## When to Use

- After all pillars are complete (best)
- After `/validate-design` passes
- Anytime as a synthesis checkpoint
- Before sharing with stakeholders/team

---

## Phase 0: Scout Context

**BEFORE any other step**, gather all design context via Scout sub-agent:

Use Task tool:
- subagent_type: 'Explore'
- model: 'haiku'
- prompt: |
    Scout all design documents for GDD generation:

    1. Read docs/game-brief.md - extract:
       - Game title, genre, target audience
       - Core concept statement (elevator pitch)
       - USPs (unique selling points)
       - Target experience/emotions
       - Platform(s)

    2. Read docs/pillars/_index.md - get pillar list and completion status

    3. For each COMPLETED pillar in docs/pillars/, extract:
       - Pillar name
       - 2-3 key decisions with rationale
       - Core mechanics/systems defined
       - References mentioned

    4. Read docs/architecture.md (if exists) - extract:
       - Tech stack
       - Key patterns
       - Performance targets

    5. Read .skgd/roadmap.yaml (if exists) - extract:
       - MVP features list
       - Total features planned
       - Cycle structure

    6. Read .skgd/memory/constitution.md - extract design principles

    Return Scout Report format (max 800 tokens, this is synthesis):

    ## Scout Report: gdd
    **Status:** ready | partial | blocked

    **Game Identity:**
    - Title: [name]
    - Genre: [genre]
    - Platform: [platforms]
    - Pitch: [1-2 sentence concept]

    **Design Pillars Status:** [N]/[M] complete

    **Key Decisions by Pillar:**
    - [pillar-1]: [decisions summary]
    - [pillar-2]: [decisions summary]
    - ...

    **Core Mechanics:**
    - [mechanic 1]: [brief]
    - [mechanic 2]: [brief]

    **Technical Stack:** [summary]

    **Scope:**
    - MVP: [features list]
    - Full: [N features across M cycles]

    **Design Principles:** [from constitution]

    **Missing:** [files not found or "none"]

**IF Scout returns "blocked":** Minimum requirement is game-brief.md. If missing, route to `/brainstorm`.
**IF Scout returns "partial":** Proceed with available info, note gaps in GDD.

---

## Step 1: Review Completeness

```
GDD Generation Check

Design Documents Found:
✅ game-brief.md - Core vision
[✅|⬜] pillars/ - [N]/[M] complete
[✅|⬜] architecture.md - Technical design
[✅|⬜] roadmap.yaml - Scope/priorities

Recommendation:
[If all complete]: "Ready to generate comprehensive GDD"
[If partial]: "Can generate GDD with gaps noted. Missing: [list]"
```

Ask user:
```
Proceed with GDD generation?
  [A] Yes, generate now
  [B] Let me complete more pillars first
```

---

## Step 2: Generate GDD

Transform Scout Report + any targeted reads into formal GDD structure:

```markdown
# [Game Title] - Game Design Document

> [Elevator pitch from game-brief]

## Document Info
- **Version:** 1.0
- **Generated:** [timestamp]
- **Status:** [Draft/In Progress/Complete]
- **Pillars Complete:** [N]/[M]

---

## 1. Game Overview

### 1.1 Concept Statement
[Expanded from game-brief core concept]

### 1.2 Genre
[Primary genre] with [secondary elements]

### 1.3 Target Audience
- **Age:** [from game-brief]
- **Player Type:** [casual/core/hardcore]
- **Interests:** [what they enjoy]

### 1.4 Unique Selling Points
1. [USP 1 from game-brief]
2. [USP 2]
3. [USP 3]

### 1.5 Platform(s)
- Primary: [platform]
- Secondary: [if any]

### 1.6 Design Principles
[From constitution.md]
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]

---

## 2. Gameplay

### 2.1 Core Loop
[From game-loop pillar or game-brief]
```
[Action] → [Feedback] → [Reward] → [Progression] → [Action]
```

### 2.2 Core Mechanics

#### [Mechanic 1 Name]
*Source: [pillar-name] pillar*

- **Description:** [from pillar decisions]
- **Controls:** [if defined]
- **Feel Target:** [from pillar]
- **Key Decision:** [rationale from pillar]

#### [Mechanic 2 Name]
*Source: [pillar-name] pillar*

- **Description:** [from pillar]
- **Controls:** [if defined]
- **Feel Target:** [from pillar]
- **Key Decision:** [rationale]

### 2.3 Game Feel Targets
| Aspect | Target | Reference |
|--------|--------|-----------|
| [Aspect 1] | [Target] | [Game reference from pillars] |
| [Aspect 2] | [Target] | [Reference] |

---

## 3. Progression

### 3.1 Progression Type
[From progression pillar or game-brief]

### 3.2 Progression Curve
[From pillar decisions]

### 3.3 Unlocks & Rewards
[From pillar]

---

## 4. Game World

### 4.1 Setting
[From art-direction or player-experience pillar]

### 4.2 Visual Style
- **Art Direction:** [from pillar]
- **Color Palette:** [from pillar]
- **Mood:** [from pillar]

### 4.3 Audio Direction
[From pillar if exists, or note as TBD]

---

## 5. Levels/Worlds

### 5.1 Structure
[From level-design pillar]

### 5.2 Level Design Principles
[From pillar decisions]

---

## 6. Characters/Entities

[From relevant pillars - enemy-design, character-progression, etc.]

---

## 7. UI/UX

### 7.1 HUD Philosophy
[From player-experience pillar]

### 7.2 Accessibility Goals
[From game-brief or pillar]

---

## 8. Technical Specs

*Source: architecture.md*

### 8.1 Technology Stack
- Engine: [Unity/Godot]
- Language: [C#/GDScript]
- Key Patterns: [from architecture]

### 8.2 Target Performance
| Platform | FPS | Resolution |
|----------|-----|------------|
| [Platform] | [Target] | [Target] |

### 8.3 Save System
[From architecture]

---

## 9. Scope & Milestones

*Source: roadmap.yaml*

### 9.1 MVP Features (Cycle 1)
- [ ] [Feature 1]
- [ ] [Feature 2]
- [ ] [Feature 3]

### 9.2 Full Release Features
[Cycles 2+ from roadmap]

### 9.3 Post-Release Ideas
[From roadmap stretch goals]

---

## 10. References

### 10.1 Game References
[Aggregated from all pillars]

| Game | What We Take | Pillar Source |
|------|--------------|---------------|
| [Game] | [Element] | [pillar-name] |

---

## 11. Risks & Mitigation

[Aggregated from pillar risk sections]

| Risk | Source | Mitigation |
|------|--------|------------|
| [Risk] | [pillar] | [Strategy] |

---

## 12. Open Questions

[Aggregated from pillar open questions]

- [ ] [Question from pillar-1]
- [ ] [Question from pillar-2]

---

## Appendix A: Pillar Summary

| Pillar | Status | Key Decisions |
|--------|--------|---------------|
| [pillar-1] | ✅ Complete | [Decisions] |
| [pillar-2] | ✅ Complete | [Decisions] |
| [pillar-3] | ⬜ Stub | - |

---

## Appendix B: Decision Log

| Decision | Choice | Rationale | Pillar |
|----------|--------|-----------|--------|
| [Question] | [Answer] | [Why] | [Source] |

---

*Generated by SKGD v3.5*
*Source: docs/game-brief.md, docs/pillars/*.md, docs/architecture.md, .skgd/roadmap.yaml*
*See also: docs/pillars/_index.md for pillar details*
```

---

## Step 3: Write GDD

Write to `docs/gdd.md`

---

## Step 4: Update State

Update `.skgd/state.yaml`:
```yaml
gdd:
  generated: true
  version: 1.0
  timestamp: [ISO-8601]
  pillars_at_generation: [N]/[M]
```

---

## Step 5: Git Commit

```bash
git add docs/gdd.md
git commit -m "docs: generate GDD v1.0

Synthesized from:
- game-brief.md
- [N] pillars
- architecture.md
- roadmap.yaml

Pillars complete: [N]/[M]"
```

---

## Step 6: Summary

```
📄 Game Design Document Generated

docs/gdd.md created (v1.0)

Content Summary:
• Sections: 12 + 2 appendices
• Pillars synthesized: [N]/[M]
• Mechanics documented: [count]
• References consolidated: [count]
• Open questions: [count]

Document Status:
[If all pillars complete]: COMPLETE - Ready to share
[If partial]: DRAFT - Gaps noted, update after more pillars

Next Steps:
  - Review and refine manually if needed
  - Share with team/stakeholders
  - Run /gdd again after completing more pillars
```

---

## Regeneration

Running `/gdd` again will:
- Overwrite existing `docs/gdd.md`
- Incorporate any new pillar completions
- Update version and timestamp

---

## Anti-Patterns

```
BAD: Generating GDD with zero pillars complete
GOOD: At least game-brief and 2-3 pillars

BAD: Copying pillar text verbatim
GOOD: Synthesizing and organizing into GDD structure

BAD: Leaving template placeholders [like this]
GOOD: Marking sections as "TBD - needs [pillar]" if info missing

BAD: Making up content not in source docs
GOOD: Only synthesize what exists, note gaps
```

---

*Version: 3.5*
*Pattern: Scout-First for context gathering*
