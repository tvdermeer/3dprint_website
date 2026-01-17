#!/bin/bash
# script to run tests for both backend and frontend
# Usage: ./run_tests.sh [backend|frontend] [test_file] [--cov]

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$(dirname "$(dirname "$(dirname "$(dirname "$SCRIPT_DIR")")")")"

TARGET="backend"
ARGS=()
COV=false

for arg in "$@"; do
  case "$arg" in
    backend|frontend)
      TARGET="$arg"
      ;;
    --cov)
      COV=true
      ;;
    *)
      ARGS+=("$arg")
      ;;
  esac
done

if [ "$TARGET" == "backend" ]; then
  cd "$REPO_ROOT/backend" || exit 1

  CMD="uv run pytest"

  if [ "$COV" = true ]; then
    CMD="$CMD --cov --cov-report=term-missing"
  fi

  if [ ${#ARGS[@]} -gt 0 ]; then
    CMD="$CMD ${ARGS[*]}"
  fi

  echo "Running: $CMD"
  eval "$CMD"

elif [ "$TARGET" == "frontend" ]; then
  cd "$REPO_ROOT/frontend" || exit 1

  CMD="npx playwright test"

  if [ ${#ARGS[@]} -gt 0 ]; then
    CMD="$CMD ${ARGS[*]}"
  fi

  echo "Running: $CMD"
  eval "$CMD"
fi
