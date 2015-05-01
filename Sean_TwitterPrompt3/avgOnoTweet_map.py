#!/usr/bin/env python

# MAP FUNCTION
# How does @PrezOno's tweet length compare to the average of all others?  
# What is his average length?  All others?

import sys
import string


prezono_length_sum = 0
prezono_tweet_count = 0
others_length_sum = 0
others_tweet_count = 0

# Input in the form "screenname \t tweet_length \t tweet_date \t popularity \t tweet_id"
for line in sys.stdin:
    try:
        (screenname, tweet_length, tweet_date, popularity, tweet_id) = line.strip().split('\t')
        tweet_length = int(tweet_length)
        if screenname == 'PrezOno':
            prezono_length_sum += tweet_length
            prezono_tweet_count += 1
        else:
            others_length_sum += tweet_length
            others_tweet_count += 1
        
    except:
        continue

print 'PrezOno\t%s\t%s' % (prezono_length_sum, prezono_tweet_count)
print 'OtherUser\t%s\t%s' % (others_length_sum, others_tweet_count)
