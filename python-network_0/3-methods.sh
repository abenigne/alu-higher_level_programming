#!/bin/bash
# Displays all HTTP methods accepted by the server for a given URL
curl -sI "$1" | grep -i "^Allow:" | cut -d ' ' -f2- | tr -d '\r'
