#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Generate each scene
for i in {1..20}
do
    scene_num=$(printf "%02d" $i)
    python scripts/generate_scene.py --config config/scenes.yaml --scene $scene_num
done

# Compile all scenes into the final video
python scripts/compile_video.py --input_dir scenes/ --output output/final_video.mp4
