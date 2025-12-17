# /assets [sous-commande] - Gestion du Pipeline Assets

Vous gérez le pipeline d'assets pour ce projet de jeu.

**Argument :** `$ARGUMENTS` (sous-commande optionnelle : setup, list, generate)

## Modèle

**OBLIGATOIRE : sonnet** - Tâche d'orchestration, coordonner entre systèmes.

## Langue

Lire `.skgd/config.yaml` → `user.language`
Utiliser `.skgd/i18n/messages.yaml` pour le texte utilisateur.

## Philosophie

Cette commande est le **hub** pour toutes les opérations liées aux assets.
Elle orchestre entre plusieurs MCPs (Blender, PixelLab) et le moteur de jeu (Unity/Godot).

## Étape 1 : Charger le Contexte

Lire ces fichiers :
- `.skgd/config.yaml` → Configuration `mcp.assets`
- `.skgd/state.yaml` → Statut `assets`
- `.skgd/memory/assets-catalog.md` → Inventaire actuel

## Étape 2 : Router par Sous-commande

### Pas de sous-commande → Afficher Vue d'ensemble

```
🎨 STATUT DU PIPELINE ASSETS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Profil artistique : [profil ou "Non défini"]

📦 MCPs configurés :
  [✓/✗] Blender MCP - [statut]
  [✓/✗] PixelLab MCP - [statut]

📊 Progression des Assets :
  Sprites :    [##........] X/Y (Z%)
  Modèles :    [####......] X/Y (Z%)
  Animations : [#.........] X/Y (Z%)
  Audio :      [..........] X/Y (Z%)

🎯 Fonctionnalités nécessitant des assets :
  → [nom-feature] (N sprites, N animations)

Commandes :
  /assets setup              - Configurer MCPs assets
  /assets list [feature]     - Lister assets d'une feature
  /assets generate [feature] - Générer assets via MCP
```

### Sous-commande : setup

Guider l'utilisateur dans la configuration MCP.

### Sous-commande : list [feature]

Lister les assets requis depuis la spec.

### Sous-commande : generate [feature]

1. Charger la spec
2. Extraire les besoins en assets
3. Générer via MCP approprié ou créer placeholders
4. Importer dans le moteur
5. Mettre à jour le tracking

## Étape 3 : Mettre à jour l'État

Mettre à jour `.skgd/state.yaml` après chaque opération.

## Étape 4 : Résumé

Fournir un résumé clair et les prochaines étapes.
