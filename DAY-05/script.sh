#!/bin/bash

CURRENT_DIR=$(basename "$PWD")

echo "Creating virtual environment: $CURRENT_DIR"

python3.12 -m venv ".$CURRENT_DIR"

source ".$CURRENT_DIR/bin/activate"

echo "Virtual environment activated ✅"