#!/bin/bash
# Displays the size of the HTTP response body in bytes for a given URL
curl -s -o /dev/null -w "%{size_download}\n" "$1"
