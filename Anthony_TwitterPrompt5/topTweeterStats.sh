#!/bin/bash
hadoop fs -rm -r /user/kleiseaj/$2
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file topTweeterStats_map.py topTweeterStats_reduce.py -mapper topTweeterStats_map.py -reducer topTweeterStats_reduce.py
