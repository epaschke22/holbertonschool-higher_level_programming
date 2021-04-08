#!/bin/bash
# sets header variables with curl and uses POST
curl $1 -s -X POST -d "email: hr@holbertonschool.com" -d "subject: I will always be here for PLD"
