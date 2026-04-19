import requests
from .config import GROQ_API_KEY, GROQ_MODELS

class LLMHandler:
    def __init__(self, model: str):
        if model not in GROQ_MODELS:
            raise ValueError(f"Model {model} not supported.")
        self.model = model
        self.api_key = GROQ_API_KEY
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"

    def ask(self, messages, temperature=0.2, max_tokens=2048):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            return data['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response:
                return f"[LLM API Error] {e.response.status_code}: {e.response.text}"
            return f"[LLM API Error] {str(e)}"