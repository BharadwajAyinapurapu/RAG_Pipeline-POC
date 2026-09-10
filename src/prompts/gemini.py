# Basic model testing

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

response = client.chat.completions.create(
    model = "gemini-3.6-flash",
    messages = [
        {
            "role": "system",
            "content": "You are an expert in Maths and only answer questions related to maths. If you face any question unrelated to maths, just say sorry and do not answer"
        },
        {
            "role": "user",
            "content": "Please help me solve s plus b whole square"
        }
    ]
)
print(response.choices[0].message.content)