import unittest

from bot.messages import get_mongo


class TestGetMongo(unittest.TestCase):

    def test_get_mongo_no_uri(self):
        mongo = get_mongo('mongodb://bogus')

        self.assertEqual(None, mongo)

    def test_get_mongo_with_valid_uri(self):
        mongo = get_mongo('mongodb://127.0.0.1/heartbottest')

        self.assertFalse(mongo is None)
