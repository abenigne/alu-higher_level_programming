#!/bin/bash
# Sends an OPTIONS request to the URL passed as argument and displays all HTTP methods the server accepts
curl -s -X OPTIONS -I "$1" | grep -i "^Allow:" | cut -d ':' -f2- | tr -d '\r' | sed 's/^ *//'
