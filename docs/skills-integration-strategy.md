# Claude Skills Integration Strategy for SKGD

## Executive Summary

Les Claude Skills offrent une opportunité majeure pour SKGD: **charger automatiquement le contexte technique approprié** sans intervention explicite de l'utilisateur. Cette analyse détaille la stratégie d'intégration optimale.

---

## 1. Pourquoi les Skills pour SKGD?

### Différence fondamentale: Slash Commands vs Skills

| Aspect | Slash Commands (actuel) | Agent Skills (proposé) |
|--------|------------------------|------------------------|
| **Invocation** | Explicite (`/implement`) | Automatique (contexte) |
| **Découverte** | L'user doit connaître | Claude détecte et charge |
| **Structure** | 1 fichier MD | Dossier multi-fichiers |
| **Contexte** | Tout chargé à l'invocation | Progressive disclosure |

### Le gap actuel dans SKGD

```
AUJOURD'HUI:
User: "Je veux créer un prefab player avec CharacterController"
Claude: [Doit utiliser /implement qui charge TOUT implement-unity.md]
        [~3000 tokens chargés même pour une petite tâche]

AVEC SKILLS:
User: "Je veux créer un prefab player avec CharacterController"
Claude: [Skill unity-gamedev détecté automatiquement]
        [Charge SKILL.md minimal ~200 tokens]
        [Charge prefabs.md à la demande si nécessaire]
        [Contexte total: ~500 tokens au lieu de 3000]
```

### Bénéfices concrets

1. **Réduction contexte**: -60% de tokens pour tâches simples
2. **Découverte fluide**: Pas besoin de connaître la commande exacte
3. **Progressive disclosure**: Info technique chargée à la demande
4. **Meilleure qualité**: Patterns validés directement accessibles

---

## 2. Architecture Skills proposée

### Structure générale

```
.claude/skills/
├── unity-gamedev/              # Skill principal Unity
│   ├── SKILL.md                # Overview + navigation (~400 tokens)
│   ├── reference/
│   │   ├── scripts.md          # Patterns C# + create_script
│   │   ├── gameobjects.md      # manage_gameobject patterns
│   │   ├── prefabs.md          # Prefab workflow
│   │   ├── scenes.md           # Scene management
│   │   └── testing.md          # run_tests patterns
│   └── checklists/
│       └── pre-implement.md    # Verification checklist
│
├── godot-gamedev/              # Skill principal Godot
│   ├── SKILL.md                # Overview + navigation
│   ├── reference/
│   │   ├── scripts.md          # GDScript patterns
│   │   ├── nodes.md            # add_node patterns
│   │   ├── scenes.md           # Scene structure
│   │   └── signals.md          # Signal patterns
│   └── checklists/
│       └── pre-implement.md
│
└── gamedev-specs/              # Skill écriture specs (optionnel)
    ├── SKILL.md
    └── templates/
        ├── mechanic-spec.md
        └── system-spec.md
```

### Synergie Slash Commands + Skills

```
┌─────────────────────────────────────────────────────────────┐
│                    WORKFLOW HYBRIDE                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SLASH COMMANDS (workflow explicite)                        │
│  ├── /brainstorm  → Dialogue créatif structuré              │
│  ├── /spec        → Génération spec complète                │
│  ├── /plan        → Planification technique                 │
│  ├── /implement   → Orchestration implémentation            │
│  └── /playtest    → Validation structurée                   │
│                                                             │
│                         ↓                                   │
│                    DÉCLENCHE                                │
│                         ↓                                   │
│                                                             │
│  SKILLS (contexte automatique)                              │
│  ├── unity-gamedev   → Patterns Unity MCP                   │
│  ├── godot-gamedev   → Patterns GDAI MCP                    │
│  └── gamedev-specs   → Templates specs game                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘

EXEMPLE CONCRET:
1. User: /implement
2. implement.md s'exécute, détecte engine=unity
3. Claude voit la tâche nécessite un script
4. Skill unity-gamedev auto-détecté
5. Charge scripts.md de reference/
6. Patterns C# + best practices disponibles
7. Implémentation avec contexte optimal
```

---

## 3. Spécifications des Skills

### Skill 1: unity-gamedev

**SKILL.md (frontmatter)**:
```yaml
---
name: unity-gamedev
description: Unity game development patterns and Unity MCP tool usage. Provides C# scripting templates, GameObject management, prefab workflows, scene operations, and testing patterns. Use when working with Unity, creating MonoBehaviours, managing GameObjects, or running Unity tests.
---
```

**Contenu SKILL.md (~400 tokens)**:
- Quick reference des outils MCP clés
- Navigation vers fichiers de référence
- Checklist pré-implémentation
- Anti-patterns Unity à éviter

**Fichiers reference/ (chargés à la demande)**:
- `scripts.md`: Patterns create_script, apply_text_edits, validation
- `gameobjects.md`: manage_gameobject, hierarchy, components
- `prefabs.md`: Workflow création/modification prefabs
- `scenes.md`: manage_scene, save patterns
- `testing.md`: run_tests, console checking

