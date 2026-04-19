from .service import generate_code

def handle_code_generate(answers, model, llm_handler):
    return generate_code(answers, model, llm_handler)
