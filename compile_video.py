import argparse, os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def compile_video(input_dir, output_path):
    clips = []
    for i in range(1, 21):
        sn = f"{i:02d}"
        clips.append(VideoFileClip(os.path.join(input_dir, f"scene_{sn}", "scene.mp4")))
    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile(output_path, fps=24)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--input_dir', required=True)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    compile_video(args.input_dir, args.output)
