# Template Jeu de Stratégie

> Guide spécifique pour le développement de jeux de stratégie

## Caractéristiques du Genre
- Focus sur la prise de décision
- Gestion de ressources
- Contrôle d'unités/actifs
- Planification et exécution
- Souvent compétitif (vs IA ou joueurs)

## Sous-genres
| Type | Timing | Exemple |
|------|--------|---------|
| Tour par tour | Tours séquentiels | Civilization, XCOM |
| Temps réel (RTS) | Continu | StarCraft, Age of Empires |
| 4X | Explorer, Étendre, Exploiter, Exterminer | Stellaris, Endless Legend |
| Tower Defense | Par vagues | BTD, Kingdom Rush |
| Auto-battler | Préparation + combat auto | Teamfight Tactics |

## Priorité des Systèmes Principaux

### 1. Contrôle d'Unités (Critique)
**Tour par tour :**
- Sélection
- Portée de mouvement
- Points d'action
- Ordre des tours

**Temps réel :**
- Sélection (clic, boîte)
- Commandes (mouvement, attaque, arrêt)
- Formation
- Pathfinding

### 2. Système de Ressources
- Sources de revenus
- Types de ressources
- Dépenses (unités, bâtiments, améliorations)
- Équilibre économique

### 3. Résolution de Combat
**Tour par tour :**
- Calcul de touche
- Formule de dégâts
- Modificateurs couverture/terrain
- Capacités spéciales

**Temps réel :**
- Calculs DPS
- Portée/ciblage
- Compteurs d'unités
- Potentiel de micro

### 4. IA Adversaire
- Prise de décision
- Scaling de difficulté
- Triche vs jouer fair
- Comportement lisible

## Ordre de Roadmap Recommandé

```
1. Système de Carte/Grille
2. Placement d'Unités
3. Sélection d'Unités
4. Système de Mouvement
5. Combat Basique
6. Condition Victoire/Défaite
7. Ressources
8. Production d'Unités
9. IA Adversaire (basique)
10. Passe d'Équilibrage
```

## Conseils d'Implémentation Unity

### Système de Grille
```csharp
public class GridManager : MonoBehaviour
{
    [SerializeField] private int width = 10;
    [SerializeField] private int height = 10;
    [SerializeField] private float cellSize = 1f;

    private Cell[,] grid;

    public Cell GetCell(Vector3 worldPosition)
    {
        int x = Mathf.FloorToInt(worldPosition.x / cellSize);
        int y = Mathf.FloorToInt(worldPosition.z / cellSize);
        return grid[x, y];
    }

    public Vector3 GetWorldPosition(int x, int y)
    {
        return new Vector3(x * cellSize + cellSize/2, 0, y * cellSize + cellSize/2);
    }
}
```

### Sélection d'Unités (RTS)
```csharp
public class SelectionManager : MonoBehaviour
{
    private List<Unit> selectedUnits = new();
    private Vector3 dragStart;
    private bool isDragging;

    private void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            dragStart = Input.mousePosition;
            isDragging = true;
        }

        if (Input.GetMouseButtonUp(0))
        {
            if (isDragging)
            {
                SelectUnitsInBox(dragStart, Input.mousePosition);
            }
            isDragging = false;
        }
    }
}
```

### Gestionnaire de Tours
```csharp
public class TurnManager : MonoBehaviour
{
    public enum Phase { PlayerTurn, EnemyTurn }

    public Phase currentPhase;
    public int turnNumber = 1;

    public event Action<Phase> OnPhaseChanged;

    public void EndTurn()
    {
        currentPhase = currentPhase == Phase.PlayerTurn
            ? Phase.EnemyTurn
            : Phase.PlayerTurn;

        if (currentPhase == Phase.PlayerTurn)
            turnNumber++;

        OnPhaseChanged?.Invoke(currentPhase);
    }
}
```

### Erreurs Courantes
- Performance du pathfinding
- Problèmes d'empilement d'unités
- IA trop facile ou injuste
- Surcharge d'information
- Rythme lent
- Effets boule de neige

## Jeux de Référence
- Into the Breach (tour par tour, élégant)
- StarCraft (RTS, compétitif)
- XCOM (tour par tour, tactique)
- Civilization (4X, profondeur)
- Slay the Spire (stratégie + roguelike)

## Sections GDD à Accentuer
- Roster d'unités et stats
- Économie de ressources
- Arbre technologique (si applicable)
- Conditions de victoire
- Règles de comportement IA

## Points de Focus Playtest
- [ ] Les décisions sont-elles significatives ?
- [ ] L'information est-elle lisible ?
- [ ] L'IA est-elle challengeante mais équitable ?
- [ ] Le rythme est-il approprié ?
- [ ] Y a-t-il des stratégies viables ?
- [ ] L'effet boule de neige est-il contrôlé ?
