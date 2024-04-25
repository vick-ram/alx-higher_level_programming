#!/bin/bash
# Script to get the size of the body of an HTTP response
url=$1
response=$(curl -s $url)
size=$(echo -n "$response" | wc -c)
echo "$size"
