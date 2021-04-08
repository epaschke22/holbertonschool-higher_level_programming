#!/bin/bash
# sends GET request to url to display size of body of 200 staus code
curl $1 -s -X GET -L
