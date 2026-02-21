@echo off
echo 🚀 Setting up AI Math Mentor...

REM Create directories
if not exist data\uploads mkdir data\uploads
if not exist data\chromadb mkdir data\chromadb
if not exist data\feedback mkdir data\feedback
if not exist logs mkdir logs

REM Build knowledge base
echo 📚 Building knowledge base...
uv run python src/rag/knowledge_builder.py

echo.
echo ✅ Setup complete!
echo.
echo To run the app:
echo   uv run streamlit run src/ui/app.py
