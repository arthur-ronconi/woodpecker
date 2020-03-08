import tweepy
import time
import config
from auth import api
import functions


def run():
    print(config.searchLogMessage)
    print(config.actionCountLogMessage)
    functions.likeRetweet(config.search, config.actionCount, config.likeLogMessage,
                          config.retweetLogMessage, config.timeBetweenActions)


run()
