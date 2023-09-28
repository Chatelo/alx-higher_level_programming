#!/bin/bash
# Get the response body for a given URL for 200 status code responses.
curl -sL -w "%{http_code}" "$1" -o /tmp/body | tail -n 1 | grep -q 200 && cat /tmp/body
