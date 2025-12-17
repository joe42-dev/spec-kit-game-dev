# /plan [feature-name] - Generate Implementation Plan

You are Opus, creating a technical implementation plan.

**Argument:** `$ARGUMENTS` (feature name, defaults to current_spec from state)

## Model

**MANDATORY: opus** - Technical architecture requires deep analysis and decision-making.

## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for user-facing text.

## Philosophy

**DO NOT delegate to a sub-agent.** You create the plan directly, making architectural decisions with full context.

Use Task(Sonnet) ONLY for:
- Exploring existing Unity project structure
- Reading multiple codebase files
- Finding existing patterns to follow

## Step 1: Validate

Read `.skgd/state.yaml`:
- If no argument, use `production.current_spec`
- Verify spec exists at `docs/specs/[feature]/spec.md`

## Step 2: Load Context

**Always read:**
- `docs/specs/[feature]/spec.md` - The specification
- `.skgd/memory/constitution.md` - Constraints
- `.skgd/memory/learnings-core.md` - Validated patterns

**Use Task(Sonnet) for:**
- Exploring Unity project structure
- Finding existing similar implementations

## Step 3: Fetch Up-to-Date Documentation (Context7)

If the feature uses specific Unity APIs or packages, use Context7 MCP to get current documentation:

**When to use:**
- InputSystem, UI Toolkit, Addressables, or other Unity packages
- Third-party libraries (DOTween, UniTask, etc.)
- Complex C# patterns you want to validate

**How to use:**
1. `mcp__context7__resolve-library-id` with query like "Unity InputSystem"
2. `mcp__context7__get-library-docs` with the library ID + topic

**Example:**
```yaml
# Find library
mcp__context7__resolve-library-id:
  query: "Unity InputSystem"

# Get specific docs
mcp__context7__get-library-docs:
  libraryId: "[returned-id]"
  topic: "PlayerInput component setup"
```

Skip Context7 if using only basic Unity features (Transform, Rigidbody, etc.).

**Fallback if Context7 unavailable:**

If the library isn't in Context7 (niche plugins, proprietary assets):

1. **WebSearch** - Find official documentation online:
   ```yaml
   WebSearch:
     query: "[PluginName] Unity documentation API"
   ```

2. **Local package docs** - Check the package folder:
   ```
   Packages/com.example.plugin/
   ├── README.md
   ├── Documentation~/
   └── Samples~/
   ```

3. **Read source code** - Analyze the plugin's C# scripts directly:
   - Public API signatures
   - XML comments
   - Example usages

4. **Ask user** - Request documentation URL or existing usage examples

## Step 4: Architectural Decisions

Before writing, decide:
- **Patterns**: Which Unity patterns apply? (Component, ScriptableObject, Events, etc.)
- **Structure**: How do scripts organize? What references what?
- **Phases**: What order of implementation minimizes risk?
- **Integration**: How does this connect to existing systems?

If unclear, ASK the user about architectural preferences.

## Step 5: Create Plan

Create `docs/specs/[feature-name]/plan.md`:

```markdown
# [Feature Name] - Implementation Plan

## Technical Approach

### Strategy
[High-level approach in 2-3 sentences]

### Patterns Used
| Pattern | Why |
|---------|-----|
| [Pattern] | [Rationale] |

### Key Decisions
| Decision | Choice | Rationale |
|----------|--------|-----------|
| [Decision] | [Choice] | [Why] |

## Component Architecture

### Scripts to Create
```
Assets/Scripts/[Feature]/
├── [Script1].cs      # [Responsibility]
└── [Script2].cs      # [Responsibility]
```

### Dependencies
```
[Component1] → [Component2]
     ↓
[Component3]
```

## Implementation Phases

### Phase 1: Foundation
**Goal:** [What this achieves]

**Steps:**
1. Create [Script].cs
   - Responsibility: [what it does]
   - Key methods: [list]

2. Create [GameObject]
   - Components: [list]
   - Position: [where]

**Verification:** [How to know phase is done]

### Phase 2: Core Logic
**Goal:** [What this achieves]

**Steps:**
1. [Step]
2. [Step]

**Verification:** [How to verify]

### Phase 3: Integration
**Goal:** [Connect with existing systems]

**Steps:**
1. [Step]

**Verification:** [How to verify]

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | Low/Med/High | Low/Med/High | [How to handle] |

## Testing Strategy

### Automated
- EditMode: [What to test]
- PlayMode: [What to test]

### Manual
- [Manual verification step]

---
*Created: [timestamp]*
*Spec: docs/specs/[feature]/spec.md*
*Complexity: [Low/Medium/High]*
```

## Step 6: Update State

```yaml
production:
  current_step: tasks
```

## Step 7: Git Commit

```bash
git add docs/specs/[feature-name]/
git commit -m "docs: plan [feature-name]

Strategy: [brief]
Complexity: [level]
Phases: [count]"
```

## Step 8: Summary

```
Plan created: [feature-name]

Location: docs/specs/[feature-name]/plan.md

Summary:
- [N] Phases
- [N] Scripts
- Complexity: [level]
- Key pattern: [main pattern used]

Next:
  /tasks [feature] - Generate actionable task list
  /continue - Auto-route
```

## Remember

- **Patterns from learnings**: Use validated approaches
- **Phase verification**: Each phase must be testable
- **Risk first**: Tackle risky parts early
- **Simple first**: Start with minimum, add complexity
