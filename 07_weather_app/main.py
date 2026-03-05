from openai import OpenAI
from dotenv import load_dotenv
import requests, json, os
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()

client = OpenAI()

def run_command(cmd: str):
    result = os.system(cmd)
    return result
    
def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}/?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f" >> The weather in {city} is {response.text}"
    
    return "Something went wrong"

SYSTEM_PROMPT = """
    You're an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also call a tool if required from the list of available tools.
    for every tool call wait for the observe step which is output from the called tool
    
    Rules:
    - Strictly follow the given json output format
    - Only run one step at a time
    - The sequence of steps is START ( where user gives an input ), PLAN ( That can be multiple times) and 
    finally OUTPUT ( which is going to be displayed to the users).
    
    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string", "tool": "string", "input": "string" }
    
    Available tool:
    - get_weather(city: str): Takes city name as input string and returns the weather info about the city
    - run_command(cmd: str): Takes a system linux command as a string and executes the command on user's system and return the output from that command
    
    Example 1:
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
    
    Example 2:
    START: What is the weather of Delhi ?
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in getting the weather of Delhi in India" }
    PLAN: { "step": "PLAN", "content": "let's see if we have any available tools from the list of available tools" }
    PLAN: { "step": "PLAN", "content": "Great we have get_weather tool available for this query" }
    PLAN: { "step": "PLAN", "content": "I need to call get_weather tool for Delhi as input for city"}
    PLAN: { "step": "TOOL", "tool": "get_weather", "input": "Delhi"}
    PLAN: { "step": "OBSERVE", "tool": "get_weather", "output": "The temp of delhi is sunny with 37 C"}
    PLAN: { "step": "PLAN", "content": "Great I got the weather info about delhi"}
    OUTPUT: { "step": "OUTPUT", "content": "The current weather in delhi is 37 C"}
    
"""
class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step, example: PLAN, OUTPUT, TOOL")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The ID of the tool to call..")
    input: Optional[str] = Field(None, description="The input params for the tool")


    
available_tools = {
    "get_weather": get_weather,
    "run_command": run_command
}


message_history = [
    { "role": "system", "content": SYSTEM_PROMPT },
]

while True:
    user_query = input("🫴 ")
    message_history.append({ "role": "user", "content": user_query })

    while True:
        response = client.chat.completions.parse(
            model="gpt-4o",
            response_format=MyOutputFormat,
            messages = message_history
        )
        
        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})
        parsed_result = response.choices[0].message.parsed
        
        
        
        if parsed_result.step == "START":
            print("💋 ", parsed_result.content)
            continue
        
        if parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.tool
            print(f" > {tool_to_call} ({tool_input}) ")
            
            tool_response = available_tools[tool_to_call](tool_input)
            
            print(f" > {tool_to_call} ({tool_input}) => {tool_response}")
            
            message_history.append({ "role": "developer", "content": json.dumps(
                {
                    "step": "observe",
                    "tool": "tool_to_call",
                    "input": tool_input,
                    "output": tool_response
                }
            )})
            continue
        
        if parsed_result.step == "PLAN":
            print("👀 ", parsed_result.content)
            continue
        
        if parsed_result.step == "OUTPUT":
            print("🐳 ", parsed_result.content)
            break


# main()