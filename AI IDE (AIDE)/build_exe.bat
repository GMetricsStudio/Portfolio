@echo off
echo 🛠️ Preparing to build standalone executable...

if not exist ".venv" (
    echo 📦 Creating virtual environment...
    python -m venv .venv
)

echo 🛠️ Activating environment and installing dependencies...
call .venv\Scripts\activate
pip install -r requirements.txt

echo 🏗️ Building EXE (this may take several minutes)...
python build_exe.py

echo.
echo ✨ Process complete. Check the 'dist' folder for your executable.
pause
