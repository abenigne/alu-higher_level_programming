#!/usr/bin/python3
"""Module that displays the X-Request-Id header value of a URL response."""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.getheader("X-Request-Id"))
