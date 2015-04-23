import unittest

from bot.messages import get_mongo


class TestGetMongo(unittest.TestCase):

    def test_get_mongo_no_uri(self):
        self.assertEqual(None, get_mongo('mongodb://bogus'))

    def test_get_mongo_with_uri(self):
        self.assertFalse(get_mongo('mongodb://127.0.0.1/heartbottest') is None)
