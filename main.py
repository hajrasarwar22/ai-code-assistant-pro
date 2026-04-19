import streamlit as st

st.write("App loaded!")  # Debug line

st.set_page_config(
    page_title="Code Assistant Pro",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
with open("assets/styles.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ── Lazy imports (only load the selected module) ──────────────────────────────
def _load_view(name):
    if name == "Home":
        from modules.home.view import home_view; return home_view
    elif name == "Fix Errors":
        from modules.error_fix.view import error_fix_view; return error_fix_view
    elif name == "Improve Code":
        from modules.code_improve.view import code_improve_view; return code_improve_view
    elif name == "Generate Code":
        from modules.code_generate.view import code_generate_view; return code_generate_view
    elif name == "UI Designer":
        from modules.ui_design.view import ui_design_view; return ui_design_view
    elif name == "Code Explainer":
        from modules.code_explain.view import code_explain_view; return code_explain_view
    elif name == "Code Converter":
        from modules.code_convert.view import code_convert_view; return code_convert_view
    elif name == "Doc Generator":
        from modules.doc_gen.view import doc_gen_view; return doc_gen_view
    elif name == "Test Generator":
        from modules.test_gen.view import test_gen_view; return test_gen_view
    elif name == "Security Audit":
        from modules.security_analyzer.view import security_view; return security_view

# ── Session defaults ──────────────────────────────────────────────────────────
for k, v in [("theme","dark"), ("default_model","llama2-70b-4096"), ("session_count", 0)]:
    if k not in st.session_state:
        st.session_state[k] = v

# ── Top banner ────────────────────────────────────────────────────────────────
st.markdown("""
<div style="display:flex;align-items:center;gap:1rem;
    padding:.9rem 0 1.4rem;border-bottom:1px solid #1A2840;margin-bottom:1.6rem;">
  <div style="width:40px;height:40px;
      background:linear-gradient(135deg,#1D4ED8,#2563EB);
      border-radius:10px;display:flex;align-items:center;justify-content:center;
      font-size:1.2rem;box-shadow:0 0 24px rgba(37,99,235,.5);">⬡</div>
  <div>
    <div style="font-family:'Oxanium',sans-serif;font-weight:800;font-size:1.35rem;
        letter-spacing:.04em;color:#EDF2F7;">CODE ASSISTANT <span style="color:#3B82F6;">PRO</span></div>
    <div style="font-family:'Fira Code',monospace;font-size:.62rem;color:#4B6280;
        letter-spacing:.18em;text-transform:uppercase;">AI Development Suite</div>
  </div>
  <div style="margin-left:auto;display:flex;align-items:center;gap:.5rem;">
    <span class="pd"></span>
    <span style="font-family:'Fira Code',monospace;font-size:.65rem;color:#4B6280;letter-spacing:.12em;">ONLINE</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
PAGES = [
    "Home",
    "Fix Errors",
    "Improve Code",
    "Generate Code",
    "UI Designer",
    "Code Explainer",
    "Code Converter",
    "Doc Generator",
    "Test Generator",
    "Security Audit",
]

with st.sidebar:
    st.markdown("""
    <div style="font-family:'Fira Code',monospace;font-size:.6rem;letter-spacing:.2em;
        color:#4B6280;text-transform:uppercase;padding-bottom:.8rem;border-bottom:1px solid #1A2840;
        margin-bottom:1rem;">⬡ &nbsp;Navigation</div>
    """, unsafe_allow_html=True)

    menu = st.radio("nav", PAGES, key="nav_radio", label_visibility="hidden")

    st.markdown("<div style='margin:.9rem 0;border-top:1px solid #1A2840;'></div>", unsafe_allow_html=True)

    st.markdown("""<div style="font-family:'Fira Code',monospace;font-size:.6rem;letter-spacing:.18em;
        color:#4B6280;text-transform:uppercase;margin-bottom:.4rem;">Default Model</div>""",
        unsafe_allow_html=True)
    default_model = st.selectbox("model",
        ["llama-3.1-8b-instant", "llama3-70b-8192", "llama3-8b-8192"],
        key="global_model", label_visibility="hidden")
    st.session_state["default_model"] = default_model

    st.markdown("<div style='margin:.9rem 0;border-top:1px solid #1A2840;'></div>", unsafe_allow_html=True)

    # Session counter
    st.session_state["session_count"] += 0  # keep it stable
    st.markdown(f"""
    <div style="font-family:'Fira Code',monospace;font-size:.62rem;color:#4B6280;line-height:2;">
      MODELS &nbsp;<span style="color:#3B82F6;">3</span><br>
      FEATURES &nbsp;<span style="color:#10B981;">10</span><br>
      ENGINE &nbsp;<span style="color:#F59E0B;">GROQ</span>
    </div>""", unsafe_allow_html=True)

    st.markdown("<div style='margin:.9rem 0;border-top:1px solid #1A2840;'></div>", unsafe_allow_html=True)

    if st.button("⇄  Toggle Theme", use_container_width=True):
        st.session_state["theme"] = "light" if st.session_state["theme"] == "dark" else "dark"
        st.rerun()

    st.markdown("""
    <div style="margin-top:1rem;font-family:'Fira Code',monospace;
        font-size:.58rem;color:#1E2D40;letter-spacing:.1em;">
      v3.0 · GROQ INFERENCE · PRO
    </div>""", unsafe_allow_html=True)

# ── Render selected page ──────────────────────────────────────────────────────
view_fn = _load_view(menu)
if view_fn:
    view_fn()
