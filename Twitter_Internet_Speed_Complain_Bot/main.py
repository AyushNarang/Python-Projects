from internet_speed_twitter_bot import InternetSpeedTwitterBot

PROMISED_UP = 50
PROMISED_DOWN = 150
USERNAME = ""
PASSWORD = ""

bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
# bot.get_internet_speed()
bot.tweet_at_provider(USERNAME, PASSWORD, PROMISED_UP, PROMISED_DOWN)