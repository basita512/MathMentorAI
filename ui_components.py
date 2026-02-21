"""Agent timeline visualization component."""
import streamlit as st
from typing import List, Dict

def render_agent_timeline(agent_trace: List[Dict]):
    """
    Render real-time agent execution timeline.
    
    Args:
        agent_trace: List of agent execution events
    """
    st.markdown("### 🤖 Agent Execution Timeline")
    
    if not agent_trace:
        st.info("⏳ Waiting for agents to start...")
        return
    
    # Group traces by agent
    agent_groups = {}
    for trace in agent_trace:
        agent_name = trace.get('agent', 'unknown')
        if agent_name not in agent_groups:
            agent_groups[agent_name] = []
        agent_groups[agent_name].append(trace)
    
    # Display timeline
    for agent_name, traces in agent_groups.items():
        started = any(t.get('status') == 'started' for t in traces)
        completed = any(t.get('status') == 'completed' for t in traces)
        
        if completed:
            status_icon = "✅"
            status_color = "green"
        elif started:
            status_icon = "🔄"
            status_color = "blue"
        else:
            status_icon = "⏸️"
            status_color = "gray"
        
        confidence = None
        for t in traces:
            if 'confidence' in t:
                confidence = t['confidence']
        
        start_time = None
        end_time = None
        for t in traces:
            if t.get('status') == 'started' and 'timestamp' in t:
                start_time = t['timestamp']
            if t.get('status') == 'completed' and 'timestamp' in t:
                end_time = t['timestamp']
        
        duration = None
        if start_time and end_time:
            duration = end_time - start_time
        
        with st.expander(f"{status_icon} **{agent_name.upper()}**", expanded=True):
            cols = st.columns([2, 1, 1])
            
            with cols[0]:
                st.caption(f"Status: :{status_color}[{('Running' if started and not completed else 'Completed' if completed else 'Pending')}]")
            
            with cols[1]:
                if confidence is not None:
                    st.caption(f"Confidence: **{confidence:.0%}**")
                    st.progress(confidence)
            
            with cols[2]:
                if duration is not None:
                    st.caption(f"Duration: **{duration:.2f}s**")


def render_confidence_breakdown(state: Dict):
    """Render confidence score breakdown visualization."""
    st.markdown("### 📊 Confidence Breakdown")
    
    confidences = {}
    for trace in state.get('agent_trace', []):
        if 'confidence' in trace and trace.get('status') == 'completed':
            confidences[trace['agent']] = trace['confidence']
    
    if state.get('verification_confidence') is not None:
        confidences['verification'] = state['verification_confidence']
    
    if not confidences:
        st.info("No confidence scores available yet")
        return
    
    def get_color(conf):
        if conf >= 0.8:
            return "green"
        elif conf >= 0.6:
            return "orange"
        else:
            return "red"
    
    for agent, conf in confidences.items():
        col1, col2, col3 = st.columns([2, 3, 1])
        
        with col1:
            st.markdown(f"**{agent.capitalize()}**")
        
        with col2:
            st.progress(conf)
        
        with col3:
            color = get_color(conf)
            st.markdown(f":{color}[{conf:.0%}]")
    
    if confidences:
        overall = sum(confidences.values()) / len(confidences)
        st.markdown("---")
        st.markdown(f"**Overall Confidence:** :{get_color(overall)}[**{overall:.0%}**]")


def render_retrieved_context(retrieved_context: List[Dict]):
    """Render retrieved RAG context with scores."""
    st.markdown("### 📚 Retrieved Knowledge")
    
    if not retrieved_context:
        st.info("No context retrieved yet")
        return
    
    for i, ctx in enumerate(retrieved_context, 1):
        if isinstance(ctx, dict):
            score = ctx.get('score', ctx.get('hybrid_score', 0))
            text = ctx.get('text', str(ctx))
            metadata = ctx.get('metadata', {})
        else:
            score = 0
            text = str(ctx)
            metadata = {}
        
        if score > 0.015:
            score_color = "green"
        elif score > 0.010:
            score_color = "orange"
        else:
            score_color = "red"
        
        with st.expander(f"📄 Document {i} (:{score_color}[score: {score:.4f}])", expanded=(i == 1)):
            st.markdown(f"**Type:** {metadata.get('type', 'unknown')}")
            st.markdown(f"**Relevance Score:** {score:.4f}")
            st.markdown("**Content:**")
            st.text(text)
