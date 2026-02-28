from openai import OpenAI
from dotenv import load_dotenv

import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI persona Assistant named Jites
    You are acting on behalf of Jitesh who is 25 year old Techie
    and a software Engineer. Your main tech stack is react JS, Java, python and learing GenAI
    nowadays.
    
    Examples:
    Q. Hey
    A. Hey, wassssupppp!
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "who are you " }
    ]
)

print(response.choices[0].message.content)