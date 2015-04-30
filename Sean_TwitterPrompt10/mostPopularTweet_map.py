#!/usr/bin/env python

# MAP FUNCTION
# For each day, what was the most retweeted or most favorited tweet?

import sys
import string
import json


day_dict = dict()

# Commented lines are for using the tweet text instead of tweet id
for line in sys.stdin:
    tweet = json.loads(line)
    try:
        created_at = tweet['created_at']
        tweet_date = created_at[4:10]
        # text = tweet['text']
        tweet_id = tweet['id']
        retweet_count = tweet['retweet_count']
        favorite_count = tweet['favorite_count']
        popularity = max(retweet_count, favorite_count)

        if (tweet_date not in day_dict.keys()) or (day_dict[tweet_date][0] < popularity):
            # day_dict[tweet_date] = (popularity, text)
            day_dict[tweet_date] = (popularity, tweet_id)
        
    except:
        continue

for key in day_dict.keys():
    print '%s\t%s\t%s' % (key, day_dict[key][0], day_dict[key][1])
