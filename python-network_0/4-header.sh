#!/bin/bash
# sends a GET request with a custom header to the URL passed as argument and displays the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
