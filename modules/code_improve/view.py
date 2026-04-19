import streamlit as st
from core.llm_handler import LLMHandler
from core.config import GROQ_MODELS
from .controller import handle_code_improve
from utils.helpers import syntax_highlight


def code_improve_view():
    # Hero
    st.markdown("""
    <div class="hero hero-blue">
        <div class="hero-title">🔵 Improve Code</div>
        <div class="hero-sub">Submit working code → get an optimized, idiomatic, professional version</div>
    </div>
    """, unsafe_allow_html=True)

    # Goal pills
    st.markdown("""
    <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
        letter-spacing:.16em;text-transform:uppercase;margin-bottom:.5rem;">
        ◈ &nbsp;Improvement Goals
    </div>
    """, unsafe_allow_html=True)

    gc1, gc2, gc3, gc4 = st.columns(4)

    with gc1:
        g_perf = st.checkbox("⚡ Performance", value=True)
    with gc2:
        g_read = st.checkbox("📖 Readability", value=True)
    with gc3:
        g_sec = st.checkbox("🔒 Security", value=False)
    with gc4:
        g_test = st.checkbox("🧪 Testability", value=False)

    goals = [
        g for g, flag in [
            ("performance", g_perf),
            ("readability", g_read),
            ("security", g_sec),
            ("testability", g_test)
        ] if flag
    ]

    # Form
    with st.form("code_improve_form"):
        st.markdown("""
        <div style="font-family:'Fira Code',monospace;font-size:.63rem;color:#4B6280;
            letter-spacing:.16em;text-transform:uppercase;margin-bottom:.4rem;">
            ◈ &nbsp;Your Code
        </div>
        """, unsafe_allow_html=True)

        code = st.text_area(
            "code",
            height=220,
            placeholder="# paste the code you want improved...",
            label_visibility="hidden"
        )

        c1, c2 = st.columns([3, 1])

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

        submitted = st.form_submit_button("✦ Improve Code", use_container_width=False)

    # Processing
    if submitted and code:
        llm = LLMHandler(model)

        with st.spinner(""):
            st.markdown("""
            <div style="display:flex;align-items:center;gap:.8rem;
                font-family:'Fira Code',monospace;font-size:.76rem;color:#F59E0B;padding:.7rem 0;">
                <div class="ti">
                    <span style="background:#2563EB"></span>
                    <span style="background:#2563EB"></span>
                    <span style="background:#2563EB"></span>
                </div>
                Refactoring and optimizing...
            </div>
            """, unsafe_allow_html=True)

            result = handle_code_improve(code, model, llm)

        # Goal badges
        if goals:
            badges = "".join([f'<span class="badge ba">{g}</span>' for g in goals])
            st.markdown(f"""
            <div style="margin:.8rem 0 .3rem;">
                <span style="font-family:'Fira Code',monospace;font-size:.62rem;color:#4B6280;
                    letter-spacing:.1em;margin-right:.5rem;">APPLIED:</span>
                {badges}
            </div>
            """, unsafe_allow_html=True)

        # Tabs
        t1, t2 = st.tabs(["✦ Improved Code", "📋 Change Summary"])

        with t1:
            st.markdown("""
            <div class="rh">
                <div class="rb rb-a"></div>
                <span class="rl">Improved Code</span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(syntax_highlight(result, language="python"), unsafe_allow_html=True)

        with t2:
            st.write(result)

    elif submitted and not code:
        st.markdown(
            '<div class="ie">⚠ Please paste your code before submitting.</div>',
            unsafe_allow_html=True
        )