#!/bin/bash
# Displays all HTTP methods accepted by the server for a given URL
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
