#!/bin/bash
# sends an OPTIONS request to the URL passed as argument and displays the allowed HTTP methods
curl -s -X OPTIONS "$1" -I | grep -i "allow" | cut -d " " -f2-
