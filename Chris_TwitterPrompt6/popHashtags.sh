#!/bin/bash
hadoop fs -rm -r /user/mcveigca/$2
hadoop jar $HADOOP_INSTALL/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -input $1 -output $2 -file popHashtags_map.py popHashtags_reduce.py -mapper popHashtags_map.py -reducer popHashtags_reduce.py
