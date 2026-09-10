# Few shot promption : Model is provided with a few examples for reference before asking it to generate a resonse

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

SYSTEM_PROMPT = """
Your name is Alex and you should answerr only coding related questions. Do not answer anythiong else. If you face any non coding related questions, Just say sorry and do not answer

Examples:
Q: Can you please explain a+b whole square?
A: Sorry, I can only help with coding related questions

Q: Can you please give me a Python function to add two numbers?
A: Sure! Here's the Python function snippet to add two numbers
    def add(a, b):
        return a+b
"""

response = client.chat.completions.create(
    model = "gemini-3.6-flash",
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "can you translate word hello to telugu"
        }
    ]
)
print(response.choices[0].message.content)