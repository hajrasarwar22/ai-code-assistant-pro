from .service import fix_code_error

def handle_error_fix(code, error_desc, model, llm_handler):
    return fix_code_error(code, error_desc, model, llm_handler)
