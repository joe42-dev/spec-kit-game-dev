# SPEC KIT GAME DEV - System Philosophy

## The Ultimate AI Game Dev Workflow

A context-engineered system for **long-term game development** with Claude.

---

## Core Philosophy: Cognitive Partnership

```
OLD PARADIGM (Task Execution)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
User → Command → Sub-agent executes script → Template output
       (passive)   (isolated)                (rigid)

NEW PARADIGM (Cognitive Partnership)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
User ↔ Opus dialogue ↔ Sonnet explores/researches
        (active)        (support)
             ↓
   Session memory preserved
             ↓
   Cognitive continuity over MONTHS
```

---

## The Five Pillars

### 1. DIALOGUE > DELEGATION

For creative and decision-making tasks, Opus dialogues directly with the user.

**Why:** Sub-agents lose conversational context. Direct dialogue preserves nuance, builds on previous exchanges, and enables emergence.

**When to delegate to Sonnet:**
- Exploring large codebases
- Reading multiple files
- Searching for patterns
- Executing well-defined tasks

### 2. CONTEXT = CONTINUITY

Preserve inter-session memory for projects spanning months.

**Living Memory System:**
```
Layer 1: constitution.md (~500 tokens)
         Immutable core vision
         NEVER modified except by /pivot

Layer 2: learnings-core.md (~1000 tokens)
         Crystallized, validated patterns
         Compressed periodically via /crystallize

Layer 3: session-context.md (~500 tokens)
         Last session only
         Decisions, insights, momentum

Layer 4: Active work (~3000 tokens)
         Current spec/plan/tasks
         Focus of the moment

Layer 5: Archive (not loaded)
         All completed specs
         Accessed via Sonnet sub-agent when needed
```

**Total loaded: ~5000 tokens**
**Available for conversation: ~75k tokens (Smart Zone)**

### 3. ESCALATION INTELLIGENTE

Start with the right model, escalate when blocked.

```
Task well-defined → Sonnet sub-agent
     ↓ blocked?
Complex problem → Opus takes over
     ↓ still blocked?
User dialogue → Collaborative decision
```

### 4. EMERGENCE > STRUCTURE

Let ideas emerge before structuring them.

**Brainstorm pattern:**
1. IGNITION - Curious questions, no agenda
2. EXPANSION - Wild ideas, tangents, references
3. COLLISION - Combine threads, name patterns
4. CRYSTALLIZATION - Structure only when ready

### 5. USER AGENCY

Always offer choices, never force actions.

```
Next logical step: /implement

Options:
  [A] Continue (recommended)
  [B] Review first
  [C] Something else?
```

---

## Command Architecture

### 11 Commands (Focused Set)

| Command | Purpose | Model |
|---------|---------|-------|
| `/init` | Setup project | opus |
| `/brainstorm` | Creative dialogue (creation/spark modes) | opus |
| `/roadmap` | Vision + priorities | opus |
| `/spec` | Feature specification | opus |
| `/plan` | Technical architecture | opus |
| `/implement` | Unity MCP execution | opus |
| `/playtest` | Validation + learning capture | opus |
| `/crystallize` | Compress learnings | opus |
| `/continue` | Flow-preserving router | opus |
| `/pivot` | Major direction change | opus |
| `/snapshot` | Version milestone | opus |
| `/project-status` | Dashboard | opus |

**All commands use Opus** - MCP operations and game dev decisions require maximum capability.

**Sonnet via Task tool** - Only for research/exploration sub-tasks.

---

## Workflow for Long Projects

### Session Pattern (Optimal)

```
SESSION START
1. /continue (loads session-context)
2. See where you left off
3. Choose next action

DURING SESSION
- Work on 1-2 features maximum
- Update learnings after each playtest
- Keep context under 80k tokens

SESSION END
- session-context.md auto-updated
- Git commit with progress
- Ready for next session
```

### Weekly Pattern

```
Week 1-2: /brainstorm → /roadmap (Vision established)
Week 3-N: Feature cycles (/spec → /plan → /implement → /playtest)
Every 5-10 features: /crystallize (Compress learnings)
Milestones: /snapshot (Version tagged)
Direction change: /pivot (Analyzed, archived, redirected)
```

### Monthly Pattern

```
Month 1: Core loop playable
Month 2: Core gameplay complete
Month 3: Polish + additional features
Month N: Continue iteration...
```

---

## Context Engineering Strategies

### Stay in the Smart Zone

```
GREEN ZONE:  < 80k tokens  → Opus at maximum
YELLOW:      80-120k       → Still good
ORANGE:      120-160k      → Quality degrading
RED:         > 160k        → Avoid
```

### Load Minimum Context

```markdown
ALWAYS LOAD:
- state.yaml
- config.yaml
- session-context.md (if exists)

LOAD ON DEMAND:
- game-brief.md (for creative tasks)
- learnings-core.md (for implementation)
- constitution.md (for validation)
- Current spec/plan (for active work)

NEVER LOAD (use sub-agent):
- All specs at once
- Full archive
- Multiple snapshots
```

### Delegate Exploration

```markdown
INSTEAD OF:
"Let me read all 15 spec files to understand the project..."

DO:
Task(Sonnet): "Search docs/specs/ for any features related to combat"
→ Sonnet returns focused summary
→ Opus works with relevant context only
```

---

## Quality Principles

### For Specifications
- Every requirement testable
- Parameters have rationale
- Edge cases covered
- Aligns with constitution

### For Implementation
- Compile after each script
- Check console constantly
- Save scene frequently
- Follow learnings-core patterns

### For Testing
- Test ALL acceptance criteria
- Be honest (FAIL > broken feature)
- Capture learnings every time
- Game feel matters

---

## Integration with Unity MCP

All Unity operations go through MCP tools directly:

```yaml
# Scripts
mcp__UnityMCP__create_script
mcp__UnityMCP__apply_text_edits

# GameObjects
mcp__UnityMCP__manage_gameobject

# Scenes
mcp__UnityMCP__manage_scene

# Testing
mcp__UnityMCP__run_tests
mcp__UnityMCP__manage_editor (play/stop)

# Monitoring
mcp__UnityMCP__read_console
```

**Why Opus for MCP:** Operations are complex, errors need interpretation, decisions are made in real-time.

---

## Anti-Patterns to Avoid

```
❌ Loading all docs at once
✓ Load minimum, delegate exploration

❌ Delegating creative work to sub-agents
✓ Direct Opus dialogue for brainstorm/design

❌ Accumulating raw learnings forever
✓ Crystallize periodically into patterns

❌ Skipping playtest learnings capture
✓ Every test teaches something

❌ Micro-managing with rigid templates
✓ Let emergence happen, structure later

❌ Forcing next action
✓ Offer choices, preserve user agency
```

---

## Summary

**Spec Kit Game Dev** is optimized for:

- **Solo developers** building games over months
- **AI-first workflow** with Claude + Unity MCP
- **Context efficiency** staying in the smart zone
- **Cognitive continuity** across sessions
- **Emergent creativity** with structured capture

The system treats Claude as a **cognitive partner**, not a task executor.

---

*Version: 2.0*
*Philosophy: Opus-First, Delegate-Smart*
*Target: Long-term game development with AI*
