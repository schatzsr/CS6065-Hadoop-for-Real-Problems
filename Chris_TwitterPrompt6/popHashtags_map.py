#!/usr/bin/env python


import sys
import string
import json

#file = open("test.txt",'r')

#for line in file:
for line in sys.stdin:
    tweet = json.loads(line)
    try:
        datetime = tweet["created_at"]
        weekday = datetime[:3]
        hour = datetime[11:13]
        hashtags = tweet["entities"]["hashtags"]
        for hashtag in hashtags:
            print "%s\t%s\t%s" % (hashtag["text"],weekday,hour)
    except:
        continue

#file.close
