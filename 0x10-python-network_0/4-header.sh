#!/bin/bash
# a Bash script that takes in a URL as an argument.
curl -sX GET -H "X-School-User-Id: 98" "$1"
