# /playtest - Lancer les Tests et la Validation

Vous lancez les tests automatisés et générez une checklist de playtest manuel.

## Votre Tâche

### Étape 1 : Charger le Contexte

Lire :
- `.skgd/state.yaml` - Fonctionnalité actuelle
- `docs/specs/[feature]/spec.md` - Critères d'acceptation
- `docs/specs/[feature]/tasks.md` - État de l'implémentation
- `.skgd/templates/playtest-checklist.md` - Template de checklist

### Étape 2 : Lancer les Tests Automatisés Unity

#### Tests EditMode
```yaml
mcp__UnityMCP__run_tests:
  mode: "EditMode"
  timeout_seconds: 60
```

#### Tests PlayMode
```yaml
mcp__UnityMCP__run_tests:
  mode: "PlayMode"
  timeout_seconds: 120
```

### Étape 3 : Vérifier l'État de la Console

```yaml
mcp__UnityMCP__read_console:
  types: ["error", "warning"]
  count: 50
```

Catégoriser les problèmes :
- **Bloquants** : Erreurs qui empêchent le gameplay
- **Avertissements** : Problèmes non critiques à suivre
- **Info** : Messages informatifs

### Étape 4 : Générer la Checklist de Playtest

Créer/mettre à jour `docs/specs/[feature]/playtest.md` :

```markdown
# [Nom de la Fonctionnalité] - Checklist de Playtest

## Résultats des Tests Automatisés
- EditMode : [✓ Passé / ✗ Échoué] ([N] tests)
- PlayMode : [✓ Passé / ✗ Échoué] ([N] tests)

## État de la Console
- Erreurs : [N]
- Avertissements : [N]

### Problèmes Trouvés
| Type | Message | Sévérité | Statut |
|------|---------|----------|--------|
| [Erreur/Avertissement] | [message] | [Élevée/Moyenne/Faible] | [Ouvert/Corrigé] |

---

## Checklist de Playtest Manuel

### Fonctionnalité Principale
Basée sur les critères d'acceptation de la spec :

- [ ] **CA-1** : [Critère depuis la spec]
  - Étapes : [Comment tester]
  - Attendu : [Résultat attendu]
  - Actuel : _____________

- [ ] **CA-2** : [Critère]
  - Étapes : [Comment tester]
  - Attendu : [Résultat attendu]
  - Actuel : _____________

### Cas Limites
Depuis les cas limites de la spec :

- [ ] **Limite 1** : [Cas limite]
  - Test : [Comment déclencher]
  - Attendu : [Comportement]
  - Actuel : _____________

### Ressenti & Polish
Vérifications qualité spécifiques au jeu :

- [ ] **Réactivité** : Les inputs sont immédiats
- [ ] **Feedback** : Les actions ont un retour clair
- [ ] **Cohérence** : Le comportement est prévisible
- [ ] **Pas de Saccades** : Pas de glitches visuels ou stutters

### Performance
- [ ] **Frame Rate** : Stable à [cible] FPS
- [ ] **Pas de Freezes** : Pas de drops de frames pendant le gameplay
- [ ] **Mémoire** : Pas de fuites mémoire évidentes

---

## Session de Playtest

### Testeur
Nom : _____________
Date : _____________

### Notes de Session
[Observations libres pendant le jeu]

### Bugs Trouvés
| ID | Description | Sévérité | Étapes de Repro |
|----|-------------|----------|-----------------|
| B1 | | | |

### Suggestions
[Idées d'amélioration émergées pendant le jeu]

---

## Résumé

### Réussite/Échec
- [ ] Tous les critères d'acceptation remplis
- [ ] Pas de bugs bloquants
- [ ] Performance acceptable

### Verdict
[ ] **RÉUSSI** - Prêt pour complétion
[ ] **ÉCHOUÉ** - Nécessite corrections (voir problèmes ci-dessus)

### Prochaine Action
Si RÉUSSI : `/continue` ou marquer la fonctionnalité comme terminée
Si ÉCHOUÉ : Corriger les problèmes, puis `/playtest` à nouveau
```

### Étape 5 : Guide de Playtest Interactif

Si l'utilisateur veut faire le playtest manuel maintenant, le guider :

```
🎮 Démarrage de la Session de Playtest

Je vais mettre Unity en mode Play. Suivez la checklist ci-dessus.

1. Ouverture du mode Play...
```

```yaml
mcp__UnityMCP__manage_editor:
  action: "play"
```

