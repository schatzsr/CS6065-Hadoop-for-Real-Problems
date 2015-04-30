#!/usr/bin/env python

import sys
import string
import json
import traceback

# QUESTION:
# What twitter user tweeted the most?  What is the top 5 longest tweeters?  Bottom 5?

user_dict = {}

#text = open('exampletwitterdata.txt', 'r')
#print 'opened'
for line in sys.stdin:
#for line in text:
    #print 'load'
    tweet_data = json.loads(line)
    try:
        #print 'got json'
        user_info = tweet_data["user"]
        #print 'found user'
        user_name = user_info["screen_name"]
        #print 'screen_name'
        tweet_content = tweet_data["text"]
        #print 'content'
        tweet_len = len(tweet_content)
        #print 'length'
        print str(user_name) + '\t' + '1' + '\t' + str(tweet_len)
    except:
        continue
