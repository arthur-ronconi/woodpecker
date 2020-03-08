import tweepy
import time
import config
import auth


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
                print(likeLogMessage + " from " + name + " - " + username)

            def retweetTweet():
                tweet.retweet()
                print(retweetLogMessage + " from " + name + " - " + username)
            try:
                if config.enableLikes and config.enableRetweets:
                    likeTweet()
                    retweetTweet()
                    print("\n" + msg + "\n")
                    time.sleep(timeBetweenActions)

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
