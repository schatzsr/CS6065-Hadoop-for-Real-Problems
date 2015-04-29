#!/bin/bash
hadoop fs -rm -r /user/schatzsr/$2
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file mostPopularTweet_map.py mostPopularTweet_reduce.py -mapper mostPopularTweet_map.py -reducer mostPopularTweet_reduce.py
