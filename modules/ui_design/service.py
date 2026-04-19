def generate_ui_design(user_idea, model, llm_handler):
    prompt = [
        {
            "role": "system",
            "content": (
                "You are a UI/UX expert. Generate HTML/CSS/JS code for the user's UI idea.\n"
                "You MUST respond using EXACTLY this format:\n\n"
                "<<CODE>>\n"
                "[put only the complete UI code here — no prose, no markdown fences]\n"
                "<</CODE>>\n\n"
                "<<NOTES>>\n"
                "[explain layout decisions, design choices, and how to customise the output]\n"
                "<</NOTES>>"
            )
        },
        {
            "role": "user",
            "content": f"UI Idea: {user_idea}"
        }
    ]
    return llm_handler.ask(prompt)
