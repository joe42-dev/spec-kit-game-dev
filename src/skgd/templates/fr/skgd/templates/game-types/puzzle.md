# Template Jeu de Puzzle

> Guide spécifique pour le développement de jeux de puzzle

## Caractéristiques du Genre
- Focus sur la résolution de problèmes
- Mécaniques basées sur des règles
- États victoire/défaite clairs
- Souvent basé sur les niveaux
- Moments "Eureka !"

## Priorité des Systèmes Principaux

### 1. Mécanique de Puzzle (Critique)
**Définir clairement :**
- Que peut manipuler le joueur ?
- Quelles sont les règles ?
- Quel est l'état de victoire ?
- Qu'est-ce qui fournit du feedback ?

**Types :**
| Type | Exemple | Mécanique Principale |
|------|---------|----------------------|
| Spatial | Tetris, Sokoban | Arrangement |
| Logique | Sudoku, Démineur | Déduction |
| Physique | Angry Birds | Simulation |
| Pattern | Bejeweled | Correspondance |
| Séquence | Portal | Ordre des opérations |

### 2. Système de Validation de Niveau
- Vérifier les conditions de victoire
- Détecter les états insolubles
- Fournir des indices (optionnel)
- Suivre les étapes de solution

### 3. Progression de Niveaux
- Niveaux tutoriels
- Courbe de difficulté
- Introduction des mécaniques
- Défis de maîtrise

### 4. Système Annuler/Recommencer
- Historique d'état
- Annuler le dernier coup
- Recommencer le puzzle entier
- Sauvegarder la progression

## Ordre de Roadmap Recommandé

```
1. Mécanique de Puzzle Principale (une règle)
2. Détection de Condition de Victoire
3. Input/Interaction Basique
4. Feedback Visuel
5. 3-5 Niveaux Faits à la Main
6. Système d'Annulation
7. Sélection de Niveau
8. Indices Tutoriels
9. Progression de Niveaux
10. Polish (animations, son)
```

## Conseils d'Implémentation Unity

### Pattern Basé sur l'État
```csharp
public class PuzzleState
{
    public int[,] grid;
    public int moveCount;
    public bool isSolved;

    public PuzzleState Clone()
    {
        // Copie profonde pour système d'annulation
    }
}

public class PuzzleManager : MonoBehaviour
{
    private Stack<PuzzleState> history;
    private PuzzleState currentState;

    public void MakeMove(Move move)
    {
        history.Push(currentState.Clone());
        ApplyMove(move);
        CheckWinCondition();
    }

    public void Undo()
    {
        if (history.Count > 0)
            currentState = history.Pop();
    }
}
```

### Puzzles Basés sur Grille
```csharp
public class GridPuzzle : MonoBehaviour
{
    [SerializeField] private int width = 5;
    [SerializeField] private int height = 5;
    [SerializeField] private GameObject cellPrefab;

    private Cell[,] cells;
}
```

### Erreurs Courantes
- Ne pas tester la résolvabilité
- Trop complexe trop vite
- Règles peu claires
- Pas d'annulation (frustrant)
- Niveaux pas assez playtestés

## Jeux de Référence
- Baba Is You (manipulation de règles)
- The Witness (environnemental)
- Portal (raisonnement spatial)
- Tetris (puzzle action classique)
- Candy Crush (match-3)

## Sections GDD à Accentuer
- Règles de la mécanique principale (être précis)
- Conditions victoire/défaite
- Flux tutoriel
- Principes de level design
- Courbe de difficulté

## Points de Focus Playtest
- [ ] Les règles sont-elles claires sans explication ?
- [ ] Le moment "eureka" est-il satisfaisant ?
- [ ] La courbe de difficulté est-elle appropriée ?
- [ ] Les joueurs bloqués peuvent-ils s'en sortir ?
- [ ] Les tutoriels sont-ils sautables mais utiles ?

## Conseils de Level Design
1. Introduire un concept à la fois
2. Laisser les joueurs échouer en sécurité d'abord
3. Construire la complexité progressivement
4. Inclure des niveaux "pause"
5. Récompenser la maîtrise avec des défis optionnels
