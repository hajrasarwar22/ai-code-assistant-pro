from .service import generate_ui_design

def handle_ui_design(user_idea, model, llm_handler):
    return generate_ui_design(user_idea, model, llm_handler)
