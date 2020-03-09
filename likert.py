import tweepy
import time
import config
from auth import api
import functions


def likert():

    functions.likeRetweet(config.search, config.actionCount, config.likeLogMessage,
                          config.retweetLogMessage, config.timeBetweenActions)


# likert()
