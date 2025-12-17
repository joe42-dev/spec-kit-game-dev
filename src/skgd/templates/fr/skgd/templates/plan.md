# [Nom de la Fonctionnalité] - Plan d'Implémentation

> Template pour les plans d'implémentation techniques

## Approche Technique

### Stratégie
[Description de haut niveau de comment cela sera construit]

### Pattern d'Architecture
[Pattern utilisé : Composant, Machine à États, Événementiel, etc.]

### Décisions Clés
| Décision | Choix | Justification |
|----------|-------|---------------|
| [Point de décision] | [Approche choisie] | [Pourquoi] |

## Architecture des Composants

### Vue d'ensemble des Scripts
```
Assets/Scripts/[Fonctionnalité]/
├── [ScriptPrincipal].cs       # [Responsabilité principale]
├── [ScriptAuxiliaire].cs      # [Responsabilité de support]
└── [ScriptDonnées].cs         # [Responsabilité données/config]
```

### Diagramme de Classes
```
[ClassePrincipale]
├── Champs
│   ├── [champ1]: [type]
│   └── [champ2]: [type]
├── Méthodes
│   ├── [Méthode1]()
│   └── [Méthode2]()
└── Événements
    └── [OnÉvénement]
```

### Dépendances des Composants
```
[ComposantA] ──référence──> [ComposantB]
     │
     └──écoute──> [SystèmeÉvénements]
```

## Phases d'Implémentation

### Phase 0 : Préparation des Assets
**Objectif :** S'assurer que tous les assets requis existent avant l'implémentation du code
**Complexité Estimée :** Variable

> Cette phase s'exécute AVANT l'implémentation du code.
> Utilisez /assets generate [fonctionnalité] ou créez des placeholders.

#### Liste de Contrôle des Assets (depuis la spec)
| Asset | Type | Statut | MCP | Notes |
|-------|------|--------|-----|-------|
| [nom_asset] | sprite | en attente | pixellab | [notes] |
| [nom_asset] | modèle | en attente | blender | [notes] |
| [nom_asset] | sfx | en attente | manuel | [notes] |

#### Commandes de Génération d'Assets
```yaml
# Option A : Générer via PixelLab MCP (sprites 2D)
# [Les commandes seront ajoutées par /assets generate]

# Option B : Générer via Blender MCP (modèles 3D)
# [Les commandes seront ajoutées par /assets generate]

# Option C : Créer des placeholders
mcp__UnityMCP__manage_asset:
  action: create
  asset_type: "Texture2D"
  path: "Assets/Art/Sprites/placeholder_[nom].png"
  properties:
    width: 32
    height: 32
    color: "#FF6B6B"  # Couleur placeholder
```

#### Import des Assets (après génération)
```yaml
# Importer les assets générés dans Unity
mcp__UnityMCP__manage_asset:
  action: import
  path: "Assets/Art/Sprites/[fichier_généré]"
```

#### Vérification
- [ ] Tous les assets requis existent dans le projet
- [ ] Les assets respectent les conventions de nommage
- [ ] Pas de références manquantes dans les prefabs/scènes

---

### Phase 1 : Fondation
**Objectif :** [Ce que cette phase accomplit]
**Complexité Estimée :** Faible

#### Tâches
1. [ ] Créer la structure de dossiers
2. [ ] Créer le(s) script(s) de base
3. [ ] Configurer le GameObject initial

#### Commandes Unity MCP
```yaml
# Étape 1 : Créer le dossier
manage_asset:
  action: create_folder
  path: "Assets/Scripts/[Fonctionnalité]"

# Étape 2 : Créer le script
create_script:
  path: "Assets/Scripts/[Fonctionnalité]/[Script].cs"
  contents: |
    using UnityEngine;

    public class [Script] : MonoBehaviour
    {
        // Code de fondation
    }

# Étape 3 : Créer le GameObject
manage_gameobject:
  action: create
  name: "[NomObjet]"
  components_to_add: ["[Script]"]
```

#### Vérification
- [ ] Pas d'erreurs de compilation
- [ ] Le GameObject existe dans la scène
- [ ] Le composant est attaché

---

### Phase 2 : Logique Principale
**Objectif :** [Ce que cette phase accomplit]
**Complexité Estimée :** Moyenne

#### Tâches
1. [ ] Implémenter la fonctionnalité principale
2. [ ] Ajouter les composants requis
3. [ ] Configurer les paramètres initiaux

#### Commandes Unity MCP
```yaml
# [Commandes spécifiques pour cette phase]
```

#### Vérification
- [ ] Le comportement principal fonctionne en mode play
- [ ] Les paramètres affectent correctement le comportement

---

### Phase 3 : Intégration
**Objectif :** [Ce que cette phase accomplit]
**Complexité Estimée :** Moyenne

#### Tâches
1. [ ] Connecter aux autres systèmes
2. [ ] Configurer les événements/callbacks
3. [ ] Tester les interactions

#### Commandes Unity MCP
```yaml
# [Commandes spécifiques pour cette phase]
```

#### Vérification
- [ ] Les systèmes communiquent correctement
- [ ] Pas d'erreurs de référence null

---

### Phase 4 : Polish
**Objectif :** [Ce que cette phase accomplit]
**Complexité Estimée :** Faible

#### Tâches
1. [ ] Gérer les cas limites
2. [ ] Ajouter le feedback (hooks visuels/audio)
3. [ ] Vérification des performances

#### Vérification
- [ ] Cas limites gérés
- [ ] Performance fluide
- [ ] Tous les critères d'acceptation remplis

## Évaluation des Risques

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| [Risque 1] | Faible/Moy/Élevé | Faible/Moy/Élevé | [Comment mitiger] |
| [Risque 2] | Faible/Moy/Élevé | Faible/Moy/Élevé | [Comment mitiger] |

## Stratégie de Test

### Tests Automatisés

#### Tests EditMode
```csharp
[Test]
public void [NomDuTest]()
{
    // Logique de test
}
```

#### Tests PlayMode
```csharp
[UnityTest]
public IEnumerator [NomDuTest]()
{
    // Logique de test
    yield return null;
}
```

### Vérification Manuelle
- [ ] [Vérification manuelle 1]
- [ ] [Vérification manuelle 2]

## Plan de Rollback

Si l'implémentation échoue :
1. Revenir au dernier commit fonctionnel
2. Analyser ce qui a mal tourné
3. Ajuster l'approche ou la spec
4. Réessayer

## Effort Estimé

| Phase | Scripts | GameObjects | Complexité |
|-------|---------|-------------|------------|
| Fondation | [N] | [N] | Faible |
| Logique Principale | [N] | [N] | Moyenne |
| Intégration | [N] | [N] | Moyenne |
| Polish | [N] | [N] | Faible |
| **Total** | **[N]** | **[N]** | **[Global]** |

---

*Créé : [timestamp]*
*Spec : docs/specs/[fonctionnalité]/spec.md*
*Auteur : Agent Architecte*
