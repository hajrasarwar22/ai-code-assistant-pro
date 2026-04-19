import streamlit as st
from core.llm_handler import LLMHandler
from core.config import GROQ_MODELS
from .controller import handle_ui_design
from utils.helpers import syntax_highlight, parse_structured_response

PRESETS = [
    "Custom...", "Login / Auth Page", "Admin Dashboard", "Landing Page",
    "Data Table with Filters", "Settings Panel", "Chat Interface",
    "E-commerce Product Page", "Portfolio Page", "Pricing Page"
]

STYLES = ["Minimal", "Modern", "Glassmorphism", "Neumorphism", "Brutalist", "Retro"]
THEMES = ["Dark", "Light", "Both"]
FRAMEWORKS = ["Plain HTML/CSS", "Tailwind CSS", "Bootstrap 5", "React + Tailwind", "Vue 3"]


def ui_design_view():

    st.markdown(
        """
        <div class="hero hero-blue">
            <div class="hero-title">🔵 UI Designer</div>
            <div class="hero-sub">
                Describe your UI → get responsive, styled code with design rationale
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """<div style="font-family:'Fira Code',monospace;font-size:.63rem;
        color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
        margin-bottom:.45rem;">◈ &nbsp;Quick Preset</div>""",
        unsafe_allow_html=True,
    )

    preset = st.selectbox(
        "preset",
        PRESETS,
        label_visibility="hidden",
        key="ui_preset"
    )

    pc1, pc2, pc3 = st.columns(3)

    with pc1:
        st.markdown(
            """<div style="font-family:'Fira Code',monospace;font-size:.63rem;
            color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
            margin-bottom:.4rem;">◈ &nbsp;Design Style</div>""",
            unsafe_allow_html=True,
        )
        style_pref = st.selectbox("style", STYLES, label_visibility="hidden", key="ui_style")

    with pc2:
        st.markdown(
            """<div style="font-family:'Fira Code',monospace;font-size:.63rem;
            color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
            margin-bottom:.4rem;">◈ &nbsp;Theme</div>""",
            unsafe_allow_html=True,
        )
        theme_pref = st.selectbox("theme", THEMES, label_visibility="hidden", key="ui_theme")

    with pc3:
        st.markdown(
            """<div style="font-family:'Fira Code',monospace;font-size:.63rem;
            color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
            margin-bottom:.4rem;">◈ &nbsp;Framework</div>""",
            unsafe_allow_html=True,
        )
        fw_pref = st.selectbox("framework", FRAMEWORKS, label_visibility="hidden", key="ui_fw")

    with st.form("ui_design_form"):

        st.markdown(
            """<div style="font-family:'Fira Code',monospace;font-size:.63rem;
            color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
            margin-bottom:.4rem;">◈ &nbsp;Describe Your UI</div>""",
            unsafe_allow_html=True,
        )

        default_idea = "" if preset == "Custom..." else preset

        user_idea = st.text_area(
            "idea",
            height=140,
            placeholder="e.g. A dark-themed admin dashboard with sidebar, KPI cards, charts...",
            value=default_idea,
            label_visibility="hidden",
        )

        c1, c2 = st.columns([3, 1])

        with c2:
            st.markdown(
                """<div style="font-family:'Fira Code',monospace;font-size:.63rem;
                color:#4B6280;letter-spacing:.16em;text-transform:uppercase;
                margin-bottom:.4rem;">◈ &nbsp;Model</div>""",
                unsafe_allow_html=True,
            )

            model_options = GROQ_MODELS
            default_model = st.session_state.get("default_model", GROQ_MODELS[0])

            try:
                idx = model_options.index(default_model)
            except ValueError:
                idx = 0

            model = st.selectbox(
                "model",
                model_options,
                index=idx,
                label_visibility="hidden",
            )

        add_animations = st.checkbox("Include CSS animations", value=True)
        add_responsive = st.checkbox("Make responsive (mobile-first)", value=True)

        submitted = st.form_submit_button("◐ Generate UI")

    if submitted and user_idea:

        enriched = (
            f"{user_idea}\n\n"
            f"Style: {style_pref}, Theme: {theme_pref}, "
            f"Framework: {fw_pref}, Animations: {add_animations}, Responsive: {add_responsive}"
        )

        llm = LLMHandler(model)

        with st.spinner("Designing UI..."):

            st.markdown(
                """
                <div style="display:flex;align-items:center;gap:.8rem;
                font-family:'Fira Code',monospace;font-size:.76rem;
                color:#3B82F6;padding:.7rem 0;">
                <div class="ti"><span></span><span></span><span></span></div>
                Generating UI layout...
                </div>
                """,
                unsafe_allow_html=True,
            )

            result = handle_ui_design(enriched, model, llm)

        code_part, notes_part = parse_structured_response(result)

        st.markdown(
            f"""
            <div style="display:flex;gap:1.2rem;flex-wrap:wrap;margin:.8rem 0 .3rem;
            font-family:'Fira Code',monospace;font-size:.65rem;
            color:#4B6280;letter-spacing:.1em;">
            <span>STYLE <span style="color:#3B82F6;">{style_pref.upper()}</span></span>
            <span>THEME <span style="color:#3B82F6;">{theme_pref.upper()}</span></span>
            <span>FW <span style="color:#3B82F6;">{fw_pref.upper()}</span></span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        t1, t2 = st.tabs(["◐ UI Code", "💡 Design Notes"])

        with t1:
            st.markdown(
                """<div class="rh"><div class="rb rb-b"></div>
                <span class="rl">Generated UI Code</span></div>""",
                unsafe_allow_html=True,
            )

            st.markdown(
                syntax_highlight(code_part, language="html"),
                unsafe_allow_html=True,
            )

        with t2:
            st.markdown(
                """<div class="rh"><div class="rb rb-b"></div>
                <span class="rl">Design Notes</span></div>""",
                unsafe_allow_html=True,
            )
            st.write(notes_part)

    elif submitted and not user_idea:
        st.markdown(
            '<div class="ie">⚠ Please describe the UI you want to generate.</div>',
            unsafe_allow_html=True,
        )
