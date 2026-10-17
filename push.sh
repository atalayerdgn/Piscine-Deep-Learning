#!/usr/bin/env bash
#
# push_to_github.sh — commit everything in a local repo and push it to
# git@github.com:atalayerdgn/Piscine-Deep-Learning.git over SSH.
#
# Usage:
#   ./push_to_github.sh [REPO_DIR] [COMMIT_MESSAGE]
#
#   REPO_DIR       Path to your local codebase (default: current directory)
#   COMMIT_MESSAGE Commit message (default: auto-generated with timestamp)
#
# Examples:
#   ./push_to_github.sh ~/code/Piscine-Deep-Learning "Week 2 exercises"
#   ./push_to_github.sh                        # push current directory
#
# Optional env vars:
#   REMOTE_URL   Override the SSH remote (default: the Piscine-Deep-Learning repo)
#   BRANCH       Branch to push (default: current branch, or main if unborn)
#   FORCE_PUSH=1 Push with --force (overwrite remote history — careful!)

set -euo pipefail

REMOTE_URL="${REMOTE_URL:-git@github.com:atalayerdgn/Piscine-Deep-Learning.git}"
REPO_DIR="${1:-.}"
COMMIT_MSG="${2:-Update codebase - $(date '+%Y-%m-%d %H:%M:%S')}"
FORCE_PUSH="${FORCE_PUSH:-0}"

# --- Pre-flight checks -------------------------------------------------------

if ! command -v git >/dev/null 2>&1; then
    echo "ERROR: git is not installed or not in PATH." >&2
    exit 1
fi

if [ ! -d "$REPO_DIR" ]; then
    echo "ERROR: directory '$REPO_DIR' does not exist." >&2
    exit 1
fi

cd "$REPO_DIR"
echo "==> Working in: $(pwd)"

# --- Init repo if needed ------------------------------------------------------

if [ ! -d .git ]; then
    echo "==> No git repo found — running 'git init'..."
    git init
    git branch -M main
fi

# --- Configure remote ---------------------------------------------------------

if git remote get-url origin >/dev/null 2>&1; then
    current_url="$(git remote get-url origin)"
    if [ "$current_url" != "$REMOTE_URL" ]; then
        echo "==> Remote 'origin' points to '$current_url' — updating to '$REMOTE_URL'"
        git remote set-url origin "$REMOTE_URL"
    else
        echo "==> Remote 'origin' already correct."
    fi
else
    echo "==> Adding remote 'origin' -> $REMOTE_URL"
    git remote add origin "$REMOTE_URL"
fi

# --- Stage and commit ---------------------------------------------------------

git add -A

if git diff --cached --quiet; then
    echo "==> Nothing to commit — working tree clean."
else
    echo "==> Committing changes..."
    git commit -m "$COMMIT_MSG"
fi

# Bail out if there is still no commit (e.g. empty directory) — nothing to push
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
    echo "ERROR: no commits in this repo — there is nothing to push." >&2
    echo "       '$REPO_DIR' appears to be empty. Put your files in it and re-run." >&2
    exit 1
fi

# --- Determine branch ----------------------------------------------------------

BRANCH="${BRANCH:-$(git branch --show-current)}"
if [ -z "$BRANCH" ]; then
    BRANCH="main"
    git branch -M main
fi
echo "==> Branch: $BRANCH"

# --- Push ----------------------------------------------------------------------

PUSH_ARGS=(-u origin "$BRANCH")
if [ "$FORCE_PUSH" = "1" ]; then
    echo "==> FORCE_PUSH enabled — remote history may be overwritten!"
    PUSH_ARGS+=(--force)
fi

echo "==> Pushing to origin/$BRANCH ..."
git push "${PUSH_ARGS[@]}"

echo "==> Done. Repo: $REMOTE_URL (branch: $BRANCH)"
