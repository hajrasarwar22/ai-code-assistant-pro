def improve_code(code, model, llm_handler):
    prompt = [
        {
            "role": "system",
            "content": (
                "You are a senior software engineer. Improve the user's code for performance, readability, and best practices.\n"
                "You MUST respond using EXACTLY this format:\n\n"
                "<<CODE>>\n"
                "[put only the improved, runnable code here — no prose, no markdown fences]\n"
                "<</CODE>>\n\n"
                "<<NOTES>>\n"
                "[list every change you made and why — use plain text or bullet points]\n"
                "<</NOTES>>"
            )
        },
        {
            "role": "user",
            "content": f"Code:\n{code}"
        }
    ]
    return llm_handler.ask(prompt)
