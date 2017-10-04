#!/bin/bash

DATE=$1; 
LOGS=; 

for D in {0..13}; do 
PAST_DATE=`date -d "${DATE} -${D} days" +%F`; 
LOGS="${LOGS} /user/sandello/logs/access.log.${PAST_DATE}"; 
done; 

yarn jar /opt/hadoop/hadoop-streaming.jar \
-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=2 \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.text.key.comparator.options="-k1,1 -k2,2" \
-files mapper1.py,reducer1.py \
-mapper "mapper1.py" \
-reducer "reducer1.py" \
-input ${LOGS} \
-output /user/imorozov/hw1/group4/$1-temp \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-numReduceTasks 10

yarn jar /opt/hadoop/hadoop-streaming.jar \
-files mapper2.py,reducer2.py \
-mapper "mapper2.py" \
-reducer "reducer2.py" \
-input /user/imorozov/hw1/group4/$1-temp \
-output /user/imorozov/hw1/group4/$1-res \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-numReduceTasks 1

hadoop fs -getmerge /user/imorozov/hw1/group4/$1-res/ ~/hw1/group4/results/$1.txt