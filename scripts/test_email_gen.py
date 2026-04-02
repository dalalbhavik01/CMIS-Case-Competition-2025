import google.generativeai as genai
import os

# Manual setup for test
api_key = "AIzaSyA_0JK0MdrCTW2dMj8KvUqLJTv-oJUrVhU" 
# Note: I'm using the key provided by the user directly here for the test script 
# to ensure it works even if .env issues persist.

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

student_name = "Alex Doe"
event_title = "Intro to Hackathons 2025"

prompt = f"""
Write a short, warm, and professional HTML email body for a student named '{student_name}' who just registered for the event '{event_title}'.

Requirements:
- Congratulate them on registering.
- Mention the event title clearly.
- Use a friendly and encouraging tone.
- Keep it brief (under 100 words).
- Output ONLY the HTML body content (do not include <html> or <body> tags, just the inner elements like <p>, <h3>, etc).
- Sign off as 'The CMIS Team'.
"""

print("Listing models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Error: {e}")
