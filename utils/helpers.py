import streamlit as st
import pyperclip
from pygments import highlight
from pygments.lexers import PythonLexer, HtmlLexer, CssLexer, get_lexer_by_name
from pygments.formatters import HtmlFormatter

def copy_to_clipboard(text):
    st.code(text, language=None)
    st.button("Copy", on_click=lambda: pyperclip.copy(text))

def syntax_highlight(code, language='python'):
    try:
        lexer = get_lexer_by_name(language)
    except Exception:
        lexer = PythonLexer()
    formatter = HtmlFormatter(style="monokai", full=False, noclasses=True)
    return highlight(code, lexer, formatter)

def show_spinner(message="Processing..."):
    return st.spinner(message)
