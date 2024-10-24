# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install COLMAP
echo "Installing COLMAP..."
sudo apt update && sudo apt install colmap

# Clone and build instant-ngp (NeRF)
echo "Cloning NeRF..."
git clone https://github.com/NVlabs/instant-ngp.git
cd instant-ngp
cmake . -B build -DNGP_BUILD_WITH_GUI=off
make -C build -j
cd ..

echo "Setup complete!"