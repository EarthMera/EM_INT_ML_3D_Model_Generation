# Product 3D Modeling from Video using CUDA-Based Neural Radiance Fields (NeRF)

## Overview
This repository provides a fully automated pipeline to generate a 3D model from a video using a **CUDA-optimized NeRF implementation** with **torch-ngp**. The pipeline leverages **tiny-cuda-nn** for fast training and **PyTorch** with **CUDA** for high performance.

## Prerequisites
1. **Python 3.8+** (we used Python 3.10.15 for testing)
2. **CUDA 12.1+**: Ensure your NVIDIA drivers support this version or higher.
3. **PyTorch 2.1.0+**: We used PyTorch 2.4.1 with CUDA 12.4 for testing.
4. **instant-ngp**: We use NVIDIA's instant-ngp for NeRF. Ensure that you meet instant-ngp's requirements as well.

### Note
This project was tested on **CUDA 12.4** and **PyTorch 2.4.1**, using **Python 3.10.15** on a Windows 11 64-bit system.

## Setup

### 1. Clone the Repository
```bash
.$ git clone https://github.com/EarthMera/EM_INT_ML_3D_Model_Generation.git
.$ cd EM_INT_ML_3D_Model_Generation
```

### 2. Install Dependencies
Run the provided setup script, ```setup.bat```, to clone in necessary repositories.
```bash
./EM_INT_ML_3D_Model_Generation$ setup.bat
```

### 3. Use CMake to build instant-ngp (on Windows, this must be in a developer command prompt)
```bash
./EM_INT_ML_3D_Model_Generation/instant-ngp$ cmake . -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo
./EM_INT_ML_3D_Model_Generation/instant-ngp$ cmake --build build --config RelWithDebInfo -j
```

### 3. Input Video
Create a new folder for your product under ```data/``` and place your product video in your folder, ```data/{product}/{product}.mp4```. Ensure your folder name and your video name are both your product's name.

### 4. Run the Pipeline
To run the entire pipeline, provide the name of the product:
```bash
./EM_INT_ML_3D_Model_Generation$ python main_nerf_pipeline.py --product {product}
```

This will:

1. Extract frames from the input video.
2. Use COLMAP to estimate camera poses and generate ```transforms.json```.
3. Automatically start training the NeRF model using **instant-ngp**.
4. After training, a marching-cubes based mesh from the NeRF model will be saved in OBJ format in ```data/{product}```

## Output
The NeRF model will be trained, and the mesh OBJ file will be saved in ```data/{product}```.

