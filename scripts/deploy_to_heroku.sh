#!/bin/bash

# This script will quit on the first error that is encountered.
set -e

CIRCLE=$1

if [ $CIRCLE ]
then
    git push https://heroku:$HEROKU_API_KEY@git.heroku.com/heartbotapp.git master
else
    git push heroku master
fi
