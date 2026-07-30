#!/bin/bash
# sends a DELETE request to the URL passed as argument and displays the response body
curl -s -X DELETE "$1"
