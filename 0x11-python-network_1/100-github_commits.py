#!/usr/bin/python3
"""script that takes 2 arguments in order
to solve this challenge
"""
import requests
import sys


def get_recent_commits(repo_name, owner_name):
    """
    Retrieve the 10 most recent commits from the specified repository.

    Args:
        repo_name (str): The name of the repository.
        owner_name (str): The name of the repository owner.
    Returns:
        list: A list of the 10 most recent commits, where each
        commit is represented as a tuple
        containing the commit SHA and the author's name.
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]
        return ([(commit["sha"], commit["commit"]["author"]["name"])
                 for commit in commits]
                )
    else:
        return []


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repo_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    commits = get_recent_commits(repo_name, owner_name)

    for commit in commits:
        print(f"{commit[0]}: {commit[1]}")
