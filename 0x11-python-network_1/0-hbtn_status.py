#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed in this format (tabulation before -)
You must use a with statement
"""


from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        response = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode(encoding='utf-8')))
