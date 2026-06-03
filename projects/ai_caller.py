import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)
while True:
    user_input = input("\nAsk AI (or type exit): ")

    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    print("\nAI:", response.choices[0].message.content)