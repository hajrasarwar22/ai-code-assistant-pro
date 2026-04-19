def generate_code(answers, model, llm_handler):
    prompt = [
        {
            "role": "system",
            "content": (
                "You are an expert code generator. Generate complete, well-commented code as per user requirements.\n"
                "You MUST respond using EXACTLY this format:\n\n"
                "<<CODE>>\n"
                "[put only the generated, runnable code here — no prose, no markdown fences]\n"
                "<</CODE>>\n\n"
                "<<NOTES>>\n"
                "[explain your implementation choices, how it works, and any usage notes]\n"
                "<</NOTES>>"
            )
        },
        {
            "role": "user",
            "content": (
                f"Purpose: {answers['purpose']}\n"
                f"Language/Framework: {answers['language']}\n"
                f"Complexity: {answers['complexity']}\n"
                f"Constraints: {answers['constraints']}\n"
                f"Include tests: {answers['include_tests']}\n"
                f"Include docstrings: {answers['include_docs']}"
            )
        }
    ]
    return llm_handler.ask(prompt)
