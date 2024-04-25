#!/bin/bash
# Script to get the HTTP status code of a URL
curl -s -o /dev/null -w "%{http_code}" $1
