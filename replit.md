# Code Assistant Pro

An AI-powered development suite built with Streamlit and the Groq API. Provides 10 AI-driven coding features through a modern web dashboard.

## Architecture

- **Language:** Python 3.12
- **Web Framework:** Streamlit
- **AI Backend:** Groq API (Llama models)
- **Entry point:** `main.py`

## Project Structure

- `main.py` — App entry point, page routing, sidebar navigation
- `core/` — Shared infrastructure
  - `config.py` — Loads env vars, defines supported models
  - `llm_handler.py` — Groq API wrapper
- `modules/` — Feature modules (MVC pattern)
  - `home/`, `error_fix/`, `code_improve/`, `code_generate/`, `ui_design/`
  - `code_explain/`, `code_convert/`, `doc_gen/`, `test_gen/`, `security_analyzer/`
  - Each module has `view.py`, `controller.py`, `service.py`
- `assets/styles.css` — Custom UI styling
- `utils/helpers.py` — Shared helper functions
- `.streamlit/config.toml` — Streamlit server config (port 5000, host 0.0.0.0)

## Environment Variables

- `GROQ_API_KEY` — Required. Groq API key for AI inference. Get one at https://console.groq.com

## Running the App

```bash
streamlit run main.py
```

Runs on port 5000 via the "Start application" workflow.

## Deployment

Configured for autoscale deployment on Replit. Run command: `streamlit run main.py --server.port=5000 --server.address=0.0.0.0`
