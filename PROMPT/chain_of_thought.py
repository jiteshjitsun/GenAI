# Chain of thought propmting 

from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    
    Rules:
    - Strictly follow the given json output format
    - Only run one step at a time
    - The sequence of steps is START ( where user gives an input ), PLAN ( That can be multiple times) and 
    finally OUTPUT ( which is going to be displayed to the users).
    
    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }
    
    Example:
    START: Hey, can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN", "content": "Yes, the BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN", "content": "First we must multiply 3*5 which is 15"}
    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10 "}
    PLAN: { "step": "PLAN", "content": "We must perform the divide that is 15/10 = 1.5 "}
    PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 1.5"}
    PLAN: { "step": "PLAN", "content": "Now finally lets perform the add 3.5 "}
    PLAN: { "step": "PLAN", "content": "Great we have solved and finally left with 3.5 as answer"}
    OUTPUT: { "step": "OUTPUT", "content": "3.5"}
    
"""


message_history = [
    { "role": "system", "content": SYSTEM_PROMPT },
]

user_query = input("🫴 ")
message_history.append({ "role": "user", "content": user_query })

print('\n\n\n')
while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        # model="gemini-2.5-flash",
        response_format={ "type": "json_object" },
        messages = message_history
    )
    
    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)
    
    if parsed_result.get("step") == "START":
        print("💋 ", parsed_result.get("content"))
        continue
    
    if parsed_result.get("step") == "PLAN":
        print("👀 ", parsed_result.get("content"))
        continue
    
    if parsed_result.get("step") == "OUTPUT":
        print("🐳 ", parsed_result.get("content"))
        break

print('\n\n\n')

# response = client.chat.completions.create(
#     model="gemini-2.5-flash",
#     response_format={ "type": "json_object" },
#     messages=[
#         {
#             "role": "system",
#             "content": SYSTEM_PROMPT
#         },
#         {
#             "role": "user",
#             "content": "Write a code to add n numbers in js"
#         },
#         # Manually keep adding message to History   
#         { "role": "assistant", "content": json.dumps({ "step": "START", "content": "you want a JavaScript code to add n numbers "})},
#         { "role": "assistant", "content": json.dumps({ "step": "PLAN", "content": "I need to write a JavaScript function that can add 'n' numbers." })},
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "The function should accept an array of numbers as input."})},
#         { "role": "assistant", "content": json.dumps({
#     "step": "PLAN",
#     "content": "Inside the function, I'll initialize a variable (e.g., `sum`) to 0. This `sum` variable will accumulate the total."
# })},
#         { "role": "assistant", "content": json.dumps({"step": "PLAN", "content": "I will then iterate through the input array, adding each number to the `sum` variable."})},
#         { "role": "assistant", "content": json.dumps({
#     "step": "PLAN",
#     "content": "Finally, the function will return the calculated `sum`."
# })},
        
#     ]
# )

# print(response.choices[0].message.content)