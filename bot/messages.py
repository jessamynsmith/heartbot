import random
import os

import pymongo
from twitter_bot import SettingsError


def get_mongo(mongo_uri):
    """ Get mongo database instance based on uri
    :param mongo_uri: connection string uri for mongo
    :return: mongo instance, with database selected
    """
    mongo = pymongo.MongoClient(mongo_uri)
    if mongo:
        config = pymongo.uri_parser.parse_uri(mongo_uri)
        if config['database']:
            return mongo[config['database']]
    return None


class ComplimentProvider(object):

    def __init__(self, mongo_uri=None):
        if not mongo_uri:
            mongo_uri = os.environ.get('MONGOLAB_URI')
            if not mongo_uri:
                raise SettingsError("You must supply mongo_uri or set the MONGOLAB_URI "
                                    "environment variable.")
        self.mongo = get_mongo(mongo_uri)

    def create(self):
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
