from .service import explain_code

def handle_explain_code(code, model, llm_handler):
    return explain_code(code, model, llm_handler)
