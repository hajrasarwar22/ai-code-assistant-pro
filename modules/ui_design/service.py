def generate_ui_design(user_idea, model, llm_handler):
    prompt = [
        {"role": "system", "content": "You are a UI/UX expert. Generate Streamlit/HTML/CSS code for the user's idea. Suggest layout and design improvements."},
        {"role": "user", "content": f"UI Idea: {user_idea}"}
    ]
    response = llm_handler.ask(prompt)
    return response
