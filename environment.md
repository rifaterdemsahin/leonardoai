Here’s everything you need to set up a clean Python environment with a `.env` file, create a virtual environment via a bash script, and install the required dependencies for the Leonardo.ai video script.

---

## 🎯 Sample `.env` File

Create a `.env` in your project's root:

```dotenv
# .env

# Your Leonardo.ai API key (keep this secret!)
LEONARDO_API_KEY="sk-your_leonardo_token_here"

# Optional configuration
LEONARDO_MODEL_ID="e316348f-7773-490e-adcd-46757c738eb7"
VIDEO_FPS=24
CLIP_DURATION=30
```

Make sure to add `.env` to `.gitignore` to avoid accidentally committing secrets.

---

## 🧱 Bash Setup Script: `setup_env.sh`

This script creates/activates the virtual environment and installs the dependencies:

```bash
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
```

Make it executable:

```bash
chmod +x setup_env.sh
```

Then run:

```bash
./setup_env.sh
```

---

## 🔁 Using the Setup

1. Ensure `.env` is configured.
2. Run `./setup_env.sh` to set up the environment.
3. Activate it whenever you work:

```bash
source .venv/bin/activate
```

4. Run your Python scripts (e.g., `generate_scene.py`, `compile_video.py`).

---

### ✅ Why This Works

* `python3 -m venv .venv` creates an isolated environment .
* `source .venv/bin/activate` ensures pip installs go into `.venv`, not globally .
* We install `leonardo-ai-sdk` which is the official Python client .

---

## 👣 Quick Steps Summary

| Step | Description                                                     |
| ---- | --------------------------------------------------------------- |
| 1    | Create `.env` with your Leonardo key                            |
| 2    | Run `./setup_env.sh` to set up `.venv` and install dependencies |
| 3    | Activate whenever working with `source .venv/bin/activate`      |

With this, you're ready to securely generate AI images, build your Memory Palace video, and compile it. Just let me know if you'd like a snippet to read `.env` values in Python or automate further!
