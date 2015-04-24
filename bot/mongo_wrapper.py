import pymongo


def get_mongo(mongo_uri):
    """ Get mongo database instance based on uri
    :param mongo_uri: connection string uri for mongo
    :return: mongo instance, with database selected
    """
    mongo = pymongo.MongoClient(mongo_uri)
    config = pymongo.uri_parser.parse_uri(mongo_uri)
    if config['database']:
        return mongo[config['database']]
    return None
