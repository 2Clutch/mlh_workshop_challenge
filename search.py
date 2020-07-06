import GetOldTweets3 as got
from pprint import pprint as pp


class TwitterScraper:

    def __init__(self):
        self.user = 'pascivite'
        self.count = 10
        self.tweet_criteria = None
        self.tweets = None

    def scrape_latest_tweets(self):
        # Creation of query object
        self.tweet_criteria = got.manager.TweetCriteria().setUsername(self.user).setMaxTweets(self.count)

        # Creation of list that contains all tweets
        self.tweets = got.manager.TweetManager.getTweets(self.tweet_criteria)

        return self.tweets


if __name__ == '__main__':
    test = TwitterScraper()
    tweets = test.scrape_latest_tweets()

    for i in range(1):
        pp(tweets[0].__dict__)
