#!/bin/bash
hadoop fs -rm -r /user/schatzsr/$2
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file avgOnoTweet_map.py avgOnoTweet_reduce.py -mapper avgOnoTweet_map.py -reducer avgOnoTweet_reduce.py
