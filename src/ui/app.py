"""Main Streamlit app."""
import streamlit as st
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.preprocessing.ocr import OCRProcessor
from src.preprocessing.audio import AudioProcessor
from src.preprocessing.text import TextCleaner
from src.agents.orchestrator import Orchestrator
from src.memory.episodic import EpisodicMemory
from src.utils.logger import get_logger
import tempfile
import time

logger = get_logger()

# Page config
st.set_page_config(
    page_title="AI Math Mentor",
    page_icon="🧮",
    layout="wide"
)

# Initialize session state
if 'orchestrator' not in st.session_state:
    with st.spinner("Initializing AI Math Mentor..."):
        st.session_state.orchestrator = Orchestrator()
        st.session_state.memory = EpisodicMemory()
        st.session_state.ocr = OCRProcessor()
        st.session_state.audio = AudioProcessor()

st.title("🧮 AI Math Mentor")
st.markdown("**Multimodal RAG-powered JEE Math Problem Solver**")

# Sidebar
with st.sidebar:
    st.header("📋 Input Mode")
    input_mode = st.radio(
        "Select input type:",
        ["📝 Text", "📸 Image", "🎤 Audio"]
    )
    
    st.divider()
    st.header("ℹ️ About")
    st.info("""
    This AI Math Mentor:
    - Solves JEE-level math problems
    - Uses RAG for knowledge retrieval
    - Multi-agent system
    - Learns from feedback
    
    **Topics:** Algebra, Calculus, Probability, Linear Algebra
    """)

# Main area
raw_input = None
needs_confirmation = False
extracted_text = ""

def solve_problem(problem_text: str):
    """Solve problem and display results."""
    
    # Check memory for similar problems
    with st.spinner("Checking memory for similar problems..."):
        similar = st.session_state.memory.retrieve_similar(problem_text, top_k=2)
        
        if similar and similar[0]['similarity'] > 0.85:
            st.info(f"📚 Found similar problem in memory (similarity: {similar[0]['similarity']:.1%})")
            with st.expander("View similar solution"):
                st.write(similar[0]['text'])
    
    # Agent execution
    st.subheader("🤖 Agent Execution")
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Step 1: Parsing
    status_text.text("🔄 Parsing problem...")
    progress_bar.progress(20)
    time.sleep(0.5)
    
    # Step 2: Solving
    status_text.text("🧮 Solving with RAG + Tools...")
    progress_bar.progress(50)
    time.sleep(0.5)
    
    # Step 3: Verification
    status_text.text("✅ Verifying solution...")
    progress_bar.progress(75)
    time.sleep(0.5)
    
    # Step 4: Explanation
    status_text.text("📖 Generating explanation...")
    progress_bar.progress(90)
    
    # Run orchestrator
    result = st.session_state.orchestrator.process(problem_text)
    
    progress_bar.progress(100)
    status_text.text("✅ Complete!")
    time.sleep(0.3)
    status_text.empty()
    progress_bar.empty()
    
    # Handle different statuses
    if result['status'] == 'needs_clarification':
        st.warning("⚠️ **Clarification Needed**")
        st.write("**Ambiguities detected:**")
        for amb in result['parsed'].ambiguities:
            st.write(f"- {amb}")
        st.info("Please rephrase your question or provide more details.")
        return
    
    if result['status'] == 'needs_review':
        st.warning("⚠️ **Low Confidence - Human Review Recommended**")
        st.metric("Verification Confidence", f"{result['verification']['confidence']:.1%}")
        
        if result['verification']['issues']:
            st.write("**Issues found:**")
            for issue in result['verification']['issues']:
                st.write(f"- {issue}")
    
    # Display results
    st.success("✅ **Solution Complete**")
    
    # Tabs for organization
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Solution", "📖 Explanation", "🔍 Context", "🔧 Details"])
    
    with tab1:
        st.subheader("Solution")
        st.markdown(result['solution'])
        
        if result.get('verification'):
            st.divider()
            col1, col2 = st.columns(2)
            with col1:
                status = "✅ Verified" if result['verification']['verification_passed'] else "❌ Issues Found"
                st.metric("Verification", status)
            with col2:
                st.metric("Confidence", f"{result['verification']['confidence']:.1%}")
    
    with tab2:
        st.subheader("Step-by-Step Explanation")
        st.markdown(result['explanation'])
    
    with tab3:
        st.subheader("Retrieved Knowledge")
        for i, ctx in enumerate(result['retrieved_context'], 1):
            with st.expander(f"Context {i}"):
                st.write(ctx)
    
    with tab4:
        st.subheader("Processing Details")
        st.json({
            'topic': result['parsed'].topic,
            'difficulty': result['parsed'].difficulty,
            'variables': result['parsed'].variables,
            'question_type': result['parsed'].question_type
        })
    
    # Feedback section
    st.divider()
    st.subheader("📝 Feedback")
    
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        if st.button("✅ Correct", use_container_width=True):
            st.session_state.memory.store_solution(
                problem_text,
                result['solution'],
                {'correct': True, 'rating': 5}
            )
            st.success("Feedback saved!")
    
    with col2:
        if st.button("❌ Incorrect", use_container_width=True):
            st.session_state.memory.store_solution(
                problem_text,
                result['solution'],
                {'correct': False, 'rating': 1}
            )
            st.error("Feedback saved - will learn from this!")
    
    with col3:
        feedback_text = st.text_input("Additional comments (optional):")

# Input handling
if input_mode == "📝 Text":
    st.subheader("Type your math problem")
    raw_input = st.text_area(
        "Enter problem:",
        placeholder="Example: Solve x² - 5x + 6 = 0",
        height=150
    )

elif input_mode == "📸 Image":
    st.subheader("Upload image of problem")
    uploaded_file = st.file_uploader(
        "Choose image (JPG/PNG):",
        type=['jpg', 'jpeg', 'png']
    )
    
    if uploaded_file:
        # Display image
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        
        with col2:
            with st.spinner("Extracting text from image..."):
                # Save temp file
                with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name
                
                # OCR
                ocr_result = st.session_state.ocr.process(tmp_path)
                
                st.metric("OCR Confidence", f"{ocr_result.confidence:.1%}")
                
                if ocr_result.needs_review:
                    st.warning("⚠️ Low confidence - please review and edit")
                
                extracted_text = st.text_area(
                    "Extracted text (editable):",
                    value=ocr_result.text,
                    height=150
                )
                
                needs_confirmation = True

elif input_mode == "🎤 Audio":
    st.subheader("Upload or record audio")
    audio_file = st.file_uploader(
        "Choose audio file:",
        type=['mp3', 'wav', 'm4a', 'ogg']
    )
    
    if audio_file:
        st.audio(audio_file)
        
        with st.spinner("Transcribing audio..."):
            # Save temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp:
                tmp.write(audio_file.read())
                tmp_path = tmp.name
            
            # Transcribe
            transcript = st.session_state.audio.transcribe(tmp_path)
            
            extracted_text = st.text_area(
                "Transcript (editable):",
                value=transcript.text,
                height=150
            )
            
            if transcript.unclear_sections:
                st.warning(f"Unclear sections detected: {len(transcript.unclear_sections)}")
            
            needs_confirmation = True

# Confirmation for multimodal inputs
if needs_confirmation:
    if st.button("✅ Confirm & Solve", type="primary"):
        raw_input = extracted_text
        solve_problem(raw_input)

# Solve button for text input
if raw_input and not needs_confirmation:
    if st.button("🚀 Solve Problem", type="primary"):
        solve_problem(raw_input)

if __name__ == "__main__":
    pass
