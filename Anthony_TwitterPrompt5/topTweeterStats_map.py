#!/usr/bin/env python

import sys
import string
import json
import traceback
import operator

user_list = []

#text = open('exampletwitterdata.txt', 'r')
#print 'opened'
for line in sys.stdin:
#for line in text:
    #print 'load'
    tweet_data = json.loads(line)
    try:
        user_info = tweet_data["user"]
        user_name = user_info["screen_name"]
        tweet_content = tweet_data["text"]
        tweet_len = len(tweet_content)
        user_list.append([user_name, tweet_len])
    except:
        continue

top_dict = {}
for user in user_list:
    username = user[0]
    value = user[1]
    #print username
    #print value
    if username in top_dict:
        tmp = top_dict[username][1]
        #print 'did it work' + str(top_dict[username][1])
        #print tmp
        top_dict[username][0] += 1
        top_dict[username][1] += value
    else:
        #print 'here'
        top_dict[username] = [1, value]

sorted_user = sorted(top_dict.items(), key=lambda e: e[1][1])
print sorted_user
for user in sorted_user[:5]:
    print str(user[0]) + '\t' + str(user[1][0]) + '\t' + str(user[1][1])
#print 'break \n'
for user in sorted_user[-5:]:
    print str(user[0]) + '\t' + str(user[1][0]) + '\t' + str(user[1][1])
