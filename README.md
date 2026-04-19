# Code Assistant Pro

An AI-powered development suite built with Streamlit and the Groq API. Provides 10 AI-driven coding tools through a sleek, modern web dashboard.

---

## Features

- **Fix Errors** — Paste broken code and get a corrected version with a root cause diagnosis
- **Improve Code** — Optimize for performance, readability, security, and testability
- **Generate Code** — Describe what you need and get production-ready, commented code
- **UI Designer** — Generate responsive HTML/CSS/JS UI code with design rationale
- **Code Explainer** — Get structured explanations at beginner, intermediate, or expert level
- **Code Converter** — Translate code between 16 languages with migration notes
- **Doc Generator** — Auto-generate docstrings, README sections, and API reference docs
- **Test Generator** — Create full test suites with edge cases (pytest, Jest, JUnit, and more)
- **Security Audit** — Scan for vulnerabilities, injection flaws, and insecure patterns
- **Multi-model support** — Switch between Llama 3.1 8B, Llama 3 70B, and Llama 3 8B

---

## 1. Executive Summary

**Code Assistant Pro** is an industry-grade, modular AI coding suite built with Python, Streamlit, and the Groq API. It delivers 10 advanced developer tools—including code fixing, improvement, generation, UI design, explanation, conversion, documentation, testing, and security audit—through a modern, animated web dashboard. The platform supports multiple Groq LLMs (Llama 3.1, Llama 3 70B, Llama 3 8B), features a unified blue/void/white theme, and is engineered for production deployment.

---

## 2. Project Overview

**Project Name:** Code Assistant Pro  
**Developer:** Zulkifal Raja  
**Technology Stack:** Python · Streamlit · Groq API · Custom CSS  
**AI Models:** Llama 3.1 8B, Llama 3 70B, Llama 3 8B  
**Application Type:** Modular Streamlit Web App  
**Date:** April 2026  
**Version:** v3.0 — Production Ready

### 2.1 Goals & Objectives
- Provide instant, AI-powered assistance for Python and multi-language developers
- Support 10 distinct workflows via a mode-based interface
- Deliver fast, reliable responses using Groq's LLMs
- Offer a professional, animated, and consistent UI/UX
- Ensure modular, maintainable, and extensible architecture

### 2.2 Target Users
- Professional developers and teams
- Students and educators
- Code reviewers and QA engineers
- Anyone needing rapid, high-quality code assistance

---

## 3. Technology Stack

| Layer         | Technology         | Purpose                                      |
|--------------|--------------------|----------------------------------------------|
| Frontend/UI  | Streamlit          | Web interface, layout, widgets, session state |
| Language     | Python 3.10+       | Core logic, scripting, API integration        |
| AI Inference | Groq API           | Ultra-fast LLM inference engine              |
| LLMs         | Llama 3.1, 3 70B   | Fast, powerful, creative code generation      |
| Styling      | Custom CSS         | Glassmorphism, animated UI, color themes      |
| Utilities    | Pygments, pyperclip| Syntax highlighting, clipboard                |
| Config       | dotenv, requests   | Env management, HTTP calls                   |

### 3.1 Dependencies
- streamlit >= 1.32.0
- python-dotenv >= 1.0.0
- requests >= 2.31.0
- Pygments >= 2.17.2
- pyperclip >= 1.8.2

---

## 4. Project Structure

```
code-assistant-pro/
│
├── main.py                  # App entry point, routing, sidebar
├── modules/                 # Feature modules (MVC pattern)
│   ├── home/                # Dashboard
│   ├── error_fix/           # Fix Errors
│   ├── code_improve/        # Improve Code
│   ├── code_generate/       # Generate Code
│   ├── ui_design/           # UI Designer
│   ├── code_explain/        # Code Explainer
│   ├── code_convert/        # Code Converter
│   ├── doc_gen/             # Doc Generator
│   ├── test_gen/            # Test Generator
│   └── security_analyzer/   # Security Audit
├── core/
│   ├── config.py            # Loads env vars, defines supported models
│   └── llm_handler.py       # Groq API wrapper
├── assets/
│   └── styles.css           # Custom UI styling
├── utils/
│   └── helpers.py           # Shared helpers (parsing, display)
├── .streamlit/
│   └── config.toml          # Streamlit server config
├── requirements.txt
├── .env                     # (Not committed) Groq API key
└── README.md
```

