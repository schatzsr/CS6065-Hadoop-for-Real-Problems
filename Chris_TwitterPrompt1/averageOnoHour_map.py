#!/usr/bin/env python


import sys
import string
import json


keys = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
vals = dict((key, 0) for key in keys)
for line in sys.stdin:
    tweet = json.loads(line)
    try:
        user = tweet["user"]
        if user["screen_name"] == 'PrezOno':
            datetime = tweet["created_at"]
            hour = datetime[11:13]
            vals[hour] += 1
    except:
        continue
for key in vals.keys():
    if vals[key] > 0:
        print "%s\t%s" % (key,vals[key])

