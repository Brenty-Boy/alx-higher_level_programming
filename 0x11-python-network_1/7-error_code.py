#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code.
You must use the packages requests and sys.
You are not allowed to import any packages other than requests and sys.
You don’t need to check arguments passed to the script (number or type).
Please test your script in the sandbox provided,
using the web server running on port 5000.
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    rqst = requests.get(url)
    if rqst.status_code >= 400:
        print("Error code: {}".format(rqst.status_code))
    else:
        print(rqst.text)
