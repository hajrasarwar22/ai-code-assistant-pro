import streamlit as st
from core.llm_handler import LLMHandler
from core.config import GROQ_MODELS
from .controller import handle_code_generate
from utils.helpers import syntax_highlight

LANGS = [
    "Python", "JavaScript", "TypeScript", "React", "FastAPI",
    "Flask", "Node.js", "Go", "Rust", "SQL", "Bash",
    "C++", "Java", "Other"
]

COMPLEXITY = [
    "Simple (< 30 lines)",
    "Medium (30–100 lines)",
    "Full module (100+ lines)"
]


def code_generate_view():
    # Hero
    st.markdown("""
    <div class="hero hero-blue">
        <div class="hero-title">🔵 Generate Code</div>
        <div class="hero-sub">Describe what you need → get production-ready, commented code</div>
    </div>
    """, unsafe_allow_html=True)

    # Form
    with st.form("code_generate_form"):

        st.markdown("""
        <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;What should the code do?
        </div>
        """, unsafe_allow_html=True)

        purpose = st.text_area(
            "purpose",
            height=120,
            placeholder="e.g. A function that fetches weather data from an API and returns temperature in Celsius...",
            label_visibility="hidden"
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("""
            <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
                letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
                ◈ &nbsp;Language
            </div>
            """, unsafe_allow_html=True)

            language = st.selectbox("lang", LANGS, label_visibility="hidden")

        with c2:
            st.markdown("""
            <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
                letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
                ◈ &nbsp;Complexity
            </div>
            """, unsafe_allow_html=True)

            complexity = st.selectbox("cplx", COMPLEXITY, label_visibility="hidden")

        with c3:
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

        st.markdown("""
        <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin:.7rem 0 .4rem;">
            ◈ &nbsp;Constraints / Requirements
        </div>
        """, unsafe_allow_html=True)

        constraints = st.text_input(
            "constraints",
            placeholder="e.g. no external libs, async, type hints...",
            label_visibility="hidden"
        )

        include_tests = st.checkbox("Also generate unit tests", value=False)
        include_docs = st.checkbox("Include docstrings", value=True)

        submitted = st.form_submit_button("◎ Generate Code", use_container_width=False)

    # Processing
    if submitted and purpose:
        lang_slug = language.lower().replace(" ", "_").replace("/", "_").replace(".", "").replace("+", "p")

        llm = LLMHandler(model)

        answers = {
            "purpose": purpose,
            "language": language,
            "constraints": constraints,
            "complexity": complexity,
            "include_tests": include_tests,
            "include_docs": include_docs,
        }

        with st.spinner(""):
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:.8rem;
                font-family:'Fira Code',monospace;font-size:.76rem;color:#10B981;padding:.7rem 0;">
                <div class="ti">
                    <span style="background:#2563EB"></span>
                    <span style="background:#2563EB"></span>
                    <span style="background:#2563EB"></span>
                </div>
                Generating {language} code...
            </div>
            """, unsafe_allow_html=True)

            result = handle_code_generate(answers, model, llm)

        # Meta row
        st.markdown(f"""
        <div style="display:flex;gap:1.2rem;flex-wrap:wrap;margin:.8rem 0 .3rem;
            font-family:'Fira Code',monospace;font-size:.65rem;color:#4B6280;letter-spacing:.1em;">
            <span>LANG <span style="color:#10B981;">{language.upper()}</span></span>
            <span>SCOPE <span style="color:#10B981;">{complexity.split('(')[0].strip().upper()}</span></span>
            <span>MODEL <span style="color:#10B981;">{model}</span></span>
        </div>
        """, unsafe_allow_html=True)

        t1, t2 = st.tabs(["◎ Generated Code", "📋 Explanation"])

        with t1:
            st.markdown("""
            <div class="rh">
                <div class="rb rb-g"></div>
                <span class="rl">Generated Code</span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(
                syntax_highlight(result, language=lang_slug),
                unsafe_allow_html=True
            )

        with t2:
            st.write(result)

    elif submitted and not purpose:
        st.markdown(
            '<div class="ie">⚠ Please describe what the code should do.</div>',
            unsafe_allow_html=True
        )