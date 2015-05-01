#!/usr/bin/env python

# REDUCE FUNCTION
# For each day, what was the most retweeted or most favorited tweet?

import sys
import string


day_dict = dict()

for line in sys.stdin:
    try:
        (key, popularity, tweet_id) = line.strip().split('\t')
        popularity = int(popularity)
        
        if (key not in day_dict.keys()) or (day_dict[key][0] < popularity):
            day_dict[key] = (popularity, tweet_id)

    except:
        continue

for key in day_dict.keys():
    print 'Most popular tweet for %s (id only): %s' % (key, day_dict[key][1])
