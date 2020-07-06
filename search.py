import GetOldTweets3 as got
from pprint import pprint as pp

user = 'pascivite'
count = 10

# Creation of query object
tweetCriteria = got.manager.TweetCriteria().setUsername(user).setMaxTweets(count)

# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

# option 1
# for tweet in tweets:
#     pp(tweet.__dict__)
#     print()
#     print('---------')
#     print()

# option 2
for i in range(1):
    pp(tweets[0].__dict__)
