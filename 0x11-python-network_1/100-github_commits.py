#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name.
The second argument will be the owner name.
You must use the packages requests and sys.
You are not allowed to import any packages other than requests and sys.
You don’t need to check arguments passed to the script (number or type).
"""


import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    rqst = requests.get(url)
    commits = rqst.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
