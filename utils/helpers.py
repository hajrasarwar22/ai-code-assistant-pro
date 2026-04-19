import streamlit as st
import pyperclip
from pygments import highlight
from pygments.lexers import PythonLexer, HtmlLexer, CssLexer, get_lexer_by_name
from pygments.formatters import HtmlFormatter
import re


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


def extract_code_block(text):
    pattern = r'```(?:\w+)?\n?([\s\S]*?)```'
    matches = re.findall(pattern, text)
    if matches:
        return '\n\n'.join(m.strip() for m in matches)
    return text.strip()


def parse_structured_response(text):
    code_match = re.search(r'<<CODE>>([\s\S]*?)<</CODE>>', text, re.DOTALL)
    notes_match = re.search(r'<<NOTES>>([\s\S]*?)<</NOTES>>', text, re.DOTALL)

    if code_match and notes_match:
        return code_match.group(1).strip(), notes_match.group(1).strip()

    code = extract_code_block(text)
    lines = text.split('\n')
    explanation_lines = [l for l in lines if not l.strip().startswith('```')]
    explanation = '\n'.join(explanation_lines).strip()
    return code, explanation
