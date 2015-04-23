from twitter_bot import Settings

from bot.messages import ComplimentProvider
from bot.since_id import MongoProvider


class HeartBotSettings(Settings):
    """ Settings for HeartBot """
    def __init__(self):
        super(HeartBotSettings, self).__init__()
        self.MESSAGE_PROVIDER = ComplimentProvider
        self.SINCE_ID_PROVIDER = MongoProvider
