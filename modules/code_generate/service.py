def generate_code(answers, model, llm_handler):
    prompt = [
        {"role": "system", "content": "You are an expert code generator. Generate complete, well-commented code as per user requirements. Explain your solution."},
        {"role": "user", "content": f"Purpose: {answers['purpose']}\nLanguage/Framework: {answers['language']}\nConstraints: {answers['constraints']}"}
    ]
    response = llm_handler.ask(prompt)
    return response
