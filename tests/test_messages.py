import unittest

from mock import patch
from twitter_bot import SettingsError

from bot.messages import ComplimentProvider


class TestComplimentProvider(unittest.TestCase):

    def setUp(self):
        self.provider = ComplimentProvider(mongo_uri='mongodb://localhost/heartbottest')
        self.provider.mongo.sentences.delete_many({})
        self.provider.mongo.words.delete_many({})

    @patch('os.environ.get')
    def test_constructor_empty_mongo_env_var(self, mock_env_get):
        mock_env_get.return_value = ''

        try:
            ComplimentProvider()
            self.fail("Should not be able to instantiate provider without mongo")
        except SettingsError as e:
            error = "You must supply mongo_uri or set the MONGOLAB_URI environment variable."
            self.assertEqual(error, '{0}'.format(e))

    def test_create_no_data(self):
        message = self.provider.create()

        self.assertEqual('No compliments found.', message)

    def test_create_simple_sentence(self):
        sentence = {'type': None, 'sentence': 'You shine brightly.'}
        self.provider.mongo['sentences'].insert_one(sentence)

        message = self.provider.create()

        self.assertEqual('You shine brightly.', message)

    def test_create_substitution_sentence(self):
        sentence = {'type': 'noun', 'sentence': 'I value your {0}.'}
        self.provider.mongo['sentences'].insert_one(sentence)
        self.provider.mongo['words'].insert_one({'type': 'noun', 'word': 'courage'})

        message = self.provider.create()

        self.assertEqual('I value your courage.', message)
