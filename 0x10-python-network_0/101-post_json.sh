#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as first argument
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
