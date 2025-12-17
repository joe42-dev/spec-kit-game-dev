# SKGD Tutorial - Part 7: Troubleshooting

## Common Issues by Phase

### Setup Issues

#### "skgd command not found"
```bash
# Ensure pip installed to user
pip install --user skgd

# Add to PATH (Linux/Mac)
export PATH="$HOME/.local/bin:$PATH"

# Or use pipx
pipx install skgd
```

#### "Unity MCP not connected"
1. Check Unity Editor is running
2. Install Unity MCP package via Package Manager
3. Open Window > Unity MCP
4. Click "Start Server"
5. Restart Claude Code

#### "GDAI not responding"
1. Ensure Godot project is open
2. Enable GDAI plugin: Project > Project Settings > Plugins
3. Check GDAI server is running (terminal output)
4. Verify port isn't blocked

#### "Templates not copying"
```bash
# Force reinstall
pip uninstall skgd
pip install skgd

# Or copy manually
cp -r ~/.local/lib/python3.x/site-packages/skgd/templates/en/* .
```

### Concept Phase Issues

#### "/brainstorm stuck in loop"
- Claude asking same questions repeatedly
- **Solution:** Answer more specifically, or say "crystallize what we have"

#### "/pillars generating wrong type"
- Check `game-brief.md` has clear "Game Type" section
- Or specify type: "This is a roguelike platformer"

#### "/deep-dive feels shallow"
- Ask for more reference games
- Request specific sub-questions
- Say "go deeper on [aspect]"

#### "/validate-design always finds issues"
- Some tension is normal!
- Focus on CRITICAL only
- Accept documented trade-offs

### Planning Phase Issues

#### "Roadmap missing features"
- Edit `roadmap.yaml` manually
- Add features under appropriate cycle
- Run `/roadmap` again to verify

#### "Architecture too generic"
- Provide more context about your game
- Reference specific features from roadmap
- Ask for engine-specific patterns

### Production Phase Issues

#### "Spec requirements unclear"
- Run `/analyze` to identify ambiguity
- Re-run `/spec` with more detail
- Or edit spec.md directly

#### "Tasks too large"
- Break down in tasks.md manually
- Each task should be < 30 min
- Add sub-bullets under task

#### "Implementation errors accumulating"
```
STOP! Fix before continuing.

1. Read full error message
2. Check the script file
3. Fix the syntax/logic
4. Verify compilation
5. Only then continue
```

#### "Lost implementation progress"
```bash
# Find checkpoint commits
git log --oneline | grep checkpoint

# View specific checkpoint
git show [commit-hash]

# Restore if needed
git checkout [commit-hash] -- docs/specs/[feature]/tasks.md
```

#### "MCP disconnected mid-implement"
1. Progress is auto-checkpointed
2. Reconnect MCP (restart Unity/Godot)
3. Run `/implement` - will detect and resume

### Validation Phase Issues

#### "Tests pass but feels wrong"
- Game Feel assessment matters
- Document specific issues
- Use CONDITIONAL verdict
- Fix feel issues before PASS

#### "Learnings too long"
- Run `/crystallize`
- Extract patterns
- Archive one-offs

### Utility Issues

#### "/continue goes to wrong step"
- Check `.skgd/state.yaml`
- Verify `current_step` is correct
- Edit manually if corrupted

#### "/pivot seems too destructive"
- Always creates pre-pivot snapshot
- Can undo via git
- Consider smaller scope change

## Error Messages

### "Feature not in roadmap"
```
/spec unknown-feature

Error: Feature "unknown-feature" not found in roadmap.

Available features:
  - player-movement (pending)
  - basic-combat (pending)

Run /roadmap to see full list.
```
**Solution:** Add feature to roadmap first, or use correct name.

### "Prerequisites not met"
```
/plan basic-combat

Error: spec.md not found for basic-combat.

Run: /spec basic-combat
```
**Solution:** Run commands in order.

### "Constitution violation"
```
/analyze combat-system

CRITICAL: FR-5 violates constitution principle "Simple controls"
- Requirement: "12-button combo system"
- Principle: "Maximum 4 inputs for any action"
```
**Solution:** Revise requirement or update constitution via `/pivot`.

### "MCP timeout"
```
Error: Unity MCP request timed out after 30s

Possible causes:
1. Unity is processing (domain reload)
2. Large operation in progress
3. MCP server crashed
```
**Solution:**
1. Wait for Unity to finish
2. Check MCP server status
3. Restart MCP bridge

## Recovery Procedures

### Corrupted state.yaml

```bash
# View current state
cat .skgd/state.yaml

# Reset to known good state
cp .skgd/snapshots/v0.3/state.yaml .skgd/state.yaml

# Or reset to initial
cat > .skgd/state.yaml << 'EOF'
phase: production
production:
  current_spec: null
  current_step: null
implementation:
  active: false
EOF
```

### Lost learnings
```bash
# Check archive
ls .skgd/memory/learnings-archive/

# Restore from archive
cat .skgd/memory/learnings-archive/2024-01-15.md >> .skgd/memory/learnings.md
```

### Broken roadmap
```bash
# Regenerate
rm .skgd/roadmap.yaml
# Then run /roadmap
```

### Mixed up specs
```bash
# View all specs
find docs/specs -name "*.md" -exec echo "=== {} ===" \; -exec head -5 {} \;

# Check completion status
grep -r "status:" docs/specs/
```

## Performance Tips

### Context Management
- SKGD is designed for ~5k tokens loaded
- Don't load all docs at once
- Trust the Scout pattern

### Long Sessions
- Take breaks every 90 min
- Checkpoint before breaks
- `/continue` handles resume

### Large Projects
- Keep specs focused (one feature each)
- Archive completed features
- Use milestones for organization

## Getting Help

### Debug Information
```
/project-status
```
Provides current state for debugging.

### Check Versions
```bash
skgd --version
claude --version
```

### Community
- GitHub Issues: [Report bugs]
- Discussions: [Ask questions]

## Appendix

Continue to **[Appendix: Data Flow](appendix-data-flow.md)** for complete reference.
