# /implement - Exécuter l'Implémentation

Tu es Opus, implémentant une fonctionnalité via les outils MCP du moteur configuré (Unity ou Godot).

## Modèle

**OBLIGATOIRE: opus** - Les opérations MCP requièrent compréhension précise et décisions complexes.

## Langue

Lire `.skgd/config.yaml` → `user.language`
Utiliser `.skgd/i18n/messages.yaml` pour le texte utilisateur.

## Philosophie

**NE PAS déléguer l'implémentation à un sous-agent.** Les opérations MCP nécessitent:
- Compréhension du contexte depuis le plan
- Adaptation aux situations inattendues
- Décisions temps réel sur les erreurs
- Maintien des standards de qualité

Utiliser Task(Sonnet) UNIQUEMENT pour:
- Rechercher des patterns de code existants
- Lire plusieurs fichiers de référence
- Trouver des emplacements d'assets

---

## Phase 0 : Scout Context

**AVANT toute autre étape**, utiliser l'outil Task pour collecter le contexte :

```yaml
Task:
  subagent_type: 'Explore'
  model: 'haiku'
  prompt: |
    Scout de contexte pour implémentation. Lire et résumer :

    1. `.skgd/config.yaml` :
       - Extraire `engine` (unity ou godot)
       - Extraire `user.language`

    2. `.skgd/state.yaml` :
       - Extraire `current_spec`
       - Extraire `implementation.checkpoint` si présent
       - Extraire `implementation.tasks_completed` si présent

    3. `docs/specs/[current_spec]/tasks.md` :
       - Compter total des tâches
       - Lister UNIQUEMENT les tâches NON cochées [ ]
       - Identifier les tâches [MVP] vs [POLISH]

    4. `docs/specs/[current_spec]/plan.md` :
       - Identifier la phase actuelle (basé sur tâches restantes)
       - Extraire 2-3 points clés de cette phase

    5. `.skgd/memory/learnings-core.md` :
       - Extraire 3-5 patterns pertinents pour cette feature

    Retourner au format Scout Report (max 500 tokens) :

    ## Scout Report: implement
    **Status:** [ready|resume|blocked]
    **Engine:** [unity|godot]
    **Feature:** [nom de la feature]
    **Language:** [fr|en]

    **Session:**
    - État: [nouveau | reprise depuis T0XX]
    - Checkpoint: [timestamp ou "aucun"]

    **Tâches:**
    - Total: [N] | Faites: [X] | Restantes: [N-X]
    - MVP restants: [liste courte]
    - Polish restants: [nombre]

    **Phase Actuelle:** [nom de la phase]
    - [point clé 1]
    - [point clé 2]

    **Learnings à Appliquer:**
    - [pattern 1]
    - [pattern 2]
    - [pattern 3]

    **Bloqueurs:** [liste ou "aucun"]
```

### Traitement du Scout Report

**Si Status = `blocked`:**
```
⛔ Implémentation bloquée

Raison : [du Scout Report]

Actions requises :
1. [action corrective]
2. Relancer /implement
```

**Si Status = `resume`:**
```
🔄 Session précédente détectée

Feature : [nom]
Progression : [X]/[N] tâches complétées
Dernier checkpoint : [timestamp]

[A] Reprendre depuis T0XX
[B] Recommencer depuis le début
[C] Voir le détail des tâches
```

**Si Status = `ready`:** Continuer avec Phase 1.

---

## Phase 1 : Vérifier Connexion MCP

### Si Engine = Unity

```yaml
mcp__UnityMCP__manage_editor:
  action: "get_state"
```

Si non connecté :
```
Connexion Unity requise.

Veuillez :
1. Ouvrir Unity Editor
2. Vérifier que le pont Unity MCP fonctionne (Window > Unity MCP)
3. Relancer /implement
```

### Si Engine = Godot

```yaml
mcp__gdai__get_project_info: {}
```

Si non connecté :
```
Connexion GDAI requise.

Veuillez :
1. Ouvrir Godot Editor avec votre projet
2. Vérifier que le plugin GDAI est activé (Project > Project Settings > Plugins)
3. Vérifier que le serveur GDAI tourne
4. Relancer /implement
```

---

## Phase 2 : Flux d'Implémentation

Pour chaque tâche du Scout Report (en ordre) :

### Unity - Créer Scripts

```yaml
mcp__UnityMCP__create_script:
  path: "Assets/Scripts/[Feature]/[Name].cs"
  contents: |
    using UnityEngine;

    public class [Name] : MonoBehaviour
    {
        // Implémentation suivant les patterns learnings-core
    }
```

### Godot - Créer Scripts

```yaml
mcp__gdai__create_script:
  file_path: "res://scripts/[feature]/[name].gd"
  content: |
    extends Node
    class_name [ClassName]

    # Implémentation suivant les patterns learnings-core
```

### Après CHAQUE Script - Vérifier Compilation

**Unity:**
```yaml
mcp__UnityMCP__read_console:
  types: ["error"]
  count: 10
```

**Godot:**
```yaml
mcp__gdai__get_godot_errors: {}
```

**Si erreurs: CORRIGER avant de continuer.** Ne pas accumuler les erreurs.

### Unity - Créer GameObjects

```yaml
mcp__UnityMCP__manage_gameobject:
  action: "create"
  name: "[Name]"
  primitive_type: "[Type]"
  position: [x, y, z]
  components_to_add: ["[Script]"]
```

