#!/bin/bash
# hat takes in a URL and displays all HTTP methods the server will accept.
curl -sIX OPTIONS $1
