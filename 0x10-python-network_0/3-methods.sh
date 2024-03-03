#!/bin/bash
# script that takes in a URL % displays all HTTP methods d server will acpt
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
