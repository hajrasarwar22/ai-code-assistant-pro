def generate_ui_design(user_idea, model, llm_handler):
    prompt = [
        {
            "role": "system",
            "content": (
                "You are a UI/UX expert. Generate complete HTML/CSS/JS code for the user's UI idea.\n"
                "Respond in EXACTLY this format — no deviations:\n\n"
                "```html\n"
                "<complete UI code only here>\n"
                "```\n\n"
                "**Design Notes:**\n"
                "<explain layout decisions, design choices, and how to customise>"
            )
        },
        {
            "role": "user",
            "content": f"UI Idea: {user_idea}"
        }
    ]
    return llm_handler.ask(prompt)
