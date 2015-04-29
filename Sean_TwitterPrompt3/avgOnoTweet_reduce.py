#!/usr/bin/env python

# REDUCE FUNCTION
# How does @PrezOno's tweet length compare to the average of all others?  
# What is his average length?  All others?

import sys
import string


prezono_length_sum = 0
prezono_tweet_count = 0
others_length_sum = 0
others_tweet_count = 0

for line in sys.stdin:
    try:
        (key,val) = line.strip().split('\t')
        val = val.split(',')
        if key == 'PrezOno':
            prezono_length_sum += int(val[0])
            prezono_tweet_count += int(val[1])
        elif key == 'OtherUser':
            others_length_sum += int(val[0])
            others_tweet_count += int(val[1])
    except:
        continue

if (prezono_length_sum or prezono_tweet_count) == 0:
    print "No tweets from PrezOno"
else:
    prezono_avg_length = float(prezono_length_sum) / float(prezono_tweet_count)
    print "PrezOno's Average Tweet Length: %s" % prezono_avg_length

others_avg_length = float(others_length_sum) / float(others_tweet_count)
print "Others' Average Tweet Length: %s" % others_avg_length
