import unittest

from mock import patch
from twitter_bot import SettingsError

from bot.since_id import MongoProvider


class TestMongoProvider(unittest.TestCase):

    def setUp(self):
        self.provider = MongoProvider(mongo_uri='mongodb://localhost/heartbottest')
        self.provider.mongo.since_id.delete_many({})

    @patch('os.environ.get')
    def test_constructor_empty_mongo_env_var(self, mock_env_get):
        mock_env_get.return_value = ''

        try:
            MongoProvider()
            self.fail("Should not be able to instantiate provider without mongo")
        except SettingsError as e:
            error = "You must supply mongo_uri or set the MONGOLAB_URI environment variable."
            self.assertEqual(error, '{0}'.format(e))

    def test_get_since_id_none_exist(self):
        since_id = self.provider.get()

        self.assertEqual('', since_id)

    def test_get_since_id_exists(self):
        self.provider.mongo.since_id.insert_one({'value': '33'})

        since_id = self.provider.get()

        self.assertEqual('33', since_id)

    def test_set(self):
        self.provider.mongo.since_id.insert_one({'value': '11'})

        result = self.provider.set('22')

        self.assertFalse(result is None)
        self.assertEqual('22', self.provider.get())

    def test_delete(self):
        self.provider.mongo.since_id.insert_one({'value': '11'})

        result = self.provider.delete()

        self.assertFalse(result is None)
        self.assertEqual('', self.provider.get())
