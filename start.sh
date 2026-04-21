#!/bin/bash

clear

echo Starting up OheyaBot

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$SCRIPT_DIR"

"./.venv/bin/python3" "$SCRIPT_DIR/main.py"

