# Template Jeu de Tir

> Guide spécifique pour le développement de jeux de tir (FPS/TPS/Top-down)

## Caractéristiques du Genre
- Armes à projectiles/hitscan
- IA ennemie
- Systèmes santé/dégâts
- Souvent rythmé rapidement
- Précision de visée

## Sous-genres
| Type | Caméra | Contrôles |
|------|--------|-----------|
| FPS | Première personne | ZQSD + Souris |
| TPS | Troisième personne | ZQSD + Souris |
| Top-down | Vue de dessus | ZQSD ou flèches + Visée souris |
| Twin-stick | Vue de dessus | Stick gauche mouvement, stick droit visée |

## Priorité des Systèmes Principaux

### 1. Mécanique de Tir (Critique)
**Paramètres Clés :**
| Paramètre | Description | Plage Typique |
|-----------|-------------|---------------|
| Cadence de tir | Tirs par seconde | 1-20 |
| Dégâts | Par projectile | 5-100 |
| Dispersion | Cône de précision | 0-15 degrés |
| Recul | Kick caméra/visée | 0-10 degrés |
| Temps de rechargement | Secondes | 1-3s |

**Projectile vs Hitscan :**
- Projectile : Balle physique, temps de trajet
- Hitscan : Raycast instantané, impact immédiat

### 2. Contrôleur de Joueur
- Mouvement (ZQSD ou sticks)
- Visée (souris ou stick droit)
- Contrôle caméra
- Déplacement latéral

### 3. IA Ennemie
- Détection (vue, son)
- Pathfinding
- Comportement de combat
- Gestion de la mort

### 4. Système d'Armes
- Types d'armes multiples
- Gestion des munitions
- Changement d'arme
- Améliorations (optionnel)

## Ordre de Roadmap Recommandé

```
1. Mouvement du Joueur
2. Contrôle Caméra
3. Tir Basique (raycast/projectile)
4. Mannequin Cible (pas d'IA)
5. Système Santé/Dégâts
6. Ennemi Basique (bouge, tire)
7. IA Ennemie (patrouille, poursuite, attaque)
8. Armes Multiples
9. Munitions/Rechargement
10. Niveau avec Couvertures
```

## Conseils d'Implémentation Unity

### Système de Tir (Raycast)
```csharp
public class Weapon : MonoBehaviour
{
    [SerializeField] private float damage = 10f;
    [SerializeField] private float range = 100f;
    [SerializeField] private float fireRate = 10f;
    [SerializeField] private LayerMask hitLayers;

    private float nextFireTime;

    public void TryShoot()
    {
        if (Time.time < nextFireTime) return;
        nextFireTime = Time.time + 1f / fireRate;

        Ray ray = Camera.main.ViewportPointToRay(new Vector3(0.5f, 0.5f, 0));
        if (Physics.Raycast(ray, out RaycastHit hit, range, hitLayers))
        {
            hit.collider.GetComponent<IDamageable>()?.TakeDamage(damage);
        }
    }
}
```

### Pattern de Projectile
```csharp
public class Projectile : MonoBehaviour
{
    [SerializeField] private float speed = 20f;
    [SerializeField] private float damage = 10f;
    [SerializeField] private float lifetime = 5f;

    private void Start()
    {
        Destroy(gameObject, lifetime);
    }

    private void Update()
    {
        transform.Translate(Vector3.forward * speed * Time.deltaTime);
    }

    private void OnTriggerEnter(Collider other)
    {
        other.GetComponent<IDamageable>()?.TakeDamage(damage);
        Destroy(gameObject);
    }
}
```

### Erreurs Courantes
- Ignorer le feeling (screenshake, flash de canon)
- Ennemis trop précis
- Pas de feedback de touche
- Variété d'armes ennuyeuse
- Mauvais level design (pas de couvertures)

## Jeux de Référence
- DOOM (sensation, vitesse)
- Halo (bac à sable combat)
- Hotline Miami (top-down, brutal)
- Enter the Gungeon (twin-stick)

## Sections GDD à Accentuer
- Stats et sensation des armes
- Types et comportements d'ennemis
- Level design (couvertures, flux)
- Équilibrage de difficulté
- Feedback audio/visuel

## Points de Focus Playtest
- [ ] Le tir est-il percutant ?
- [ ] La visée est-elle réactive ?
- [ ] Les ennemis sont-ils équitables mais challengeants ?
- [ ] Le feedback est-il clair (marqueurs de touche, etc) ?
- [ ] Le mouvement est-il agréable pendant le combat ?
