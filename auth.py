import tweepy
import time
from access import *

auth = tweepy.OAuthHandler(key, secretkey)
auth.set_access_token(token, secrettoken)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
