#!/bin/bash
# Sends a GET request to the URL passed as argument with a custom header and displays the body of the response
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