### Godot - Créer Nodes

```yaml
mcp__gdai__add_node:
  parent_node_path: "/root/[Parent]"
  node_type: "CharacterBody2D"
  node_name: "[Name]"
```

### Configurer Propriétés

**Unity:**
```yaml
mcp__UnityMCP__manage_gameobject:
  action: "set_component_property"
  target: "[GameObject]"
  component_name: "[Component]"
  component_properties:
    "[Property]": "[Value]"
```

**Godot:**
```yaml
mcp__gdai__update_property:
  node_path: "/root/[Node]"
  property_name: "position"
  property_value: "Vector2(100, 200)"
```

### Sauvegarder (après chaque étape majeure)

**Unity:**
```yaml
mcp__UnityMCP__manage_scene:
  action: "save"
```

**Godot:** Auto-save via GDAI.

---

## Phase 3 : Checkpoints

Toutes les **5-10 tâches** ou sur demande utilisateur ("stop", "pause", "save"):

1. **Mettre à jour tasks.md** - Marquer les tâches complétées [x]

2. **Sauvegarder le checkpoint** dans `.skgd/state.yaml`:
```yaml
implementation:
  feature: [nom]
  checkpoint: [timestamp ISO]
  tasks_completed: ["T001", "T002", ...]
  last_task: "T0XX"
```

3. **Informer l'utilisateur:**
```
💾 Checkpoint sauvegardé

Progression : [X]/[N] tâches
Dernière tâche : T0XX - [description]

Pour reprendre : /implement (détection auto)
Pour forcer reprise : /implement continue
```

---

## Phase 4 : Vérification Finale

Après toutes les tâches complétées :

### Vérification Console

**Unity:**
```yaml
mcp__UnityMCP__read_console:
  types: ["error", "warning"]
```

**Godot:**
```yaml
mcp__gdai__get_godot_errors: {}
```

### Test Rapide en Play Mode

**Unity:**
```yaml
mcp__UnityMCP__manage_editor:
  action: "play"
  wait_for_completion: false

# Observer brièvement, puis :
mcp__UnityMCP__manage_editor:
  action: "stop"
```

**Godot:**
```yaml
mcp__gdai__play_scene:
  scene_path: "res://scenes/[current].tscn"

# Observer brièvement, puis :
mcp__gdai__stop_running_scene: {}
```

---

## Phase 5 : Finalisation

### Mettre à Jour l'État

```yaml
# .skgd/state.yaml
production:
  current_step: playtest

implementation:
  feature: [nom]
  status: completed
  completed_at: [timestamp]
```

### Git Commit

```bash
git add Assets/ docs/specs/[feature]/tasks.md .skgd/state.yaml
# ou pour Godot: git add res://scenes/ res://scripts/ ...

git commit -m "feat([feature]): implémenter [nom-feature]

Scripts: [liste]
[GameObjects|Nodes]: [liste]
Console: [propre/warnings]"
```

### Résumé

```
✅ Implémentation terminée : [feature-name]

Créé :
  Scripts : [liste avec chemins]
  [GameObjects|Nodes] : [liste]

Console : [statut]
Tâches : [N]/[N] complétées
```

### Auto-Suggest

Après l'affichage du résumé, montrer le prompt auto-suggest :

```
───────────────────────────────────────
Suivant : Valider l'implémentation
[Entrée] /playtest | [S] stop
───────────────────────────────────────
```

- Si l'utilisateur appuie sur **Entrée** ou dit "oui"/"continuer" : Exécuter `/playtest`
- Si l'utilisateur dit **"stop"**, **"s"**, ou autre chose : Quitter et laisser l'utilisateur contrôler le rythme

---

## Gestion des Erreurs

### Erreurs de Compilation
1. Lire l'erreur complète
2. Identifier script et ligne
3. Corriger immédiatement
4. Revérifier la compilation
5. Continuer seulement si propre

### Erreurs Runtime
1. Arrêter le mode play
2. Lire les détails de l'erreur
3. Analyser la cause racine
4. Corriger et retester

### Connexion MCP Perdue
1. Sauvegarder le checkpoint immédiatement
2. Informer l'utilisateur
3. Reprendre avec `/implement` après reconnexion

---

## Standards de Qualité

### Unity (C#)
- Une responsabilité par script
- Composants plutôt qu'héritage
- `[SerializeField]` pour les valeurs inspector
- Cache des références dans `Awake()`
- Éviter `Find*` dans `Update()`

### Godot (GDScript)
- Une responsabilité par script
- Composition via nodes
- `@export` pour les valeurs inspector
- `@onready` pour les références de nodes
- Signal Bus pour événements globaux

---

## Arguments Optionnels

- `/implement` - Détection auto (nouveau ou reprise)
- `/implement continue` - Forcer la reprise sans question
- `/implement mvp` - Scope MVP uniquement
- `/implement T001-T020` - Range de tâches spécifique

---

## Rappel

- **Compiler après chaque script** - Ne pas accumuler les erreurs
- **Sauvegarder fréquemment** - Les changements de scène peuvent être perdus
- **Vérifier la console constamment** - Les warnings deviennent souvent des erreurs
- **Suivre le plan** - Mais s'adapter si problèmes découverts
- **Qualité avant vitesse** - Mieux vaut corriger maintenant que débugger plus tard
