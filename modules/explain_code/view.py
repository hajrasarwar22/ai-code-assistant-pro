import streamlit as st
from core.llm_handler import LLMHandler
from core.config import GROQ_MODELS
from .controller import handle_explain_code
from utils.helpers import syntax_highlight


def explain_code_view():
    # Hero
    st.markdown("""
    <div class="hero hero-blue">
        <div class="hero-title">🔵 Explain Code</div>
        <div class="hero-sub">Paste your code to get a detailed, beginner-friendly explanation</div>
    </div>
    """, unsafe_allow_html=True)

    # Form
    with st.form("explain_code_form"):
        st.markdown("""
        <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Your Code
        </div>
        """, unsafe_allow_html=True)

        code = st.text_area(
            "code",
            height=200,
            placeholder="# paste your code here...",
            label_visibility="hidden"
        )

        st.markdown("""
        <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Model
        </div>
        """, unsafe_allow_html=True)

        # ✅ FIXED: Using GROQ_MODELS from config
        model_options = GROQ_MODELS
        default_model = st.session_state.get("default_model", GROQ_MODELS[0])
        
        # Safe index lookup
        try:
            idx = model_options.index(default_model)
        except ValueError:
            idx = 0
        
        model = st.selectbox(
            "model",
            model_options,
            index=idx,
            label_visibility="hidden"
        )

        submitted = st.form_submit_button("🔍 Explain Code", use_container_width=False)

    # Processing
    if submitted and code:
        llm = LLMHandler(model)

        with st.spinner(""):
            st.markdown("""
            <div style="display:flex;align-items:center;gap:.8rem;
                font-family:'Fira Code',monospace;font-size:.76rem;color:#8B5CF6;padding:.7rem 0;">
                <div class="ti">
                    <span style="background:#2563EB"></span>
                    <span style="background:#2563EB"></span>
                    <span style="background:#2563EB"></span>
                </div>
                Analyzing and explaining code...
            </div>
            """, unsafe_allow_html=True)

            result = handle_explain_code(code, model, llm)

        # Tabs
        t1, t2 = st.tabs(["🔍 Explanation", "📄 Original Code"])

        with t1:
            st.markdown("""
            <div class="rh">
                <div class="rb rb-p"></div>
                <span class="rl">Code Explanation</span>
            </div>
            """, unsafe_allow_html=True)

            st.write(result)

        with t2:
            st.markdown("""
            <div class="rh">
                <div class="rb rb-p"></div>
                <span class="rl">Original Code</span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(
                syntax_highlight(code, language="python"),
                unsafe_allow_html=True
            )

    elif submitted and not code:
        st.markdown(
            '<div class="ie">⚠ Please paste code to explain.</div>',
            unsafe_allow_html=True
        )