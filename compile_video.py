import argparse
from moviepy.editor import *

def compile_video(input_dir, output_path):
    clips = []
    for i in range(1, 21):
        scene_num = f"{i:02d}"
        clip = VideoFileClip(f"{input_dir}/scene_{scene_num}/scene_{scene_num}.mp4")
        clips.append(clip)
    final_video = concatenate_videoclips(clips)
    final_video.write_videofile(output_path, fps=24)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True, help='Directory containing scene videos')
    parser.add_argument('--output', required=True, help='Path for the final compiled video')
    args = parser.parse_args()
    compile_video(args.input_dir, args.output)
