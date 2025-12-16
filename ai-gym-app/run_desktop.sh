#!/bin/bash
echo "Setting up Fitness App..."
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate
echo "Installing requirements..."
pip install PySide6
mkdir -p data
echo "Starting Fitness App..."
python FrameWork.py