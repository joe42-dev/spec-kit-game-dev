# Internationalization (i18n)

## How It Works

1. Check `.skgd/config.yaml` → `user.language` (en/fr)
2. Load messages from `.skgd/i18n/messages.yaml`
3. Use appropriate language for all user-facing outputs

## For Commands

At the start of each command, after loading config:

```markdown
## Language

Read `.skgd/config.yaml` → `user.language`
Use `.skgd/i18n/messages.yaml` for all user-facing text.

Adapt your communication style:
- **en**: Direct, technical
- **fr**: Natural, conversational (tutoiement)
```

## Message Categories

- **Common**: Generic terms (next steps, completed, etc.)
- **Command-specific**: Messages for each command
- **Errors**: Error messages and recovery instructions

## Adding New Messages

1. Add to both `en:` and `fr:` sections in `messages.yaml`
2. Use the same key structure
3. Keep messages concise

## Examples

### English Output
```
Specification created: player-movement

Location: docs/specs/player-movement/spec.md

Summary:
- 5 Requirements
- 4 Acceptance criteria

Next steps:
  /plan player-movement - Generate implementation plan
```

### French Output (same command)
```
Specification creee: player-movement

Emplacement: docs/specs/player-movement/spec.md

Resume:
- 5 Exigences
- 4 Criteres d'acceptation

Prochaines etapes:
  /plan player-movement - Generer le plan d'implementation
```

## Notes

- ASCII characters only (no accents) for terminal compatibility
- Messages are guidance - Claude adapts naturally
- Technical terms (Unity, MCP, etc.) stay in English
