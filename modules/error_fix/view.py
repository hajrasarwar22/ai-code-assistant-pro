import streamlit as st
from core.llm_handler import LLMHandler
from core.config import GROQ_MODELS
from .controller import handle_error_fix
from utils.helpers import parse_code_and_notes


def error_fix_view():
    st.markdown("""
    <div class="hero hero-blue">
        <div class="hero-title">🔵 Fix Code Errors</div>
        <div class="hero-sub">Paste broken code → get corrected code + root cause diagnosis</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
        letter-spacing:.16em;text-transform:uppercase;margin-bottom:.45rem;">
        ◈ &nbsp;Common Error Types
    </div>
    """, unsafe_allow_html=True)

    ec1, ec2, ec3, ec4, ec5 = st.columns(5)
    err_types = {"SyntaxError": ec1, "TypeError": ec2, "KeyError": ec3, "ImportError": ec4, "Other": ec5}

    for name, col in err_types.items():
        with col:
            if st.button(name, key=f"err_{name}", use_container_width=True):
                st.session_state["err_type_selected"] = name

    chosen = st.session_state.get("err_type_selected", "")

    with st.form("error_fix_form"):
        st.markdown("""
        <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Paste Your Broken Code
        </div>
        """, unsafe_allow_html=True)

        code = st.text_area("code", height=220,
                            placeholder="# paste the broken code here...",
                            label_visibility="hidden")

        c1, c2 = st.columns([2, 1])
        with c1:
            st.markdown("""
            <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
                letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
                ◈ &nbsp;Error Description
            </div>
            """, unsafe_allow_html=True)
            error_desc = st.text_input("err_desc", value=chosen,
                                       placeholder="Describe the error or paste the traceback...",
                                       label_visibility="hidden")

        with c2:
            st.markdown("""
            <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
                letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
                ◈ &nbsp;Model
            </div>
            """, unsafe_allow_html=True)
            model_options = GROQ_MODELS
            default_model = st.session_state.get("default_model", GROQ_MODELS[0])
            try:
                idx = model_options.index(default_model)
            except ValueError:
                idx = 0
            model = st.selectbox("model", model_options, index=idx, label_visibility="hidden")

        submitted = st.form_submit_button("⚡ Diagnose & Fix", use_container_width=False)

    if submitted and code:
        llm = LLMHandler(model)
        with st.spinner("Analyzing error pattern and generating fix..."):
            result = handle_error_fix(code, error_desc, model, llm)

        code_part, explanation_part = parse_code_and_notes(result)

        t1, t2 = st.tabs(["🔧 Corrected Code", "📋 Diagnosis & Explanation"])

        with t1:
            st.markdown("""
            <div class="rh">
                <div class="rb rb-r"></div>
                <span class="rl">Corrected Code</span>
                <span class="badge br" style="margin-left:.4rem;">Fixed</span>
            </div>
            """, unsafe_allow_html=True)
            st.code(code_part, language="python")

        with t2:
            st.markdown("""
            <div class="rh">
                <div class="rb rb-b"></div>
                <span class="rl">Root Cause & Explanation</span>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(explanation_part)

    elif submitted and not code:
        st.markdown('<div class="ie">⚠ Please paste your code before submitting.</div>',
                    unsafe_allow_html=True)
