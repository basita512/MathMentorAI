"""Solve Problem Page - Complete multimodal interface with Image, Audio, Text."""
import streamlit as st
import sys
from pathlib import Path
import tempfile

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.orchestration.graph import GraphOrchestrator
from src.preprocessing.ocr import OCRProcessor
from src.preprocessing.audio import AudioProcessor
from src.memory.episodic import EpisodicMemory
from src.memory.feedback_store import feedback_store
from ui_components import render_agent_timeline, render_confidence_breakdown, render_retrieved_context

st.set_page_config(page_title="Solve Problem", page_icon="📐", layout="wide")

st.title("Solve Math Problems")
st.caption("Upload an image, record audio, or type your math problem")

# Initialize components
@st.cache_resource
def get_orchestrator():
    return GraphOrchestrator()

@st.cache_resource
def get_ocr():
    return OCRProcessor()

@st.cache_resource
def get_audio():
    return AudioProcessor()

@st.cache_resource
def get_memory():
    return EpisodicMemory()

try:
    orch = get_orchestrator()
    ocr = get_ocr()
    audio_proc = get_audio()
    memory = get_memory()
except Exception as e:
    st.error(f"Failed to initialize: {e}")
    st.stop()

# Sidebar settings
with st.sidebar:
    st.markdown("### Input Mode")
    input_mode = st.radio(
        "Choose input method:",
        ["Text", "Image (OCR)", "Audio"],
        index=0
    )
    
    st.markdown("---")
    st.markdown("### Display Settings")
    show_trace = st.checkbox("Show Agent Trace", value=True)
    show_context = st.checkbox("Show Retrieved Context", value=True)
    show_confidence = st.checkbox("Show Confidence", value=True)

# Main content
col_input, col_viz = st.columns([1, 1])

problem_text = None
ocr_confidence = None
solve_button = False  # Initialize before conditionals

# Initialize session state for text input (must be before conditionals)
if 'problem_input' not in st.session_state:
    st.session_state['problem_input'] = ""

with col_input:
    st.markdown("### Problem Input")
    
    # ========== TEXT INPUT ==========
    if input_mode == "Text":
        # Symbol reference guide (better UX than inserting at end)
        with st.expander("Math Symbol Reference - Click to expand", expanded=False):
            st.markdown("""
            **Type these shortcuts in your problem:**
            
            | Symbol | Type | Symbol | Type | Symbol | Type |
            |--------|------|--------|------|--------|------|
            | π | `pi` | √ | `sqrt()` | ∞ | `infinity` |
            | ² | `^2` | ³ | `^3` | ≤ | `<=` |
            | ≥ | `>=` | ≠ | `!=` | ∈ | `in` |
            | ∫ | `integral` | ∑ | `sum` | ± | `+-` |
            | α | `alpha` | β | `beta` | θ | `theta` |
            
            **Example:** Type `x^2 - 5x + 6 = 0` or `x² - 5x + 6 = 0`
            """)
        
        problem_text = st.text_area(
            "Enter your math problem:",
            value=st.session_state['problem_input'],
            height=150,
            placeholder="Example: Solve x^2 - 5x + 6 = 0 (or x² - 5x + 6 = 0)\nTip: Type 'pi', 'sqrt(x)', 'x^2' or paste Unicode symbols"
        )
        
        # Update session state when user types
        st.session_state['problem_input'] = problem_text
        
        solve_button = st.button("Solve Problem", type="primary", use_container_width=True)
    
    # ========== IMAGE INPUT (OCR) ==========
    elif input_mode == "Image (OCR)":
        st.info("Upload an image of your math problem (JPG, PNG)")
        
        uploaded_file = st.file_uploader(
            "Upload image",
            type=["png", "jpg", "jpeg"],
            help="Take a photo of handwritten notes or a textbook page"
        )
        
        if uploaded_file:
            # Display the uploaded image
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
            
            # Process button
            if st.button("🔍 Extract Text (OCR)", use_container_width=True):
                with st.spinner("Running OCR..."):
                    # Save to temp file
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                        tmp.write(uploaded_file.getvalue())
                        tmp_path = tmp.name
                    
                    # Run OCR
                    result = ocr.process(tmp_path)
                    st.session_state['ocr_result'] = result
            
            # Show OCR result and allow editing
            if 'ocr_result' in st.session_state:
                result = st.session_state['ocr_result']
                ocr_confidence = result.confidence  # Pydantic model attribute
                
                # Confidence indicator
                if ocr_confidence < 0.75:
                    st.warning(f"Low OCR confidence: {ocr_confidence:.0%} - Please review and edit")
                else:
                    st.success(f"OCR confidence: {ocr_confidence:.0%}")
                
                # Initialize OCR text in session state
                if 'ocr_edit_text' not in st.session_state:
                    st.session_state['ocr_edit_text'] = result.text
                
                # Symbol reference for HITL editing
                st.info("**Common OCR mistakes:** Replace € with ∈, ? with ², add missing = signs")
                
                with st.expander("Symbol Reference", expanded=False):
                    st.markdown("""
                    | Symbol | Type | Symbol | Type |
                    |--------|------|--------|------|  
                    | π | `pi` or π | = | type `=` |
                    | ² | `^2` or ² | ³ | `^3` or ³ |
                    | √ | `sqrt()` | ∈ | type `in` |
                    | ≤ | `<=` | ≥ | `>=` |
                    
                    Just edit the text directly - you can type or paste Unicode symbols!
                    """)
                
                # Editable text area (HITL)
                problem_text = st.text_area(
                    "Extracted text (edit if needed):",
                    value=st.session_state['ocr_edit_text'],
                    height=150,
                    help="Review and correct any OCR errors before solving"
                )
                
                # Update session state when user types
                st.session_state['ocr_edit_text'] = problem_text
                
                solve_button = st.button("✅ Confirm & Solve", type="primary", use_container_width=True)
        else:
            solve_button = False
    
    # ========== AUDIO INPUT ==========
    elif input_mode == "Audio":
        st.info("🎤 Click the microphone button below to start recording your problem.")
        
        audio_recording = st.audio_input("Record your math problem")
        
        if audio_recording is not None:
            # Auto-transcribe as soon as recording is available
            with st.spinner("Transcribing with Whisper..."):
                try:
                    audio_bytes = audio_recording.getvalue()
                    result = audio_proc.transcribe_bytes(audio_bytes, suffix=".wav")
                    st.session_state['asr_result'] = result
                except Exception as e:
                    st.error(f"Transcription failed: {e}")
            
        # Show transcription result and allow editing
        if 'asr_result' in st.session_state:
            result = st.session_state['asr_result']
            
            st.success("✅ Transcription complete — review and edit if needed")
            
            # Editable text area (HITL)
            problem_text = st.text_area(
                "Transcribed text (edit if needed):",
                value=result.text if hasattr(result, 'text') else result.get('text', ''),
                height=150,
                help="Review and correct any transcription errors before solving"
            )
            
            solve_button = st.button("✅ Confirm & Solve", type="primary", use_container_width=True)
        else:
            solve_button = False

