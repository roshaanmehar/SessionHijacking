@echo off
echo 🚀 Setting up Framer Auto Publisher...

REM Create virtual environment
python -m venv venv
call venv\Scripts\activate.bat

REM Install requirements
pip install -r requirements.txt

echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Copy .env.example to .env and set your project URL
echo 2. Run: python run.py (this will handle setup and publishing)
echo    OR manually: python setup_session.py then python publish.py
pause
