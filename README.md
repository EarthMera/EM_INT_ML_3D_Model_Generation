# Product 3D Modeling from Video using Neural Radiance Fields (NeRF)

## Overview
This repository provides tools to extract video frames of a product shot from various angles and reconstruct a 3D model using **Neural Radiance Fields (NeRF)**, specifically **instant-ngp** by NVlabs.

## Prerequisites
1. **Python 3.7+** for frame extraction
2. **COLMAP**: For generating `transforms.json` with camera poses
3. **torch-ngp**: CUDA-optimized NeRF implementation (cloned into this repository)

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/EarthMera/EM_INT_ML_3D_Model_Generation.git
cd EM_INT_ML_3D_Model_Generation
```

### 2. Install Dependencies
Run the provided setup script to install Python packages and external tools like COLMAP and NeRF.
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Input Video
Place your product video in the ```data/raw_videos/``` directory.

### 4. Run the Pipeline
To run the entire pipeline, provide the path to the input video:
```bash
python main_nerf_pipeline.py --video data/raw_videos/product_test.mp4 --output data/
```

This will:

1. Extract frames from the input video.
2. Use COLMAP to estimate camera poses and generate transforms.json.
3. Automatically start training the NeRF model using torch-ngp.

## Output
The NeRF model will be trained, and results will be saved in the torch-ngp output directory.

