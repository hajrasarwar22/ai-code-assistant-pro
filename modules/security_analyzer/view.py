import streamlit as st
from core.llm_handler import LLMHandler
from core.config import GROQ_MODELS

VULN_CATEGORIES = [
    "All Vulnerabilities",
    "Injection (SQL, Command, XSS)",
    "Authentication & Authorization",
    "Insecure Data Handling",
    "Cryptographic Issues",
    "Dependency/Import Risks",
    "Input Validation",
    "Sensitive Data Exposure",
]

LANG_SLUG = {
    "Python": "python", "JavaScript": "javascript", "TypeScript": "typescript",
    "PHP": "php", "Java": "java", "Go": "go", "Ruby": "ruby",
    "C++": "cpp", "Other": "text"
}


def _security_audit(code, lang, categories, severity_filter, llm_handler):
    cat_str = ", ".join(categories) if categories else "all vulnerability types"
    lang_slug = LANG_SLUG.get(lang, "text")
    prompt = [
        {
            "role": "system",
            "content": (
                f"You are a senior application security engineer (AppSec). "
                f"Perform a thorough security audit of the following {lang} code. "
                f"Focus on: {cat_str}. "
                f"Only report issues of {severity_filter} severity or higher. "
                "For each issue found, provide: "
                "1. SEVERITY (Critical/High/Medium/Low) "
                "2. VULNERABILITY TYPE "
                "3. AFFECTED LINE/SECTION "
                "4. DESCRIPTION of the risk "
                "5. RECOMMENDED FIX with corrected code snippet. "
                "End with an overall security score out of 10 and a summary."
            ),
        },
        {
            "role": "user",
            "content": f"Audit this {lang} code:\n\n```{lang_slug}\n{code}\n```",
        },
    ]
    return llm_handler.ask(prompt, temperature=0.1, max_tokens=2048)


def security_view():
    st.markdown("""
    <div class="hero hero-blue">
        <div class="hero-title">🔵 Security Audit</div>
        <div class="hero-sub">Scan code for vulnerabilities — injection, auth flaws, insecure patterns & more</div>
    </div>
    """, unsafe_allow_html=True)

    sc1, sc2 = st.columns(2)
    with sc1:
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;
            color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
            margin-bottom:.4rem;">◈ &nbsp;Minimum Severity</div>""", unsafe_allow_html=True)
        severity = st.selectbox("sev", ["Low (show all)", "Medium", "High", "Critical only"],
                                label_visibility="hidden", key="sec_sev")
        sev_label = severity.split(" ")[0]

    with sc2:
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;
            color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
            margin-bottom:.4rem;">◈ &nbsp;Language</div>""", unsafe_allow_html=True)
        lang = st.selectbox("lang", list(LANG_SLUG.keys()),
                            label_visibility="hidden", key="sec_lang")

    st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;
        color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
        margin-bottom:.4rem;margin-top:.5rem;">
        ◈ &nbsp;Vulnerability Categories to Check</div>""", unsafe_allow_html=True)
    categories = st.multiselect("cats", VULN_CATEGORIES,
                                default=["All Vulnerabilities"],
                                label_visibility="hidden", key="sec_cats")

    with st.form("security_form"):
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;
            color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
            margin-bottom:.4rem;">◈ &nbsp;Code to Audit</div>""", unsafe_allow_html=True)
        code = st.text_area("code", height=250,
                            placeholder="# paste the code to audit — routes, auth handlers, DB queries...",
                            label_visibility="hidden")

        c1, c2 = st.columns([3, 1])
        with c2:
            st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;
                color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
                margin-bottom:.4rem;">◈ &nbsp;Model</div>""", unsafe_allow_html=True)
            model_options = GROQ_MODELS
            default_model = st.session_state.get("default_model", GROQ_MODELS[0])
            try:
                idx = model_options.index(default_model)
            except ValueError:
                idx = 0
            model = st.selectbox("model", model_options, index=idx, label_visibility="hidden")

        submitted = st.form_submit_button("🔒 Run Security Audit")

    if submitted and code:
        llm = LLMHandler(model)
        with st.spinner("Scanning for vulnerabilities..."):
            result = _security_audit(code, lang, categories, sev_label, llm)

        st.markdown("""
        <div style="background:rgba(220,38,38,.08);border:1px solid rgba(220,38,38,.25);
            border-radius:8px;padding:.7rem 1rem;margin:.8rem 0;
            font-family:'Fira Code',monospace;font-size:.72rem;color:#FCA5A5;">
            ⚠ AI-assisted audit — always verify manually or use SAST tools.
        </div>
        """, unsafe_allow_html=True)

        t1, t2 = st.tabs(["🔒 Audit Report", "📄 Audited Code"])

        with t1:
            st.markdown(f"""<div class="rh">
                <div class="rb rb-r"></div>
                <span class="rl">Security Audit Report</span>
                <span class="badge br">{lang}</span>
                <span class="badge br">min: {sev_label}</span>
            </div>""", unsafe_allow_html=True)
            st.markdown(result)

        with t2:
            st.markdown("""<div class="rh">
                <div class="rb rb-r"></div>
                <span class="rl">Audited Code</span>
            </div>""", unsafe_allow_html=True)
            st.code(code, language=LANG_SLUG.get(lang, "text"))

    elif submitted and code == "":
        st.markdown('<div class="ie">⚠ Please paste code to audit.</div>',
                    unsafe_allow_html=True)
