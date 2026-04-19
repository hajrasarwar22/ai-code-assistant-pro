from .service import improve_code

def handle_code_improve(code, model, llm_handler):
    return improve_code(code, model, llm_handler)
