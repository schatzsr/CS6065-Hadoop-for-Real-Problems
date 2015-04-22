#!/bin/bash
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file averageOnoDay_map.py averageOnoDay_reduce.py -mapper averageOnoDay_map.py -reducer averageOnoDay_reduce.py
