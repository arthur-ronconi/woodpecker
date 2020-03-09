import tweepy
import time
import config
import auth
import random


class likeRetweet:

    def __init__(self, search, actionCount, likeLogMessage, retweetLogMessage, timeBetweenActions):
        self.config = config
        self.search = search
        self.actionCount = actionCount
        self.likeLogMessage = likeLogMessage
        self.timeBetweenActions = timeBetweenActions
        api = auth.api
        for tweet in tweepy.Cursor(api.search, search).items(actionCount):
            name = tweet.user.name
            username = "@" + tweet.user.screen_name
            msg = tweet.text

            def likeTweet():
                tweet.favorite()
                print(likeLogMessage + " from " +
                      name + " - " + username + '\n')
                time.sleep(config.timeBetweenActions)

            def retweetTweet():
                tweet.retweet()
                print(retweetLogMessage + " from " +
                      name + " - " + username + '\n')
                time.sleep(config.timeBetweenActions)
            try:
                if config.enableLikes and config.enableRetweets:
                    likeTweet()
                    retweetTweet()
                    print(msg + "\n")

                elif config.enableLikes == True and config.enableRetweets == False:
                    likeTweet()
                elif config.enableRetweets == True and config.enableLikes == False:
                    retweetTweet()
                else:
                    print(config.allDisabledMsg)
                    break
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                print(config.stopIterationMessage)
                break


class meow:
    def __init__(self):
        api = auth.api
        self.api = api

    def meowGen():
        rn = random.randrange(1, 8)
        letters = 'a' * rn
        meow = 'mi' + letters + 'u '
        return meow

    def twt():
        api = auth.api
        rn = random.randrange(1, 8)
        text = []
        for i in range(rn):
            text.append(meow.meowGen())
        catTweet = ''.join(text)
        api.update_status(catTweet)
        print('Published a tweet: \n'+catTweet+'\n')
