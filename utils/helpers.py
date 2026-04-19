import streamlit as st
import pyperclip
import re


def copy_to_clipboard(text):
    st.code(text, language=None)
    st.button("Copy", on_click=lambda: pyperclip.copy(text))


def show_spinner(message="Processing..."):
    return st.spinner(message)


def parse_code_and_notes(text):
    code_blocks = re.findall(r'```(?:\w+)?\n?([\s\S]*?)```', text)
    if code_blocks:
        code_part = '\n\n'.join(b.strip() for b in code_blocks)
        explanation_part = re.sub(r'```(?:\w+)?\n?[\s\S]*?```', '', text).strip()
        explanation_part = re.sub(r'\n{3,}', '\n\n', explanation_part).strip()
    else:
        lines = text.strip().split('\n')
        code_lines = []
        note_lines = []
        in_code = False
        for line in lines:
            if re.match(r'^\s*(def |class |import |from |for |while |if |return |#)', line):
                in_code = True
            if in_code:
                code_lines.append(line)
            else:
                note_lines.append(line)
        code_part = '\n'.join(code_lines).strip() or text.strip()
        explanation_part = '\n'.join(note_lines).strip()

    return code_part, explanation_part


def show_code(code, language='python'):
    st.code(code, language=language)
