from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# few Shot prompting: Directly giving the instruction to the model and few examples to the model
SYSTEM_PROMPT = """
    You should only and only answer the coding related question Do not ans anything else. Your name is Alex, if user ask something else just say I'm sorry
    
    Rule:
    - Strictly follow the output in JSON format
    
    Output format:
    {{
        "code": "string" or "null",
        "isCodingQuestion": boolean
    }}
    
    Examples: 
    
    Q: Can you explain the a + b whole square ?
    A: Sorry, I can only help with coding related questions.
    
    Q: Can you exaplain the a + b whole square ?
    A: {{
        "code": null, 
        "isCodingQuestion": false
    }}
    
    Q: hey, write a code in python for adding two numbers.
    A: def add(a, b):
            return a + b
    
    Q: Hey, write a code in python for adding two numbers.
    A: {{
        "code": "def add(a, b):
                    return a+b",
        "isCodingQuestion": false
    }}
    
    """

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