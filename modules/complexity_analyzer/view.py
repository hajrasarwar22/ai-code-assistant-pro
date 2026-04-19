import streamlit as st
from core.llm_handler import LLMHandler
from core.config import GROQ_MODELS


def _analyze_complexity(code, language, llm_handler):
    prompt = [
        {
            "role": "system",
            "content": (
                f"You are a complexity analyst. Analyze the following {language} code for time and space complexity. "
                "Explain Big-O for each function and suggest optimizations."
            )
        },
        {
            "role": "user",
            "content": code
        },
    ]

    return llm_handler.ask(prompt, temperature=0.2, max_tokens=2048)


def complexity_analyzer_view():
    # Hero
    st.markdown("""
    <div class="hero hero-blue">
        <div class="hero-title">🔵 Complexity Analyzer</div>
        <div class="hero-sub">Analyze time and space complexity, get Big-O and optimization tips</div>
    </div>
    """, unsafe_allow_html=True)

    langs = [
        "Python", "JavaScript", "TypeScript", "Java", "C++", "C#",
        "Go", "Rust", "Kotlin", "Swift", "PHP", "Ruby",
        "SQL", "Bash", "MATLAB", "Other"
    ]

    # Form
    with st.form("complexity_form"):

        language = st.selectbox("Language", langs)

        code = st.text_area(
            "Paste code for analysis",
            height=180
        )

        # ✅ FIXED: Using GROQ_MODELS from config
        model_options = GROQ_MODELS
        default_model = st.session_state.get("default_model", GROQ_MODELS[0])
        
        # Safe index lookup
        try:
            idx = model_options.index(default_model)
        except ValueError:
            idx = 0
        
        model = st.selectbox(
            "Model",
            model_options,
            index=idx
        )

        submitted = st.form_submit_button("⚡ Analyze Complexity")

    # Processing
    if submitted and code:
        llm = LLMHandler(model)

        with st.spinner(""):
            st.markdown("""
            <div class='ti ti-green'>⠶⠶⠶ Analyzing complexity...</div>
            """, unsafe_allow_html=True)

            result = _analyze_complexity(code, language, llm)

        st.markdown(f"""
        <div class='rh'>
            <div class='rb rb-g'></div>
            <span class='rl'>Complexity Analysis</span>
            <span class='badge bg' style='margin-left:.4rem;'>{language}</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(result, unsafe_allow_html=True)

    elif submitted and not code:
        st.markdown(
            '<div class="ie">⚠ Please paste code for complexity analysis.</div>',
            unsafe_allow_html=True
        )