```
2. Testez chaque élément de la checklist
3. Notez les résultats dans playtest.md
4. Quand terminé, dites-moi d'arrêter

Commandes pendant le playtest :
- "stop" - Quitter le mode play
- "console" - Vérifier les erreurs
- "bug [description]" - Logger un bug
- "done" - Terminer le playtest
```

### Étape 6 : Traiter les Résultats

Après le playtest :

1. **Si tout est passé :**
   - Mettre à jour l'état vers prêt pour complétion
   - Suggérer de marquer la fonctionnalité comme terminée

2. **Si échecs :**
   - Lister les problèmes à corriger
   - Garder l'état en playtest
   - Suggérer de corriger puis relancer

### Étape 7 : Extraire & Sauvegarder les Apprentissages (Automatique)

Basé sur les résultats du playtest, extraire et catégoriser les apprentissages :

#### 7.1 Catégoriser les Découvertes

Pour chaque observation significative du playtest, catégoriser dans :

**Apprentissages Techniques:**
- Unity Patterns Qui Fonctionnent : [patterns qui ont réussi]
- Unity Patterns à Éviter : [patterns qui ont causé des problèmes]
- Insights Performance : [observations de performance]

**Apprentissages Design:**
- Mécaniques Qui Font du Bien : [ce qui semblait bien]
- Mécaniques à Améliorer : [ce qui nécessite du travail]
- Thèmes de Feedback Joueur : [patterns de feedback récurrents]

**Apprentissages Process:**
- Ce Qui Accélère le Développement : [pratiques efficaces découvertes]
- Ce Qui Ralentit le Développement : [goulots d'étranglement identifiés]

**Patterns de Bugs:**
- Problèmes Courants : [bugs récurrents rencontrés]
- Solutions Trouvées : [corrections qui ont fonctionné]

#### 7.2 Ajouter à learnings.md

Lire `.skgd/memory/learnings.md` puis AJOUTER les découvertes sous les en-têtes de sous-section appropriés.

**Format pour chaque découverte:**
```markdown
- [AAAA-MM-JJ] [feature]: [observation]
```

**Exemples d'ajouts:**
```markdown
### Unity Patterns That Work
<!-- Auto-populated -->
- 2024-01-15 player-movement: ScriptableObject events pour découplage des inputs

### Mechanics That Feel Good
<!-- Auto-populated -->
- 2024-01-15 player-movement: Coyote time (0.15s) se sent réactif
```

**Important:**
- Ajouter sous les en-têtes de sous-section EXISTANTS (ne pas créer de nouvelles sections)
- Garder les commentaires `<!-- Auto-populated -->` en place
- Une ligne par découverte, préfixée avec date et nom de feature

#### 7.3 Mettre à Jour les Métadonnées

En bas de learnings.md, mettre à jour les métadonnées :
```markdown
*Entries: [nouveau compte]*
*Last updated: [AAAA-MM-JJ]*
```

#### 7.4 Vérifier le Déclencheur de Cristallisation

Compter le total des entrées dans learnings.md (lignes commençant par `- ` sous les sous-sections).

**Si >30 entrées:** Afficher la suggestion :
```
Les apprentissages s'accumulent ([N] entrées). Considérez lancer /crystallize pour consolider les patterns.
```

### Étape 8 : Mettre à Jour l'État

```yaml
# Si passé :
production:
  current_step: null  # Prêt pour la prochaine fonctionnalité
specs:
  completed: [incrémenter]
  in_progress: null

# Si échoué :
production:
  current_step: implement  # Retour aux corrections
```

### Étape 9 : Commit Git

```bash
git add docs/specs/[feature]/playtest.md .skgd/
git commit -m "test([feature]): résultats du playtest

- Automatisé : [Passé/Échoué]
- Manuel : [N]/[N] vérifications passées
- Problèmes : [N] trouvés"
```

### Étape 10 : Résumé

```
🧪 Playtest Terminé : [nom-fonctionnalité]

Tests Automatisés :
  EditMode : [✓/✗]
  PlayMode : [✓/✗]

Vérifications Manuelles : [N]/[N] passées

Verdict : [RÉUSSI ✓ / ÉCHOUÉ ✗]

[Si RÉUSSI]
Suivant : /continue pour passer à la prochaine fonctionnalité
          /snapshot si c'est un jalon

[Si ÉCHOUÉ]
Problèmes à corriger :
1. [Problème 1]
2. [Problème 2]

Suivant : Corriger les problèmes, puis /playtest à nouveau
```

## Modèle
Utiliser : **sonnet** (tâche de test et validation)
