Here's an updated version of your `config/scenes.yaml` with two new properties per scene:

1. **script** – a voiceover/dialogue snippet.
2. **outline** – a brief scene description for planning or teleprompting.

```yaml
scenes:
  - id: "01"
    prompt: "Cinematic entrance, wooden front door with engraved details, early morning light, warm glow through doorway, photorealistic, ultra‑detailed"
    text: "Scene 1: Entrance – recall the opening gateway."
    script: "Welcome to our journey. This door marks the beginning of your exploration."
    outline: "Wide shot of the entrance; soft morning sunlight; narrator introduces the path ahead."

  - id: "02"
    prompt: "Cozy living room, plush sofa and fireplace, soft afternoon sunlight, warm tones, digital painting, cinematic composition"
    text: "Scene 2: Living Room – where memories gather."
    script: "Step inside—here, warmth and comfort cradle every thought."
    outline: "Cut to living room; fire crackles; narrator evokes nostalgia."

  # ... repeat for scenes 3 through 19

  - id: "20"
    prompt: "Old wooden garden gate, climbing vines, golden hour backlight, sense of exit or conclusion, cinematic composition, ultra‑detailed"
    text: "Scene 20: Exit – closing the journey."
    script: "Behind this gate lies the end of our journey—and the start of yours."
    outline: "Close-up on gate close; ambient evening sounds; narrator concludes journey."
```

---

### 🎬 Separate YAML Files for Full Script & Outline

These are standalone versions if you'd rather separate content into dedicated files.

#### `script.yaml`

```yaml
script:
  "01": "Welcome to our journey. This door marks the beginning of your exploration."
  "02": "Step inside—here, warmth and comfort cradle every thought."
  # ...
  "20": "Behind this gate lies the end of our journey—and the start of yours."
```

#### `outline.yaml`

```yaml
outline:
  "01": "Wide shot of entrance; soft morning sunlight; narrator introduces the path ahead."
  "02": "Cut to living room; fire crackles; narrator evokes nostalgia."
  # ...
  "20": "Close-up on gate close; ambient evening sounds; narrator concludes journey."
```

---

### ✅ How to Integrate in Python

In your `generate_scene.py`, load both:

```python
with open("config/scenes.yaml") as f:
    scenes = yaml.safe_load(f)["scenes"]
for scene in scenes:
    prompt = scene["prompt"]
    text = scene["text"]
    script = scene["script"]
    outline = scene["outline"]
    # Use or store these values as needed...
```

Or if using separate files:

```python
with open("script.yaml") as f:
    scripts = yaml.safe_load(f)["script"]
with open("outline.yaml") as f:
    outlines = yaml.safe_load(f)["outline"]

script_text = scripts[f"{scene_id:02d}"]
outline_text = outlines[f"{scene_id:02d}"]
```

---

With these additions, you'll have tightly coordinated visuals, narration, and scene planning—ideal for both production flow and memory palace storytelling. Let me know if you'd like help fleshing out the voiceover or handling YAML loading!
