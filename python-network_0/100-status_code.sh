#!/bin/bash
# Displays only the HTTP status code of the response without pipes or redirections
curl -s -o /dev/null -w "%{http_code}" "$1"
