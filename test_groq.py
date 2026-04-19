import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

# Correct endpoint
endpoint = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Test with different current models
models_to_test = [
    'llama-3.1-8b-instant',
    'llama3-70b-8192',
    'llama3-8b-8192'
]

for model in models_to_test:
    print(f"\nTesting model: {model}")
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Say 'hello'"}],
        "max_tokens": 20
    }
    
    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=10)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ WORKING! Response: {result['choices'][0]['message']['content']}")
            print(f"🎯 Use this model: {model}")
            break
        else:
            print(f"Failed: {response.text[:100]}")
    except Exception as e:
        print(f"Error: {e}")