#!/usr/bin/env bash

# Stop on any error
set -e

# Remove old venv if exists
rm -rf .venv

# Create a clean virtual environment
python3 -m venv .venv  # standard venv usage :contentReference[oaicite:0]{index=0}

# Activate the virtual environment
# Use "source" so the current shell is modified :contentReference[oaicite:1]{index=1}
source .venv/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install necessary packages
pip install moviepy PyYAML leonardo-ai-sdk requests python-dotenv

# Feedback
echo "✅ Virtual environment created and packages installed."

echo 'Use `source .venv/bin/activate` to start the environment.'
