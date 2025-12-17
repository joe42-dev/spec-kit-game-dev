# /roadmap - Feuille de Route de Développement Intelligente

Vous générez ou affichez la feuille de route de développement priorisée.

## Votre Tâche

### Étape 1 : Charger le Contexte

Lire ces fichiers :
- `.skgd/state.yaml` - État actuel
- `.skgd/config.yaml` - Config du projet (surtout game_type)
- `.skgd/roadmap.yaml` - Roadmap existante si disponible
- `docs/game-brief.md` - Si existe
- `docs/gdd.md` - Si existe
- `.skgd/memory/constitution.md` - Principes fondamentaux

### Étape 2 : Déterminer le Mode Roadmap

**Si pas de roadmap ou changement d'état majeur :**
→ Générer une nouvelle roadmap (utiliser Opus)

**Si roadmap existe et état correspond :**
→ Afficher la roadmap actuelle avec progression (utiliser Haiku)

### Étape 3 : Générer la Roadmap (si nécessaire)

Utiliser l'outil Task pour déléguer à l'agent **Architect** avec le modèle opus :

```
Analyser le projet et générer une roadmap priorisée.

Contexte :
- Type de jeu : [depuis config]
- Phase actuelle : [depuis state]
- Specs terminées : [liste]
- Brief de jeu : [contenu si existe]
- GDD : [contenu si existe]

Générer la roadmap selon ces principes :
1. Boucle principale d'abord (minimum jouable)
2. Dépendances respectées (ce qui bloque quoi)
3. Progression de complexité (simple → complexe)
4. Priorités spécifiques au type de jeu (charger template)

Format de sortie pour .skgd/roadmap.yaml
```

### Étape 4 : Structure YAML de la Roadmap

```yaml
# .skgd/roadmap.yaml
generated: "[horodatage]"
game_type: "[type]"
current_phase: "[phase]"

phases:
  concept:
    status: completed|in_progress|pending
    items:
      - brainstorm
      - game-brief

  design:
    status: completed|in_progress|pending
    items:
      - core-mechanics
      - progression-system
      - [spécifique au type de jeu]

  architecture:
    status: completed|in_progress|pending
    items:
      - technical-architecture
      - unity-project-structure

  production:
    status: completed|in_progress|pending
    cycles:
      - cycle: 1
        milestone: "Boucle Principale Jouable"
        features:
          - id: player-movement
            priority: critical
            complexity: low
            dependencies: []
            status: pending|in_progress|completed
          - id: basic-level
            priority: critical
            complexity: low
            dependencies: [player-movement]
            status: pending
          # ... plus de fonctionnalités

next_recommended:
  feature: "[feature-id]"
  reason: "[pourquoi c'est la prochaine]"
  command: "/spec [feature-id]"

blocked:
  - feature: "[feature-id]"
    blocked_by: "[dépendance]"
```

### Étape 5 : Afficher la Roadmap

Formater la sortie :

```
🗺️ FEUILLE DE ROUTE DE DÉVELOPPEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE : CONCEPT [✓ Terminé]
  ✓ Session de brainstorming
  ✓ Brief de jeu

PHASE : DESIGN [○ En Cours]
  ✓ Spec mécaniques principales
  ○ Système de progression      ← Actuel
  · Level design
  · Système d'ennemis

PHASE : ARCHITECTURE [· En Attente]
  · Architecture technique
  · Structure projet Unity

PHASE : PRODUCTION [· En Attente]
  Cycle 1 : "Boucle Principale Jouable"
  ┌─────────────────────────────────────────────────────────┐
  │  · player-movement [Critique] [Complexité Faible]       │
  │  · basic-level [Critique] [Faible] ← dépend: player-mov │
  │  · game-camera [Haute] [Faible]                         │
  └─────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏭️  SUIVANT : /spec progression-system
    Raison : Requis pour la définition de la boucle principale
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Étape 6 : Mettre à Jour l'État

Après génération/affichage de la roadmap, mettre à jour `.skgd/state.yaml` :
```yaml
last_action:
  command: roadmap
  timestamp: [maintenant]
  result: success
```

## Sélection du Modèle
- **Générer une nouvelle roadmap** : opus (analyse complexe)
- **Afficher une roadmap existante** : haiku (lecture simple)
