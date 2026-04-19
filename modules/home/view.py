import streamlit as st
from core.config import GROQ_MODELS  # Optional - for displaying model count


def home_view():
    # Hero
    st.markdown("""
    <div class="hero hero-blue">
      <div class="hero-title">Code Assistant Pro</div>
      <div class="hero-sub">AI Development Suite — 10 tools powered by Groq</div>
    </div>
    """, unsafe_allow_html=True)

    # Feature grid
    st.markdown(f"""
    <div style="font-family:'Fira Code',monospace;font-size:.65rem;color:#4B6280;
        letter-spacing:.16em;text-transform:uppercase;margin-bottom:.7rem;">
        ◈ &nbsp;Available Tools | {len(GROQ_MODELS)} Models Available
    </div>

    <div class="feat-grid">

      <div class="feat-card" style="--accent-color:#2563EB;">
        <div style="position:absolute;top:0;left:0;right:0;height:2px;background:#2563EB;border-radius:2px 2px 0 0;"></div>
        <span class="feat-ic">🔵</span>
        <div class="feat-nm">Fix Errors</div>
        <div class="feat-ds">Diagnose and repair broken code with root cause analysis and highlighted diffs.</div>
      </div>

      <div class="feat-card" style="--accent-color:#2563EB;">
        <div style="position:absolute;top:0;left:0;right:0;height:2px;background:#2563EB;border-radius:2px 2px 0 0;"></div>
        <span class="feat-ic">🔵</span>
        <div class="feat-nm">Improve Code</div>
        <div class="feat-ds">Refactor for performance, readability, security and testability simultaneously.</div>
      </div>

      <div class="feat-card" style="--accent-color:#2563EB;">
        <div style="position:absolute;top:0;left:0;right:0;height:2px;background:#2563EB;border-radius:2px 2px 0 0;"></div>
        <span class="feat-ic">🔵</span>
        <div class="feat-nm">Generate Code</div>
        <div class="feat-ds">Generate production-ready code in any language from plain English descriptions.</div>
      </div>

      <div class="feat-card" style="--accent-color:#2563EB;">
        <div style="position:absolute;top:0;left:0;right:0;height:2px;background:#2563EB;border-radius:2px 2px 0 0;"></div>
        <span class="feat-ic">🔵</span>
        <div class="feat-nm">UI Designer</div>
        <div class="feat-ds">Design beautiful, responsive UIs with code and rationale for any framework.</div>
      </div>

      <div class="feat-card" style="--accent-color:#2563EB;">
        <div style="position:absolute;top:0;left:0;right:0;height:2px;background:#2563EB;border-radius:2px 2px 0 0;"></div>
        <span class="feat-ic">🔵</span>
        <div class="feat-nm">Code Explainer</div>
        <div class="feat-ds">Get structured, multi-level explanations for any code, tailored to your expertise.</div>
      </div>

      <div class="feat-card" style="--accent-color:#2563EB;">
        <div style="position:absolute;top:0;left:0;right:0;height:2px;background:#2563EB;border-radius:2px 2px 0 0;"></div>
        <span class="feat-ic">🔵</span>
        <div class="feat-nm">Code Converter</div>
        <div class="feat-ds">Convert code between any two languages, preserving logic and idioms.</div>
      </div>

      <div class="feat-card" style="--accent-color:#2563EB;">
        <div style="position:absolute;top:0;left:0;right:0;height:2px;background:#2563EB;border-radius:2px 2px 0 0;"></div>
        <span class="feat-ic">🔵</span>
        <div class="feat-nm">Doc Generator</div>
        <div class="feat-ds">Auto-generate docstrings, API docs, and README sections for any code.</div>
      </div>

      <div class="feat-card" style="--accent-color:#2563EB;">
        <div style="position:absolute;top:0;left:0;right:0;height:2px;background:#2563EB;border-radius:2px 2px 0 0;"></div>
        <span class="feat-ic">🔵</span>
        <div class="feat-nm">Test Generator</div>
        <div class="feat-ds">Generate comprehensive unit tests for any function, class, or module.</div>
      </div>

      <div class="feat-card" style="--accent-color:#2563EB;">
        <div style="position:absolute;top:0;left:0;right:0;height:2px;background:#2563EB;border-radius:2px 2px 0 0;"></div>
        <span class="feat-ic">🔵</span>
        <div class="feat-nm">Security Audit</div>
        <div class="feat-ds">Scan code for vulnerabilities, insecure patterns, and get recommended fixes.</div>
      </div>

    </div>
    """, unsafe_allow_html=True)

    # Getting started
    st.markdown("""
    <div style="margin-top:1.6rem;padding:1.2rem 1.4rem;
        background:var(--panel);border:1px solid #1A2840;border-radius:12px;
        border-left:3px solid #2563EB;">
      <div style="font-family:'Fira Code',monospace;font-size:.65rem;color:#4B6280;
          letter-spacing:.16em;text-transform:uppercase;margin-bottom:.5rem;">◈ Quick Start</div>
      <div style="font-family:'Fira Code',monospace;font-size:.78rem;color:#94A3B8;line-height:1.9;">
        1. Pick a <span style="color:#3B82F6;">Default Model</span> in the sidebar<br>
        2. Choose a <span style="color:#10B981;">tool</span> from the navigation<br>
        3. Paste your code or describe what you need<br>
        4. Hit the action button and get results in seconds
      </div>
    </div>
    """, unsafe_allow_html=True)