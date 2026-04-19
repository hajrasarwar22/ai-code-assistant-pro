# Code Assistant Pro

An AI-powered development suite built with Streamlit and the Groq API. Provides 10 AI-driven coding tools through a modern web dashboard.

## Architecture

- **Language:** Python 3.12
- **Web Framework:** Streamlit (port 5000)
- **AI Backend:** Groq API (Llama models)
- **Entry point:** `main.py`

## Project Structure

- `main.py` — App entry point, page routing, sidebar navigation
- `core/config.py` — Loads env vars, defines supported models
- `core/llm_handler.py` — Groq API wrapper
- `modules/` — Feature modules (MVC pattern), one folder per tool:
  - `home/`, `error_fix/`, `code_improve/`, `code_generate/`, `ui_design/`
  - `code_explain/`, `code_convert/`, `doc_gen/`, `test_gen/`, `security_analyzer/`
  - Each module has `view.py` (and `controller.py`/`service.py` where needed)
- `assets/styles.css` — Custom UI styling
- `utils/helpers.py` — Shared helpers: `parse_code_and_notes()` splits LLM response into code + explanation
- `.streamlit/config.toml` — Server config (port 5000, host 0.0.0.0, headless)

## Environment Variables

- `GROQ_API_KEY` — Required. Groq API key for AI inference. Get one free at https://console.groq.com

## Running the App

```bash
streamlit run main.py
```

Configured to run on port 5000 via the "Start application" workflow.

## Deploying to Streamlit Cloud

1. Push repo to GitHub
2. Go to share.streamlit.io and connect the repo
3. Set `main.py` as the entry file
4. Add `GROQ_API_KEY` in Settings → Secrets
5. Deploy

## Key Design Decisions

- All LLM prompts use markdown code fences (` ```lang ... ``` `) to structure output
- `parse_code_and_notes()` in helpers.py extracts code vs explanation from every response
- All code blocks rendered with `st.code()` for VS Code-style display with copy button
- No hardcoded secrets — API key read from environment variable only
