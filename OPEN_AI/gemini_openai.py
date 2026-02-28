from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Zero Shot prompting: Directly giving the instruction to the model
SYSTEM_PROMPT = "You should only and only answer the coding related question Do not ans anything else. Your name is Alex, if user ask something else just say I'm sorry"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "can you help me write a code to solve the a + b whole square"
        }
    ]
)

print(response.choices[0].message.content)
# print(response)