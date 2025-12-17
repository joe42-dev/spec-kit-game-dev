# Template Jeu de Simulation

> Guide spécifique pour le développement de jeux de simulation

## Caractéristiques du Genre
- Gameplay piloté par les systèmes
- Agence du joueur dans des systèmes complexes
- Souvent open-ended
- Gestion de ressources
- Comportements émergents

## Sous-genres
| Type | Focus | Exemple |
|------|-------|---------|
| Life Sim | Vie quotidienne, relations | Stardew Valley, Animal Crossing |
| Gestion | Construction ville/entreprise | SimCity, Planet Coaster |
| Véhicule | Contrôle réaliste | Flight Sim, Euro Truck |
| God Game | Manipulation du monde | Black & White, Populous |
| Sandbox | Liberté de création | Minecraft, Terraria |

## Priorité des Systèmes Principaux

### 1. Boucle de Simulation Principale (Critique)
**Définir :**
- Qu'est-ce qui est simulé ?
- Quelles règles la gouvernent ?
- Que peut influencer le joueur ?
- Qu'est-ce qui émerge des systèmes ?

### 2. Système de Temps
- Cycle jour/nuit
- Saisons (si applicable)
- Mise à l'échelle du temps
- Événements programmés

### 3. Gestion de Ressources
- Types de ressources
- Production/consommation
- Limites de stockage
- Échange/conversion

### 4. Agents IA (si applicable)
- Comportements des PNJ
- Systèmes de besoins
- Relations
- Routines

## Ordre de Roadmap Recommandé

```
1. Boucle Système Principal (un système fonctionnel)
2. Progression du Temps
3. Ressources Basiques
4. Interaction Joueur
5. UI pour l'Information
6. Second Système (interactions)
7. Sauvegarde/Chargement
8. Objectifs/Buts
9. Événements Émergents
10. Expansion de Contenu
```

## Conseils d'Implémentation Unity

### Gestionnaire de Temps
```csharp
public class TimeManager : MonoBehaviour
{
    public static TimeManager Instance;

    [SerializeField] private float minutesPerRealSecond = 1f;

    public int day = 1;
    public int hour = 6;
    public int minute = 0;

    public event Action<int> OnHourChanged;
    public event Action<int> OnDayChanged;

    private void Update()
    {
        minute += Mathf.RoundToInt(minutesPerRealSecond * Time.deltaTime);

        if (minute >= 60)
        {
            minute = 0;
            hour++;
            OnHourChanged?.Invoke(hour);

            if (hour >= 24)
            {
                hour = 0;
                day++;
                OnDayChanged?.Invoke(day);
            }
        }
    }
}
```

### Système de Ressources
```csharp
public class ResourceManager : MonoBehaviour
{
    private Dictionary<ResourceType, float> resources = new();

    public event Action<ResourceType, float> OnResourceChanged;

    public void AddResource(ResourceType type, float amount)
    {
        if (!resources.ContainsKey(type))
            resources[type] = 0;

        resources[type] += amount;
        OnResourceChanged?.Invoke(type, resources[type]);
    }

    public bool TryConsume(ResourceType type, float amount)
    {
        if (!resources.ContainsKey(type) || resources[type] < amount)
            return false;

        resources[type] -= amount;
        OnResourceChanged?.Invoke(type, resources[type]);
        return true;
    }
}
```

### Système de Besoins d'Agent
```csharp
public class NeedsSystem : MonoBehaviour
{
    [System.Serializable]
    public class Need
    {
        public string name;
        [Range(0, 100)] public float value = 50f;
        public float decayRate = 1f; // par heure
    }

    public Need[] needs;

    private void OnEnable()
    {
        TimeManager.Instance.OnHourChanged += UpdateNeeds;
    }

    private void UpdateNeeds(int hour)
    {
        foreach (var need in needs)
        {
            need.value -= need.decayRate;
            need.value = Mathf.Clamp(need.value, 0, 100);
        }
    }
}
```

### Erreurs Courantes
- Systèmes trop opaques (joueur ne comprend pas)
- Pas assez de feedback
- Tedium du micromanagement
- Pas d'objectifs ou direction clairs
- Bugs du système de sauvegarde (état complexe)

## Jeux de Référence
- Stardew Valley (life sim, polish)
- Dwarf Fortress (émergence, complexité)
- Cities: Skylines (gestion, échelle)
- RimWorld (narration, IA)
- Factorio (systèmes, optimisation)

## Sections GDD à Accentuer
- Diagramme d'interactions des systèmes
- Design temps/rythme
- Flux de ressources
- Boucles de feedback joueur
- Conditions de victoire (si applicable)

## Points de Focus Playtest
- [ ] Les systèmes sont-ils compréhensibles ?
- [ ] Le feedback est-il clair et opportun ?
- [ ] Le rythme est-il engageant (pas ennuyeux) ?
- [ ] Des situations intéressantes émergent-elles ?
- [ ] L'information est-elle accessible ?
- [ ] La sauvegarde/chargement fonctionne-t-elle de manière fiable ?
