#!/bin/sh

set -e

echo "removing empty files"
fd --size -0b --exclude='requirements.txt' --exclude 'py.typed' -X rm

if command -v deactivate; then
    echo "A venv is already active. Not setting up new venv."
else
    echo "setting up venv"
    python3 -m venv .venv
    . .venv/bin/activate
fi

echo "installing dev requirements"
pip3 install -r requirements-dev.txt 1>/dev/null

# `git rev-parse` checks if the current directory is a git repository
if ! git rev-parse 1>/dev/null 2>/dev/null; then
    git init
    command -v pre-commit || pipx install pre-commit
    pre-commit autoupdate
    pre-commit install
else
    rm .pre-commit-config.yaml
fi
