#!/bin/bash
# Script to get the size of the body of an HTTP response
echo -n "$(curl -s $1)" | wc -c
