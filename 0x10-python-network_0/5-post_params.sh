#!/bin/bash
# takes in a URL (uniform resource locator) as an argument, send post request, displa4y the body of the response
curl -sX POST -d 'email=test@gmail.com' -d 'subject=I will allways be here for PLD' "$1"
