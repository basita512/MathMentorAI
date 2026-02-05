# AI Math Mentor

**Multimodal RAG-powered JEE Math Problem Solver**

A production-ready AI-powered math tutor that solves JEE-level mathematics problems using a multi-agent system with RAG (Retrieval Augmented Generation), multimodal input support, and self-learning capabilities.

## 🌟 Features

- **Multimodal Input**: Text, Image (OCR), and Audio (Speech-to-Text)
- **RAG System**: Knowledge retrieval using ChromaDB and sentence transformers
- **Multi-Agent Architecture**: Parser, Solver, Verifier, and Explainer agents
- **Symbolic Math**: Integration with SymPy for exact computations
- **Self-Learning**: Episodic memory system that learns from feedback
- **Human-in-the-Loop**: Automatic triggers for clarification and review
- **Topics Supported**: Algebra, Calculus, Probability, Linear Algebra

## 🏗️ Architecture

```
Input (Text/Image/Audio)
    ↓
Preprocessing Layer (OCR/Whisper/TextCleaner)
    ↓
Parser Agent → Solver Agent → Verifier Agent → Explainer Agent
    ↑               ↑
    |          RAG System
    |        (Vector Store)
    |               
Episodic Memory (ChromaDB)
```

## 📋 Prerequisites

- Python 3.11+
- [UV](https://docs.astral.sh/uv/) package manager
- Groq API key ([Get one here](https://console.groq.com/))

## 🚀 Quick Start

### 1. Install UV (if not already installed)

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux/Mac:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify installation:
```bash
uv --version
```

### 2. Clone and Setup

```bash
cd MathMentorAI
```

### 3. Install Dependencies

```bash
uv sync
```

### 4. Configure Environment

Copy the example environment file:
```bash
copy .env.example .env
```

Edit `.env` and add your Groq API key:
```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

### 5. Initialize Project

**Windows:**
```bash
scripts\setup.bat
```

**Linux/Mac:**
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### 6. Run the Application

```bash
uv run streamlit run src/ui/app.py
```

The app will open in your browser at `http://localhost:8501`

## 🧪 Testing

Run manual tests to verify all components:

```bash
uv run python scripts/test_manual.py
```

## 📁 Project Structure

```
MathMentorAI/
├── src/
│   ├── agents/           # Multi-agent system
│   │   ├── parser.py     # Problem structure extraction
│   │   ├── solver.py     # RAG-powered solver
│   │   ├── verifier.py   # Solution verification
│   │   ├── explainer.py  # Student-friendly explanations
│   │   └── orchestrator.py  # Agent coordinator
│   ├── rag/              # RAG system
│   │   ├── vector_store.py
│   │   └── knowledge_builder.py
│   ├── memory/           # Episodic memory
│   │   └── episodic.py
│   ├── tools/            # Mathematical tools
│   │   └── sympy_solver.py
│   ├── preprocessing/    # Input processing
│   │   ├── ocr.py
│   │   ├── audio.py
│   │   └── text.py
│   ├── ui/               # Streamlit UI
│   │   └── app.py
│   └── utils/            # Utilities
├── knowledge_base/       # Curated knowledge
│   ├── formulas/
│   ├── templates/
│   └── examples/
├── data/                 # Runtime data
├── scripts/              # Setup scripts
└── pyproject.toml        # Dependencies
```

## 🎯 Usage Examples

### Text Input
1. Select "📝 Text" mode
2. Enter: `Solve x² - 5x + 6 = 0`
3. Click "🚀 Solve Problem"

### Image Input
1. Select "📸 Image" mode
2. Upload an image of a handwritten/printed math problem
3. Review and edit OCR output if needed
4. Click "✅ Confirm & Solve"

### Audio Input
1. Select "🎤 Audio" mode
2. Upload an audio file saying a math problem
3. Review the transcript
4. Click "✅ Confirm & Solve"

## 🔧 Configuration

Edit `.env` to customize:

```env
# Model Configuration
LLM_MODEL=llama-3.3-70b-versatile
GROQ_TEMPERATURE=0.1

# OCR Confidence
OCR_CONFIDENCE_THRESHOLD=0.75

# Whisper Model (tiny/base/small/medium/large)
WHISPER_MODEL=base

# RAG Settings
TOP_K_RETRIEVAL=3
CHUNK_SIZE=500
CHUNK_OVERLAP=50
```

## 🛠️ Troubleshooting

### Module not found
```bash
uv sync
```

### ChromaDB error
```bash
rmdir /s data\chromadb  # Windows
rm -rf data/chromadb    # Linux/Mac
uv run python src/rag/knowledge_builder.py
```

### Groq API error
Check your API key in `.env`:
```bash
type .env | findstr GROQ_API_KEY    # Windows
cat .env | grep GROQ_API_KEY        # Linux/Mac
```

## 📚 Tech Stack

- **LLM**: Groq (llama-3.3-70b-versatile)
- **Vector DB**: ChromaDB
- **Embeddings**: sentence-transformers (all-MiniLM-L6-v2)
- **OCR**: PaddleOCR
- **Speech-to-Text**: OpenAI Whisper
- **Symbolic Math**: SymPy
- **UI**: Streamlit
- **Package Manager**: UV

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

MIT License - feel free to use this project for learning and development.

## 🙏 Acknowledgments

- Groq for fast LLM inference
- PaddleOCR for accurate text extraction
- OpenAI Whisper for speech recognition
- LangChain for agent framework
- ChromaDB for vector storage

---

**Built with ❤️ for JEE students**
