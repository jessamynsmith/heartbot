from twitter_bot import Settings


class HeartBotSettings(Settings):
    """ Settings for HeartBot """
    def __init__(self):
        super(HeartBotSettings, self).__init__()

        # Messages provider
        self.MESSAGE_PROVIDER = 'bot.messages.ComplimentProvider'
