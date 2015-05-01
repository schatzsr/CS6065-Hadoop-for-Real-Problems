#!/bin/bash
hadoop fs -rm -r /user/schatzsr/$2
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -D mapred.reduce.tasks=0 -input $1 -output $2 -file printdata_map.py -mapper printdata_map.py
