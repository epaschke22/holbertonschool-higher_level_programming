#!/bin/bash
# sets header variables with curl and uses POST
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1
