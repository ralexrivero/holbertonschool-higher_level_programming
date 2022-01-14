#!/bin/bash
# takes a URL (uniform resource locator) as an argument, sends a GET request, and displays the body of the response
curl -sL "$1"
