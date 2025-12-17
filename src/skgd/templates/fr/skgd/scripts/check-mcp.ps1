# Spec Kit Game Dev - MCP Check & Install Script (Windows PowerShell)
# Run this script to verify MCP setup for Unity game development

$ErrorActionPreference = "Continue"

Write-Host ""
Write-Host "╔══════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  🎮 SPEC KIT GAME DEV - MCP SETUP CHECK                      ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Track overall status
$AllOK = $true

# Function to check if command exists
function Test-Command {
    param ($Command)
    $null -ne (Get-Command $Command -ErrorAction SilentlyContinue)
}

# ============================================
# 1. Check Claude Code CLI
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "1. Claude Code CLI" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

if (Test-Command "claude") {
    try {
        $claudeVersion = claude --version 2>$null
        Write-Host "✓ Claude Code CLI installed: $claudeVersion" -ForegroundColor Green
    } catch {
        Write-Host "✓ Claude Code CLI installed" -ForegroundColor Green
    }
} else {
    Write-Host "✗ Claude Code CLI not found" -ForegroundColor Red
    Write-Host "  Install: npm install -g @anthropic-ai/claude-code" -ForegroundColor Yellow
    $AllOK = $false
}
Write-Host ""

# ============================================
# 2. Check Node.js
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "2. Node.js Runtime" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

if (Test-Command "node") {
    $nodeVersion = node --version
    Write-Host "✓ Node.js installed: $nodeVersion" -ForegroundColor Green
} else {
    Write-Host "⚠ Node.js not found (optional but recommended)" -ForegroundColor Yellow
    Write-Host "  Install: https://nodejs.org/" -ForegroundColor Yellow
}

if (Test-Command "npm") {
    $npmVersion = npm --version
    Write-Host "✓ npm installed: $npmVersion" -ForegroundColor Green
} else {
    Write-Host "⚠ npm not found" -ForegroundColor Yellow
}
Write-Host ""

# ============================================
# 3. Check Python
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "3. Python Runtime (for Unity MCP)" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

$pythonFound = $false
if (Test-Command "python") {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python installed: $pythonVersion" -ForegroundColor Green
    $pythonFound = $true
} elseif (Test-Command "python3") {
    $pythonVersion = python3 --version 2>&1
    Write-Host "✓ Python3 installed: $pythonVersion" -ForegroundColor Green
    $pythonFound = $true
}

if (-not $pythonFound) {
    Write-Host "✗ Python not found (required for Unity MCP)" -ForegroundColor Red
    Write-Host "  Install: https://www.python.org/downloads/" -ForegroundColor Yellow
    $AllOK = $false
}

if (Test-Command "uv") {
    $uvVersion = uv --version
    Write-Host "✓ uv installed: $uvVersion" -ForegroundColor Green
} elseif (Test-Command "pip") {
    $pipVersion = pip --version 2>&1 | Select-Object -First 1
    Write-Host "✓ pip installed: $pipVersion" -ForegroundColor Green
} else {
    Write-Host "⚠ Neither uv nor pip found" -ForegroundColor Yellow
}
Write-Host ""

# ============================================
# 4. Check Unity MCP
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "4. Unity MCP Server" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

if (Test-Command "claude") {
    try {
        $mcpList = claude mcp list 2>&1

        if ($mcpList -match "unity") {
            Write-Host "✓ Unity MCP is registered" -ForegroundColor Green

            if ($mcpList -match "unity.*(running|connected)") {
                Write-Host "✓ Unity MCP appears to be running" -ForegroundColor Green
            } else {
                Write-Host "⚠ Unity MCP registered but status unknown" -ForegroundColor Yellow
                Write-Host "  Ensure Unity Editor is open with MCP bridge installed" -ForegroundColor Yellow
            }
        } else {
            Write-Host "✗ Unity MCP not registered" -ForegroundColor Red
            Write-Host ""
            Write-Host "  To install Unity MCP:" -ForegroundColor Yellow
            Write-Host "  1. Add the MCP server to Claude:" -ForegroundColor Yellow
            Write-Host '     claude mcp add unity-mcp -- uvx --from git+https://github.com/SirLorrence/unity-mcp unity-mcp' -ForegroundColor Cyan
            Write-Host ""
            Write-Host "  2. In Unity, install the MCP Bridge package:" -ForegroundColor Yellow
            Write-Host "     Window > Package Manager > + > Add from git URL" -ForegroundColor Cyan
            Write-Host "     https://github.com/SirLorrence/unity-mcp.git?path=com.slorrence.unitymcp" -ForegroundColor Cyan
            Write-Host ""
            Write-Host "  3. Enable the bridge in Unity:" -ForegroundColor Yellow
            Write-Host "     Window > Unity MCP > Enable" -ForegroundColor Cyan
            $AllOK = $false
        }
    } catch {
        Write-Host "⚠ Could not check MCP status" -ForegroundColor Yellow
    }
} else {
    Write-Host "⚠ Cannot check MCP status (Claude CLI not found)" -ForegroundColor Yellow
}
Write-Host ""

# ============================================
# 5. Check Unity Editor
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "5. Unity Editor" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

$unityProcess = Get-Process -Name "Unity" -ErrorAction SilentlyContinue
if ($unityProcess) {
    Write-Host "✓ Unity Editor is running" -ForegroundColor Green
} else {
    Write-Host "⚠ Unity Editor not detected" -ForegroundColor Yellow
    Write-Host "  Please open Unity Editor before using /implement" -ForegroundColor Yellow
}
Write-Host ""

# ============================================
# 6. Check Git
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "6. Git (for version control)" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

if (Test-Command "git") {
    $gitVersion = git --version
    Write-Host "✓ Git installed: $gitVersion" -ForegroundColor Green
} else {
    Write-Host "✗ Git not found (required for workflow)" -ForegroundColor Red
    Write-Host "  Install: https://git-scm.com/" -ForegroundColor Yellow
    $AllOK = $false
}
Write-Host ""

# ============================================
# Summary
# ============================================
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
Write-Host "SUMMARY" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray

if ($AllOK) {
    Write-Host "✓ All required components are installed!" -ForegroundColor Green
    Write-Host ""
    Write-Host "You're ready to use Spec Kit Game Dev." -ForegroundColor White
    Write-Host "Run /init to start your project." -ForegroundColor Cyan
} else {
    Write-Host "✗ Some required components are missing." -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install the missing components above before proceeding." -ForegroundColor Yellow
}
Write-Host ""
