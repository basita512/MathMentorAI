#!/bin/bash

echo "🚀 Setting up AI Math Mentor..."

# Create directories
mkdir -p data/{uploads,chromadb,feedback}
mkdir -p logs

# Build knowledge base
echo "📚 Building knowledge base..."
uv run python src/rag/knowledge_builder.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "To run the app:"
echo "  uv run streamlit run src/ui/app.py"