### Skill 2: godot-gamedev

**SKILL.md (frontmatter)**:
```yaml
---
name: godot-gamedev
description: Godot game development patterns and GDAI MCP tool usage. Provides GDScript templates, node management, scene structure, and signal patterns. Use when working with Godot, creating GDScript files, managing nodes, or debugging Godot projects.
---
```

**Structure similaire à unity-gamedev** adaptée pour:
- GDScript patterns
- Node hierarchy
- Signal/slot patterns
- Godot-specific testing

### Skill 3: gamedev-specs (optionnel)

**SKILL.md (frontmatter)**:
```yaml
---
name: gamedev-specs
description: Game design specification templates and patterns. Provides structured templates for game mechanics, systems, and features. Use when writing game design documents, specs, or planning game features.
---
```

**Contenu**:
- Templates specs par type (mechanic, system, UI)
- Checklist validation specs
- Patterns de paramètres game feel

---

## 4. Impact sur la gestion du contexte

### Comparaison avant/après

| Scénario | AVANT (slash only) | APRÈS (skills) | Économie |
|----------|-------------------|----------------|----------|
| Créer 1 script | ~3000 tokens | ~500 tokens | **-83%** |
| Modifier prefab | ~3000 tokens | ~600 tokens | **-80%** |
| Question patterns | ~3000 tokens | ~300 tokens | **-90%** |
| Implémentation complète | ~3000 tokens | ~1500 tokens | **-50%** |

### Progressive Disclosure en action

```
NIVEAU 1: Métadonnées (toujours chargé)
┌────────────────────────────────────────┐
│ name: unity-gamedev                    │  ~50 tokens
│ description: Unity game development... │
└────────────────────────────────────────┘

NIVEAU 2: SKILL.md (si pertinent)
┌────────────────────────────────────────┐
│ Quick reference                        │  ~400 tokens
│ Navigation links                       │
│ Core patterns                          │
└────────────────────────────────────────┘

NIVEAU 3: Reference file (si nécessaire)
┌────────────────────────────────────────┐
│ scripts.md OU gameobjects.md OU ...    │  ~500-800 tokens
│ Patterns détaillés pour la tâche       │
└────────────────────────────────────────┘

TOTAL MAXIMUM: ~1300 tokens
vs AVANT: ~3000 tokens (implement-unity.md complet)
```

---

## 5. Stratégie d'implémentation

### Phase 1: Fondation (Aujourd'hui)
1. Créer structure `.claude/skills/`
2. Implémenter `unity-gamedev` SKILL.md
3. Créer fichiers reference/ essentiels
4. Tester découverte automatique

### Phase 2: Extension (Semaine prochaine)
1. Implémenter `godot-gamedev`
2. Raffiner basé sur usage réel
3. Ajouter checklists validation

### Phase 3: Optimisation (Ongoing)
1. Analyser patterns d'utilisation
2. Ajuster granularité des fichiers reference/
3. Considérer `gamedev-specs` si bénéfique

### Règles d'intégration

**NE PAS remplacer les slash commands** - ils orchestrent le workflow
**Skills = contexte technique** - patterns, best practices, tool usage
**Slash commands = processus** - étapes structurées, validation, state management

---

## 6. Bénéfices attendus

### Qualité output
- Patterns validés toujours disponibles
- Anti-patterns documentés
- Checklists automatiques
- Moins d'erreurs (console check patterns inclus)

### Gestion contexte
- **-60% tokens** pour tâches simples
- **-40% tokens** pour tâches complexes
- Plus d'espace pour le code généré
- Meilleure rétention du contexte conversation

### Expérience utilisateur
- Découverte fluide ("je veux un prefab" → skill charge)
- Moins de commandes à mémoriser
- Aide contextuelle automatique
- Workflow plus naturel

---

## 7. Risques et mitigations

| Risque | Impact | Mitigation |
|--------|--------|------------|
| Conflit skills/commands | Medium | Descriptions distinctes, scopes clairs |
| Sur-découverte (trop de skills activés) | Low | Descriptions précises, test empirique |
| Maintenance double | Medium | Skills = static patterns, Commands = dynamic workflow |
| Learning curve team | Low | Documentation claire, skills auto-explicatifs |

---

## 8. Métriques de succès

- **Réduction tokens/tâche**: Target -50% moyenne
- **Découverte automatique**: >80% des cas Unity/Godot
- **Erreurs d'implémentation**: -30% (grâce aux checklists)
- **Satisfaction workflow**: Feedback qualitatif utilisateur

---

## Conclusion

L'intégration des Claude Skills dans SKGD représente une **évolution naturelle** du workflow:

1. **Slash commands** restent le backbone pour le processus structuré
2. **Skills** ajoutent le contexte technique à la demande
3. **Progressive disclosure** optimise drastiquement l'usage du contexte
4. **Découverte automatique** rend le workflow plus fluide

La stratégie recommandée est d'implémenter `unity-gamedev` en premier (cas d'usage principal), puis `godot-gamedev`, en itérant basé sur l'usage réel.
