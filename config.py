### VARIABLES ###
search = 'gatos'  # TERM TO SEARCH
actionCount = 1000  # NUMBER OF ACTIONS TO EXECUTE (LIKES AND/OR REWTWEETS)
timeBetweenActions = 300  # IN SECONDS

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
enableRetweets = True


print("LOADED CONFIGS")
