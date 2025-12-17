# Template Jeu Action-Aventure

> Guide spécifique pour le développement de jeux action-aventure

## Caractéristiques du Genre
- Exploration et découverte
- Rencontres de combat
- Éléments de narration/histoire
- Progression de capacités/objets
- Mélange d'action et d'éléments de puzzle

## Sous-genres
| Type | Focus | Exemple |
|------|-------|---------|
| Metroidvania | Exploration, portes à capacités | Hollow Knight, Metroid |
| Zelda-like | Donjons, objets, puzzles | Zelda, Tunic |
| Character Action | Profondeur combat, combos | Devil May Cry, Bayonetta |
| Soulslike | Combat difficile, exploration | Dark Souls, Elden Ring |
| Monde Ouvert | Liberté, découverte | Breath of the Wild |

## Priorité des Systèmes Principaux

### 1. Contrôleur de Joueur (Critique)
**Mouvement :**
- Marche/course
- Saut (si applicable)
- Esquive/roulade
- Escalade/nage (si applicable)

**Combat :**
- Attaque basique
- Esquive/blocage
- Capacités spéciales
- Verrouillage (3D)

### 2. Système d'Exploration
- Zones interconnectées
- Raccourcis/voyage rapide
- Secrets et collectibles
- Carte/navigation

### 3. Système de Progression
- Améliorations santé/endurance
- Nouvelles capacités
- Améliorations d'équipement
- Progression narrative

### 4. Rencontres Ennemies
- Variété d'ennemis
- Patterns d'attaque
- Attaques télégraphiées
- Rencontres de boss

## Ordre de Roadmap Recommandé

```
1. Mouvement du Joueur
2. Combat Basique (attaque, esquive)
3. Système de Santé
4. Ennemi Basique (un type)
5. Première Zone (petite, complète)
6. Système de Déblocage de Capacités
7. Transitions de Zones
8. Plus d'Ennemis
9. Premier Boss
10. Objets de Progression
```

## Conseils d'Implémentation Unity

### Machine à États du Joueur
```csharp
public class PlayerController : MonoBehaviour
{
    private enum State { Idle, Moving, Attacking, Dodging, Hit }
    private State currentState = State.Idle;

    [Header("Mouvement")]
    [SerializeField] private float moveSpeed = 5f;
    [SerializeField] private float dodgeSpeed = 10f;
    [SerializeField] private float dodgeDuration = 0.3f;

    [Header("Combat")]
    [SerializeField] private float attackDuration = 0.4f;
    [SerializeField] private float attackDamage = 10f;

    private void Update()
    {
        switch (currentState)
        {
            case State.Idle:
            case State.Moving:
                HandleMovement();
                HandleCombatInput();
                break;
            case State.Attacking:
                // Bloqué jusqu'à animation terminée
                break;
            case State.Dodging:
                // I-frames actives
                break;
        }
    }
}
```

### Gestion de Zone/Salle
```csharp
public class AreaManager : MonoBehaviour
{
    [SerializeField] private Transform[] spawnPoints;
    [SerializeField] private Enemy[] enemyPrefabs;

    private List<Enemy> activeEnemies = new();
    private bool isCleared;

    public event Action OnAreaCleared;

    public void OnPlayerEnter()
    {
        SpawnEnemies();
    }

    private void OnEnemyDeath(Enemy enemy)
    {
        activeEnemies.Remove(enemy);
        if (activeEnemies.Count == 0)
        {
            isCleared = true;
            OnAreaCleared?.Invoke();
        }
    }
}
```

### Système de Porte à Capacité
```csharp
public class AbilityGate : MonoBehaviour
{
    [SerializeField] private AbilityType requiredAbility;
    [SerializeField] private GameObject blockedVisual;
    [SerializeField] private GameObject unlockedVisual;

    private void Start()
    {
        bool hasAbility = PlayerAbilities.Instance.HasAbility(requiredAbility);
        blockedVisual.SetActive(!hasAbility);
        unlockedVisual.SetActive(hasAbility);
        GetComponent<Collider>().enabled = !hasAbility;
    }
}
```

### Erreurs Courantes
- Le mouvement ne se sent pas bien
- Le combat manque d'impact
- Exploration vide
- Progression peu claire
- Tedium du backtracking
- Frustration des points de sauvegarde

## Jeux de Référence
- Hollow Knight (metroidvania, sensation)
- Dark Souls (combat, exploration)
- Zelda: BotW (liberté, découverte)
- Hyper Light Drifter (sensation, style)
- Tunic (mystère, design)

## Sections GDD à Accentuer
- Sensation mouvement et combat
- Structure du monde (carte)
- Progression des capacités
- Design des ennemis
- Rencontres de boss

## Points de Focus Playtest
- [ ] Le mouvement est-il agréable ?
- [ ] Le combat est-il satisfaisant ?
- [ ] L'exploration est-elle gratifiante ?
- [ ] Les portes à capacités sont-elles claires ?
- [ ] Les boss sont-ils challengeants mais équitables ?
- [ ] Se perdre est-il amusant ou frustrant ?
