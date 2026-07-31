#!/usr/bin/python3
"""Module that sends a POST request with an email parameter using requests."""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(r.text)
