#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

curl -s -o /dev/null -w "%{http_code}" "$URL"
