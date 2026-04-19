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

## Project Structure

```
code-assistant-pro/
│
├── main.py                  # App entry point, routing, sidebar
│
├── modules/                 # Feature modules (MVC pattern)
│   ├── home/
│   ├── error_fix/
│   ├── code_improve/
│   ├── code_generate/
│   ├── ui_design/
│   ├── code_explain/
│   ├── code_convert/
│   ├── doc_gen/
│   ├── test_gen/
│   └── security_analyzer/
│
├── core/
│   ├── config.py            # Loads env vars, defines supported models
│   └── llm_handler.py       # Groq API wrapper
│
├── assets/
│   └── styles.css           # Custom UI styling
│
├── utils/
│   └── helpers.py           # Shared helpers (parsing, display)
│
├── .streamlit/
│   └── config.toml          # Streamlit server config
│
├── requirements.txt
└── README.md
```

---

## Deploy on Streamlit Cloud

1. **Fork or push this repo to GitHub**

2. **Go to [share.streamlit.io](https://share.streamlit.io)** and sign in

3. **Create a new app:**
   - Repository: your GitHub repo
   - Branch: `main`
   - Main file: `main.py`

4. **Add your secret:**
   - In the Streamlit Cloud dashboard, go to **Settings → Secrets**
   - Add:
     ```toml
     GROQ_API_KEY = "your_groq_api_key_here"
     ```

5. **Click Deploy** — your app will be live at a `.streamlit.app` URL

> Get a free Groq API key at [console.groq.com](https://console.groq.com)

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