# ========== PROCESS AND DISPLAY RESULTS ==========
if solve_button and problem_text:
    with col_viz:
        st.markdown("### 🔄 Live Processing")
        status_placeholder = st.empty()
        trace_placeholder = st.empty()
    
    with status_placeholder:
        with st.spinner("🤖 Running agent pipeline..."):
            try:
                result = orch.process(problem_text)
                st.session_state['last_result'] = result
                
                # Store in episodic memory
                memory.store_solution(
                    problem=problem_text,
                    solution=result.get('current_solution', ''),
                    feedback={
                        'input_mode': input_mode,
                        'status': result['status'],
                        'topic': result.get('topic'),
                        'ocr_confidence': ocr_confidence
                    }
                )
                
                st.success(f"Processing complete: {result['status']}")
            except Exception as e:
                st.error(f"Error: {e}")
                st.stop()
    
    if 'last_result' in st.session_state:
        result = st.session_state['last_result']
        
        # Agent trace
        if show_trace:
            with col_viz:
                with trace_placeholder:
                    render_agent_timeline(result.get('agent_trace', []))
        
        st.markdown("---")
        
        # Solution display
        st.markdown("## Solution")
        
        if result['status'] == 'success':
            # Display solution in a nice container
            with st.container():
                st.success("Solution found!")
                
                # Render solution with proper markdown
                solution_text = result.get('current_solution', 'No solution available')
                st.markdown(solution_text, unsafe_allow_html=False)
                
        elif result['status'] == 'needs_clarification':
            st.warning(f"Clarification Needed: {result.get('clarification_reason', 'Ambiguous input')}")
        elif result['status'] == 'needs_review':
            st.warning(f"Human Review Needed: {result.get('human_trigger_reason', 'Low confidence')}")
            solution_text = result.get('current_solution', '')
            if solution_text:
                st.markdown(solution_text, unsafe_allow_html=False)
        
        # Explanation in expander
        if result.get('explanation'):
            with st.expander("**Step-by-Step Explanation**", expanded=True):
                st.markdown(result['explanation'], unsafe_allow_html=False)
        
        # Web Search Indicator
        if result.get('web_search_used'):
            st.info("🔍 **Web Search Used** - Knowledge base had insufficient information, so we searched the web for you.")
        
        # Citations Section
        if result.get('citations'):
            with st.expander("📚 **Sources & Citations**", expanded=False):
                for i, citation in enumerate(result['citations'], 1):
                    source_type = citation.get('source', 'knowledge_base')
                    if source_type == 'web_search':
                        st.markdown(f"{i}. 🌐 [{citation['title']}]({citation['url']}) - Web Search (Score: {citation.get('score', 0):.2f})")
                    else:
                        st.markdown(f"{i}. 📖 {citation['text'][:100]}... - Knowledge Base (Score: {citation.get('score', 0):.2f})")
        
        # Visualization panels
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            if show_confidence:
                render_confidence_breakdown(result)
        
        with viz_col2:
            if show_context:
                render_retrieved_context(result.get('retrieved_context', []))
        
        # ========== FEEDBACK SECTION (HITL) ==========
        st.markdown("---")
        st.markdown("### Feedback")
        st.caption("Your feedback helps the system learn and improve over time")
        
        # Show warning if needs review
        if result['status'] == 'needs_review':
            st.warning("⚠️ This solution needs human review. Please approve or correct it.")
        
        feedback_col1, feedback_col2, feedback_col3 = st.columns([1, 1, 1])
        
        with feedback_col1:
            if st.button("✅ Approve", use_container_width=True, type="primary"):
                # Store approval in feedback store
                feedback_store.add_review(
                    problem=problem_text,
                    solution=result.get('current_solution', ''),
                    verification_confidence=result.get('confidence', 0),
                    user_approved=True,
                    user_comments=None,
                    metadata={'status': result['status']}
                )
                st.success("✅ Solution approved! Stored for future learning.")
                st.balloons()
        
        with feedback_col2:
            if st.button("❌ Incorrect", use_container_width=True):
                st.session_state['show_correction'] = True
        
        with feedback_col3:
            if st.button("⚠️ Needs Clarification", use_container_width=True):
                st.session_state['show_clarification'] = True
        
        # Correction input
        if st.session_state.get('show_correction'):
            st.markdown("#### Provide Correct Solution")
            correction_reason = st.selectbox(
                "What was wrong?",
                ["Wrong formula", "Calculation error", "Misunderstood problem", "Incomplete solution", "Other"]
            )
            correct_solution = st.text_area(
                "Enter the correct solution:",
                height=150,
                placeholder="Provide the correct step-by-step solution..."
            )
            
            col_submit, col_cancel = st.columns([1, 1])
            with col_submit:
                if st.button("Submit Correction", use_container_width=True):
                    if correct_solution.strip():
                        # Store correction in feedback store
                        feedback_store.add_correction(
                            problem=problem_text,
                            incorrect_solution=result.get('current_solution', ''),
                            correct_solution=correct_solution,
                            correction_reason=correction_reason,
                            metadata={'status': result['status']}
                        )
                        
                        # Also store the corrected version in episodic memory
                        memory.store_solution(
                            problem=problem_text,
                            solution=correct_solution,
                            feedback={'correct': True, 'was_corrected': True}
                        )
                        
                        st.success("✅ Correction stored! The system will learn from this.")
                        st.session_state['show_correction'] = False
                        st.rerun()
                    else:
                        st.error("Please provide a correct solution")
            
            with col_cancel:
                if st.button("Cancel", use_container_width=True):
                    st.session_state['show_correction'] = False
                    st.rerun()
        
        # Clarification request
        if st.session_state.get('show_clarification'):
            st.markdown("#### Request Clarification")
            clarification_parts = st.multiselect(
                "Which parts are ambiguous?",
                ["Variables unclear", "Missing constraints", "Unclear operation", "Other"]
            )
            clarified_input = st.text_area(
                "Provide clarified problem:",
                value=problem_text,
                height=100
            )
            
            col_submit, col_cancel = st.columns([1, 1])
            with col_submit:
                if st.button("Submit Clarification", use_container_width=True):
                    if clarified_input.strip():
                        feedback_store.add_clarification(
                            original_problem=problem_text,
                            ambiguous_parts=clarification_parts,
                            clarified_problem=clarified_input,
                            metadata={'status': result['status']}
                        )
                        st.success("✅ Clarification stored!")
                        st.session_state['show_clarification'] = False
                        st.rerun()
                    else:
                        st.error("Please provide clarified problem")
            
            with col_cancel:
                if st.button("Cancel Clarification", use_container_width=True):
                    st.session_state['show_clarification'] = False
                    st.rerun()

# Show similar past problems from memory
with col_viz:
    if not solve_button:
        st.markdown("### Example Problems")
        examples = [
            "Solve: x² - 5x + 6 = 0",
            "Find the derivative of x³ + 2x² - 5x + 1",
            "Calculate the probability of getting 2 heads in 3 coin flips",
            "Find the limit: lim(x→0) sin(x)/x"
        ]
        for example in examples:
            if st.button(f"{example}", use_container_width=True, key=example):
                st.session_state['problem_input'] = example
                # Force switch to Text mode so the input appears
                st.rerun()
