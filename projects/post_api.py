import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Learning APIs",
    "body": "This is my first POST request",
    "userId": 1
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())