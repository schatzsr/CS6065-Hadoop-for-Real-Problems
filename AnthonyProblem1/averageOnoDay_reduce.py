#!/usr/bin/env python

import sys
import string

total_count = 0
mon_count = 0
tue_count = 0
wed_count = 0
thu_count = 0
fri_count = 0
sat_count = 0
sun_count = 0

for line in sys.stdin:
    (key,val) = line.strip().split('\t',1)
    try:
        day = val
        if key == 'Ono':
            total_count += 1
            if val is "Mon":
                mon_count += 1
            if val is "Tue":
                tue_count += 1
            if val is "Wed":
                wed_count += 1
            if val is "Thu":
                thu_count += 1
            if val is "Fri":
                fri_count += 1
            if val is "Sat":
                sat_count += 1
            if val is "Sun":
                sun_count += 1
    except:
        continue
       
average_mon_value = round(float(mon_count)/float(total_count), 3)
average_tue_value = round(float(tue_count)/float(total_count), 3)
average_wed_value = round(float(wed_count)/float(total_count), 3)
average_thu_value = round(float(thu_count)/float(total_count), 3)
average_fri_value = round(float(fri_count)/float(total_count), 3)
average_sat_value = round(float(sat_count)/float(total_count), 3)
average_sun_value = round(float(sun_count)/float(total_count), 3)

print '%s\t%s' % ('Monday Average:',average_mon_value)
print '%s\t%s' % ('Monday Average:',average_tue_value)
print '%s\t%s' % ('Monday Average:',average_wed_value)
print '%s\t%s' % ('Monday Average:',average_thu_value)
print '%s\t%s' % ('Monday Average:',average_fri_value)
print '%s\t%s' % ('Monday Average:',average_sat_value)
print '%s\t%s' % ('Monday Average:',average_sun_value)
