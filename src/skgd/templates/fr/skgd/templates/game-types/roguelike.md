# Template Jeu Roguelike

> Guide spécifique pour le développement de roguelikes/roguelites

## Caractéristiques du Genre
- Génération procédurale
- Permadeath (ou permadeath souple)
- Structure basée sur les runs
- Haute rejouabilité
- Souvent inclut de la méta-progression

## Roguelike vs Roguelite
| Fonctionnalité | Roguelike | Roguelite |
|----------------|-----------|-----------|
| Mort | Reset complet | Persistance partielle |
| Progression | Dans le run uniquement | Méta-progression |
| Exemple | Nethack, DCSS | Hades, Dead Cells |

## Priorité des Systèmes Principaux

### 1. Génération Procédurale (Critique)
**Approches :**
| Méthode | Complexité | Contrôle |
|---------|------------|----------|
| Placement aléatoire | Faible | Faible |
| Salles templateés | Moyenne | Élevé |
| Wave Function Collapse | Élevée | Moyenne |
| Donjons BSP | Moyenne | Moyenne |

**Décisions Clés :**
- Qu'est-ce qui est généré ? (niveaux, ennemis, objets)
- Basé sur une seed ou purement aléatoire ?
- Combien de contenu fait main ?

### 2. Système de Permadeath
- État de mort clair
- Résumé du run
- Redémarrage immédiat
- Hooks de méta-progression

### 3. Système d'Objets/Power-ups
- Drops d'objets aléatoires
- Synergies entre objets
- Variété de builds
- Choix risque/récompense

### 4. Méta-Progression (Roguelite)
- Monnaie persistante
- Déblocages permanents
- Options de départ
- Hooks narratifs

## Ordre de Roadmap Recommandé

```
1. Boucle de Gameplay Principale (combat ou action)
2. Génération de Salle Simple
3. Système Santé/Mort
4. Objets/Power-ups Basiques
5. Transitions de Salles
6. Variété d'Ennemis
7. Rencontre de Boss
8. Structure de Run (étages)
9. Méta-Progression
10. Synergies d'Objets
```

## Conseils d'Implémentation Unity

### Génération de Salle Simple
```csharp
public class DungeonGenerator : MonoBehaviour
{
    [SerializeField] private GameObject[] roomPrefabs;
    [SerializeField] private int roomCount = 10;

    private List<Room> rooms = new List<Room>();

    public void Generate(int seed)
    {
        Random.InitState(seed);
        // Générer la disposition des salles
        // Connecter les salles
        // Placer les ennemis
        // Placer les objets
    }
}
```

### Pattern de Gestionnaire de Run
```csharp
public class RunManager : MonoBehaviour
{
    public static RunManager Instance;

    public int currentFloor;
    public int gold;
    public List<Item> collectedItems;
    public float runTime;

    public void StartNewRun()
    {
        currentFloor = 1;
        gold = 0;
        collectedItems.Clear();
        runTime = 0;
    }

    public void EndRun(bool victory)
    {
        // Sauvegarder la méta-progression
        // Afficher le résumé du run
        // Retourner au hub
    }
}
```

### Système d'Objets
```csharp
[CreateAssetMenu(menuName = "Roguelike/Objet")]
public class ItemData : ScriptableObject
{
    public string itemName;
    public Sprite icon;
    public Rarity rarity;
    public ItemEffect[] effects;
    public string[] synergizesWith;
}
```

### Erreurs Courantes
- Trop aléatoire (pas de contrôle)
- Builds ennuyeux (pas de synergies)
- Runs trop longs ou trop courts
- Morts injustes
- Méta-progression trop lente

## Jeux de Référence
- Hades (méta-progression, narratif)
- Slay the Spire (roguelite deckbuilding)
- Dead Cells (roguelite action)
- Spelunky (roguelike pur, génération de niveaux)
- Risk of Rain (empilement d'objets)

## Sections GDD à Accentuer
- Algorithme de génération
- Design du pool d'objets
- Système de synergies
- Courbe de méta-progression
- Structure du run

## Points de Focus Playtest
- [ ] Chaque run est-il assez différent ?
- [ ] Les choix d'objets sont-ils intéressants ?
- [ ] La mort est-elle frustrante ou motivante ?
- [ ] La méta-progression est-elle satisfaisante ?
- [ ] Les synergies sont-elles découvrables ?
- [ ] La durée du run est-elle appropriée ?

## Considérations d'Équilibrage
- Taux de drop par rareté
- Courbe de puissance pendant le run
- Rythme de méta-progression
- Scaling de difficulté des boss
- Puissance de départ vs débloquée
