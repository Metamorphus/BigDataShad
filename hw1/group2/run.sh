#!/bin/bash

yarn jar /opt/hadoop/hadoop-streaming.jar \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=2 \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.text.key.comparator.options="-k1,1 -k2,2n" \
-files mapper1.py,reducer1.py \
-mapper "mapper1.py" \
-reducer "reducer1.py" \
-input /user/sandello/logs/access.log.$1 \
-output /user/imorozov/hw1/group2/$1-temp \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-numReduceTasks 10

yarn jar /opt/hadoop/hadoop-streaming.jar \
-files mapper2.py,reducer2.py \
-mapper "mapper2.py" \
-reducer "reducer2.py" \
-input /user/imorozov/hw1/group2/$1-temp \
-output /user/imorozov/hw1/group2/$1-res \
-numReduceTasks 1

hadoop fs -getmerge /user/imorozov/hw1/group2/$1-res/ ~/hw1/group2/results/$1.txt