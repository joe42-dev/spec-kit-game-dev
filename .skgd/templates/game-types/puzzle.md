# Puzzle Game Template

> Specific guidance for puzzle game development

## Genre Characteristics
- Problem-solving focused
- Rules-based mechanics
- Clear win/lose states
- Often level-based
- "Aha!" moments

## Core Systems Priority

### 1. Puzzle Mechanic (Critical)
**Define clearly:**
- What can player manipulate?
- What are the rules?
- What is the goal state?
- What provides feedback?

**Types:**
| Type | Example | Core Mechanic |
|------|---------|---------------|
| Spatial | Tetris, Sokoban | Arrangement |
| Logic | Sudoku, Minesweeper | Deduction |
| Physics | Angry Birds | Simulation |
| Pattern | Bejeweled | Matching |
| Sequence | Portal | Order of operations |

### 2. Level Validation System
- Check win conditions
- Detect unsolvable states
- Provide hints (optional)
- Track solution steps

### 3. Level Progression
- Tutorial levels
- Difficulty curve
- Mechanic introduction
- Mastery challenges

### 4. Undo/Reset System
- State history
- Undo last move
- Reset entire puzzle
- Save progress

## Recommended Roadmap Order

```
1. Core Puzzle Mechanic (one rule)
2. Win Condition Detection
3. Basic Input/Interaction
4. Visual Feedback
5. 3-5 Hand-crafted Levels
6. Undo System
7. Level Selection
8. Tutorial Hints
9. Level Progression
10. Polish (animations, sound)
```

## Unity Implementation Tips

### State-Based Pattern
```csharp
public class PuzzleState
{
    public int[,] grid;
    public int moveCount;
    public bool isSolved;

    public PuzzleState Clone()
    {
        // Deep copy for undo system
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

### Grid-Based Puzzles
```csharp
public class GridPuzzle : MonoBehaviour
{
    [SerializeField] private int width = 5;
    [SerializeField] private int height = 5;
    [SerializeField] private GameObject cellPrefab;

    private Cell[,] cells;
}
```

### Common Pitfalls
- Not testing solvability
- Too complex too fast
- Unclear rules
- No undo (frustrating)
- Levels not playtested enough

## Reference Games
- Baba Is You (rule manipulation)
- The Witness (environmental)
- Portal (spatial reasoning)
- Tetris (classic action puzzle)
- Candy Crush (match-3)

## GDD Sections to Emphasize
- Core mechanic rules (be precise)
- Win/lose conditions
- Tutorial flow
- Level design principles
- Difficulty curve

## Playtest Focus Areas
- [ ] Are rules clear without explanation?
- [ ] Is the "aha" moment satisfying?
- [ ] Is difficulty curve appropriate?
- [ ] Can stuck players recover?
- [ ] Are tutorials skippable but helpful?

## Level Design Tips
1. Introduce one concept at a time
2. Let players fail safely first
3. Build complexity gradually
4. Include "breather" levels
5. Reward mastery with optional challenges
