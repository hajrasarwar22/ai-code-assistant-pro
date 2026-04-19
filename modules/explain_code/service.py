def explain_code(code, model, llm_handler):
    prompt = [
        {"role": "system", "content": "You are a senior developer. Explain the user's code in a clear, beginner-friendly way."},
        {"role": "user", "content": f"Code:\n{code}"}
    ]
    response = llm_handler.ask(prompt)
    return response
