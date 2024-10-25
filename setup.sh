# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install COLMAP
echo "Installing COLMAP..."
sudo apt update && sudo apt install colmap

# Clone and set up torch-ngp for CUDA-based NeRF
echo "Cloning torch-ngp..."
git clone https://github.com/ashawkey/torch-ngp.git
cd torch-ngp
pip install -r requirements.txt
pip install git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch
cd ..

echo "Setup complete!"