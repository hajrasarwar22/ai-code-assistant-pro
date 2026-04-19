import streamlit as st
from core.llm_handler import LLMHandler
from core.config import GROQ_MODELS
from utils.helpers import parse_code_and_notes

LANGS = [
    "Python", "JavaScript", "TypeScript", "Java", "C++", "C#",
    "Go", "Rust", "PHP", "Ruby", "Swift", "Kotlin",
    "SQL", "Bash", "R", "MATLAB"
]

LANG_SLUG = {
    "Python": "python", "JavaScript": "javascript", "TypeScript": "typescript",
    "Java": "java", "C++": "cpp", "C#": "csharp", "Go": "go", "Rust": "rust",
    "PHP": "php", "Ruby": "ruby", "Swift": "swift", "Kotlin": "kotlin",
    "SQL": "sql", "Bash": "bash", "R": "r", "MATLAB": "matlab"
}


def _convert_code(code, src, dst, preserve_comments, llm_handler):
    dst_slug = LANG_SLUG.get(dst, dst.lower())
    prompt = [
        {
            "role": "system",
            "content": (
                f"You are an expert multilingual programmer. Convert the following {src} code to {dst}. "
                f"Preserve all logic and use idiomatic {dst} patterns. "
                + ("Preserve comments and docstrings." if preserve_comments else "Omit comments.")
                + "\nRespond in EXACTLY this format — no deviations:\n\n"
                f"```{dst_slug}\n"
                "<converted code only here>\n"
                "```\n\n"
                "**Migration Notes:**\n"
                "<key differences, library equivalents, anything the dev should know>"
            )
        },
        {
            "role": "user",
            "content": f"Convert this {src} code to {dst}:\n\n```{LANG_SLUG.get(src, src.lower())}\n{code}\n```"
        },
    ]
    return llm_handler.ask(prompt, temperature=0.2, max_tokens=2048)


def code_convert_view():
    st.markdown("""
    <div class="hero hero-blue">
        <div class="hero-title">🔵 Code Converter</div>
        <div class="hero-sub">Translate code between any two languages — logic preserved</div>
    </div>
    """, unsafe_allow_html=True)

    fc1, arrow_col, fc2 = st.columns([5, 1, 5])
    with fc1:
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;From Language</div>""", unsafe_allow_html=True)
        src_lang = st.selectbox("src", LANGS, index=0, label_visibility="hidden", key="conv_src")

    with arrow_col:
        st.markdown("""<div style="text-align:center;font-size:1.4rem;color:#4B6280;padding-top:1.8rem;">
            →</div>""", unsafe_allow_html=True)

    with fc2:
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;To Language</div>""", unsafe_allow_html=True)
        dst_lang = st.selectbox("dst", LANGS, index=1, label_visibility="hidden", key="conv_dst")

    with st.form("code_convert_form"):
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Source Code</div>""", unsafe_allow_html=True)
        code = st.text_area("code", height=230,
                            placeholder=f"# paste your {src_lang} code here...",
                            label_visibility="hidden")

        c1, c2 = st.columns([3, 1])
        with c1:
            preserve_comments = st.checkbox("Preserve comments & docstrings", value=True)
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

        submitted = st.form_submit_button("🔄 Convert Code", use_container_width=False)

    if submitted and code:
        if src_lang == dst_lang:
            st.markdown('<div class="ie">⚠ Source and target language are the same.</div>',
                        unsafe_allow_html=True)
            return

        llm = LLMHandler(model)
        with st.spinner(f"Converting {src_lang} → {dst_lang}..."):
            result = _convert_code(code, src_lang, dst_lang, preserve_comments, llm)

        code_part, notes_part = parse_code_and_notes(result)
        dst_slug = LANG_SLUG.get(dst_lang, dst_lang.lower())

        t1, t2 = st.tabs([f"🔄 {dst_lang} Code", "📋 Migration Notes"])
        with t1:
            st.markdown("""<div class="rh">
                <div style="width:3px;height:20px;border-radius:2px;background:#0D9488;"></div>
                <span class="rl">Converted Code</span></div>""", unsafe_allow_html=True)
            st.code(code_part, language=dst_slug)

        with t2:
            st.markdown("""<div class="rh">
                <div style="width:3px;height:20px;border-radius:2px;background:#0D9488;"></div>
                <span class="rl">Migration Notes</span></div>""", unsafe_allow_html=True)
            st.markdown(notes_part)

    elif submitted and not code:
        st.markdown('<div class="ie">⚠ Please paste source code to convert.</div>',
                    unsafe_allow_html=True)
