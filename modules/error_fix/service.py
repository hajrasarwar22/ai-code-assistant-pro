def fix_code_error(code, error_desc, model, llm_handler):
    prompt = [
        {
            "role": "system",
            "content": (
                "You are a professional code assistant. Fix the user's broken code.\n"
                "Respond in EXACTLY this format — no deviations:\n\n"
                "```python\n"
                "<corrected code only here>\n"
                "```\n\n"
                "**Root Cause & Explanation:**\n"
                "<explain what was wrong, what you changed, and why — plain text or bullet points>"
            )
        },
        {
            "role": "user",
            "content": f"Code:\n{code}\n\nError Description: {error_desc}"
        }
    ]
    return llm_handler.ask(prompt)
