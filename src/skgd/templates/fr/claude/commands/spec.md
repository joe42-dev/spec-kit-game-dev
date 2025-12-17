# /spec [nom-fonctionnalité] - Créer une Spécification de Fonctionnalité

Vous créez une spécification détaillée pour une fonctionnalité de jeu.

**Argument :** `$ARGUMENTS` (nom de fonctionnalité, ex: "player-movement", "enemy-ai")

## Votre Tâche

### Étape 1 : Valider la Fonctionnalité

Lire `.skgd/roadmap.yaml` pour vérifier :
- La fonctionnalité existe dans la roadmap
- Les dépendances sont satisfaites (fonctionnalités bloquantes terminées)
- La fonctionnalité est appropriée pour la phase actuelle

Si pas d'argument fourni, lire la roadmap et suggérer la prochaine fonctionnalité.

### Étape 2 : Charger le Contexte

Lire ces fichiers :
- `docs/game-brief.md` - Vision principale
- `docs/gdd.md` - Si existe, sections pertinentes
- `.skgd/templates/spec.md` - Template de spec
- `.skgd/templates/game-types/[type].md` - Guidance spécifique au type
- `.skgd/memory/constitution.md` - Contraintes
- `.skgd/memory/learnings.md` - Apprentissages passés
- `.skgd/config.yaml` - Obtenir `mcp.assets.profile` pour le style artistique
- `.skgd/memory/assets-catalog.md` - Assets existants et guide de style

Pour les dépendances, lire aussi :
- `docs/specs/[dépendance]/spec.md` - Chaque spec de dépendance

### Étape 3 : Déléguer à l'Agent Designer

Utiliser l'outil Task avec le modèle **sonnet** :

```
Tâche : Créer une spécification de fonctionnalité

Agent : designer
Modèle : sonnet

Fonctionnalité : [nom-fonctionnalité]
Contexte : [résumé du contexte chargé - garder minimal]

Créer une spécification suivant la structure du template :
1. Vue d'ensemble - Quoi et pourquoi
2. User Stories - En tant que joueur, je veux...
3. Exigences - Fonctionnelles et non-fonctionnelles
4. Détail des Mécaniques - Comment ça fonctionne
5. Cas Limites - Ce qui pourrait mal tourner
6. Dépendances - Ce dont cela a besoin
7. Critères d'Acceptation - Comment on sait que c'est fait
8. Besoins en Assets - Assets visuels/audio nécessaires (IMPORTANT: être précis sur tailles, styles)
9. Indices d'Implémentation Unity - Composants, scripts suggérés

IMPORTANT : Toujours remplir la section Besoins en Assets basé sur le style artistique de la config.
Référencer `.skgd/memory/assets-catalog.md` pour les assets existants et le guide de style.
```

### Étape 4 : Créer le Fichier de Spec

Créer `docs/specs/[nom-fonctionnalité]/spec.md` :

