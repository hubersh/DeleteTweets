#!/usr/bin/env python

import csv
import twitter
import time
from dateutil.parser import parse


class TweetDeleter:
    def __init__(self, api_key, api_secret, access_token, access_token_secret):
        self.api = twitter.Api(consumer_key=api_key,
                               consumer_secret=api_secret,
                               access_token_key=access_token,
                               access_token_secret=access_token_secret)

    def delete(self, filename, date="", restrict=""):
        with open(filename) as f:

            total = 0
            for index, row in enumerate(csv.DictReader(f)):
                tweet_id = int(row["tweet_id"])
                tweet_date = parse(row["timestamp"], ignoretz=True).date()

                if date != "" and tweet_date >= parse(date).date():
                    continue

                if (restrict == "retweet" and row["retweeted_status_id"] == ""
                        or restrict == "reply" and row["in_reply_to_status_id"] == ""):
                    continue

                try:
                    print "Deleting tweet #{0} ({1})".format(tweet_id, tweet_date)

                    _ = self.api.DestroyStatus(tweet_id)
                    total = index
                    time.sleep(1)

                except Exception, e:
                    print "Exception: %s\n" % e.message

            print "Number of deleted tweets: %s\n" % total


if __name__ == "__main__":

    deleter = TweetDeleter(api_key="", api_secret="", access_token="", access_token_secret="")

    deleter.delete("tweets.csv", date='2018-11-01', restrict='retweet')

