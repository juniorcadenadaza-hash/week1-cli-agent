import sys
import requests


def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Request failed with status code: {response.status_code}")
        print(response.json())
        return

    data = response.json()

    print("--- GitHub User Summary ---")
    print(f"Username: {data['login']}")
    print(f"Name: {data['name']}")
    print(f"Location: {data['location']}")
    print(f"Public repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")


if len(sys.argv) < 2:
    print("Please provide a GitHub username.")
    print("Example: python github_user_summary.py octocat")
else:
    username = sys.argv[1]
    get_github_user(username)