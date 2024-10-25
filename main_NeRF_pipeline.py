import os
import subprocess
from scripts.extract_frames import extract_frames

def run_full_nerf_pipeline(video_path, output_folder, frame_rate=10):
    """
    Runs the full pipeline for NeRF preparation and training.
    1. Extract frames from video.
    2. Use COLMAP to generate transforms.json with camera poses.
    3. Automatically train NeRF using instant-ngp.
    
    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Path to the folder where data will be processed.
        frame_rate (int): Frame extraction rate.
    """
    frames_folder = os.path.join(output_folder, 'frames')

    # Step 1: Extract frames from the video
    print("Extracting frames from video...")
    extract_frames(video_path, frames_folder, frame_rate)

    # Step 2: Use COLMAP to estimate camera poses and create transforms.json
    print("Running COLMAP for camera pose estimation...")
    database_path = os.path.join(output_folder, 'colmap.db')
    sparse_model_path = os.path.join(output_folder, 'sparse')
    transforms_json_path = os.path.join(output_folder, 'transforms.json')

    # Run COLMAP commands
    subprocess.run(['colmap', 'feature_extractor', '--database_path', database_path, '--image_path', frames_folder], check=True)
    subprocess.run(['colmap', 'exhaustive_matcher', '--database_path', database_path], check=True)
    subprocess.run(['colmap', 'mapper', '--database_path', database_path, '--image_path', frames_folder, '--output_path', sparse_model_path], check=True)
    subprocess.run(['colmap', 'model_converter', '--input_path', os.path.join(sparse_model_path, '0'), '--output_path', transforms_json_path, '--output_type', 'TXT'], check=True)

    print(f"Camera poses saved to {transforms_json_path}")

    # Step 3: Run instant-ngp training
    print("Starting NeRF training with instant-ngp...")
    subprocess.run(['./instant-ngp/build/neural_rendering', '--mode', 'nerf', '--scene', frames_folder], cwd='./instant-ngp')

    print("Pipeline complete. NeRF training finished.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run full pipeline for NeRF.")
    parser.add_argument('--video', type=str, required=True, help="Path to the input video.")
    parser.add_argument('--output', type=str, required=True, help="Path to output folder.")
    parser.add_argument('--frame_rate', type=int, default=10, help="Frame extraction rate (every nth frame).")
    
    args = parser.parse_args()

    run_full_nerf_pipeline(args.video, args.output, args.frame_rate)