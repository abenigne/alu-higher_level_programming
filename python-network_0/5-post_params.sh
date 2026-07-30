#!/bin/bash
# sends a POST request with email and subject parameters to the URL passed as argument and displays the response body
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
