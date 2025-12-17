# Template de Checklist de Playtest

> Template de base pour le playtest de fonctionnalités

## Informations de la Session
- **Fonctionnalité :** [Nom de la fonctionnalité]
- **Testeur :** [Nom]
- **Date :** [Date]
- **Build :** [Version/Commit]

---

## Tests Automatisés

### Tests EditMode
- [ ] Tous les tests passent
- **Résultat :** [ ] Réussi [ ] Échoué
- **Détails :** _____________

### Tests PlayMode
- [ ] Tous les tests passent
- **Résultat :** [ ] Réussi [ ] Échoué
- **Détails :** _____________

---

## État de la Console

### Avant le Play
- [ ] Console effacée
- [ ] Pas d'erreurs existantes

### Après le Play
| Type | Nombre | Critique ? |
|------|--------|------------|
| Erreurs | | [ ] Oui [ ] Non |
| Avertissements | | [ ] Oui [ ] Non |

### Problèmes Trouvés
| Message | Sévérité | Action |
|---------|----------|--------|
| | | |

---

## Critères d'Acceptation

> Depuis la spec - chacun doit réussir

### CA-1 : [Critère de la spec]
- **Étapes de Test :**
  1. [Étape]
  2. [Étape]
- **Attendu :** [Résultat]
- **Réel :** _____________
- **Résultat :** [ ] Réussi [ ] Échoué

### CA-2 : [Critère]
- **Étapes de Test :**
  1. [Étape]
  2. [Étape]
- **Attendu :** [Résultat]
- **Réel :** _____________
- **Résultat :** [ ] Réussi [ ] Échoué

### CA-3 : [Critère]
- **Étapes de Test :**
  1. [Étape]
  2. [Étape]
- **Attendu :** [Résultat]
- **Réel :** _____________
- **Résultat :** [ ] Réussi [ ] Échoué

---

## Cas Limites

> Depuis les cas limites de la spec

### Limite 1 : [Cas limite]
- **Déclencheur :** [Comment le provoquer]
- **Attendu :** [Comportement]
- **Réel :** _____________
- **Résultat :** [ ] Réussi [ ] Échoué

### Limite 2 : [Cas limite]
- **Déclencheur :** [Comment le provoquer]
- **Attendu :** [Comportement]
- **Réel :** _____________
- **Résultat :** [ ] Réussi [ ] Échoué

---

## Évaluation du Game Feel

### Réactivité
- [ ] L'input semble immédiat (< 100ms perçu)
- [ ] Pas de latence d'input
- [ ] Pas d'inputs perdus
- **Notes :** _____________

### Feedback
- [ ] Les actions ont un feedback visuel clair
- [ ] Feedback sonore présent (ou noté comme TODO)
- [ ] Les changements d'état sont évidents
- **Notes :** _____________

### Cohérence
- [ ] Même input = même résultat
- [ ] Comportement prévisible
- [ ] Pas de cas limites inattendus
- **Notes :** _____________

### Polish
- [ ] Pas de glitches visuels
- [ ] Pas de saccades d'animation
- [ ] Transitions fluides
- **Notes :** _____________

---

## Performance

### Frame Rate
- [ ] Stable au FPS cible
- [ ] Pas de chutes significatives
- **Mesuré :** _____ FPS (moy)

### Réactivité
- [ ] Pas de freezes
- [ ] Pas de saccades
- [ ] Chargement de scène rapide

### Mémoire
- [ ] Pas de fuites évidentes (jouer 5 min)
- [ ] Mémoire stable

---

## Observations Libres

### Ce qui Fonctionne Bien
-
-

### Ce qui Doit Être Amélioré
-
-

### Comportements Inattendus
-
-

### Idées/Suggestions
-
-

---

## Bugs Trouvés

| ID | Description | Sévérité | Étapes de Repro | Statut |
|----|-------------|----------|-----------------|--------|
| B1 | | [ ] Bloquant [ ] Critique [ ] Majeur [ ] Mineur | | [ ] Ouvert |
| B2 | | | | |
| B3 | | | | |

---

## Résumé

### Critères Remplis
- Acceptation : [X]/[Total]
- Cas Limites : [X]/[Total]
- Game Feel : [X]/[Total]

### Verdict Global
[ ] **RÉUSSI** - Tous les critères remplis, prêt à continuer
[ ] **CONDITIONNEL** - Problèmes mineurs, peut continuer avec les éléments notés
[ ] **ÉCHOUÉ** - Problèmes bloquants, nécessite des corrections

### Problèmes Bloquants
1. [Si applicable]

### Prochaines Actions
- [ ] [Action nécessaire]
- [ ] [Action nécessaire]

---

*Testé par : Agent Testeur*
*Version du template : 1.0*
