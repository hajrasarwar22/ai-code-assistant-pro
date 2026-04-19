import streamlit as st
from core.llm_handler import LLMHandler
from core.config import GROQ_MODELS
from utils.helpers import parse_code_and_notes

TEST_FRAMEWORKS = {
    "Python": ["pytest", "unittest", "doctest"],
    "JavaScript": ["Jest", "Mocha + Chai", "Jasmine"],
    "TypeScript": ["Jest", "Vitest", "Jasmine"],
    "Java": ["JUnit 5", "TestNG"],
    "Go": ["testing (stdlib)", "testify"],
    "Other": ["Generic unit tests"],
}

LANG_SLUG = {
    "Python": "python", "JavaScript": "javascript", "TypeScript": "typescript",
    "Java": "java", "Go": "go", "Other": "text"
}


def _generate_tests(code, lang, framework, cover_edge, cover_mock, llm_handler):
    extras = []
    if cover_edge:
        extras.append("edge cases and boundary values")
    if cover_mock:
        extras.append("mocks and stubs for dependencies")
    extra_str = f"Also include: {', '.join(extras)}." if extras else ""

    lang_slug = LANG_SLUG.get(lang, "text")
    prompt = [
        {
            "role": "system",
            "content": (
                f"You are a senior QA engineer specializing in {lang}. "
                f"Generate comprehensive {framework} unit tests for the following code. {extra_str} "
                "Include: happy path tests, failure/error tests, and descriptive test names. "
                "Add comments explaining what each test validates.\n"
                "Respond in EXACTLY this format — no deviations:\n\n"
                f"```{lang_slug}\n"
                "<test code only here>\n"
                "```\n\n"
                "**Test Coverage Notes:**\n"
                "<briefly describe what is covered and any edge cases>"
            ),
        },
        {
            "role": "user",
            "content": f"Generate {framework} tests for:\n\n```{lang_slug}\n{code}\n```",
        },
    ]
    return llm_handler.ask(prompt, temperature=0.2, max_tokens=2048)


def test_gen_view():
    st.markdown("""
    <div class="hero hero-blue">
        <div class="hero-title">🔵 Test Generator</div>
        <div class="hero-sub">Paste any function or class → get full test suite with edge cases</div>
    </div>
    """, unsafe_allow_html=True)

    tc1, tc2 = st.columns(2)
    with tc1:
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;
            color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
            margin-bottom:.4rem;">◈ &nbsp;Language</div>""", unsafe_allow_html=True)
        lang = st.selectbox("lang", list(TEST_FRAMEWORKS.keys()),
                            label_visibility="hidden", key="test_lang")

    with tc2:
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;
            color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
            margin-bottom:.4rem;">◈ &nbsp;Test Framework</div>""", unsafe_allow_html=True)
        fw = st.selectbox("fw", TEST_FRAMEWORKS.get(lang, ["Generic"]),
                          label_visibility="hidden", key="test_fw")

    with st.form("test_gen_form"):
        st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.63rem;
            color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
            margin-bottom:.4rem;">◈ &nbsp;Code to Test</div>""", unsafe_allow_html=True)
        code = st.text_area("code", height=230,
                            placeholder="# paste functions or classes to generate tests for...",
                            label_visibility="hidden")

        oc1, oc2, oc3 = st.columns(3)
        with oc1:
            cover_edge = st.checkbox("Edge cases", value=True)
        with oc2:
            cover_mock = st.checkbox("Mocks/stubs", value=False)
        with oc3:
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

        submitted = st.form_submit_button("🧪 Generate Tests")

    if submitted and code:
        llm = LLMHandler(model)
        with st.spinner("Generating test suite..."):
            result = _generate_tests(code, lang, fw, cover_edge, cover_mock, llm)

        test_code, coverage_notes = parse_code_and_notes(result)
        lang_slug = LANG_SLUG.get(lang, "text")

        t1, t2 = st.tabs(["🧪 Test Code", "📋 Coverage Notes"])

        with t1:
            st.markdown(f"""<div class="rh">
                <div class="rb rb-g"></div>
                <span class="rl">Generated Tests</span>
                <span class="badge bg">{fw}</span>
                {"<span class='badge bg'>+ edge cases</span>" if cover_edge else ""}
                {"<span class='badge bg'>+ mocks</span>" if cover_mock else ""}
            </div>""", unsafe_allow_html=True)
            st.code(test_code, language=lang_slug)

        with t2:
            st.markdown("""<div class="rh">
                <div class="rb rb-g"></div>
                <span class="rl">What's Covered</span>
            </div>""", unsafe_allow_html=True)
            st.markdown(coverage_notes)

        with st.expander("📄 View original code"):
            st.code(code, language=lang_slug)

    elif submitted and not code:
        st.markdown('<div class="ie">⚠ Please paste code to generate tests for.</div>',
                    unsafe_allow_html=True)