---

## 5. Features & Functionality

### 5.1 Fix Errors
- Paste broken code, select error type, get corrected code + root cause diagnosis

### 5.2 Improve Code
- Refactor for performance, readability, security, and testability
- Select improvement goals via checkboxes

### 5.3 Generate Code
- Describe requirements, pick language/complexity/model, get production-ready code

### 5.4 UI Designer
- Generate responsive UI code for multiple frameworks with design rationale
- Choose presets, style, theme, and framework

### 5.5 Code Explainer
- Paste code, get multi-level, beginner-friendly explanations

### 5.6 Code Converter
- Translate code between 16+ languages, preserving logic and idioms
- Optionally preserve comments/docstrings

### 5.7 Doc Generator
- Auto-generate docstrings (Google/NumPy/RST), README, API docs, inline comments

### 5.8 Test Generator
- Create full test suites (pytest, Jest, JUnit, etc.) with edge cases and coverage notes

### 5.9 Security Audit
- Scan code for vulnerabilities, insecure patterns, and get recommended fixes
- Select vulnerability categories and severity

### 5.10 Home Dashboard
- Animated feature grid, quick start guide, and model count

---

## 6. UI / UX Design
- Full glassmorphism dark theme (blue/void/white)
- Animated backgrounds, hero banners, and feature cards
- Sidebar navigation, model selector, and session stats
- Consistent accent colors and modern typography (Google Fonts: Oxanium, Fira Code)
- Responsive layout for all modules

---

## 7. Security & Best Practices
- API key loaded from .env (never exposed in UI)
- No eval/exec used; code is only displayed, not executed
- Session state isolation for each user
- Input validation and error handling throughout
- Recommended: keep .env and users.json out of version control

---

## 8. Setup & Deployment

### 8.1 Local Development
1. Clone the repo
2. Create a `.env` file with your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   streamlit run main.py
   ```
5. Open in browser: [http://localhost:8501](http://localhost:8501)

### 8.2 Cloud Deployment
- **Streamlit Cloud:**
  - Push to GitHub, connect repo, set `GROQ_API_KEY` as a secret
  - App auto-deploys at `.streamlit.app` URL
- **Docker:**
  - Add Dockerfile, expose port 8501, set env vars
- **Other Clouds:**
  - Railway, Render, AWS, GCP, Azure supported (see Streamlit docs)

---

## 9. Usage Workflow
1. Select a default model in the sidebar
2. Choose a tool from the navigation menu
3. Paste code or describe your task
4. Configure options (language, complexity, etc.)
5. Submit and receive results instantly
6. Download code, explanations, or test suites as needed

---

## 10. Future Enhancements
- Cloud-based user database (e.g., Supabase, Firebase)
- Conversation export (PDF/Markdown)
- Multi-language support for all modes
- File upload for .py and other code files
- Usage analytics dashboard
- API usage tracker

---

## 11. Credits
- **Developer:** Zulkifal Raja
- **Year:** 2026
- **Confidential — For academic/industry submission only**

---

## 12. License
This project is confidential and intended for academic/industry submission. Not for public distribution.

---

## Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/code-assistant-pro.git
   cd code-assistant-pro
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API key** — create a `.env` file:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the app**
   ```bash
   streamlit run main.py
   ```

---

## Requirements

- Python 3.10+
- `streamlit >= 1.32.0`
- `requests`
- `python-dotenv`
- `Pygments`
- `pyperclip`

All dependencies are listed in `requirements.txt`.

---

## Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| AI Inference | Groq API |
| Models | Llama 3.1 8B, Llama 3 70B, Llama 3 8B |
| Language | Python 3.10+ |

---

## Notes

- Each module is fully independent using an MVC pattern
- The app reads `GROQ_API_KEY` from environment variables or a `.env` file
- Code outputs use Streamlit's native code renderer for a VS Code-like experience
- All explanation and code outputs are cleanly separated into labelled tabs
