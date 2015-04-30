#!/usr/bin/env python

# MAP FUNCTION
# How does @PrezOno's tweet length compare to the average of all others?  
# What is his average length?  All others?

import sys
import string
import json


prezono_length_sum = 0
prezono_tweet_count = 0
others_length_sum = 0
others_tweet_count = 0

for line in sys.stdin:
    tweet = json.loads(line)
    try:
        user = tweet['user']
        tweet_length = len(tweet['text'])
        if user['screen_name'] == 'PrezOno':
            prezono_length_sum += tweet_length
            prezono_tweet_count += 1
        else:
            others_length_sum += tweet_length
            others_tweet_count += 1
        
    except:
        continue

print 'PrezOno\t%s,%s' % (prezono_length_sum, prezono_tweet_count)
print 'OtherUser\t%s,%s' % (others_length_sum, others_tweet_count)