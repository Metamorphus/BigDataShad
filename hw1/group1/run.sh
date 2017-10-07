#!/bin/bash

hdfs dfs -rm -rf /user/imorozov/res/hw1/group1/$1-temp
yarn jar /opt/hadoop/hadoop-streaming.jar \
-files mapper1.py,reducer1.py \
-mapper "mapper1.py" \
-reducer "reducer1.py" \
-input /user/bigdatashad/logs/$1 \
-output /user/imorozov/res/hw1/group1/$1-temp \
-numReduceTasks 10

hdfs dfs -rm -rf /user/imorozov/res/hw1/group1/$1-res
yarn jar /opt/hadoop/hadoop-streaming.jar \
-files mapper2.py,reducer2.py \
-mapper "mapper2.py" \
-reducer "reducer2.py" \
-input /user/imorozov/res/hw1/group1/$1-temp \
-output /user/imorozov/res/hw1/group1/$1-res \
-numReduceTasks 1

hadoop fs -getmerge /user/imorozov/res/hw1/group1/$1-res/ ~/res/hw1/group1/$1.txt
