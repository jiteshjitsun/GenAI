from google import genai

client = genai.Client(
    api_key="AIzaSyAnEwGfBx5PPoiL3lKIoe2z0pLksZwf2Pw"
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)

print(response.text)