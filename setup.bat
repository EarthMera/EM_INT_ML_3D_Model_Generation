@echo off

:: Install PyTorch with CUDA 12.4
echo Installing PyTorch 2.4.1 with CUDA 12.4...
pip install torch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 --index-url https://download.pytorch.org/whl/cu124

:: Clone torch-ngp for CUDA-based NeRF
:: echo Cloning torch-ngp...
:: git clone https://github.com/ashawkey/torch-ngp.git
:: cd torch-ngp
:: pip install -r requirements.txt
:: pip install git+https://github.com/NVlabs/tiny-cuda-nn/#subdirectory=bindings/torch
:: cd ..

:: Clone inntant for CUDA-based NeRF
echo Cloning instant-ngp...
git clone --recursive https://github.com/nvlabs/instant-ngp
cd instant-ngp
pip install -r requirements.txt
cd ..

echo Setup complete!
pause
