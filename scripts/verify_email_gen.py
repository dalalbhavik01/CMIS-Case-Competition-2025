import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Match logic in email_utils.py
api_keys_str = os.getenv("GEMINI_API_KEYS", "")
api_keys = [k.strip() for k in api_keys_str.split(",") if k.strip()]
if not api_keys:
    single_key = os.getenv("GEMINI_API_KEY")
    if single_key:
        api_keys.append(single_key)

print(f"Found keys: {len(api_keys)}")
if not api_keys:
    print("NO KEYS FOUND IN ENV")
    exit(1)

api_key = api_keys[0]
print(f"Using key starting with: {api_key[:5]}...")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-flash-latest')

prompt = "Write a hello world message."
print("Generating content...")
try:
    response = model.generate_content(prompt)
    print("Success!")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