```markdown
# Spécification [Nom de la Fonctionnalité]

## Vue d'Ensemble
[Ce qu'est cette fonctionnalité et pourquoi elle compte pour le jeu]

## User Stories

### Primaire
- En tant que joueur, je veux [action] afin de [bénéfice]

### Secondaire
- En tant que joueur, je veux [action] afin de [bénéfice]

## Exigences

### Fonctionnelles
- [ ] EF-1 : [Exigence]
- [ ] EF-2 : [Exigence]

### Non-Fonctionnelles
- [ ] ENF-1 : Performance - [cible]
- [ ] ENF-2 : Ressenti - [cible qualité]

## Détail des Mécaniques

### Comportement Principal
[Description détaillée de comment la mécanique fonctionne]

### Paramètres
| Paramètre | Valeur | Notes |
|-----------|--------|-------|
| [param] | [valeur] | [pourquoi] |

### Machine à États (si applicable)
```
[État A] --[déclencheur]--> [État B]
```

## Cas Limites
1. **[Cas]** : [Comment gérer]
2. **[Cas]** : [Comment gérer]

## Dépendances
- [x] [Dépendance terminée]
- [ ] [Dépendance en attente] - Bloqué

## Critères d'Acceptation
- [ ] CA-1 : [Critère testable]
- [ ] CA-2 : [Critère testable]
- [ ] CA-3 : [Critère testable]

## Besoins en Assets

### Assets Visuels
| ID | Nom | Type | Taille | Description | Priorité |
|----|-----|------|--------|-------------|----------|
| SPR-1 | [nom_asset] | sprite | [LxH] | [Ce qu'il montre] | Requis |

### Modèles 3D (si applicable)
| ID | Nom | Budget Polygones | Description | Priorité |
|----|-----|------------------|-------------|----------|

### Assets Audio
| ID | Nom | Type | Durée | Description | Priorité |
|----|-----|------|-------|-------------|----------|
| SFX-1 | [nom_asset] | sfx | [durée] | [Ce qu'il représente] | Requis |

### Notes de Style
- **Référence de style artistique :** [Depuis config ou spécifique à cette fonctionnalité]
- **Palette de couleurs :** [Depuis assets-catalog ou spécifique]
- **Contraintes de taille :** [Exigences spécifiques à la plateforme]

## Indices d'Implémentation Unity

### Composants Suggérés
- `[NomComposant]` - [but]

### Scripts Suggérés
- `[NomScript].cs` - [responsabilité]

### Configuration de Scène
- [Suggestion de structure GameObject]

---
*Créé : [horodatage]*
*Statut : Brouillon*
*Dépendances : [liste]*
```

### Étape 5 : Mettre à Jour l'État

Mettre à jour `.skgd/state.yaml` :
```yaml
production:
  current_spec: [nom-fonctionnalité]
  current_step: spec

specs:
  total: [incrémenter]
  in_progress: [nom-fonctionnalité]

assets:
  queue:
    - feature: [nom-fonctionnalité]
      pending_assets: [compte depuis section Besoins en Assets]
```

Mettre à jour `.skgd/roadmap.yaml` :
- Marquer la fonctionnalité comme `in_progress`

Si des assets ont été définis, les compter aussi :
```yaml
assets:
  total_defined: [incrémenter du nombre d'assets]
```

### Étape 6 : Commit Git

```bash
git add docs/specs/[nom-fonctionnalité]/
git commit -m "docs: ajout de la spécification [nom-fonctionnalité]"
```

### Étape 7 : Afficher le Résumé

Afficher ce message et **S'ARRÊTER** :
```
📋 Spécification Créée : [nom-fonctionnalité]

Emplacement : docs/specs/[nom-fonctionnalité]/spec.md

Résumé de la Spec :
- [N] User stories
- [N] Exigences
- [N] Critères d'acceptation
- [N] Assets définis

Prochaines étapes (au choix de l'utilisateur) :
  → /plan [nom-fonctionnalité] - Générer le plan d'implémentation
  → /assets list [nom-fonctionnalité] - Voir les assets requis
  → /spec [autre-fonctionnalité] - Spécifier une autre fonctionnalité
  → /continue - Router automatiquement vers la planification
```

Si des assets ont été définis et des MCPs sont configurés, ajouter :
```
💡 Astuce : Lancez /assets generate [nom-fonctionnalité] avant /implement pour préparer les assets.
```

## Auto-Suggest

Après l'affichage du résumé, montrer le prompt auto-suggest :

```
───────────────────────────────────────
Suivant : Créer le plan d'implémentation
[Entrée] /plan [feature] | [S] stop
───────────────────────────────────────
```

- Si l'utilisateur appuie sur **Entrée** ou dit "oui"/"continuer" : Exécuter `/plan [nom-fonctionnalité]`
- Si l'utilisateur dit **"stop"**, **"s"**, ou autre chose : Quitter et laisser l'utilisateur contrôler le rythme

## IMPORTANT : Attendre la Réponse Utilisateur

**Ne PAS procéder automatiquement** - afficher le prompt auto-suggest et attendre.

Cela donne le contrôle à l'utilisateur tout en réduisant la friction pour le chemin commun.

## Modèle
Utiliser : **sonnet** (tâche de documentation structurée)
