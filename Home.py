"""
AI Math Mentor - Multi-page Streamlit App

Entry point for the application.
"""
import streamlit as st

# Page config must be first Streamlit command
st.set_page_config(
    page_title="AI Math Mentor",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Professional Dark Mode Styles
st.markdown("""
<style>
    /* Dark Mode Global Styles */
    .stApp {
        background-color: #0e1117;
    }
    
    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        color: #ffffff;
        margin-bottom: 0.5rem;
        padding-top: 1rem;
        letter-spacing: -1px;
    }
    
    .subtitle {
        font-size: 1.25rem;
        text-align: center;
        color: #94a3b8; /* Slate-400 */
        margin-bottom: 3rem;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    
    /* Card Styles */
    .feature-card {
        background-color: #1e293b; /* Slate-800 */
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #334155; /* Slate-700 */
        height: 100%;
        min-height: 280px; /* Uniform height for all cards */
        transition: all 0.2s ease-in-out;
    }
    
    .feature-card:hover {
        border-color: #60a5fa; /* Blue-400 */
        transform: translateY(-2px);
    }
    
    .section-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #f8fafc; /* Slate-50 */
        margin-bottom: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        border-bottom: 2px solid #3b82f6;
        display: inline-block;
        padding-bottom: 4px;
    }
    
    .card-content {
        color: #cbd5e1; /* Slate-300 */
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    /* List Styles */
    ul.agent-list {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }
    
    ul.agent-list li {
        margin-bottom: 0.5rem;
        padding-left: 1rem;
        border-left: 3px solid #6366f1; /* Indigo-500 */
    }
    
    strong {
        color: #e2e8f0; /* Slate-200 */
    }

    /* Button Styles */
    .stButton button {
        background-color: #2563eb;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        width: 100%;
        transition: background-color 0.2s;
    }
    .stButton button:hover {
        background-color: #1d4ed8;
    }
</style>
""", unsafe_allow_html=True)

# Layout: Hero Section
st.markdown('<h1 class="main-header">AI Math Mentor</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">PRODUCTION-GRADE HYBRID RAG & AGENTIC SOLVER</p>', unsafe_allow_html=True)

# Primary Call-to-Action
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("START SOLVING PROBLEMS", type="primary", use_container_width=True):
        st.switch_page("pages/1_Solve_Problem.py")

st.markdown("<br>", unsafe_allow_html=True)

# Content Grid
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
    <div class="feature-card">
        <div class="section-title">5 Specialized Agents</div>
        <div class="card-content">
            <ul class="agent-list">
                <li><strong>Parser Agent</strong>: Converts unstructured input into strict JSON schema.</li>
                <li><strong>Router Agent</strong>: Routes queries to specific domains (Algebra, Calculus).</li>
                <li><strong>Solver Agent</strong>: Executes step-by-step logic using RAG and Tools.</li>
                <li><strong>Verifier Agent</strong>: Cross-checks logic and units before final output.</li>
                <li><strong>Explainer Agent</strong>: Formulates student-friendly, pedagogical answers.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div class="feature-card">
        <div class="section-title">Multimodal Input</div>
        <div class="card-content">
            This system accepts diverse input types for seamless interaction:
            <br><br>
            <strong>TEXT</strong>: Natural language queries for complex word problems.<br>
            <strong>IMAGE</strong>: Optical Character Recognition (EasyOCR) for handwritten notes.<br>
            <strong>AUDIO</strong>: High-fidelity speech-to-text transcription via Groq Whisper Turbo.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Features Row
feat_col1, feat_col2 = st.columns(2)

with feat_col1:
    st.markdown("""
    <div class="feature-card">
        <div class="section-title">Core Architecture</div>
        <div class="card-content">
            <ul class="agent-list">
                <li><strong>Orchestration</strong>: LangGraph + LangChain for stateful, cyclical flows.</li>
                <li><strong>LLM</strong>: Groq (Llama-3.3-70b) for sub-second inference.</li>
                <li><strong>Memory</strong>: Redis-backed episodic storage for learning.</li>
                <li><strong>Vector DB</strong>: ChromaDB + Rank-BM25 for hybrid search.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with feat_col2:
    st.markdown("""
    <div class="feature-card">
        <div class="section-title">Advanced Features</div>
        <div class="card-content">
             <ul class="agent-list">
                <li><strong>Hybrid RAG</strong>: Guaranteed diversity (Formula/Template/Example) with 70/30 Hybrid Weights.</li>
                <li><strong>Web Search</strong>: Integrated Tavily API fallback for novel topics.</li>
                <li><strong>Symbolic Math</strong>: SymPy integration for precise algebraic manipulation.</li>
                <li><strong>Human-in-the-Loop</strong>: Active feedback for low-confidence scenarios.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Supported Topics Section
st.markdown("###Supported Topics")
topic_col1, topic_col2, topic_col3, topic_col4 = st.columns(4)

with topic_col1:
    st.markdown("""
    <div class="feature-card" style="min-height: 180px;">
        <div class="section-title">Algebra I</div>
        <div class="card-content">
            Complex Numbers<br>
            Quadratic Equations<br>
            Sequences & Series<br>
            Binomial Theorem
        </div>
    </div>
    """, unsafe_allow_html=True)

with topic_col2:
    st.markdown("""
    <div class="feature-card" style="min-height: 180px;">
        <div class="section-title">Algebra II</div>
        <div class="card-content">
            Permutations & Combinations<br>
            Matrices & Determinants<br>
            Sets & Relations<br>
            Functions
        </div>
    </div>
    """, unsafe_allow_html=True)

with topic_col3:
    st.markdown("""
    <div class="feature-card" style="min-height: 180px;">
        <div class="section-title">Calculus</div>
        <div class="card-content">
            Limits & Continuity<br>
            Derivatives & Applications<br>
            Definite Integrals<br>
            Indefinite Integrals<br>
            Area Under Curves
        </div>
    </div>
    """, unsafe_allow_html=True)

with topic_col4:
    st.markdown("""
    <div class="feature-card" style="min-height: 180px;">
        <div class="section-title">Vectors & Prob.</div>
        <div class="card-content">
            <strong>Vector Algebra</strong><br>
            Dot & Cross Product<br>
            <strong>Probability</strong><br>
            Conditional Probability<br>
            Bayes Theorem
        </div>
    </div>
    """, unsafe_allow_html=True)

# No footer as requested