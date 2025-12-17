# Template d'Analyse de Pivot

> Template pour documenter et analyser les changements majeurs de direction

## Informations du Pivot
- **Pivot # :** [N]
- **Date :** [Date]
- **Snapshot pré-pivot :** [version]
- **Demandé par :** [Utilisateur/Découverte]

---

## 1. Description du Changement

### De (Direction Actuelle)
[Description claire de la direction actuelle du jeu, mécaniques, portée]

### Vers (Direction Proposée)
[Description claire de la nouvelle direction proposée]

### Déclencheur
[Pourquoi ce pivot est envisagé]
- [ ] Retours de playtest
- [ ] Limitation technique découverte
- [ ] Évolution créative
- [ ] Ajustement de portée (temps/ressources)
- [ ] Considération marché/audience
- [ ] Autre : _____________

---

## 2. Analyse d'Impact

### 2.1 Impact sur la Documentation

#### Documents à Réécrire
| Document | Raison | Effort | Priorité |
|----------|--------|--------|----------|
| | | Faible/Moy/Élevé | Doit/Devrait/Pourrait |

#### Documents à Mettre à Jour
| Document | Changements Nécessaires | Effort |
|----------|-------------------------|--------|
| | | Faible/Moy/Élevé |

#### Documents Toujours Valides
| Document | Notes |
|----------|-------|
| | |

#### Nouveaux Documents Nécessaires
| Document | Objectif | Priorité |
|----------|----------|----------|
| | | Doit/Devrait/Pourrait |

### 2.2 Impact sur les Spécifications

#### Specs à Garder (Sans Changements)
- [ ] [nom-spec] : [pourquoi toujours valide]

#### Specs à Modifier
| Spec | Changements Nécessaires | Effort |
|------|-------------------------|--------|
| | | Faible/Moy/Élevé |

#### Specs à Archiver
- [ ] [nom-spec] : [pourquoi plus pertinent]

#### Nouvelles Specs Requises
| Spec | Description | Priorité |
|------|-------------|----------|
| | | Critique/Haute/Moyenne |

### 2.3 Impact sur le Code/Assets

#### Code à Garder
| Script/Prefab | Notes |
|---------------|-------|
| | |

#### Code à Modifier
| Script/Prefab | Changements | Effort |
|---------------|-------------|--------|
| | | Faible/Moy/Élevé |

#### Code à Supprimer
| Script/Prefab | Raison |
|---------------|--------|
| | |

### 2.4 Impact sur l'Architecture
[Comment cela affecte-t-il l'architecture technique ?]

- [ ] Aucun changement d'architecture nécessaire
- [ ] Ajustements mineurs à l'architecture existante
- [ ] Changements d'architecture significatifs requis
- [ ] Repensage complet de l'architecture nécessaire

**Détails :**
[Expliquer les implications architecturales]

---

## 3. Évaluation des Risques

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Travail précédent perdu | | | |
| Dérive de portée | | | |
| Inconnues techniques | | | |
| Impact sur le calendrier | | | |
| [Autre risque] | | | |

---

## 4. Plan de Transition

### Phase 1 : Préparation
**Objectif :** Sécuriser l'état actuel, préparer les changements
1. [ ] Créer un snapshot pré-pivot
2. [ ] Mettre à jour constitution.md avec les nouveaux principes
3. [ ] Communiquer l'étendue des changements

### Phase 2 : Mise à Jour de la Documentation
**Objectif :** Aligner toute la documentation avec la nouvelle direction
1. [ ] Mettre à jour game-brief.md
2. [ ] Réviser/réécrire les sections du GDD affectées
3. [ ] Archiver les specs dépréciées
4. [ ] Créer les ébauches des nouvelles specs requises

### Phase 3 : Nettoyage du Code
**Objectif :** Aligner le code avec la nouvelle direction
1. [ ] Supprimer le code/assets dépréciés
2. [ ] Refactoriser les systèmes affectés
3. [ ] Mettre à jour les prefabs si nécessaire

### Phase 4 : Nouveau Développement
**Objectif :** Construire vers la nouvelle direction
1. [ ] Générer la nouvelle roadmap
2. [ ] Prioriser les nouvelles specs
3. [ ] Reprendre le workflow normal

### Effort de Transition Estimé
| Phase | Effort | Notes |
|-------|--------|-------|
| Préparation | [X heures/jours] | |
| Documentation | [X heures/jours] | |
| Nettoyage Code | [X heures/jours] | |
| **Total** | **[X heures/jours]** | Avant de reprendre le dev normal |

---

## 5. Comparaison

### Ce Qu'on Perd
- [Élément spécifique perdu]
- [Élément spécifique perdu]

### Ce Qu'on Gagne
- [Élément spécifique gagné]
- [Élément spécifique gagné]

### Évaluation Nette
[Ce pivot en vaut-il la peine ? Recommandation claire]

---

## 6. Décision

### Options

#### Option A : Pivot Complet
Exécuter la transition complète telle qu'analysée ci-dessus.
- **Avantages :** [avantages]
- **Inconvénients :** [inconvénients]

#### Option B : Pivot Partiel
Modifier la portée à : [description de la portée réduite]
- **Avantages :** [avantages]
- **Inconvénients :** [inconvénients]

#### Option C : Abandonner
Continuer avec la direction actuelle, abandonner le pivot.
- **Avantages :** [avantages]
- **Inconvénients :** [inconvénients]

### Recommandation
[Recommandation claire avec raisonnement]

### Décision Finale
[ ] **Option A : Pivot Complet**
[ ] **Option B : Pivot Partiel** - Portée : _____________
[ ] **Option C : Abandonner le Pivot**

**Décision prise par :** [Utilisateur]
**Date :** [Date]

---

## 7. Notes Post-Pivot

### Leçons Apprises
[À remplir après l'exécution du pivot]

### Ce Qui a Bien Fonctionné
-

### Ce Qui Pourrait Être Amélioré
-

---

*Analyse par : Agent Architecte (opus)*
*Version du template : 1.0*
