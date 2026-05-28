import sys
import requests


def get_user_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Request failed with status code: {response.status_code}")
        print(response.json())
        return

    repos = response.json()

    print(f"--- Public repositories for {username} ---")

    for repo in repos:
        language = repo["language"] or "Not specified"

        print(f"Name: {repo['name']}")
        print(f"URL: {repo['html_url']}")
        print(f"Language: {repo['language']}")
        print("---")


if len(sys.argv) < 2:
    print("Please provide a GitHub username.")
    print("Example: python github_repos.py octocat")
else:
    username = sys.argv[1]
    get_user_repos(username)