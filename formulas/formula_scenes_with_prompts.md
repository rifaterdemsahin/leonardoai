Here is your updated `config/scenes.yaml`, now enhanced to include:

* **video\_prompt** – tailored for Leonardo.ai’s VEO video generation,
* **image\_prompt** – optimized for still image generation,
* **audio\_prompt** – recommended ambient or audio cue for each scene.

I've structured each prompt based on the guidance from Leonardo.ai’s VEO prompt recommendations ([leonardo.ai][1]) and best practices for still image prompts .

```yaml
scenes:
  - id: "01"
    video_prompt: >-
      Scene description: Wooden front door at morning light, cinematic entrance.
      Visual style: Photorealistic.
      Camera movement: Slow static reveal.
      Main subject: Front door with engraved details.
      Background: Soft dawn light.
      Lighting/mood: Warm, inviting atmosphere.
      Audio cue: Gentle birdsong and soft footsteps.
    image_prompt: "Cinematic entrance, wooden front door with engraved details, early morning light, warm glow through doorway, photorealistic, ultra-detailed"
    audio_prompt: "Gentle birdsong, soft footsteps on stone"
    text: "Scene 1: Entrance – recall the opening gateway."
    script: "Welcome to our journey. This door marks the beginning of your exploration."
    outline: "Wide shot of the entrance; soft morning sunlight; narrator introduces the path ahead."

  - id: "02"
    video_prompt: >-
      Scene description: Cozy living room with fireplace.
      Visual style: Digital painting, cinematic.
      Camera movement: Slow dolly-in from left to center.
      Main subject: Sofa and glowing fire.
      Background: Warm afternoon light, fireplace mantel.
      Lighting/mood: Warm and nostalgic.
      Audio cue: Fire crackling; soft ambient piano note.
    image_prompt: "Cozy living room, plush sofa and fireplace, soft afternoon sunlight, warm tones, digital painting, cinematic composition"
    audio_prompt: "Fire crackling, soft piano underscore"
    text: "Scene 2: Living Room – where memories gather."
    script: "Step inside—here, warmth and comfort cradle every thought."
    outline: "Cut to living room; fire crackles; narrator evokes nostalgia."

  # … repeat for scenes 03–19, each with three prompts

  - id: "20"
    video_prompt: >-
      Scene description: Old wooden garden gate closing at golden hour.
      Visual style: Cinematic photorealism.
      Camera movement: Slow push-in closing shot.
      Main subject: Garden gate with climbing vines.
      Background: Sunset backlight through foliage.
      Lighting/mood: Poignant, conclusive warmth.
      Audio cue: Distant evening crickets and soft gate creak.
    image_prompt: "Old wooden garden gate, climbing vines, golden hour backlight, sense of exit or conclusion, cinematic composition, ultra-detailed"
    audio_prompt: "Distant evening crickets, gentle gate creak"
    text: "Scene 20: Exit – closing the journey."
    script: "Behind this gate lies the end of our journey—and the start of yours."
    outline: "Close-up on gate close; ambient evening sounds; narrator concludes journey."
```

---

### ✅ How to use these prompts

* **video\_prompt**: Feed into Leonardo.ai VEO 3 engine to generate short animated clips ([leonardo.ai][1]).
* **image\_prompt**: Use with the standard Leonardo image endpoint (in your `generate_scene.py`) for stills ([medium.com][2]).
* **audio\_prompt**: Use to source or generate matching ambient audio — ideal for background sound or layering under narration.

---

Would you like me to fill out the full YAML for all 20 scenes, or help you integrate these into your Python orchestration scripts?

[1]: https://leonardo.ai/news/mastering-prompts-for-veo-3/?utm_source=chatgpt.com "Mastering Prompts For VEO 3 | Leonardo AI"
[2]: https://medium.com/bring-your-own-ai/15-tips-to-use-leonardo-ai-like-a-pro-d16b4885bd5c?utm_source=chatgpt.com "15 Tips to Use Leonardo AI Like a Pro - Medium"
