#!/bin/bash
# Sends a GET request to the URL passed as argument and displays the body only if the response status code is 200
code=$(curl -s -o /tmp/1-body_output -w "%{http_code}" "$1"); [ "$code" = "200" ] && cat /tmp/1-body_output
