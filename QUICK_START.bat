@echo off
cd /d "%~dp0"

IF NOT EXIST "venv\Scripts\activate.bat" (
    echo ⚠️ Virtual environment not found. Creating one now, this takes a few seconds...
    python -m venv venv
)

echo ⚡ Fast starting GlowAI...
call venv\Scripts\activate.bat

echo 🛠️ Quickly fixing missing packages...
python -m pip install python-dotenv psycopg2-binary google-genai "protobuf<5" requests

echo Starting FastAPI Backend...
start /B python -m uvicorn src.api.main:app --reload

echo Waiting for API to start...
timeout /t 3 /nobreak > nul

echo Starting Streamlit Dashboard...
python -m streamlit run glowai_dashboard.py
