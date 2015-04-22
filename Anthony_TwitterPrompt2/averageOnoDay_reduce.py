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
        key = str(key)
        if key == 'Mon':
            total_count += 1
            mon_count += 1
        elif key == 'Tue':
            total_count += 1
            tue_count += 1
        elif key == 'Wed':
            total_count += 1
            wed_count += 1
        elif key == 'Thu':
            total_count += 1
            thu_count += 1
        elif key == 'Fri':
            total_count += 1
            fri_count += 1
        elif key == 'Sat':
            total_count += 1
            sat_count += 1
        elif key == 'Sun':
            total_count += 1
            sun_count += 1
        else:
            print key
    except:
        continue

if mon_count > 0:
    average_mon_value = round(float(mon_count)/float(total_count), 3)
    print '%s\t%s' % ('Monday Average:',average_mon_value)
if tue_count > 0:
    average_tue_value = round(float(tue_count)/float(total_count), 3)
    print '%s\t%s' % ('Tuesday Average:',average_tue_value)
if wed_count > 0:
    average_wed_value = round(float(wed_count)/float(total_count), 3)
    print '%s\t%s' % ('Wednesday Average:',average_wed_value)
if thu_count > 0:
    average_thu_value = round(float(thu_count)/float(total_count), 3)
    print '%s\t%s' % ('Thursday Average:',average_thu_value)
if fri_count > 0:
    average_fri_value = round(float(fri_count)/float(total_count), 3)
    print '%s\t%s' % ('Friday Average:',average_fri_value)
if sat_count > 0:
    average_sat_value = round(float(sat_count)/float(total_count), 3)    
    print '%s\t%s' % ('Saturday Average:',average_sat_value)
if sun_count > 0:
    average_sun_value = round(float(sun_count)/float(total_count), 3)
    print '%s\t%s' % ('Sunday Average:',average_sun_value)
