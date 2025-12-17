#!/bin/bash
# Spec Kit Game Dev - MCP Check & Install Script (Linux/macOS)
# Run this script to verify MCP setup for Unity game development

set -e

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  🎮 SPEC KIT GAME DEV - MCP SETUP CHECK                      ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track overall status
ALL_OK=true

# Function to check command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# ============================================
# 1. Check Claude Code CLI
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1. Claude Code CLI"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command_exists claude; then
    CLAUDE_VERSION=$(claude --version 2>/dev/null || echo "unknown")
    echo -e "${GREEN}✓${NC} Claude Code CLI installed: $CLAUDE_VERSION"
else
    echo -e "${RED}✗${NC} Claude Code CLI not found"
    echo "  Install: npm install -g @anthropic-ai/claude-code"
    ALL_OK=false
fi
echo ""

# ============================================
# 2. Check Node.js (required for some MCPs)
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "2. Node.js Runtime"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command_exists node; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✓${NC} Node.js installed: $NODE_VERSION"
else
    echo -e "${YELLOW}⚠${NC} Node.js not found (optional but recommended)"
    echo "  Install: https://nodejs.org/"
fi

if command_exists npm; then
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✓${NC} npm installed: $NPM_VERSION"
else
    echo -e "${YELLOW}⚠${NC} npm not found"
fi
echo ""

# ============================================
# 3. Check Python (required for Unity MCP)
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "3. Python Runtime (for Unity MCP)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command_exists python3; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓${NC} Python3 installed: $PYTHON_VERSION"
elif command_exists python; then
    PYTHON_VERSION=$(python --version)
    echo -e "${GREEN}✓${NC} Python installed: $PYTHON_VERSION"
else
    echo -e "${RED}✗${NC} Python not found (required for Unity MCP)"
    echo "  Install: https://www.python.org/downloads/"
    ALL_OK=false
fi

if command_exists uv; then
    UV_VERSION=$(uv --version)
    echo -e "${GREEN}✓${NC} uv installed: $UV_VERSION"
elif command_exists pip; then
    PIP_VERSION=$(pip --version 2>/dev/null | head -n1)
    echo -e "${GREEN}✓${NC} pip installed: $PIP_VERSION"
else
    echo -e "${YELLOW}⚠${NC} Neither uv nor pip found"
fi
echo ""

# ============================================
# 4. Check Unity MCP
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "4. Unity MCP Server"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if Unity MCP is registered
if command_exists claude; then
    MCP_LIST=$(claude mcp list 2>/dev/null || echo "")

    if echo "$MCP_LIST" | grep -qi "unity"; then
        echo -e "${GREEN}✓${NC} Unity MCP is registered"

        # Try to get status
        if echo "$MCP_LIST" | grep -qi "unity.*running\|unity.*connected"; then
            echo -e "${GREEN}✓${NC} Unity MCP appears to be running"
        else
            echo -e "${YELLOW}⚠${NC} Unity MCP registered but status unknown"
            echo "  Ensure Unity Editor is open with MCP bridge installed"
        fi
    else
        echo -e "${RED}✗${NC} Unity MCP not registered"
        echo ""
        echo "  To install Unity MCP:"
        echo "  1. Add the MCP server to Claude:"
        echo "     claude mcp add unity-mcp -- uvx --from git+https://github.com/SirLorrence/unity-mcp unity-mcp"
        echo ""
        echo "  2. In Unity, install the MCP Bridge package:"
        echo "     Window > Package Manager > + > Add from git URL"
        echo "     https://github.com/SirLorrence/unity-mcp.git?path=com.slorrence.unitymcp"
        echo ""
        echo "  3. Enable the bridge in Unity:"
        echo "     Window > Unity MCP > Enable"
        ALL_OK=false
    fi
else
    echo -e "${YELLOW}⚠${NC} Cannot check MCP status (Claude CLI not found)"
fi
echo ""

# ============================================
# 5. Check GDAI MCP (Godot)
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "5. GDAI MCP Server (Godot)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command_exists claude; then
    MCP_LIST=$(claude mcp list 2>/dev/null || echo "")

    if echo "$MCP_LIST" | grep -qi "gdai"; then
        echo -e "${GREEN}✓${NC} GDAI MCP is registered"
        echo "  Tools: create_script, add_node, play_scene, get_godot_errors, etc."
    else
        echo -e "${YELLOW}⚠${NC} GDAI MCP not registered (required for Godot projects)"
        echo ""
        echo "  To install GDAI MCP:"
        echo "  1. Get plugin from https://gdaimcp.com/"
        echo "  2. Copy to your Godot project's addons/ folder"
        echo "  3. Enable plugin in Project > Project Settings > Plugins"
        echo "  4. Add MCP to Claude (check GDAI docs for command)"
    fi
else
    echo -e "${YELLOW}⚠${NC} Cannot check MCP status (Claude CLI not found)"
fi
echo ""

# ============================================
# 6. Check Unity Editor
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "6. Unity Editor"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if pgrep -x "Unity" > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Unity Editor is running"
elif pgrep -f "Unity" > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Unity Editor appears to be running"
else
    echo -e "${YELLOW}⚠${NC} Unity Editor not detected"
    echo "  Please open Unity Editor before using /implement (Unity projects)"
fi
echo ""

# ============================================
# 7. Check Godot Editor
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "7. Godot Editor"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if pgrep -x "godot" > /dev/null 2>&1 || pgrep -x "Godot" > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Godot Editor is running"
elif pgrep -f "godot" > /dev/null 2>&1 || pgrep -f "Godot" > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Godot Editor appears to be running"
else
    echo -e "${YELLOW}⚠${NC} Godot Editor not detected"
    echo "  Please open Godot Editor before using /implement (Godot projects)"
fi
echo ""

# ============================================
# 8. Check Git
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "8. Git (for version control)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command_exists git; then
    GIT_VERSION=$(git --version)
    echo -e "${GREEN}✓${NC} Git installed: $GIT_VERSION"
else
    echo -e "${RED}✗${NC} Git not found (required for workflow)"
    echo "  Install: https://git-scm.com/"
    ALL_OK=false
fi
echo ""

# ============================================
# 9. Check Context7 MCP (for up-to-date library docs)
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "9. Context7 MCP (Library Documentation)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command_exists claude; then
    MCP_LIST=$(claude mcp list 2>/dev/null || echo "")

    if echo "$MCP_LIST" | grep -qi "context7"; then
        echo -e "${GREEN}✓${NC} Context7 MCP is registered"
        echo "  Tools: resolve-library-id, get-library-docs"
    else
        echo -e "${YELLOW}⚠${NC} Context7 MCP not registered (optional but recommended)"
        echo ""
        echo "  Context7 provides up-to-date library documentation for:"
        echo "  - Unity APIs (InputSystem, UI Toolkit, etc.)"
        echo "  - C# patterns and best practices"
        echo "  - Third-party packages"
        echo ""
        echo "  To install:"
        echo "  claude mcp add --transport http context7 https://mcp.context7.com/mcp"
    fi
else
    echo -e "${YELLOW}⚠${NC} Cannot check Context7 status (Claude CLI not found)"
fi
echo ""

# ============================================
# Summary
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "SUMMARY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ "$ALL_OK" = true ]; then
    echo -e "${GREEN}✓ All required components are installed!${NC}"
    echo ""
    echo "You're ready to use Spec Kit Game Dev."
    echo "Run /init to start your project."
else
    echo -e "${RED}✗ Some required components are missing.${NC}"
    echo ""
    echo "Please install the missing components above before proceeding."
fi
echo ""
