#!/bin/bash
hadoop fs -rm -r /user/mcveigca/$2
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file averageOnoHour_map.py averageOnoHour_reduce.py -mapper averageOnoHour_map.py -reducer averageOnoHour_reduce.py
