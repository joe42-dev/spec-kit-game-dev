# /deep-dive [pillar-name] - Develop Design Pillar

You are Opus, conducting an in-depth design session for a single pillar.

**Argument:** `$ARGUMENTS` (pillar name, e.g., "combat-system", "game-loop")

## Model

**MANDATORY: opus** - Deep design work requires maximum creative and analytical capability.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Philosophy

This is the **quality command**. One pillar, full depth.

**DO NOT rush.** Take time to:
- Ask clarifying questions
- Propose alternatives
- Challenge assumptions
- Reference successful games
- Think through implications

---

## Phase 0: Scout Context

**AVANT toute autre étape**, collecter le contexte via sous-agent Scout :

Utiliser l'outil Task :
- subagent_type: 'Explore'
- model: 'haiku'
- prompt: |
    Scout du système de pillars pour deep-dive sur [pillar-name] :

    1. Lire docs/pillars/_index.md - extraire la liste des pillars avec statut de complétion
    2. Pour chaque pillar COMPLÉTÉ (marqué ✅), extraire 2-3 décisions clés
    3. Lire docs/pillars/[pillar-name].md - obtenir le contenu du stub et les questions
    4. Lire docs/game-brief.md - extraire la vision core (3-5 bullet points)
    5. Lire .skgd/memory/constitution.md - extraire les principes de design (si existe)
    6. Identifier les tensions ou dépendances potentielles inter-pillars

    Retourner au format Scout Report (max 500 tokens) :

    ## Scout Report: deep-dive [pillar-name]
    **Status:** ready | blocked | partial
    **Progression Pillars:** [N]/[M] complétés
    **Résumé Vision:** [3-5 bullets du game-brief]
    **Principes Design:** [de constitution ou "pas encore définis"]
    **Décisions Pillars Complétés:**
    - [pillar-1]: [décision clé]
    - [pillar-2]: [décision clé]
    **Questions Pillar Cible:** [questions du stub]
    **Tensions Potentielles:** [problèmes inter-pillars ou "aucune identifiée"]
    **Manquant:** [fichiers non trouvés ou "aucun"]

**SI Scout retourne status "blocked":** Arrêter et informer l'utilisateur de ce qui manque.
**SI Scout retourne status "partial":** Procéder avec avertissements sur le contexte manquant.

---

## Step 1: Validate

Check pillar exists at `docs/pillars/[pillar-name].md`

**IF NOT EXISTS:**
- Check if `docs/pillars/_index.md` exists
- If yes → pillar might be optional, offer to create it
- If no → "Run /pillars first to create the pillar structure"

---

## Step 2: Review Scout Report

Utiliser le Scout Report de la Phase 0 comme contexte principal.

**Le Scout Report contient:**
- Résumé de la vision (du game-brief.md)
- Principes de design (de constitution.md)
- Progression des pillars et décisions complétées
- Questions du pillar cible
- Tensions inter-pillars

**Lire des fichiers supplémentaires uniquement si:**
- Le status du Scout Report est "partial" ou "blocked"
- L'utilisateur demande des détails spécifiques non présents dans le rapport
- Une clarification approfondie est nécessaire sur une décision particulière

**Budget contexte:** Scout Report (~500 tokens) + lectures ciblées minimales si nécessaire.

---

## Step 3: Review Questions

Present the key questions from the stub:

```
Deep Dive: [Pillar Name]

These are the questions we need to answer:

[Category 1]
□ Question 1?
□ Question 2?

[Category 2]
□ Question 3?
□ Question 4?

Let's work through these together.
Start with what you already know, or I can propose options.
```

---

## Step 4: Collaborative Design Session

For EACH question category:

### 4.1 Understand Current Thinking

```
"For [question], what's your instinct? Or should I propose approaches?"
```

### 4.2 Propose Options (if needed)

Present 2-4 distinct approaches:

```
For [question], here are the main approaches:

**Option A: [Name]**
[Brief description]
- Pro: [advantage]
- Con: [disadvantage]
- Reference: [game that does this]

**Option B: [Name]**
[Brief description]
- Pro: [advantage]
- Con: [disadvantage]
- Reference: [game that does this]

**Option C: [Name]**
[Brief description]
- Pro: [advantage]
- Con: [disadvantage]
- Reference: [game that does this]

Which direction resonates? Or combine elements?
```

### 4.3 Challenge & Refine

Once they choose, challenge:
- "Have you considered [edge case]?"
- "How does this interact with [other pillar]?"
- "What if [variation]?"

### 4.4 Document Decision

