#!/usr/bin/env bash
# Spec Kit Game Dev - Asset MCP Check Script (Linux/macOS)
# Run this script to verify asset MCPs (Blender, PixelLab) setup

set -e

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  🎨 SPEC KIT GAME DEV - ASSET MCP CHECK                      ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Track statuses
BLENDER_OK=false
BLENDER_MCP_OK=false
PIXELLAB_MCP_OK=false

# Function to check command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# ============================================
# 1. Check Blender Installation
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1. Blender (3D Modeling)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command_exists blender; then
    BLENDER_VERSION=$(blender --version 2>/dev/null | head -n1 || echo "unknown")
    echo -e "${GREEN}✓${NC} Blender installed: $BLENDER_VERSION"
    BLENDER_OK=true
else
    echo -e "${YELLOW}⚠${NC} Blender not found"
    echo "  Install: https://www.blender.org/download/"
    echo "  Note: Required for Blender MCP"
fi
echo ""

# ============================================
# 2. Check Blender MCP
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "2. Blender MCP Server"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command_exists claude; then
    MCP_LIST=$(claude mcp list 2>/dev/null || echo "")

    if echo "$MCP_LIST" | grep -qi "blender"; then
        echo -e "${GREEN}✓${NC} Blender MCP is registered"
        BLENDER_MCP_OK=true

        if [ "$BLENDER_OK" = false ]; then
            echo -e "${YELLOW}⚠${NC} Note: Blender needs to be installed for MCP to work"
        fi
    else
        echo -e "${YELLOW}○${NC} Blender MCP not registered"
        echo ""
        echo "  To install Blender MCP:"
        echo "  claude mcp add blender-mcp -- uvx blender-mcp"
        echo ""
        echo "  Requirements:"
        echo "  - Blender installed locally"
        echo "  - Python with uv package manager"
    fi
else
    echo -e "${YELLOW}⚠${NC} Cannot check MCP status (Claude CLI not found)"
fi
echo ""

# ============================================
# 3. Check PixelLab MCP
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "3. PixelLab MCP Server (Sprite Generation)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command_exists claude; then
    MCP_LIST=$(claude mcp list 2>/dev/null || echo "")

    if echo "$MCP_LIST" | grep -qi "pixellab"; then
        echo -e "${GREEN}✓${NC} PixelLab MCP is registered"
        PIXELLAB_MCP_OK=true
    else
        echo -e "${YELLOW}○${NC} PixelLab MCP not registered"
        echo ""
        echo "  To install PixelLab MCP:"
        echo "  claude mcp add pixellab -- npx pixellab-mcp"
        echo ""
        echo "  Requirements:"
        echo "  - Node.js and npm installed"
    fi
else
    echo -e "${YELLOW}⚠${NC} Cannot check MCP status (Claude CLI not found)"
fi
echo ""

# ============================================
# 4. Check uv (for Python MCPs)
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "4. Package Managers"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if command_exists uv; then
    UV_VERSION=$(uv --version)
    echo -e "${GREEN}✓${NC} uv installed: $UV_VERSION (for Blender MCP)"
else
    echo -e "${YELLOW}⚠${NC} uv not found (recommended for Blender MCP)"
    echo "  Install: curl -LsSf https://astral.sh/uv/install.sh | sh"
fi

if command_exists npm; then
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✓${NC} npm installed: $NPM_VERSION (for PixelLab MCP)"
else
    echo -e "${YELLOW}⚠${NC} npm not found (required for PixelLab MCP)"
fi
echo ""

# ============================================
# Summary
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "SUMMARY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo ""
echo "Asset MCPs Status:"
if [ "$BLENDER_MCP_OK" = true ]; then
    echo -e "  ${GREEN}✓${NC} Blender MCP - Ready for 3D assets"
else
    echo -e "  ${YELLOW}○${NC} Blender MCP - Not configured"
fi

if [ "$PIXELLAB_MCP_OK" = true ]; then
    echo -e "  ${GREEN}✓${NC} PixelLab MCP - Ready for sprite generation"
else
    echo -e "  ${YELLOW}○${NC} PixelLab MCP - Not configured"
fi

echo ""

if [ "$BLENDER_MCP_OK" = true ] || [ "$PIXELLAB_MCP_OK" = true ]; then
    echo -e "${GREEN}At least one asset MCP is configured.${NC}"
    echo "You can use /assets to generate assets."
else
    echo -e "${YELLOW}No asset MCPs configured.${NC}"
    echo ""
    echo "Asset MCPs are optional but recommended for:"
    echo "- Automated sprite/model generation"
    echo "- Consistent art style"
    echo "- Faster prototyping"
    echo ""
    echo "Run /assets setup to configure asset MCPs."
fi
echo ""
