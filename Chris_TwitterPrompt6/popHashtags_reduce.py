#!/usr/bin/env python


import sys
import string

total = 0

hour_keys = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
day_keys = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

days = dict((key,{}) for key in day_keys)
hours = dict((key,{}) for key in hour_keys)


for line in sys.stdin:
    try:
        (hashtag,day,hour) = line.strip().split('\t')
        total += 1

        if hashtag in days[day].keys():
            days[day][hashtag] += 1
        else:
            days[day][hashtag] = 1

        if hashtag in hours[hour].keys():
            hours[hour][hashtag] += 1
        else:
            hours[hour][hashtag] = 1
    except:
        continue

# Finding the max for each day and placing it in a new dict to hold these vals
for key1 in days.keys():
    tmp_tag = ""
    tmp_max = 0
    for key2 in days[key1].keys():
        if days[key1][key2] > tmp_max:
            tmp_tag = key2
            tmp_max = days[key1][key2]
    print "%s\t%s\t%s" % (key1,tmp_tag,tmp_max)

for key1 in hours.keys():
    tmp_tag = ""
    tmp_max = 0
    for key2 in hours[key1].keys():
        if hours[key1][key2] > tmp_max:
            tmp_tag = key2
            tmp_max = hours[key1][key2]
    print "%s\t%s\t%s" % (key1,tmp_tag,tmp_max)


print "Total tweets:", total

