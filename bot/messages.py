from __future__ import absolute_import
import random
import os

from twitter_bot import SettingsError

from .mongo_wrapper import get_mongo


class ComplimentProvider(object):

    def __init__(self, mongo_uri=None):
        if not mongo_uri:
            mongo_uri = os.environ.get('MONGOLAB_URI')
            if not mongo_uri:
                raise SettingsError("You must supply mongo_uri or set the MONGOLAB_URI "
                                    "environment variable.")
        self.mongo = get_mongo(mongo_uri)

    def create(self, mention, max_message_length):
        """
        Create a message
        :param mention: JSON object containing mention details from Twitter
        :param max_message_length: Maximum allowable length for created message
        :return: a message
        """
        num_records = self.mongo.sentences.count()
        if num_records < 1:
            return 'No compliments found.'
        index = random.randint(0, num_records-1)
        sentence = self.mongo.sentences.find().limit(1).skip(index)[0]
        message = sentence['sentence']
        if sentence['type']:
            words = self.mongo.words.find({'type': sentence['type']})
            index = random.randint(0, words.count()-1)
            word = words.limit(1).skip(index)[0]
            message = message.format(word['word'])
        return message
