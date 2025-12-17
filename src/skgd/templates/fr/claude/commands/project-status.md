# /project-status - Afficher l'État du Projet

Vous affichez l'état actuel du projet Spec Kit Game Dev.

## Votre Tâche

### Étape 1 : Lire les Fichiers d'État

Lire ces fichiers :
- `.skgd/state.yaml` - État actuel du workflow
- `.skgd/config.yaml` - Configuration du projet
- `.skgd/roadmap.yaml` - Si existe, roadmap actuelle

### Étape 2 : Vérifier la Connexion Unity MCP

Vérification rapide :
```
mcp__UnityMCP__manage_editor with action: "get_state"
```

### Étape 3 : Afficher le Tableau de Bord

Formater la sortie comme :

```
╔══════════════════════════════════════════════════════════════╗
║  🎮 SPEC KIT GAME DEV - ÉTAT                                 ║
╠══════════════════════════════════════════════════════════════╣
║  Projet : [Nom]                                              ║
║  Type : [Type de Jeu]                                        ║
║  Phase : [Phase Actuelle]                                    ║
╠══════════════════════════════════════════════════════════════╣
║  PROGRESSION                                                 ║
║  ├─ Concept :      [✓ Fait / ○ En Cours / · En Attente]     ║
║  ├─ Design :       [✓ / ○ / ·]                               ║
║  ├─ Architecture : [✓ / ○ / ·]                               ║
║  └─ Production :   [Cycle X - Étape Y]                       ║
╠══════════════════════════════════════════════════════════════╣
║  SPECS                                                       ║
║  ├─ Terminées : [N]                                          ║
║  ├─ En Cours : [Spec actuelle ou "Aucune"]                   ║
║  └─ Total : [N]                                              ║
╠══════════════════════════════════════════════════════════════╣
║  CONNEXIONS                                                  ║
║  ├─ Unity MCP : [🟢 Connecté / 🔴 Déconnecté]                ║
║  └─ Unity Editor : [En cours / Arrêté]                       ║
╠══════════════════════════════════════════════════════════════╣
║  SNAPSHOTS : [N] | Dernier : [version ou "Aucun"]            ║
║  PIVOTS : [N]                                                ║
╠══════════════════════════════════════════════════════════════╣
║  PROCHAINE ACTION                                            ║
║  → [Commande suggérée selon l'état]                          ║
╚══════════════════════════════════════════════════════════════╝
```

### Étape 4 : Suggérer la Prochaine Action

Selon l'état, suggérer :
- Si `phase: uninitialized` → "Lancer /init pour commencer"
- Si `phase: concept` et pas de brainstorm → "Lancer /brainstorm"
- Si `phase: concept` et brainstorm fait → "Lancer /roadmap"
- Si `phase: design` → "Lancer /spec [prochaine-fonctionnalité]"
- Si `phase: production` → "Lancer /continue"

## Modèle
Utiliser : **haiku** (simple vérification d'état)
