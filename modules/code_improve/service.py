def improve_code(code, model, llm_handler):
    prompt = [
        {"role": "system", "content": "You are a senior software engineer. Improve the user's code for performance, readability, and best practices. Explain all improvements."},
        {"role": "user", "content": f"Code:\n{code}"}
    ]
    response = llm_handler.ask(prompt)
    return response
