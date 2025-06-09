import argparse, yaml, os, time
from moviepy.editor import *
from leonardo_api import Leonardo

API_TOKEN = os.getenv("LEONARDO_API_KEY")
leonardo = Leonardo(auth_token=API_TOKEN)

def generate_scene(scene_number, config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)['scenes'][int(scene_number)-1]
    prompt, text = config['prompt'], config['text']
    # Trigger image generation
    resp = leonardo.post_generations(prompt=prompt, num_images=1,
                                     model_id='e316348f-7773-490e-adcd-46757c738eb7',
                                     width=1024, height=512, guidance_scale=7)
    gen_id = resp['sdGenerationJob']['generationId']
    img = leonardo.wait_for_image_generation(generation_id=gen_id)[0]
    url = img['url']
    # Save downloaded image
    scene_dir = f"scenes/scene_{scene_number.zfill(2)}"
    os.makedirs(scene_dir, exist_ok=True)
    img_path = os.path.join(scene_dir, "bg.png")
    with open(img_path, 'wb') as out:
        out.write(requests.get(url).content)
    # Create video clip with text overlay
    bg = ImageClip(img_path).set_duration(30)
    txt = TextClip(text, fontsize=48, color='white', font='Arial-Bold')
    txt = txt.set_position('center').set_duration(30)
    clip = CompositeVideoClip([bg, txt])
    clip.write_videofile(os.path.join(scene_dir, "scene.mp4"), fps=24)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--scene', required=True)
    p.add_argument('--config', required=True)
    args = p.parse_args()
    generate_scene(args.scene, args.config)
