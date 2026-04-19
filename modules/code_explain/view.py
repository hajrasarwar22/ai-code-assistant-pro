import streamlit as st
from core.llm_handler import LLMHandler
from core.config import GROQ_MODELS

LANG_SLUG = {
    "Python": "python", "JavaScript": "javascript", "TypeScript": "typescript",
    "Java": "java", "C++": "cpp", "Go": "go", "Rust": "rust",
    "SQL": "sql", "Bash": "bash", "Other": "text"
}


def _explain_code(code, depth, audience, lang, llm_handler):
    depth_map = {
        "Quick Overview": "Give a brief 3-5 sentence overview.",
        "Detailed Line-by-Line": "Explain each logical block and key line in detail.",
        "Deep Dive (Advanced)": "Provide expert-level analysis including time complexity, design patterns, and improvements.",
    }
    aud_map = {
        "Beginner": "Use simple language, avoid jargon, use analogies.",
        "Intermediate": "Assume basic programming knowledge.",
        "Expert": "Use technical terminology freely.",
    }
    prompt = [
        {
            "role": "system",
            "content": (
                f"You are a world-class code educator. Explain {lang} code clearly. "
                f"{depth_map[depth]} {aud_map[audience]} "
                "Structure your explanation with: Overview, Key Components, Logic Flow, Issues/Improvements."
            )
        },
        {
            "role": "user",
            "content": f"```{LANG_SLUG.get(lang, 'text')}\n{code}\n```"
        },
    ]
    return llm_handler.ask(prompt, temperature=0.3, max_tokens=2048)


def code_explain_view():
    st.markdown("""
    <div class="hero hero-blue">
        <div class="hero-title">🔵 Code Explainer</div>
        <div class="hero-sub">Submit any code → structured explanation at your level</div>
    </div>
    """, unsafe_allow_html=True)

    cc1, cc2, cc3 = st.columns(3)
    with cc1:
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Language</div>""", unsafe_allow_html=True)
        lang = st.selectbox("lang", list(LANG_SLUG.keys()), label_visibility="hidden", key="exp_lang")

    with cc2:
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Explanation Depth</div>""", unsafe_allow_html=True)
        depth = st.selectbox("depth",
                             ["Quick Overview", "Detailed Line-by-Line", "Deep Dive (Advanced)"],
                             label_visibility="hidden", key="exp_depth")

    with cc3:
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Audience Level</div>""", unsafe_allow_html=True)
        audience = st.selectbox("aud", ["Beginner", "Intermediate", "Expert"],
                                index=1, label_visibility="hidden", key="exp_aud")

    with st.form("code_explain_form"):
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Code to Explain</div>""", unsafe_allow_html=True)
        code = st.text_area("code", height=240,
                            placeholder="# paste any code here...",
                            label_visibility="hidden")

        c1, c2 = st.columns([3, 1])
        with c2:
            st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
                letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
                ◈ &nbsp;Model</div>""", unsafe_allow_html=True)
            model_options = GROQ_MODELS
            default_model = st.session_state.get("default_model", GROQ_MODELS[0])
            try:
                idx = model_options.index(default_model)
            except ValueError:
                idx = 0
            model = st.selectbox("model", model_options, index=idx, label_visibility="hidden")

        submitted = st.form_submit_button("🔍 Explain Code", use_container_width=False)

    if submitted and code:
        llm = LLMHandler(model)
        with st.spinner("Analyzing code structure and logic..."):
            result = _explain_code(code, depth, audience, lang, llm)

        t1, t2 = st.tabs(["🔍 Explanation", "📄 Original Code"])

        with t1:
            st.markdown(f"""<div class="rh">
                <div class="rb rb-p"></div>
                <span class="rl">Explanation</span>
                <span class="badge bp" style="margin-left:.4rem;">{depth}</span>
                <span class="badge bp">{audience}</span>
            </div>""", unsafe_allow_html=True)
            st.markdown(result)

        with t2:
            st.markdown("""<div class="rh">
                <div class="rb rb-p"></div>
                <span class="rl">Your Code</span>
            </div>""", unsafe_allow_html=True)
            st.code(code, language=LANG_SLUG.get(lang, "text"))

    elif submitted and not code:
        st.markdown('<div class="ie">⚠ Please paste code to explain.</div>',
                    unsafe_allow_html=True)
