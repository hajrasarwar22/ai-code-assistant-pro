import streamlit as st
from core.llm_handler import LLMHandler
from core.config import GROQ_MODELS
from utils.helpers import syntax_highlight

DOC_TYPES = [
    "Docstrings (Google style)",
    "Docstrings (NumPy style)",
    "Docstrings (reStructuredText)",
    "README.md section",
    "API Reference docs",
    "Inline comments",
    "Full module documentation",
]


def _generate_docs(code, doc_type, lang, include_examples, llm_handler):
    prompt = [
        {
            "role": "system",
            "content": (
                f"You are a technical documentation expert. Generate {doc_type} for the following {lang} code. "
                f"{'Include usage examples with sample inputs/outputs.' if include_examples else ''} "
                "Be thorough, accurate, and professional. For README/API docs, use Markdown formatting."
            )
        },
        {
            "role": "user",
            "content": f"Generate documentation for:\n\n```{lang}\n{code}\n```"
        },
    ]

    return llm_handler.ask(prompt, temperature=0.25, max_tokens=2048)


def doc_gen_view():
    # Hero
    st.markdown("""
    <div class="hero hero-blue">
        <div class="hero-title">🔵 Doc Generator</div>
        <div class="hero-sub">Paste any code → auto-generate professional documentation in seconds</div>
    </div>
    """, unsafe_allow_html=True)

    # Top selectors
    dc1, dc2 = st.columns(2)

    with dc1:
        st.markdown("""
        <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Documentation Type
        </div>
        """, unsafe_allow_html=True)

        doc_type = st.selectbox(
            "doctype",
            DOC_TYPES,
            label_visibility="hidden",
            key="doc_type"
        )

    with dc2:
        st.markdown("""
        <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Language
        </div>
        """, unsafe_allow_html=True)

        lang = st.selectbox(
            "lang",
            ["Python", "JavaScript", "TypeScript", "Java", "C++", "Go", "Rust", "PHP", "Ruby", "Other"],
            label_visibility="hidden",
            key="doc_lang"
        )

    # Form
    with st.form("doc_gen_form"):

        st.markdown("""
        <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Your Code
        </div>
        """, unsafe_allow_html=True)

        code = st.text_area(
            "code",
            height=230,
            placeholder="# paste functions, classes, or a full module...",
            label_visibility="hidden"
        )

        c1, c2 = st.columns([3, 1])

        with c1:
            include_examples = st.checkbox("Include usage examples", value=True)

        with c2:
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

        submitted = st.form_submit_button("📝 Generate Docs")

    # Processing
    if submitted and code:
        llm = LLMHandler(model)

        with st.spinner(""):
            st.markdown("""
            <div style="display:flex;align-items:center;gap:.8rem;
                font-family:'Fira Code',monospace;font-size:.76rem;color:#3B82F6;padding:.7rem 0;">
                <div class="ti"><span></span><span></span><span></span></div>
                Generating documentation...
            </div>
            """, unsafe_allow_html=True)

            result = _generate_docs(code, doc_type, lang, include_examples, llm)

        t1, t2 = st.tabs(["📝 Documentation", "📄 Code"])

        with t1:
            st.markdown(f"""
            <div class="rh">
                <div class="rb rb-b"></div>
                <span class="rl">Generated Docs</span>
                <span class="badge bb" style="margin-left:.4rem;">
                    {doc_type.split('(')[0].strip()}
                </span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(result, unsafe_allow_html=True)

        with t2:
            st.markdown("""
            <div class="rh">
                <div class="rb rb-b"></div>
                <span class="rl">Original Code</span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(
                syntax_highlight(code, language=lang.lower()),
                unsafe_allow_html=True
            )

    elif submitted and not code:
        st.markdown(
            '<div class="ie">⚠ Please paste code to document.</div>',
            unsafe_allow_html=True
        )