#!/bin/bash
# Script to make a request to 0.0.0.0:5000/catch_me
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
