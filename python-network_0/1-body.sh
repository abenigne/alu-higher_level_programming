#!/bin/bash
# sends a GET request to the URL, follows redirects, and displays the body only if the final status code is 200
curl -s -L -o /tmp/body_$$ -w "%{http_code}" "$1" | grep -q 200 && cat /tmp/body_$$; rm -f /tmp/body_$$
