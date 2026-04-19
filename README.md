# New Modules to Create

Create these folders inside `modules/`:

## modules/home/
- view.py  ← copy from home_view.py

## modules/code_explain/
- __init__.py
- view.py   ← copy from code_explain_view.py
- controller.py  (not needed, logic in vieUnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 5: character maps to <undefined>

File "D:\FJWU\Course-AI\Project7\main.py", line 12, in <module>
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
                          ~~~~~~^^
File "C:\Python314\Lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^w)

## modules/code_convert/
- __init__.py
- view.py   ← copy from code_convert_view.py

## modules/doc_gen/
- __init__.py
- view.py   ← copy from doc_gen_view.py

## modules/test_gen/
- __init__.py
- view.py   ← copy from test_gen_view.py

## modules/security_analyzer/
- __init__.py
- view.py   ← copy from security_view.py

All new modules call LLMHandler directly in their view.py.
No separate service.py needed unless you want to add that layer.
# Code Assistant Chatbot

A professional, modular Python project for an AI-powered code assistant with a modern Streamlit dashboard. Supports error fixing, code improvement, code generation, and UI design assistance using Groq API (multi-model).

---

## 📁 Folder Structure

```
root/
│
├── .env
├── main.py
│
├── modules/
│   ├── error_fix/
│   │   ├── controller.py
│   │   ├── service.py
│   │   ├── view.py
│   ├── code_improve/
│   │   ├── controller.py
│   │   ├── service.py
│   │   ├── view.py
│   ├── code_generate/
│   │   ├── controller.py
│   │   ├── service.py
│   │   ├── view.py
│   ├── ui_design/
│       ├── controller.py
│       ├── service.py
│       ├── view.py
│
├── core/
│   ├── llm_handler.py
│   ├── config.py
│
├── assets/
│   ├── styles.css
│
├── utils/
│   ├── helpers.py
│
├── requirements.txt
└── README.md
```

---

## 🚀 Features
- **Fix Errors:** Paste code + error, get fixes & explanations
- **Improve Code:** Optimize code, get best practices
- **Generate Code:** Guided Q&A, full code with comments
- **UI Design Assistant:** Generate UI code, layout, and suggestions
- **Multi-model Groq API** (3+ models selectable)
- **Modern Black & White UI** (light/dark toggle)
- **Tabs, expanders, copy buttons, syntax highlighting, spinners**
- **Session state, error handling, responsive layout**

---

## 🛠️ Setup Guide

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Project7
   ```

2. **Create and fill `.env`**
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run main.py
   ```

5. **(Optional) Run in PyCharm**
   - Open folder in PyCharm
   - Mark root as source
   - Set `main.py` as entry point
   - Run/Debug

---

## 📝 .env Example
```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 💡 Usage
- Use the sidebar to navigate between modules
- Select LLM model for each task
- Paste code or answer questions as prompted
- Copy results with one click
- Expand explanations for details

---

## 📦 Requirements
- Python 3.10+
- Streamlit
- requests
- python-dotenv
- pygments

---

## ⚠️ Notes
- Ensure your Groq API key is valid
- All modules are independent (MVC)
- UI is fully responsive and production-ready

---

## 👨‍💻 Author
- Built as a professional/final year project
- Designed for extensibility and real-world use
