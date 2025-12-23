@echo off
setlocal enabledelayedexpansion

echo 🚀 Starting AI Dev IDE Portable Launcher...

rem Check for NVIDIA GPU
nvidia-smi >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ NVIDIA GPU detected.
    set HAS_GPU=1
) else (
    echo ℹ️ No NVIDIA GPU detected or drivers not found.
    set HAS_GPU=0
)

:menu
echo.
echo Select action:
echo 1. Launch IDE (Local)
echo 2. Build Standalone EXE (PyInstaller)
echo 3. Exit
set /p choice="Enter choice (1-3): "

if "%choice%"=="1" goto local_launch
if "%choice%"=="2" goto build_exe
if "%choice%"=="3" exit /b
goto menu

:local_launch
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed! Please install Python 3.10+ from python.org
    pause
    exit /b
)

if not exist ".venv" (
    echo 📦 Creating virtual environment...
    python -m venv .venv
)

echo 🛠️ Activating environment and checking dependencies...
call .venv\Scripts\activate

if %HAS_GPU% equ 1 (
    echo 🚀 Installing CUDA-enabled PyTorch...
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
)

pip install -r requirements.txt

echo ✨ Launching IDE...
python launcher.py
pause
exit /b

:build_exe
echo 🏗️ Starting build process...
call build_exe.bat
goto menu
