import requests

url = "https://api.github.com/users/octocat"

response = requests.get(url)
data = response.json()

print(f"Status code: {response.status_code}")
print(f"Content type: {response.headers.get('Content-Type')}")
print(f"Rate limit remaining: {response.headers.get('X-RateLimit-Remaining')}")

print("--- USER DATA ---")
print(f"Username: {data['login']}")
print(f"Name: {data['name']}")
print(f"Public repos: {data['public_repos']}")
print(f"Followers: {data['followers']}")