import requests

url = "https://api.github.com/user"

headers = {
    "Authorization": "Bearer fake_token_for_learning"
}

response = requests.get(url, headers=headers)

print(f"Status code: {response.status_code}")
print(response.json())