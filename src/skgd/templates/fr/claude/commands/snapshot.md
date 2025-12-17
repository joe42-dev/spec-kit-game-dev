# /snapshot [version] - Sauvegarder l'État du Projet

Vous créez un snapshot de l'état actuel du projet pour le versionnage.

**Argument :** `$ARGUMENTS` (chaîne de version, ex: "v0.1", "v0.2-alpha")

## Votre Tâche

### Étape 1 : Déterminer la Version

Si argument fourni, l'utiliser.
Sinon, auto-incrémenter :
- Lire `.skgd/state.yaml` pour `snapshots.latest`
- Incrémenter (v0.1 → v0.2, etc.)

### Étape 2 : Collecter l'État Actuel

Lire :
- `.skgd/state.yaml` - État complet
- `.skgd/config.yaml` - Configuration
- `.skgd/roadmap.yaml` - Progression de la roadmap
- `docs/` - Toute la documentation

Lister les specs terminées :
```bash
ls docs/specs/
```

### Étape 3 : Créer le Répertoire de Snapshot

```bash
mkdir -p .skgd/snapshots/[version]/specs
```

### Étape 4 : Copier les Fichiers d'État

Copier l'état actuel vers le snapshot :

```yaml
# .skgd/snapshots/[version]/state.yaml
snapshot:
  version: "[version]"
  created: "[horodatage]"
  git_commit: "[hash HEAD actuel]"

project_state:
  phase: [phase actuelle]
  specs_completed: [liste]
  specs_in_progress: [liste]

summary:
  total_specs: [N]
  total_scripts: [N]
  total_gameobjects: [N]

notes: |
  [L'utilisateur peut ajouter des notes]
```

Copier les docs pertinents :
```bash
cp docs/game-brief.md .skgd/snapshots/[version]/
cp docs/gdd.md .skgd/snapshots/[version]/ 2>/dev/null || true
cp docs/architecture.md .skgd/snapshots/[version]/ 2>/dev/null || true
cp -r docs/specs/* .skgd/snapshots/[version]/specs/ 2>/dev/null || true
```

### Étape 5 : Mettre à Jour l'État Principal

Mettre à jour `.skgd/state.yaml` :
```yaml
snapshots:
  count: [incrémenter]
  latest: "[version]"
```

### Étape 6 : Tag Git

```bash
git add .skgd/snapshots/[version]/
git commit -m "chore: création du snapshot [version]

Phase : [phase]
Specs terminées : [N]
Jalon : [description si applicable]"

git tag -a [version] -m "Snapshot [version] : [brève description]"
```

### Étape 7 : Résumé

Afficher :
```
📸 Snapshot Créé : [version]

Emplacement : .skgd/snapshots/[version]/

Contenu :
├── state.yaml (état du projet)
├── game-brief.md
├── gdd.md (si existe)
├── architecture.md (si existe)
└── specs/
    ├── [spec1]/
    └── [spec2]/

Tag Git : [version]

Progression du Projet :
- Phase : [phase]
- Specs : [terminées]/[total]
- Depuis le dernier snapshot : [résumé des changements]

Pour restaurer ce snapshot plus tard :
  git checkout [version]

Pour comparer avec l'actuel :
  git diff [version]..HEAD

Tous les Snapshots :
[Liste de toutes les versions avec dates]
```

### Étape 8 : Demander des Notes

Utiliser AskUserQuestion :
```
Voulez-vous ajouter des notes à ce snapshot ?
(ex: jalon atteint, décisions clés prises, etc.)
```

Si oui, mettre à jour le state.yaml du snapshot avec les notes.

## Restaurer un Snapshot (pour référence)

Pour restaurer un snapshot (documenter pour l'utilisateur) :
```bash
# Voir l'état du snapshot
cat .skgd/snapshots/[version]/state.yaml

# Checkout le tag git
git checkout [version]

# Ou diff contre l'actuel
git diff [version]..HEAD -- docs/
```

## Modèle
Utiliser : **haiku** (opérations de fichiers simples)
