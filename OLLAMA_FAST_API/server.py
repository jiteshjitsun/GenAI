from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(
    host="http://localhost:11434",
)

@app.get("/")
def ded_root():
    return {"Name": "jitesh"}

@app.get("/contact")
def contact():
    return {"Mob no": "952-365269"}

@app.post("/chat")
def chat(
    message: str = Body(..., description = "The message")
):
    response = client.chat(model="gemma2:2b", messages = [
        { "role": "user", "content": message }
    ])
    
    return { "response": response.message.content }

