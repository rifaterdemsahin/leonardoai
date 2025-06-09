import argparse
import yaml
from moviepy.editor import *

def generate_scene(scene_number, config_path):
    # Load scene configuration
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    scene_config = config['scenes'][int(scene_number) - 1]

    # Create background clip
    background = ImageClip(f"assets/images/{scene_config['background']}").set_duration(30)

    # Add text overlay
    txt_clip = TextClip(scene_config['text'], fontsize=24, color='white')
    txt_clip = txt_clip.set_position('center').set_duration(30)

    # Combine background and text
    final_clip = CompositeVideoClip([background, txt_clip])

    # Write the scene to file
    output_path = f"scenes/scene_{scene_number}/scene_{scene_number}.mp4"
    final_clip.write_videofile(output_path, fps=24)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--scene', required=True, help='Scene number to generate')
    parser.add_argument('--config', required=True, help='Path to scenes configuration file')
    args = parser.parse_args()
    generate_scene(args.scene, args.config)
