def generate_code(answers, model, llm_handler):
    lang = answers['language'].lower()
    prompt = [
        {
            "role": "system",
            "content": (
                f"You are an expert code generator. Generate complete, well-commented {answers['language']} code.\n"
                "Respond in EXACTLY this format — no deviations:\n\n"
                f"```{lang}\n"
                "<generated code only here>\n"
                "```\n\n"
                "**How It Works:**\n"
                "<explain your implementation choices, how it works, and any usage notes>"
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
