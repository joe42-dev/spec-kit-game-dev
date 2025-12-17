# Template Jeu RPG

> Guide spécifique pour le développement de jeux RPG

## Caractéristiques du Genre
- Progression de personnage (stats, capacités)
- Éléments de narration/histoire
- Système de combat
- Inventaire/équipement
- Souvent inclut de l'exploration

## Priorité des Systèmes Principaux

### 1. Système de Stats de Personnage (Critique)
**Stats Principales :**
| Stat | Objectif | Plage Typique |
|------|----------|---------------|
| Santé | Survie | 10-1000+ |
| Attaque | Dégâts infligés | 1-100+ |
| Défense | Réduction de dégâts | 0-50+ |
| Vitesse | Ordre de tour/mouvement | 1-100 |

**Stats Dérivées :**
- Dégâts = Attaque - Défense (clamped)
- Chance Critique = (Chance / 100)
- Esquive = Vitesse / 200

### 2. Système de Combat
**Tour par tour :**
- Sélection d'action
- Calcul d'ordre de tour
- Exécution d'action
- Gestion d'état

**Temps réel :**
- Gestion des inputs
- Gestion des cooldowns
- Acquisition de cible
- Calcul des dégâts

### 3. Système de Progression
- Points d'expérience
- Montée de niveau
- Augmentations de stats
- Déblocage de capacités

### 4. Système d'Inventaire
- Stockage d'objets
- Emplacements d'équipement
- Effets des objets
- Gestion des piles

## Ordre de Roadmap Recommandé

```
1. Stats de Personnage (structure de données)
2. Combat Basique (un ennemi, attaque basique)
3. Système Santé/Dégâts
4. Système de Montée de Niveau
5. Inventaire Simple
6. Effets d'Équipement
7. Capacités Multiples
8. Variété d'Ennemis
9. Loot/Récompenses
10. Système de Sauvegarde
```

## Conseils d'Implémentation Unity

### Pattern de Données ScriptableObject
```csharp
[CreateAssetMenu(menuName = "RPG/Stats de Personnage")]
public class CharacterStats : ScriptableObject
{
    public int baseHealth;
    public int baseAttack;
    public int baseDefense;
    public AnimationCurve levelCurve;
}

[CreateAssetMenu(menuName = "RPG/Objet")]
public class ItemData : ScriptableObject
{
    public string itemName;
    public Sprite icon;
    public ItemType type;
    public StatModifier[] modifiers;
}
```

### Architecture Recommandée
```
Managers/
├── GameManager (singleton)
├── CombatManager
├── InventoryManager
└── SaveManager

Data/
├── ScriptableObjects/
│   ├── Characters/
│   ├── Items/
│   ├── Abilities/
│   └── Enemies/

Runtime/
├── Character.cs
├── Inventory.cs
├── CombatState.cs
└── Stats.cs
```

### Erreurs Courantes
- Coder les stats en dur au lieu de data-driven
- Ne pas séparer données et logique
- Hiérarchies d'héritage complexes
- Ne pas planifier le système de sauvegarde tôt

## Jeux de Référence
- Final Fantasy (tour par tour classique)
- Diablo (action RPG, loot)
- Undertale (simple mais efficace)
- Stardew Valley (éléments RPG légers)

## Sections GDD à Accentuer
- Design du système de stats
- Flux de combat
- Courbe de progression
- Équilibre économique
- Structure narrative

## Points de Focus Playtest
- [ ] La progression de stats est-elle satisfaisante ?
- [ ] Le combat est-il engageant ?
- [ ] Les récompenses sont-elles significatives ?
- [ ] La courbe de difficulté est-elle appropriée ?
- [ ] Les choix semblent-ils impactants ?
