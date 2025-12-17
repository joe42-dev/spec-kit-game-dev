# Scout Helper (Interne)

> **Documentation interne pour le pattern Scout-First.**
> Ce fichier N'EST PAS une commande appelable. Il documente le pattern pour les autres commandes.

## Objectif

Pattern de sous-agent pour la collecte de contexte AVANT les commandes créatives/analytiques.
Réduit la pollution du contexte de l'agent Opus principal en déléguant la lecture des fichiers à Haiku.

## Bénéfices (Validés par la Recherche)

- **-52% coûts tokens** - Haiku lit les fichiers, Opus reçoit le résumé
- **+2.6% taux de résolution** - Contexte plus propre = meilleures décisions
- **Séparation des responsabilités** - Scout collecte, Opus crée

---

## Utilisation dans les Commandes

Les commandes nécessitant du contexte doivent ajouter une **Phase 0** avant leur workflow principal :

```markdown
## Phase 0 : Scout Context

AVANT toute autre étape, utiliser l'outil Task :
- subagent_type: 'Explore'
- model: 'haiku'
- prompt: |
    [Instructions spécifiques à la commande]

    Retourner au format Scout Report (max 500 tokens).
```

### Paramètres de l'Outil Task

```yaml
Task:
  subagent_type: 'Explore'
  model: 'haiku'
  prompt: |
    [Fichiers spécifiques à lire]
    [Quoi extraire]
    [Retourner au format Scout Report]
```

---

## Format Standard du Scout Report

```markdown
## Scout Report: [nom-commande]

**Status:** ready | blocked | partial
**Contexte Clé:**
- [Point 1 - découverte la plus importante]
- [Point 2 - décision ou état clé]
- [Point 3 - contrainte pertinente]

**Manquant:** [Liste des fichiers manquants] ou "aucun"
**Estimation Tokens:** ~[nombre] tokens
```

### Définitions des Status

| Status | Signification | Action |
|--------|---------------|--------|
| `ready` | Tous les fichiers requis trouvés, contexte complet | Procéder avec la commande |
| `blocked` | Fichiers critiques manquants | Arrêter, informer l'utilisateur |
| `partial` | Certains fichiers manquants, peut procéder avec réserves | Procéder avec avertissements |

---

## Règles pour les Scouts

1. **Max 500 tokens en sortie** - Résumer, pas dumper
2. **Lecture seule** - Jamais écrire de fichiers
3. **Retourner un résumé, pas le contenu brut** - Extraire les insights, pas le texte
4. **Identifier les lacunes** - Signaler ce qui manque
5. **Rester concentré** - Collecter uniquement ce dont la commande a besoin

---

## Commandes Utilisant Scout-First

| Commande | Cible du Scout | Extractions Clés |
|----------|----------------|------------------|
| `/deep-dive` | pillars/*.md, game-brief.md | Statut des pillars, décisions, questions |
| `/validate-design` | Tous les pillars | Données de cohérence inter-pillars |
| `/crystallize` | learnings.md | Candidats patterns, nombre d'entrées |
| `/analyze` | specs/*.md, architecture.md | Relations inter-artifacts |
| `/implement` | config, state, tasks, plan, learnings | Engine, session, tâches restantes, patterns |

---

## Commandes SANS Scout (Déjà Efficaces)

- `/brainstorm` - Contexte minimal par design (liberté créative)
- `/continue` - Routeur, pas gourmand en contexte
- `/playtest` - Focalisé sur la spec actuelle uniquement

---

## Exemple : Scout pour /deep-dive

```yaml
Task:
  subagent_type: 'Explore'
  model: 'haiku'
  prompt: |
    Scout du système de pillars pour deep-dive sur [pillar-name] :

    1. Lire docs/pillars/_index.md - extraire la liste des pillars avec statut de complétion
    2. Pour chaque pillar COMPLÉTÉ (marqué ✅), extraire 2-3 décisions clés
    3. Lire docs/pillars/[pillar-name].md - obtenir les questions du stub
    4. Lire docs/game-brief.md - extraire la vision core (3-5 bullets)
    5. Identifier les tensions potentielles inter-pillars

    Retourner au format Scout Report (max 500 tokens) :

    ## Scout Report: deep-dive [pillar-name]
    **Status:** [ready/blocked/partial]
    **Progression Pillars:** [N]/[M] complétés
    **Contexte Clé:** [bullets vision]
    **Décisions Complétées:** [des pillars terminés]
    **Questions Cibles:** [du stub]
    **Tensions Potentielles:** [si présentes]
    **Manquant:** [fichiers non trouvés]
```

---

## Exemple : Scout pour /implement

```yaml
Task:
  subagent_type: 'Explore'
  model: 'haiku'
  prompt: |
    Scout de contexte pour implémentation. Lire et résumer :

    1. `.skgd/config.yaml` - extraire engine (unity/godot) et language
    2. `.skgd/state.yaml` - extraire current_spec, checkpoint, tasks_completed
    3. `docs/specs/[current_spec]/tasks.md` - compter total, lister NON cochées [ ]
    4. `docs/specs/[current_spec]/plan.md` - identifier phase actuelle
    5. `.skgd/memory/learnings-core.md` - extraire 3-5 patterns pertinents

    Retourner au format Scout Report (max 500 tokens) :

    ## Scout Report: implement
    **Status:** [ready|resume|blocked]
    **Engine:** [unity|godot]
    **Feature:** [nom]
    **Session:** [nouveau | reprise depuis T0XX]
    **Tâches:** Total: [N] | Faites: [X] | Restantes: [N-X]
    **MVP restants:** [liste courte]
    **Phase Actuelle:** [nom]
    **Learnings:** [3-5 patterns]
    **Bloqueurs:** [liste ou "aucun"]
```

---

## Anti-Patterns

```
MAUVAIS: Scout retourne le contenu complet des fichiers
BON: Scout retourne des insights résumés

MAUVAIS: Scout écrit des fichiers ou modifie l'état
BON: Scout est strictement en lecture seule

MAUVAIS: Sortie du Scout dépasse 500 tokens
BON: Scout priorise et tronque

MAUVAIS: Commande principale fait des reads inline après le Scout
BON: Commande principale fait confiance au Scout Report
```

---

*Version: 3.5*
*Pattern validé: recherche MetaGPT, Claude Flow, Google ADK*
