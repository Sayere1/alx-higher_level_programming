#!/bin/bash
# sends a request to a URL passed as argnt, % displays only status code of response.
curl -so /dev/null -w "%{http_code}" "$1"
