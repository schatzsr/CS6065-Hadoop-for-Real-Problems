#!/usr/bin/env python

import sys
import string
import operator

total_count = 0
user_dict = {}
leng_dict = {}

for line in sys.stdin:
    (key,val,val2) = line.strip().split('\t',2)
    try:
        user_key = str(key)
        #print user_key
        user_val = int(val)
        #print user_val
        leng_val = int(val2)
        if user_key in user_dict:
            temp_val = user_dict[user_key]
            temp_val += user_val
            temp_val2 = leng_dict[user_key]
            temp_val2 += leng_val
            user_dict[user_key] = temp_val
            leng_dict[user_key] = temp_val2
        else:
            user_dict[user_key] = user_val
            leng_dict[user_key] = leng_val
    except:
        continue

sorted_user = sorted(user_dict.items(), key=operator.itemgetter(1))
sorted_leng = sorted(leng_dict.items(), key=operator.itemgetter(1))
print 'Top 5\n'
print sorted_user[:5]
print sorted_leng[:5]
print '\nBottom 5\n'
print sorted_user[-5:]
print sorted_leng[-5:]
