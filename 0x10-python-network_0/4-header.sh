#!/bin/bash
# Sends a GET request to a URL with a specific header and displays the response body
curl -sH "X-School-User-Id: 98" "$1"
