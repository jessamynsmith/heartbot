from twitter_bot import Settings


class HeartBotSettings(Settings):
    """ Settings for HeartBot """
    def __init__(self):
        super(HeartBotSettings, self).__init__()
        self.MESSAGE_PROVIDER = 'bot.messages.ComplimentProvider'
        self.SINCE_ID_PROVIDER = 'bot.since_id.MongoProvider'
