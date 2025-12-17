# Spec Kit Game Dev - Asset MCP Check Script (Windows PowerShell)
# Run this script to verify asset MCPs (Blender, PixelLab) setup

$ErrorActionPreference = "Continue"

Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  🎨 SPEC KIT GAME DEV - ASSET MCP CHECK                      ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Track statuses
$BlenderOK = $false
$BlenderMcpOK = $false
$PixelLabMcpOK = $false

# Function to check if command exists
function Test-Command {
    param ($Command)
    $null -ne (Get-Command $Command -ErrorAction SilentlyContinue)
}

# ============================================
# 1. Check Blender Installation
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "1. Blender (3D Modeling)" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

if (Test-Command "blender") {
    try {
        $blenderVersion = blender --version 2>$null | Select-Object -First 1
        Write-Host "✓ Blender installed: $blenderVersion" -ForegroundColor Green
        $BlenderOK = $true
    } catch {
        Write-Host "✓ Blender installed" -ForegroundColor Green
        $BlenderOK = $true
    }
} else {
    # Check common Windows install paths
    $blenderPaths = @(
        "$env:ProgramFiles\Blender Foundation\Blender*\blender.exe",
        "$env:ProgramFiles(x86)\Blender Foundation\Blender*\blender.exe"
    )
    $found = $false
    foreach ($path in $blenderPaths) {
        if (Test-Path $path) {
            Write-Host "✓ Blender found at: $path" -ForegroundColor Green
            Write-Host "  Note: Add Blender to PATH for better integration" -ForegroundColor Yellow
            $BlenderOK = $true
            $found = $true
            break
        }
    }
    if (-not $found) {
        Write-Host "⚠ Blender not found" -ForegroundColor Yellow
        Write-Host "  Install: https://www.blender.org/download/" -ForegroundColor Yellow
        Write-Host "  Note: Required for Blender MCP" -ForegroundColor Yellow
    }
}
Write-Host ""

# ============================================
# 2. Check Blender MCP
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "2. Blender MCP Server" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

if (Test-Command "claude") {
    try {
        $mcpList = claude mcp list 2>&1

        if ($mcpList -match "blender") {
            Write-Host "✓ Blender MCP is registered" -ForegroundColor Green
            $BlenderMcpOK = $true

            if (-not $BlenderOK) {
                Write-Host "⚠ Note: Blender needs to be installed for MCP to work" -ForegroundColor Yellow
            }
        } else {
            Write-Host "○ Blender MCP not registered" -ForegroundColor Yellow
            Write-Host ""
            Write-Host "  To install Blender MCP:" -ForegroundColor Yellow
            Write-Host "  claude mcp add blender-mcp -- uvx blender-mcp" -ForegroundColor Cyan
            Write-Host ""
            Write-Host "  Requirements:" -ForegroundColor Yellow
            Write-Host "  - Blender installed locally" -ForegroundColor Yellow
            Write-Host "  - Python with uv package manager" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "⚠ Could not check MCP status" -ForegroundColor Yellow
    }
} else {
    Write-Host "⚠ Cannot check MCP status (Claude CLI not found)" -ForegroundColor Yellow
}
Write-Host ""

# ============================================
# 3. Check PixelLab MCP
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "3. PixelLab MCP Server (Sprite Generation)" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

if (Test-Command "claude") {
    try {
        $mcpList = claude mcp list 2>&1

        if ($mcpList -match "pixellab") {
            Write-Host "✓ PixelLab MCP is registered" -ForegroundColor Green
            $PixelLabMcpOK = $true
        } else {
            Write-Host "○ PixelLab MCP not registered" -ForegroundColor Yellow
            Write-Host ""
            Write-Host "  To install PixelLab MCP:" -ForegroundColor Yellow
            Write-Host "  claude mcp add pixellab -- npx pixellab-mcp" -ForegroundColor Cyan
            Write-Host ""
            Write-Host "  Requirements:" -ForegroundColor Yellow
            Write-Host "  - Node.js and npm installed" -ForegroundColor Yellow
        }
    } catch {
        Write-Host "⚠ Could not check MCP status" -ForegroundColor Yellow
    }
} else {
    Write-Host "⚠ Cannot check MCP status (Claude CLI not found)" -ForegroundColor Yellow
}
Write-Host ""

# ============================================
# 4. Check Package Managers
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "4. Package Managers" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

if (Test-Command "uv") {
    $uvVersion = uv --version
    Write-Host "✓ uv installed: $uvVersion (for Blender MCP)" -ForegroundColor Green
} else {
    Write-Host "⚠ uv not found (recommended for Blender MCP)" -ForegroundColor Yellow
    Write-Host "  Install: irm https://astral.sh/uv/install.ps1 | iex" -ForegroundColor Yellow
}

if (Test-Command "npm") {
    $npmVersion = npm --version
    Write-Host "✓ npm installed: $npmVersion (for PixelLab MCP)" -ForegroundColor Green
} else {
    Write-Host "⚠ npm not found (required for PixelLab MCP)" -ForegroundColor Yellow
}
Write-Host ""

# ============================================
# Summary
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "SUMMARY" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

Write-Host ""
Write-Host "Asset MCPs Status:" -ForegroundColor White
if ($BlenderMcpOK) {
    Write-Host "  ✓ Blender MCP - Ready for 3D assets" -ForegroundColor Green
} else {
    Write-Host "  ○ Blender MCP - Not configured" -ForegroundColor Yellow
}

if ($PixelLabMcpOK) {
    Write-Host "  ✓ PixelLab MCP - Ready for sprite generation" -ForegroundColor Green
} else {
    Write-Host "  ○ PixelLab MCP - Not configured" -ForegroundColor Yellow
}

Write-Host ""

if ($BlenderMcpOK -or $PixelLabMcpOK) {
    Write-Host "At least one asset MCP is configured." -ForegroundColor Green
    Write-Host "You can use /assets to generate assets." -ForegroundColor White
} else {
    Write-Host "No asset MCPs configured." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Asset MCPs are optional but recommended for:" -ForegroundColor White
    Write-Host "- Automated sprite/model generation" -ForegroundColor White
    Write-Host "- Consistent art style" -ForegroundColor White
    Write-Host "- Faster prototyping" -ForegroundColor White
    Write-Host ""
    Write-Host "Run /assets setup to configure asset MCPs." -ForegroundColor Cyan
}
Write-Host ""
