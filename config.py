### VARIABLES ###
search = 'gatinho'  # TERM TO SEARCH
actionCount = 1000  # NUMBER OF ACTIONS TO EXECUTE (LIKES AND/OR REWTWEETS)
timeBetweenActions = 300  # IN SECONDS (PLACEHOLDER: 5MIN)
timeBetweenTweets = 1800  # IN SECONDS (PLACEHOLDER: 30MIN)

### LOG MESSAGES (SO YOU KNOW ITS WORKING) ###
likeLogMessage = 'Liked a tweet'
retweetLogMessage = 'Retweeted a tweet'
stopIterationMessage = 'Iteration stopped'
searchLogMessage = "Search term: " + search
actionCountLogMessage = "Time " + str(actionCount)

### CUSTOM ERROR MESSAGES ###
allDisabledMsg = '[ERROR] All options are disabled!'

### OPTIONS ###
enableLikes = True
enableRetweets = False


print("LOADED CONFIGS")
