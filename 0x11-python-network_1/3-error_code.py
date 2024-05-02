#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL,
and displays the body of the response (decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions,
and print: Error code: followed by the HTTP status code.
You must use the packages urllib and sys.
You are not allowed to import any packages other than urllib and sys.
You don’t need to check arguments passed to the script (number or type).
You must use the with statement.
Please test your script in the sandbox provided,
using the web server running on port 5000.
"""


import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]

    own_request = request.Request(url)
    try:
        with request.urlopen(own_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
