# Product 3D Modeling from Video using CUDA-Based Neural Radiance Fields (NeRF)

## Overview
This repository provides a fully automated pipeline to generate a 3D model from a video using a **CUDA-optimized NeRF implementation** with **torch-ngp**. The only input required is a video file, and the rest is handled automatically.

**torch-ngp**: https://github.com/ashawkey/torch-ngp.git

**Tiny CUDA Neural Networks**: https://github.com/NVlabs/tiny-cuda-nn.git

## Prerequisites
1. **Python 3.8+** for frame extraction
2. **COLMAP**: For generating `transforms.json` with camera poses
3. **torch-ngp**: CUDA-optimized NeRF implementation (cloned into this repository)

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/EarthMera/EM_INT_ML_3D_Model_Generation.git
cd EM_INT_ML_3D_Model_Generation
```

### 2. Install Dependencies
Run the provided setup script, ```setup.sh```, to install Python packages and external tools like COLMAP and NeRF.

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

