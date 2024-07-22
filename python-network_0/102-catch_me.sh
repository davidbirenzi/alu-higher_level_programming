#!/bin/bash

# Send the request to the server
curl -sL -X PUT -d "user_id=98" -H "Origin: Alu" 0.0.0.0:5000/catch_me

