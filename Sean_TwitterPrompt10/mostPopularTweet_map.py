#!/usr/bin/env python

# MAP FUNCTION
# For each day, what was the most retweeted or most favorited tweet?

import sys
import string


day_dict = dict()

# Input in the form "screenname \t tweet_length \t tweet_date \t popularity \t tweet_id"
for line in sys.stdin:
    try:
        (screenname, tweet_length, tweet_date, popularity, tweet_id) = line.strip().split('\t')
        popularity = int(popularity)

        if (tweet_date not in day_dict.keys()) or (day_dict[tweet_date][0] < popularity):
            day_dict[tweet_date] = (popularity, tweet_id)
        
    except:
        continue

for key in day_dict.keys():
    print '%s\t%s\t%s' % (key, day_dict[key][0], day_dict[key][1])
