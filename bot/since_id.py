from __future__ import absolute_import
import os

from twitter_bot import SettingsError

from .mongo_wrapper import get_mongo


class MongoProvider(object):

    def __init__(self, mongo_uri=None):
        if not mongo_uri:
            mongo_uri = os.environ.get('MONGOLAB_URI')
            if not mongo_uri:
                raise SettingsError("You must supply mongo_uri or set the MONGOLAB_URI "
                                    "environment variable.")
        self.mongo = get_mongo(mongo_uri)

    def get(self):
        since_id = ''
        result = self.mongo.since_id.find().limit(1)
        if result.count():
            since_id = result[0]['value']
        return since_id

    def set(self, since_id):
        self.mongo.since_id.delete_many({})
        return self.mongo.since_id.insert_one({'value': since_id})

    def delete(self):
        return self.mongo.since_id.delete_many({})
