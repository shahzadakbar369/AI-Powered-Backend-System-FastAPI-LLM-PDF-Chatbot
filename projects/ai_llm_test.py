from groq import Groq
import os

api_key = os.getenv("GROQ_API_KEY")


client = Groq(api_key=api_key)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain FastAPI in simple words"
        }
    ]
)

print(response.choices[0].message.content)