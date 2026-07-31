#!/bin/bash
# sends a GET request with the X-HolbertonSchool-User-Id header to the URL passed as argument and displays the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
