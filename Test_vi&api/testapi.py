import openai
import os

openai.proxy = {"https": 'http://127.0.0.1:7897', "http":"//127.0.0.1:7897"}

# openai.api_key = os.getenv("OPENAI_API_KEY")  # Or directly set openai.api_key = "your-api-key"
openai.api_key = "your-api-key"

# Test the connection by listing models
try:
    models = openai.Model.list()
    print("Connection successful! Available models:")
    for model in models['data']:
        print(model['id'])
except openai.error.AuthenticationError:
    print("Authentication error: Check your API key.")
except Exception as e:
    print(f"An error occurred: {e}")

