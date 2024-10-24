# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Clone and build instant-ngp (NeRF)
echo "Cloning NeRF..."
git clone https://github.com/NVlabs/instant-ngp.git
cd instant-ngp
cmake . -B build -DNGP_BUILD_WITH_GUI=off
make -C build -j
cd ..

echo "Setup complete!"