import unittest

from mock import patch

from bot.settings import HeartBotSettings


class TestSettings(unittest.TestCase):

    @patch('os.environ.get')
    def test_constructor_valid(self, mock_env_get):
        mock_env_get.return_value = 'bogus'

        settings = HeartBotSettings()

        self.assertEqual('bogus', settings.OAUTH_TOKEN)
        self.assertEqual('bot.messages.ComplimentProvider', settings.MESSAGE_PROVIDER)
