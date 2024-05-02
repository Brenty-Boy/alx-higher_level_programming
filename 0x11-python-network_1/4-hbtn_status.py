#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status.

You must use the package requests.
You are not allow to import packages other than requests.
The body of the response must be displayed,
in the following format (tabulation before -).
"""


import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))