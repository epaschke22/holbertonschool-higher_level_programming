#!/bin/bash
# sets header variables with curl and uses POST
curl $1 -s  -X GET -H "email: hr@holbertonschool.com" -H "subject: I will always be here for PLD"
