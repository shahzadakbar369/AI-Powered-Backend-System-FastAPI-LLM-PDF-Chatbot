import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

url = "https://newsapi.org/v2/top-headlines"

params = {
    "country": "us",
    "apiKey": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

if data.get("status") != "ok":
    print("API Error:", data.get("message"))
    exit()

for i, article in enumerate(data.get("articles", [])[:5]):
    print("\nNews", i+1)
    print(article["title"])