#!/bin/bash
# Sends a GET request to a URL with a custom header
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
