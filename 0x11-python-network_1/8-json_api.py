#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys


def search_user(letter):
    """
    Send a POST request to http://0.0.0.0:5000/search_user
    with the given letter as a parameter.

    Args:
        letter (str): The letter to be used as
        the search parameter.
    """
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()

        if response.json():
            user = response.json()
            print(f"[{user['id']}] {user['name']}")
        else:
            print("No result")
    except requests.exceptions.RequestException as e:
        print("Not a valid JSON")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    search_user(letter)
