def fix_code_error(code, error_desc, model, llm_handler):
    prompt = [
        {"role": "system", "content": "You are a professional Python code assistant. Fix the user's code and explain the changes in a beginner-friendly way. Highlight all changes."},
        {"role": "user", "content": f"Code:\n{code}\n\nError Description: {error_desc}"}
    ]
    response = llm_handler.ask(prompt)
    return response
