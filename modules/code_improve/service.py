def improve_code(code, model, llm_handler):
    prompt = [
        {
            "role": "system",
            "content": (
                "You are a senior software engineer. Improve the user's code for performance, readability, and best practices.\n"
                "Respond in EXACTLY this format — no deviations:\n\n"
                "```python\n"
                "<improved code only here>\n"
                "```\n\n"
                "**Changes Made:**\n"
                "<list every change you made and why — plain text or bullet points>"
            )
        },
        {
            "role": "user",
            "content": f"Code:\n{code}"
        }
    ]
    return llm_handler.ask(prompt)
