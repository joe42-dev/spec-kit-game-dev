#!/usr/bin/env bash
# SKGD - Prerequisite Checker
#
# Usage: ./check-prerequisites.sh [OPTIONS] [feature-name]
#
# OPTIONS:
#   --json              Output in JSON format
#   --require-spec      Require spec.md to exist
#   --require-plan      Require plan.md to exist
#   --require-tasks     Require tasks.md to exist
#   --paths-only        Only output paths (no validation)
#   --help, -h          Show help
#
# EXAMPLES:
#   ./check-prerequisites.sh --json
#   ./check-prerequisites.sh --require-plan player-movement
#   ./check-prerequisites.sh --json --require-tasks --require-plan

set -e

# Parse arguments
JSON_MODE=false
REQUIRE_SPEC=false
REQUIRE_PLAN=false
REQUIRE_TASKS=false
PATHS_ONLY=false
FEATURE_ARG=""

for arg in "$@"; do
    case "$arg" in
        --json)
            JSON_MODE=true
            ;;
        --require-spec)
            REQUIRE_SPEC=true
            ;;
        --require-plan)
            REQUIRE_PLAN=true
            ;;
        --require-tasks)
            REQUIRE_TASKS=true
            ;;
        --paths-only)
            PATHS_ONLY=true
            ;;
        --help|-h)
            cat << 'EOF'
SKGD Prerequisite Checker

Usage: check-prerequisites.sh [OPTIONS] [feature-name]

OPTIONS:
  --json              Output in JSON format
  --require-spec      Require spec.md to exist
  --require-plan      Require plan.md to exist
  --require-tasks     Require tasks.md to exist
  --paths-only        Only output path variables
  --help, -h          Show this help

EXAMPLES:
  # Check basic prerequisites
  ./check-prerequisites.sh --json

  # Check before /implement (need spec, plan, tasks)
  ./check-prerequisites.sh --json --require-spec --require-plan --require-tasks

  # Check specific feature
  ./check-prerequisites.sh --require-plan player-movement
EOF
            exit 0
            ;;
        -*)
            echo "ERROR: Unknown option '$arg'. Use --help for usage." >&2
            exit 1
            ;;
        *)
            FEATURE_ARG="$arg"
            ;;
    esac
done

# Source common functions
SCRIPT_DIR="$(CDPATH="" cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# Get paths
REPO_ROOT=$(get_repo_root)

# Determine feature name
if [[ -n "$FEATURE_ARG" ]]; then
    FEATURE="$FEATURE_ARG"
else
    FEATURE=$(get_current_feature)
fi

# Validate feature
if ! validate_feature_name "$FEATURE" 2>/dev/null; then
    if $JSON_MODE; then
        echo '{"error":"No feature found. Run /spec first or provide a feature name."}'
    else
        echo "ERROR: No feature found. Run /spec first or provide a feature name." >&2
    fi
    exit 1
fi

FEATURE_DIR="$REPO_ROOT/docs/specs/$FEATURE"
SPEC_FILE="$FEATURE_DIR/spec.md"
PLAN_FILE="$FEATURE_DIR/plan.md"
TASKS_FILE="$FEATURE_DIR/tasks.md"

# Paths only mode
if $PATHS_ONLY; then
    if $JSON_MODE; then
        printf '{"REPO_ROOT":"%s","FEATURE":"%s","FEATURE_DIR":"%s","SPEC_FILE":"%s","PLAN_FILE":"%s","TASKS_FILE":"%s"}\n' \
            "$REPO_ROOT" "$FEATURE" "$FEATURE_DIR" "$SPEC_FILE" "$PLAN_FILE" "$TASKS_FILE"
    else
        echo "REPO_ROOT: $REPO_ROOT"
        echo "FEATURE: $FEATURE"
        echo "FEATURE_DIR: $FEATURE_DIR"
        echo "SPEC_FILE: $SPEC_FILE"
        echo "PLAN_FILE: $PLAN_FILE"
        echo "TASKS_FILE: $TASKS_FILE"
    fi
    exit 0
fi

# Validation
ERRORS=()

# Check feature directory
if [[ ! -d "$FEATURE_DIR" ]]; then
    ERRORS+=("Feature directory not found: $FEATURE_DIR. Run /spec first.")
fi

# Check required files
if $REQUIRE_SPEC && [[ ! -f "$SPEC_FILE" ]]; then
    ERRORS+=("spec.md not found. Run /spec first.")
fi

if $REQUIRE_PLAN && [[ ! -f "$PLAN_FILE" ]]; then
    ERRORS+=("plan.md not found. Run /plan first.")
fi

if $REQUIRE_TASKS && [[ ! -f "$TASKS_FILE" ]]; then
    ERRORS+=("tasks.md not found. Run /plan first (tasks are generated with plan).")
fi

# Check for errors
if [[ ${#ERRORS[@]} -gt 0 ]]; then
    if $JSON_MODE; then
        # Build JSON error array
        json_errors=$(printf '"%s",' "${ERRORS[@]}")
        json_errors="[${json_errors%,}]"
        printf '{"success":false,"errors":%s}\n' "$json_errors"
    else
        echo "Prerequisites check FAILED:" >&2
        for err in "${ERRORS[@]}"; do
            echo "  - $err" >&2
        done
    fi
    exit 1
fi

# Build available docs list
AVAILABLE_DOCS=()
[[ -f "$SPEC_FILE" ]] && AVAILABLE_DOCS+=("spec.md")
[[ -f "$PLAN_FILE" ]] && AVAILABLE_DOCS+=("plan.md")
[[ -f "$TASKS_FILE" ]] && AVAILABLE_DOCS+=("tasks.md")

# Check for optional docs
HAS_SPEC=$([[ -f "$SPEC_FILE" ]] && echo "true" || echo "false")
HAS_PLAN=$([[ -f "$PLAN_FILE" ]] && echo "true" || echo "false")
HAS_TASKS=$([[ -f "$TASKS_FILE" ]] && echo "true" || echo "false")

# Output results
if $JSON_MODE; then
    # Build JSON docs array
    if [[ ${#AVAILABLE_DOCS[@]} -eq 0 ]]; then
        json_docs="[]"
    else
        json_docs=$(printf '"%s",' "${AVAILABLE_DOCS[@]}")
        json_docs="[${json_docs%,}]"
    fi

    printf '{"success":true,"FEATURE":"%s","FEATURE_DIR":"%s","HAS_SPEC":%s,"HAS_PLAN":%s,"HAS_TASKS":%s,"AVAILABLE_DOCS":%s}\n' \
        "$FEATURE" "$FEATURE_DIR" "$HAS_SPEC" "$HAS_PLAN" "$HAS_TASKS" "$json_docs"
else
    echo "Prerequisites OK"
    echo ""
    echo "Feature: $FEATURE"
    echo "Directory: $FEATURE_DIR"
    echo ""
    echo "Available documents:"
    check_file "$SPEC_FILE" "spec.md"
    check_file "$PLAN_FILE" "plan.md"
    check_file "$TASKS_FILE" "tasks.md"
fi
