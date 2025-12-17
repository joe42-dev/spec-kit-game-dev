# Crystallized Learnings

*Last crystallized: [date]*
*Source sessions: [count]*
*Engine: [unity|godot]*

## Technical Patterns (Validated)

### Unity Architecture (C#)
| Pattern | Evidence | Confidence |
|---------|----------|------------|
| Components over inheritance | Standard | HIGH |
| SerializeField for inspector | Standard | HIGH |
| Cache refs in Awake() | Performance | HIGH |
| ScriptableObjects for data | Flexibility | HIGH |

### Godot Architecture (GDScript)
| Pattern | Evidence | Confidence |
|---------|----------|------------|
| Composition via nodes | Standard | HIGH |
| Signal Bus (Events autoload) | Decoupling | HIGH |
| Typed GDScript (`var x: int`) | Safety | HIGH |
| @export for inspector vars | Standard | HIGH |
| @onready for node refs | Performance | HIGH |

### Performance
- Unity: Avoid Find* in Update(), use object pooling
- Godot: Cache node refs, use call_deferred() for physics

### Code Standards

**Unity (C#):**
- PascalCase for classes, methods
- _camelCase for private fields
- One script = one responsibility

**Godot (GDScript):**
- snake_case for files, variables, functions
- PascalCase for class_name
- Signals for inter-node communication

## Design Patterns (Validated)

### Mechanics
| Mechanic | Sweet Spot | Evidence |
|----------|------------|----------|
| [e.g., Jump buffer] | 0.1s | 3 playtests |

### Feel
- [What makes the game feel good]

## Anti-Patterns (Confirmed)

| Don't Do | Why | Learned From |
|----------|-----|--------------|
| [Anti-pattern] | [Consequence] | [Feature/session] |

## Key Decisions & Rationale

| Decision | Choice | Why | Date |
|----------|--------|-----|------|
| [Decision] | [What we chose] | [Rationale] | [When] |

## Process Insights

### What Speeds Us Up
- [Practice]

### What Slows Us Down
- [Practice to avoid]

---
*Confidence levels: HIGH (3+ validations), MED (2 validations)*
*Review at next milestone or /crystallize*
