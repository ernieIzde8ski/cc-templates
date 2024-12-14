#!/bin/sh

set -eu

echo "Removing empty files"
fd --size -0b -X rm

# `git rev-parse` checks if the current directory is a git repository
if ! git rev-parse 1>/dev/null 2>/dev/null; then
    git init
    command -v pre-commit || pipx install pre-commit
    pre-commit autoupdate
    pre-commit install
else
    rm .pre-commit-config.yaml
fi

echo "All done! Add a crate to get started."
