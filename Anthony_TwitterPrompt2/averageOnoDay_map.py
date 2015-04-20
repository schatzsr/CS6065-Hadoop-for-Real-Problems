#!/usr/bin/env python

import sys
import string
import json

for line in sys.stdin:
    tweet_data = json.loads(line)
    user_info = tweet_data["user"]
    user_id = user_info["id"]
    if user_id is 211178363:
        date_field = tweet_data["created_at"]
        day = date_field[:3]
        print 'Ono\t%s' % day
