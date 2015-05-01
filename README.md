heartbot
========

[![Build Status](https://circleci.com/gh/jessamynsmith/heartbot.svg?style=shield)](https://circleci.com/gh/jessamynsmith/heartbot)
[![Coverage Status](https://coveralls.io/repos/jessamynsmith/heartbot/badge.svg?branch=master)](https://coveralls.io/r/jessamynsmith/heartbot?branch=master)

TwitterBot that replies to any mentions with a compliment, or posts a random compliment.
Please read Twitter's [Automation rules and best practices](https://support.twitter.com/articles/76915-automation-rules-and-best-practices/)
before setting up a bot.

Settings are populated from environment variables. The authentication variables can be
[obtained from your Twitter account](https://dev.twitter.com/oauth/overview/application-owner-access-tokens/).
You will need to set these locally to run the bot locally, and on heroku if you deploy there.
- TWITTER_CONSUMER_KEY
- TWITTER_CONSUMER_SECRET
- TWITTER_OAUTH_SECRET
- TWITTER_OAUTH_TOKEN

You will need to set the following environment variable locally:
export MONGOLAB_URI=mongodb://127.0.0.1/heartbot

This project is set up to be deployed to heroku, using the Heroku Scheduler and MongoLab addons.
There are two scheduled tasks set up:

    ./bin/run_bot.py post_message  # runs daily
    ./bin/run_bot.py reply_to_mentions  # runs every 10 minutes
 
You will also need to manually run the initialize data task initially, and any time you change the
list of compliments:

    ./bin/initialize_data.py 

Add Compliments
---------------

Edit bin/initialize_data.py and add compliments as desired. You can substitute up to one word (noun
or adjective) per sentence. The type field indicates what type of word to substitute. You can also
add a sentence to be used as-is, by specifying type=None. E.g.:
 
    sentences = [{'type': 'adjective', 'sentence': 'I really appreciate how {0} you are.'},
                 ...
                 {'type': None, 'sentence': 'My world is a better place with you in it.'}]

I'm happy to merge pull requests with appropriate compliments!

Development
-----------

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/heartbot.git

Set up virtualenv:

    mkvirtualenv heartbot
    pip install -r requirements/development.txt

Run tests with coverage (should be 100%) and check code style:

    coverage run -m nose
    coverage report -m
    flake8

Verify all supported Python versions:

    pip install tox
    tox

Run bot:

    ./bin/initialize_data.py            # Clears any current data and adds compliments to datastore
    ./bin/run_bot.py reply_to_mentions  # Check twitter stream for mentions, and reply
    ./bin/run_bot.py post_message       # Post a message to twitter
