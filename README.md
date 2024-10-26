# Product 3D Modeling from Video using CUDA-Based Neural Radiance Fields (NeRF)

## Overview
This repository provides a fully automated pipeline to generate a 3D model from a video using a **CUDA-optimized NeRF implementation** with **torch-ngp**. The pipeline leverages **tiny-cuda-nn** for fast training and **PyTorch** with **CUDA** for high performance.

## Prerequisites
1. **Python 3.8+** (we used Python 3.10.15 for testing)
2. **tiny-cuda-nn**: Integrated with torch-ngp for fast and efficient neural networks. (cloned into this repository)
3. **torch-ngp**: CUDA-optimized NeRF implementation. (cloned into this repository)
4. **CUDA 12.1+**: Ensure your NVIDIA drivers support this version or higher.
5. **PyTorch 2.1.0+**: We used PyTorch 2.4.1 with CUDA 12.4 for testing.
6. **COLMAP**: For generating `transforms.json` with camera poses.

### Note
This project was tested on **CUDA 12.4** and **PyTorch 2.4.1**, using **Python 3.10.15** on a Windows 11 64-bit system.

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/EarthMera/EM_INT_ML_3D_Model_Generation.git
cd EM_INT_ML_3D_Model_Generation
```

### 2. Install Dependencies
Run the provided setup script, ```setup.bat```, to install necessary packages, including Python dependencies, COLMAP, and torch-ngp.

### 3. Input Video
Place your product video in the ```data/raw_videos/``` directory.

### 4. Run the Pipeline
To run the entire pipeline, provide the path to the input video:
```bash
python main_nerf_pipeline.py --video data/raw_videos/product_test.mp4 --output data/
```

This will:

1. Extract frames from the input video.
2. Use COLMAP to estimate camera poses and generate ```transforms.json```.
3. Automatically start training the NeRF model using **torch-ngp**.

## Output
The NeRF model will be trained, and results will be saved in the **torch-ngp** output directory.

