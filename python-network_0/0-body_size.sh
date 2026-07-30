#!/bin/bash
# sends a request to the URL passed as argument and displays the size in bytes of the response body
curl -s -o /dev/null -w "%{size_download}\n" "$1"
