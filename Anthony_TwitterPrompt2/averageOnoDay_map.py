#!/usr/bin/env python

import sys
import string
import json
import traceback

for line in sys.stdin:
    tweet_data = json.loads(line)
    try:
        user_info = tweet_data["user"]
        user_id = user_info["id"]
        if user_id == 211178363:
            date_field = tweet_data["created_at"]
            day = date_field[:3]
            print '%s\t1' % day
    except:
        #print '%s\t1' % traceback.print_exc()
