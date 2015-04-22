#!/usr/bin/env python


import sys
import string


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


for key in vals[].keys():
    print "%s:\t%s" % (key, float(vals[key])/total)


print "total tweets: ", total

