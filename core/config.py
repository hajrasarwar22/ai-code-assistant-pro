import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Current supported Groq models
GROQ_MODELS = [
    'llama-3.1-8b-instant',
    'llama3-70b-8192',       
    'llama3-8b-8192',        
]