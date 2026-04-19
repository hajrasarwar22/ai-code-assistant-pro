def fix_code_error(code, error_desc, model, llm_handler):
    prompt = [
        {
            "role": "system",
            "content": (
                "You are a professional code assistant. Fix the user's code and explain the root cause.\n"
                "You MUST respond using EXACTLY this format:\n\n"
                "<<CODE>>\n"
                "[put only the corrected, runnable code here — no prose, no markdown fences]\n"
                "<</CODE>>\n\n"
                "<<NOTES>>\n"
                "[put the root cause explanation and what you changed here]\n"
                "<</NOTES>>"
            )
        },
        {
            "role": "user",
            "content": f"Code:\n{code}\n\nError Description: {error_desc}"
        }
    ]
    return llm_handler.ask(prompt)
