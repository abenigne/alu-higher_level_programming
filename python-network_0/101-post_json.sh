#!/bin/bash
# Sends a JSON POST request with the contents of a file passed as an argument
curl -s -H "Content-Type: application/json" -d "@$2" "$1"
