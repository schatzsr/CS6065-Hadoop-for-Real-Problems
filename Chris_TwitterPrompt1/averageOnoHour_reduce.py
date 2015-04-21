#!/usr/bin/env python


import sys
import string
import traceback


num_0 = 0
num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0
num_7 = 0
num_8 = 0
num_9 = 0
num_10 = 0
num_11 = 0
num_12 = 0
num_13 = 0
num_14 = 0
num_15 = 0
num_16 = 0
num_17 = 0
num_18 = 0
num_19 = 0
num_20 = 0
num_21 = 0
num_22 = 0
num_23 = 0
total = 0


keys = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
vals = dict((key,0) for key in keys)

for line in sys.stdin:
    try:
        (key,val) = line.strip().split('\t')
        vals[key] += int(val)
        total += int(val)
    except:
        traceback.print_exc()
        continue
print "President Santa Ono's hourly average tweets:"

for key in vals.keys():
    print "%s:\t%s" % (key, vals[key])


print "total tweets: ", total

