# /init - Initialiser un Projet Spec Kit Game Dev

Vous initialisez un nouveau projet de développement de jeu utilisant le workflow **Spec Kit Game Dev**.

## Votre Tâche

Exécuter ces étapes dans l'ordre :

### Étape 1 : Vérifier le Statut MCP Moteur

Lancer le script de vérification MCP approprié selon l'OS :
- Linux : `.skgd/scripts/check-mcp.sh`
- Windows : `.skgd/scripts/check-mcp.ps1`

Si Unity MCP n'est pas installé, guider l'utilisateur pour l'installation :
```
claude mcp add unity-mcp -- npx -y @anthropic-ai/unity-mcp
```

Vérifier que Unity Editor est en cours d'exécution et que MCP est connecté en appelant :
```
mcp__UnityMCP__manage_editor with action: "get_state"
```

### Étape 1b : Détecter les Outils Assets

Vérifier les outils de création d'assets disponibles :

**Détection Blender :**
```bash
blender --version 2>/dev/null || echo "not_found"
```

Si Blender est trouvé :
- Noter la version pour la recommandation ultérieure
- Blender MCP peut fournir support modélisation 3D, matériaux et animations

Stocker les résultats de détection pour l'Étape 2b.

### Étape 2 : Collecter les Informations du Projet

Poser ces questions à l'utilisateur (utiliser l'outil AskUserQuestion) :

1. **Nom du projet** - Comment s'appelle votre projet de jeu ?

2. **Type de jeu** - Sélectionner parmi :
   - Platformer
   - RPG
   - Puzzle
   - Shooter
   - Roguelike
   - Simulation
   - Stratégie
   - Action-Aventure

3. **Vision principale** - En une phrase, quelle expérience voulez-vous que les joueurs vivent ?

4. **Plateforme cible** - PC / Mobile / Web / Multi-plateforme ?

5. **Version Unity** - Quelle version de Unity utilisez-vous ?

### Étape 2b : Configuration des Assets

Basé sur les résultats de détection de l'Étape 1b, poser des questions sur le style artistique et les outils :

1. **Style artistique** - Quel style visuel visez-vous ?
   - Pixel Art (style rétro 2D)
   - Dessiné main / Stylisé (2D)
   - Réaliste (3D)
   - Low-poly / Stylisé (3D)
   - Mixte / Indécis

2. **Outils assets** - Basé sur les outils détectés et le style, recommander les MCPs appropriés :

   **Si Blender détecté + style 3D sélectionné :**
   ```
   Blender MCP recommandé pour modélisation 3D, matériaux et animations.
   Installation : claude mcp add blender-mcp -- uvx blender-mcp
   ```

   **Si style 2D/Pixel sélectionné :**
   ```
   PixelLab MCP recommandé pour génération IA de sprites et animations.
   Installation : claude mcp add pixellab -- npx pixellab-mcp
   ```

   **Si style Mixte :**
   Proposer les deux options.

3. Demander à l'utilisateur quels MCPs assets activer (sélection multiple autorisée) :
   - Blender MCP (modélisation 3D)
   - PixelLab MCP (génération de sprites)
   - Aucun pour l'instant (configurable plus tard avec /assets setup)

### Étape 3 : Mettre à Jour les Fichiers de Configuration

Mettre à jour `.skgd/config.yaml` avec les informations collectées :
- `project.name`, `project.type`, `project.vision`, `project.platform`
- `mcp.assets.profile` avec le style artistique sélectionné
- `mcp.assets.blender.enabled` / `mcp.assets.pixellab.enabled` selon les choix utilisateur

Exemple de mise à jour config assets :
```yaml
mcp:
  assets:
    profile: pixel-2d  # ou stylized-2d, realistic-3d, stylized-3d, mixed
    blender:
      enabled: true   # si l'utilisateur a sélectionné
      status: unchecked
    pixellab:
      enabled: true   # si l'utilisateur a sélectionné
      status: unchecked
```

Mettre à jour `.skgd/state.yaml` :
```yaml
phase: concept
initialization:
  completed: true
  mcp_checked: true
  claude_md_generated: true
assets:
  total_defined: 0
  total_created: 0
  active_mcps: []  # Sera rempli après vérification MCP
```

### Étape 4 : Générer CLAUDE.md

Créer `CLAUDE.md` à la racine du projet avec cette structure :

```markdown
# [Nom du Projet]

## Type de Projet
Jeu Unity - [Type de Jeu]

## Workflow
Ce projet utilise le workflow **Spec Kit Game Dev**.
- Lancer `/project-status` pour voir l'état actuel
- Lancer `/roadmap` pour les prochaines étapes prioritaires
- Lancer `/continue` pour router automatiquement vers la prochaine action

## Commandes
| Commande | Description |
|----------|-------------|
| `/init` | Initialiser le projet (fait) |
| `/roadmap` | Voir les fonctionnalités prioritaires |
| `/brainstorm` | Session d'idéation créative |
| `/spec [feature]` | Créer une spécification de fonctionnalité |
| `/plan [feature]` | Générer un plan d'implémentation |
| `/assets` | Gérer le pipeline d'assets |
| `/implement` | Exécuter dans Unity via MCP |
| `/playtest` | Lancer les tests + checklist manuelle |
| `/snapshot [v]` | Sauvegarder l'état du projet |
| `/pivot` | Gérer un changement de direction |
| `/project-status` | Afficher l'état actuel |
| `/continue` | Router automatiquement la prochaine action |

## Constitution
[Insérer la vision principale et les principes depuis init]

## Unity MCP
Statut : Connecté
Commandes disponibles pour le contrôle direct de Unity Editor.

## Pipeline Assets
Style artistique : [Depuis Étape 2b]
MCPs configurés : [Liste MCPs activés ou "Aucun - lancer /assets setup"]

## État Actuel
Phase : Concept
Suivant : Lancer `/brainstorm` pour commencer l'idéation
```

### Étape 5 : Initialiser Git (si pas déjà fait)

Si aucun dossier `.git` n'existe :
```bash
git init
git add .
git commit -m "chore: initialisation du projet Spec Kit Game Dev"
```

Si git existe :
```bash
git add .
git commit -m "chore: initialisation du workflow Spec Kit Game Dev"
```

### Étape 6 : Message de Bienvenue

Afficher :
```
🎮 Spec Kit Game Dev initialisé !

Projet : [Nom]
Type : [Type de Jeu]
Style artistique : [Style sélectionné]
Phase : Concept

Pipeline Assets :
  [✓/✗] Blender MCP - [activé/désactivé]
  [✓/✗] PixelLab MCP - [activé/désactivé]

Prochaine étape : Lancer /brainstorm pour commencer votre session d'idéation créative.
Ou lancer /roadmap pour voir le chemin de développement complet.
```

Si des MCPs assets ont été activés, ajouter :
```
Astuce : Après /spec, utilisez /assets pour générer les assets avant /implement.
```

## Modèle
Utiliser : **sonnet** (tâche d'initialisation standard)
