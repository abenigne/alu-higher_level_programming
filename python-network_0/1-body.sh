#!/bin/bash
# sends a GET request to the URL passed as argument and displays the response body, only if the status code is 200
curl -s "$1" -o /tmp/body_$$ -w "%{http_code}" | grep -q 200 && cat /tmp/body_$$; rm -f /tmp/body_$$
