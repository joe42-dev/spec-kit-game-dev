# /pivot - Gérer un Changement de Direction Majeur

Vous gérez un changement significatif de direction ou de portée du jeu.

## Votre Tâche

### Étape 1 : Comprendre le Pivot

Demander à l'utilisateur (utiliser AskUserQuestion) :

1. **Qu'est-ce qui change ?**
   - Changement de mécanique principale
   - Changement de genre
   - Réduction/expansion de portée
   - Changement de public cible
   - Changement de plateforme

2. **Pourquoi ce pivot ?**
   - Retours de playtest
   - Limitation technique
   - Évolution créative
   - Contrainte de temps/ressources

3. **Quelle est la nouvelle direction ?**
   - Description en texte libre

### Étape 2 : Créer un Snapshot Pré-Pivot

Créer automatiquement un snapshot avant tout changement :

```bash
# Auto-snapshot
/snapshot v[X.X]-pre-pivot
```

### Étape 3 : Charger le Contexte Complet

Lire TOUTE la documentation du projet :
- `docs/game-brief.md`
- `docs/gdd.md`
- `docs/architecture.md`
- `docs/specs/*/spec.md`
- `.skgd/roadmap.yaml`
- `.skgd/memory/constitution.md`

### Étape 4 : Déléguer l'Analyse d'Impact à l'Architecte

Utiliser l'outil Task avec le modèle **opus** :

```
Tâche : Analyser l'impact du pivot

Agent : architect
Modèle : opus

État Actuel :
- Brief de jeu : [résumé]
- Sections GDD : [liste]
- Specs terminées : [liste]
- Specs en cours : [liste]
- Architecture : [résumé]

Description du Pivot :
[Description du changement par l'utilisateur]

Analyser :
1. Quel travail existant est invalidé ?
2. Quel travail existant peut être préservé ?
3. Quel nouveau travail est requis ?
4. Quel est l'impact sur le calendrier/portée ?
5. Quels sont les risques de ce pivot ?
6. Approche recommandée pour la transition ?
```

### Étape 5 : Générer le Document d'Analyse de Pivot

Créer `docs/pivots/pivot-[N]-[date].md` :

```markdown
# Analyse de Pivot #[N]

## Date
[horodatage]

## Déclencheur
[Pourquoi ce pivot a lieu]

## Résumé du Changement
**De :** [Direction précédente]
**Vers :** [Nouvelle direction]

## Analyse d'Impact

### Impact sur la Documentation

#### Invalidée (nécessite réécriture)
| Document | Raison | Effort |
|----------|--------|--------|
| [doc] | [pourquoi invalide] | Élevé/Moyen/Faible |

#### Préservée (toujours valide)
| Document | Notes |
|----------|-------|
| [doc] | [mises à jour mineures nécessaires] |

#### Nouvelle Requise
| Document | Description | Priorité |
|----------|-------------|----------|
| [doc] | [ce qu'elle couvre] | Élevée/Moyenne/Faible |

### Impact sur les Specs

#### Garder Telles Quelles
- [spec] : [pourquoi toujours valide]

#### Modifier
- [spec] : [changements nécessaires]

#### Déprécier
- [spec] : [pourquoi plus pertinente]

#### Nouvelles Requises
- [spec] : [description]

### Impact sur le Code

#### Garder
- [script/objet] : [toujours nécessaire]

#### Modifier
- [script/objet] : [changements nécessaires]

#### Supprimer
- [script/objet] : [plus nécessaire]

### Impact sur l'Architecture
[Comment l'architecture technique est affectée]

## Plan de Transition

### Phase 1 : Mise à Jour de la Documentation
1. Mettre à jour constitution.md avec les nouveaux principes
2. Réviser game-brief.md
3. Mettre à jour/créer les sections GDD pertinentes

### Phase 2 : Nettoyage des Specs
1. Archiver les specs dépréciées
2. Modifier les specs affectées
3. Créer les nouvelles specs requises

### Phase 3 : Nettoyage du Code
1. Supprimer le code déprécié
2. Modifier le code existant
3. Mettre à jour la roadmap

### Phase 4 : Reprendre le Développement
1. Générer une nouvelle roadmap
2. Continuer avec /continue

## Évaluation des Risques

| Risque | Probabilité | Impact | Atténuation |
|--------|-------------|--------|-------------|
| [risque] | Élevée/Moyenne/Faible | Élevé/Moyen/Faible | [atténuation] |

## Recommandation

[Recommandation claire sur comment procéder]

## Décision

[ ] **Procéder** avec le pivot tel qu'analysé
[ ] **Modifier** la portée du pivot (spécifier les changements)
[ ] **Abandonner** le pivot (garder la direction actuelle)

---
*Snapshot pré-pivot : v[X.X]-pre-pivot*
*Analyse par : Agent Architecte*
```

### Étape 6 : Obtenir la Décision de l'Utilisateur

Utiliser AskUserQuestion :
```
Analyse de Pivot Terminée

Résumé de l'Impact :
- [N] docs invalidées
- [N] specs à modifier
- [N] nouvelles specs nécessaires

Options :
1. Procéder avec le pivot
2. Modifier la portée du pivot
3. Abandonner le pivot (restaurer pré-pivot)

Votre décision ?
```

### Étape 7 : Exécuter Selon la Décision

#### Si Procéder :

1. Mettre à jour `.skgd/memory/constitution.md` avec les nouveaux principes

2. Mettre à jour `.skgd/state.yaml` :
```yaml
pivots:
  count: [incrémenter]
  history:
    - version: [N]
      date: [horodatage]
      from: [ancienne direction]
      to: [nouvelle direction]
      snapshot: v[X.X]-pre-pivot
```

3. Archiver les specs dépréciées :
```bash
mkdir -p docs/specs/_archived
mv docs/specs/[deprecated] docs/specs/_archived/
```

4. Régénérer la roadmap :
```
/roadmap
```

5. Commit Git :
```bash
git add .
git commit -m "pivot: [brève description du changement]

Impact :
- [N] specs archivées
- [N] specs modifiées
- [N] nouvelles specs planifiées

Snapshot pré-pivot : v[X.X]-pre-pivot"
```

#### Si Abandonner :

1. Supprimer le document d'analyse de pivot
2. Informer l'utilisateur que le projet continue comme avant
3. Aucun changement d'état

### Étape 8 : Résumé

```
🔄 Pivot Terminé

Changement : [de] → [vers]

Actions Effectuées :
- Snapshot pré-pivot créé : v[X.X]-pre-pivot
- Constitution mise à jour avec les nouveaux principes
- [N] specs dépréciées archivées
- Roadmap modifiée

Nouvelle Roadmap :
[Bref résumé des nouvelles priorités]

Prochaines étapes :
  → /roadmap - Voir le chemin de développement mis à jour
  → /continue - Reprendre le développement avec la nouvelle direction

Pour annuler ce pivot :
  git checkout v[X.X]-pre-pivot
```

## Modèle
Utiliser : **opus** (analyse complexe et prise de décision)
