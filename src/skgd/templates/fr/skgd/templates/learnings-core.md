# Apprentissages Cristallises

*Derniere cristallisation: [date]*
*Sessions sources: [compte]*
*Moteur: [unity|godot]*

## Patterns Techniques (Valides)

### Architecture Unity (C#)
| Pattern | Evidence | Confiance |
|---------|----------|-----------|
| Composition > heritage | Standard | HAUTE |
| SerializeField pour inspecteur | Standard | HAUTE |
| Cache refs dans Awake() | Performance | HAUTE |
| ScriptableObjects pour data | Flexibilite | HAUTE |

### Architecture Godot (GDScript)
| Pattern | Evidence | Confiance |
|---------|----------|-----------|
| Composition via nodes | Standard | HAUTE |
| Signal Bus (Events autoload) | Decouplage | HAUTE |
| GDScript type (`var x: int`) | Securite | HAUTE |
| @export pour vars inspecteur | Standard | HAUTE |
| @onready pour refs nodes | Performance | HAUTE |

### Performance
- Unity: Eviter Find* dans Update(), utiliser object pooling
- Godot: Cache refs nodes, utiliser call_deferred() pour physique

### Standards Code

**Unity (C#):**
- PascalCase pour classes, methodes
- _camelCase pour champs prives
- Un script = une responsabilite

**Godot (GDScript):**
- snake_case pour fichiers, variables, fonctions
- PascalCase pour class_name
- Signaux pour communication inter-nodes

## Patterns de Design (Valides)

### Mecaniques
| Mecanique | Point Ideal | Evidence |
|-----------|-------------|----------|
| [ex: Jump buffer] | 0.1s | 3 playtests |

### Feel
- [Ce qui rend le jeu agreable]

## Anti-Patterns (Confirmes)

| A Eviter | Pourquoi | Appris De |
|----------|----------|-----------|
| [Anti-pattern] | [Consequence] | [Feature/session] |

## Decisions Cles & Justifications

| Decision | Choix | Pourquoi | Date |
|----------|-------|----------|------|
| [Decision] | [Ce qu'on a choisi] | [Justification] | [Quand] |

## Insights de Processus

### Ce Qui Nous Accelere
- [Pratique]

### Ce Qui Nous Ralentit
- [Pratique a eviter]

---
*Niveaux de confiance: HAUTE (3+ validations), MOY (2 validations)*
*Revoir au prochain milestone ou /crystallize*
