#!/bin/bash
# displays all methods a server will accept
curl -X OPTIONS -I $1 -s | grep "Allow:" | cut -b 8-
