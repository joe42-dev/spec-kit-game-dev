#!/usr/bin/env bash
# SKGD - Common functions for workflow scripts

# Get repository root
get_repo_root() {
    if git rev-parse --show-toplevel >/dev/null 2>&1; then
        git rev-parse --show-toplevel
    else
        # Fall back to script location
        local script_dir="$(CDPATH="" cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
        (cd "$script_dir/../.." && pwd)
    fi
}

# Get current feature from state.yaml
get_current_feature() {
    local repo_root=$(get_repo_root)
    local state_file="$repo_root/.skgd/state.yaml"

    # Check for SKGD_FEATURE environment variable first
    if [[ -n "${SKGD_FEATURE:-}" ]]; then
        echo "$SKGD_FEATURE"
        return
    fi

    # Parse current_spec from state.yaml
    if [[ -f "$state_file" ]]; then
        local current_spec=$(grep 'current_spec:' "$state_file" | sed 's/.*current_spec:\s*//' | tr -d ' "')
        if [[ -n "$current_spec" && "$current_spec" != "null" ]]; then
            echo "$current_spec"
            return
        fi
    fi

    # Fallback: find latest feature directory by modification time
    local specs_dir="$repo_root/docs/specs"
    if [[ -d "$specs_dir" ]]; then
        local latest=$(ls -t "$specs_dir" 2>/dev/null | head -n1)
        if [[ -n "$latest" ]]; then
            echo "$latest"
            return
        fi
    fi

    echo ""
}

# Check if git is available
has_git() {
    git rev-parse --show-toplevel >/dev/null 2>&1
}

# Get feature directory path
get_feature_dir() {
    local repo_root="$1"
    local feature="$2"
    echo "$repo_root/docs/specs/$feature"
}

# Get all feature paths
get_feature_paths() {
    local repo_root=$(get_repo_root)
    local feature=$(get_current_feature)
    local feature_dir=$(get_feature_dir "$repo_root" "$feature")
    local has_git_repo="false"

    if has_git; then
        has_git_repo="true"
    fi

    cat <<EOF
REPO_ROOT='$repo_root'
FEATURE='$feature'
HAS_GIT='$has_git_repo'
FEATURE_DIR='$feature_dir'
SPEC_FILE='$feature_dir/spec.md'
PLAN_FILE='$feature_dir/plan.md'
TASKS_FILE='$feature_dir/tasks.md'
EOF
}

# Helper: check if file exists
check_file() {
    [[ -f "$1" ]] && echo "  + $2" || echo "  - $2"
}

# Helper: check if directory exists and has content
check_dir() {
    [[ -d "$1" && -n $(ls -A "$1" 2>/dev/null) ]] && echo "  + $2" || echo "  - $2"
}

# Check feature name is valid
validate_feature_name() {
    local feature="$1"

    if [[ -z "$feature" ]]; then
        echo "ERROR: No feature name provided or found in state." >&2
        echo "Run /spec first or provide a feature name." >&2
        return 1
    fi

    return 0
}
