# /continue - Routeur Automatique Intelligent

Vous êtes le routeur intelligent qui détermine et exécute la prochaine action.

## Votre Tâche

### Étape 1 : Charger l'État Minimal

Lire uniquement :
- `.skgd/state.yaml` - État actuel

### Étape 2 : Déterminer la Prochaine Action

```
Arbre de Décision :

SI phase == "uninitialized":
    → Exécuter /init

SINON SI phase == "concept":
    SI brainstorm_done == false:
        → Exécuter /brainstorm
    SINON SI game_brief_done == false:
        → Continuer le brainstorming pour générer le brief
    SINON:
        → Mettre à jour la phase vers "design", exécuter /roadmap

SINON SI phase == "design":
    SI current_spec != null:
        → Continuer avec le workflow de spec actuel
    SINON:
        → Exécuter /roadmap pour obtenir la prochaine spec

SINON SI phase == "architecture":
    SI technical_doc_done == false:
        → Exécuter /spec architecture
    SINON:
        → Mettre à jour la phase vers "production", exécuter /roadmap

SINON SI phase == "production":
    SI current_spec == null:
        → Exécuter /roadmap pour obtenir la prochaine fonctionnalité
    SINON:
        SELON current_step:
            CAS "spec":
                → Vérifier que la spec est complète, passer à "plan"
            CAS "plan":
                → Exécuter /plan [current_spec]
            CAS "implement":
                → Exécuter /implement
            CAS "playtest":
                → Exécuter /playtest
            CAS null:
                → Commencer avec /spec [current_spec]
```

### Étape 3 : Exécuter l'Action Déterminée

Afficher ce que vous faites :
```
🔄 Routage automatique basé sur l'état du projet...

Actuel : [phase] / [étape]
Action : [action déterminée]

Exécution...
```

Puis exécuter la commande appropriée en :
1. Chargeant le fichier de commande pertinent
2. Suivant ses instructions
3. Utilisant le modèle correct pour cette commande

### Étape 4 : Mettre à Jour l'État Après l'Action

Mettre à jour `.skgd/state.yaml` avec :
- Nouvelle phase/étape si changée
- Détails de last_action
- Tout flag de complétion

### Étape 5 : Suggérer la Suite

Après avoir terminé l'action, afficher :
```
✅ Terminé : [action]

Prochaines options :
  → /continue - Routage automatique vers la prochaine action
  → /project-status - Voir l'état complet du projet
  → /roadmap - Revoir le chemin de développement
```

## Sélection du Modèle

Le routeur lui-même utilise **haiku** (léger).
Les actions déléguées utilisent leurs propres exigences de modèle :
- /brainstorm → opus
- /spec → sonnet
- /plan → opus
- /implement → sonnet
- /playtest → sonnet

## Important

- Ne jamais sauter d'étapes dans le workflow
- Toujours vérifier que l'étape précédente est terminée avant d'avancer
- Si bloqué ou erreur, suggérer /project-status pour le débogage
- Enregistrer toutes les décisions de routage dans state.yaml
