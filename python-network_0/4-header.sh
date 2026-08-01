#!/bin/bash
# Sends a GET request to a URL with a custom header variable
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
