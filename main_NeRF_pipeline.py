import os
import subprocess
from scripts.extract_frames import extract_frames

def run_full_nerf_pipeline(product, frame_rate=5, gui=False, n_steps=20000):
    """
    Runs the full pipeline for NeRF preparation and training.
    1. Use colmap2nerf.py to generate frames and transforms.json with camera poses.
    2. Automatically train NeRF using instant-ngp.
    
    Args:
        product (str): Name of product to model.
        frame_rate (int): Frame extraction rate.
    """

    # Step 1: colmap2nerf.py
    print("Running colmap2nerf.py...")

    os.chdir(os.getcwd() + '\data')
    os.chdir(os.getcwd() + f'\{product}')
    
    colamp2nerf_path = "../../instant-ngp/scripts/colmap2nerf.py"
    subprocess.run(['python', colamp2nerf_path, '--video_in', f'{product}.mp4', '--video_fps', str(frame_rate), '--run_colmap', '--aabb_scale', '32'])

    # Step 2: instant-ngp
    print("Running instant-ngp...")
    
    os.chdir("../")
    os.chdir("../")
    os.chdir(os.getcwd() + '\instant-ngp')
    
    if gui:
        subprocess.run(['python', 'scripts/run.py', f'../data/{product}', '--save_mesh', f'../data/{product}/hydro_flask.obj', '--gui', '--train', '--n_steps', str(n_steps)])
    else:
        subprocess.run(['python', 'scripts/run.py', f'../data/{product}', '--save_mesh', f'../data/{product}/hydro_flask.obj', '--n_steps', str(n_steps)])
    
    print("Pipeline complete. NeRF training finished.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run full pipeline for NeRF.")
    parser.add_argument('--product', type=str, required=True, help="Name of your product.")
    parser.add_argument('--frame_rate', type=int, default=5, help="Frame extraction rate (every nth frame).")
    parser.add_argument("--gui", action="store_true", help="Run the testbed GUI interactively.")
    parser.add_argument('--n_steps', type=int, default=20000, help="Number of steps for training.")
    
    args = parser.parse_args()

    run_full_nerf_pipeline(args.product, args.frame_rate, args.gui, args.n_steps)