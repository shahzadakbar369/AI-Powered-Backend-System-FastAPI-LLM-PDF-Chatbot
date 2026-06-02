import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

headers = {
    "User-Agent": "Mozilla/5.0 (Learning-Python-API-Project)",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())