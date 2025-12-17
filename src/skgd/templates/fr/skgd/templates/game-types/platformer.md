# Template Jeu de Plateforme

> Guide spécifique pour le développement de jeux de plateforme

## Caractéristiques du Genre
- Mouvement et saut précis
- Progression par niveaux
- Navigation d'obstacles
- Souvent inclut des collectibles
- Focus sur le timing et la conscience spatiale

## Priorité des Systèmes Principaux

### 1. Système de Mouvement (Critique)
**Objectifs de Sensation :**
- Réactif (< 50ms de latence perçue)
- Contrôle aérien ajustable
- Temps coyote (0.1-0.15s)
- Buffering de saut (0.1s)

**Paramètres Clés :**
| Paramètre | Plage Typique | Notes |
|-----------|---------------|-------|
| Vitesse de déplacement | 5-10 unités/s | Rapide mais contrôlable |
| Hauteur de saut | 2-4 unités | Affecte le level design |
| Échelle de gravité | 2-4 | Plus haut = sauts plus vifs |
| Contrôle aérien | 0.5-1.0 | Combien de contrôle en l'air |

### 2. Système de Collision
- Hitboxes précises (souvent plus petites que le sprite)
- Plateformes traversables vers le haut
- Plateformes mobiles
- Gestion des pentes (si applicable)

### 3. Système de Caméra
- Suivi fluide du joueur
- Anticipation (look-ahead)
- Zones mortes verticales
- Limites de niveau

### 4. Framework de Level Design
- Introduire les mécaniques une par une
- Espaces sûrs pour s'entraîner
- Complexité croissante
- Points de contrôle pour les niveaux longs

## Ordre de Roadmap Recommandé

```
1. Mouvement du Joueur (marche, saut)
2. Collision Basique (sol, murs)
3. Suivi Caméra
4. Niveau Simple (plateformes uniquement)
5. Dangers (piques, fosses)
6. Collectibles
7. Ennemis (basiques)
8. Mouvement Avancé (saut mural, dash)
9. Progression de Niveaux
10. Polish (particules, screenshake)
```

## Conseils d'Implémentation Unity

### Pattern de Contrôleur de Joueur
```csharp
public class PlayerController : MonoBehaviour
{
    [Header("Mouvement")]
    [SerializeField] private float moveSpeed = 7f;
    [SerializeField] private float jumpForce = 12f;

    [Header("Vérification Sol")]
    [SerializeField] private Transform groundCheck;
    [SerializeField] private LayerMask groundLayer;

    private Rigidbody2D rb;
    private bool isGrounded;
    private float coyoteTimeCounter;
    private float jumpBufferCounter;
}
```

### Composants Recommandés
- Rigidbody2D (Dynamic, Freeze Rotation Z)
- BoxCollider2D ou CapsuleCollider2D
- Script PlayerController personnalisé
- Objet enfant GroundCheck séparé

### Erreurs Courantes
- Utiliser transform.Translate au lieu de Rigidbody
- Ne pas utiliser FixedUpdate pour la physique
- Vérifier le sol dans Update au lieu de FixedUpdate
- Hitboxes trop grandes

## Jeux de Référence
- Celeste (contrôles précis, mécaniques indulgentes)
- Super Meat Boy (précision, vitesse)
- Hollow Knight (combat + plateforme)
- Mario (sensation, momentum)

## Sections GDD à Accentuer
- Objectifs de sensation de mouvement
- Paramètres de saut
- Structure des niveaux
- Progression de difficulté
- Objectif des collectibles

## Points de Focus Playtest
- [ ] Le saut est-il agréable ?
- [ ] Le temps coyote est-il perceptible mais équitable ?
- [ ] Le joueur peut-il atterrir précisément ?
- [ ] Les hitboxes sont-elles assez indulgentes ?
- [ ] Le contrôle aérien est-il intuitif ?