For each decision:
```
Decision: [Question]
Choice: [Selected approach]
Rationale: [Why this fits the vision]
Implications: [What this affects]
```

---

## Step 5: Cross-Pillar Coherence

After answering questions, check coherence:

```
Checking coherence with existing pillars...

✓ [pillar-1]: Aligns with [specific point]
⚠ [pillar-2]: Potential tension with [point] - consider [adjustment]
```

If tensions found, discuss resolution.

---

## Step 6: Generate Complete Pillar

Transform stub into complete document:

```markdown
# [Pillar Name] - [Game Name]

*Status: ✅ COMPLETE*
*Completed: [timestamp]*
*Version: 1.0*

## Connection to Vision

> "[Quote from game-brief]"

This pillar serves the vision by:
- [How it supports core experience]
- [How it enables the game's soul]

---

## Design Decisions

### [Decision Category 1]

| Question | Decision | Rationale |
|----------|----------|-----------|
| [Q1] | [Choice] | [Why] |
| [Q2] | [Choice] | [Why] |

### [Decision Category 2]

| Question | Decision | Rationale |
|----------|----------|-----------|
| [Q3] | [Choice] | [Why] |
| [Q4] | [Choice] | [Why] |

---

## Detailed Design

### [Section 1]

[Deep explanation of this aspect]

#### [Subsection if needed]
[Details]

### [Section 2]

[Deep explanation]

### [Section 3]

[Deep explanation]

---

## Systems & Mechanics

[If applicable - specific mechanics, formulas, systems]

### [System 1]
[Description]

### [System 2]
[Description]

---

## Content Examples

[Concrete examples of what this looks like in practice]

### Example 1: [Name]
[Description]

### Example 2: [Name]
[Description]

---

## References

| Game | What We Take | What We Avoid |
|------|--------------|---------------|
| [Game 1] | [Inspiration] | [Anti-pattern] |
| [Game 2] | [Inspiration] | [Anti-pattern] |

---

## Risks & Mitigation

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [Strategy] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Strategy] |

---

## Prototype Plan

To validate this pillar:

**Minimal Test (1-2 days):**
- [What to build]
- [What to measure]
- [Success criteria]

**Extended Test (1 week):**
- [What to build]
- [What to measure]
- [Success criteria]

---

## Cross-Pillar Impact

**This pillar affects:**
- **[pillar-1]:** [How it impacts]
- **[pillar-2]:** [How it impacts]

**This pillar depends on:**
- **[pillar-3]:** [What it needs from there]

---

## Open Questions

- [ ] [Remaining question to revisit]
- [ ] [Question that needs playtesting]

---

*Completed: [timestamp]*
*Session duration: [time]*
*Next suggested: /deep-dive [next-priority-pillar]*
```

---

## Step 7: Update Index

Update `docs/pillars/_index.md`:
- Change pillar status from `⬜ Stub` to `✅ Complete`

---

## Step 8: Update State

Update `.skgd/state.yaml`:
```yaml
pillars:
  [pillar-name]: complete
  last_deep_dive: [pillar-name]
  completed_count: [N]
```

---

## Step 9: Git Commit

```bash
git add docs/pillars/[pillar-name].md docs/pillars/_index.md
git commit -m "docs: deep-dive [pillar-name]

Key decisions:
- [Decision 1]
- [Decision 2]

Cross-pillar impacts: [list]"
```

---

## Step 10: Summary

```
Deep Dive Complete: [pillar-name]

Key Decisions:
• [Decision 1]: [choice]
• [Decision 2]: [choice]
• [Decision 3]: [choice]

Cross-Pillar Impacts:
• [pillar] → [impact]

Prototype Suggestion:
[Brief description of minimal test]

Pillar Progress: [N]/[total] complete

Next recommended:
  /deep-dive [next-pillar] - Continue design
  /validate-design        - Check coherence
  /roadmap               - Start planning implementation
```

---

## Deep Dive Quality Checklist

Before marking complete, ensure:

- [ ] All key questions answered with rationale
- [ ] At least 2 reference games cited
- [ ] Cross-pillar coherence checked
- [ ] Risks identified with mitigation
- [ ] Prototype plan defined
- [ ] Open questions documented

---

## Anti-Patterns

```
BAD: Rushing through questions with yes/no
GOOD: Exploring each decision with options and tradeoffs

BAD: Making decisions in isolation
GOOD: Checking coherence with completed pillars

BAD: Abstract descriptions only
GOOD: Concrete examples and systems

BAD: Ignoring risks
GOOD: Explicit risk identification with mitigation

BAD: No prototype plan
GOOD: Clear validation path
```
