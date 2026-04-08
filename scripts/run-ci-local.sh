#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="$ROOT_DIR/.venv"

if [[ ! -x "$VENV_DIR/bin/python" ]]; then
  python3 -m venv "$VENV_DIR"
fi

"$VENV_DIR/bin/python" -m pip install --upgrade pip >/dev/null
"$VENV_DIR/bin/python" -m pip install black isort bandit flake8 coverage pyftpdlib semgrep >/dev/null
"$VENV_DIR/bin/python" -m pip install -e "$ROOT_DIR/sc4py" -e "$ROOT_DIR/sc4net" >/dev/null

pushd "$ROOT_DIR" >/dev/null

"$VENV_DIR/bin/black" . --check
"$VENV_DIR/bin/isort" . --profile black --check-only
"$VENV_DIR/bin/bandit" -r .
"$VENV_DIR/bin/flake8" sc4py --count --select=E9,F63,F7,F82 --show-source --statistics
"$VENV_DIR/bin/flake8" sc4py --count --max-complexity=10 --max-line-length=127 --statistics
"$VENV_DIR/bin/flake8" sc4net --count --select=E9,F63,F7,F82 --show-source --statistics
"$VENV_DIR/bin/flake8" sc4net --count --max-complexity=10 --max-line-length=127 --statistics
"$VENV_DIR/bin/semgrep" --config p/ci

if command -v shellcheck >/dev/null 2>&1; then
  while IFS= read -r -d '' file; do
    shellcheck "$file"
  done < <(find . -type f \( -name '*.sh' -o -name '*.bash' \) -print0)
fi

if command -v npx >/dev/null 2>&1; then
  npx --yes markdownlint-cli2 '**/*.md'
fi

pushd "$ROOT_DIR/sc4py" >/dev/null
"$VENV_DIR/bin/python" -m coverage run -m unittest tests/test_*
"$VENV_DIR/bin/python" -m coverage report -m
popd >/dev/null

pushd "$ROOT_DIR/sc4net" >/dev/null
"$VENV_DIR/bin/python" -m coverage run -m unittest tests/test_*
"$VENV_DIR/bin/python" -m coverage report -m
popd >/dev/null

popd >/dev/null
