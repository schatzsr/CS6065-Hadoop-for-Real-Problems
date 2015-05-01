#!/usr/bin/env python

# MAP FUNCTION
# Retrieves the twitter data to be used in other MapReduce programs

import sys
import string
import json


for line in sys.stdin:
    tweet = json.loads(line)
    try:
        # avgOnoTweet
        user = tweet['user']
        screenname = user['screen_name']
        tweet_length = len(tweet['text'])

        #mostPopularTweet
        created_at = tweet['created_at']
        tweet_date = created_at[4:10]
        tweet_id = tweet['id']
        retweet_count = int(tweet['retweet_count'])
        favorite_count = int(tweet['favorite_count'])
        popularity = max(retweet_count, favorite_count)

        print '%s\t%s\t%s\t%s\t%s' % (screenname, tweet_length, tweet_date, popularity, tweet_id)
        
    except:
        continue
