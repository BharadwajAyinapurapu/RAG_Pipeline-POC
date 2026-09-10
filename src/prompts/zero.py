# Zero shot prompting : Directly giving instructions to the model without any examples

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

SYSTEM_PROMPT = """
Your name is Alex and you should answer only coding related questions. Do not answer anythiong else. If you face any non coding related questions, just say sorry and do not answer
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
            "content": "can you write a code to translate word hello to telugu"
        }
    ]
)
print(response.choices[0].message.content)