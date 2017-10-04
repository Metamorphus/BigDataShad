#!/bin/bash
yarn jar /opt/hadoop/hadoop-streaming.jar \
-files mapper1.py,reducer1.py \
-mapper "mapper1.py" \
-reducer "reducer1.py" \
-input /user/sandello/logs/access.log.$1 \
-output /user/imorozov/hw1/group1/$1-temp \
-numReduceTasks 10

yarn jar /opt/hadoop/hadoop-streaming.jar \
-files mapper2.py,reducer2.py \
-mapper "mapper2.py" \
-reducer "reducer2.py" \
-input /user/imorozov/hw1/group1/$1-temp \
-output /user/imorozov/hw1/group1/$1-res \
-numReduceTasks 1

hadoop fs -getmerge /user/imorozov/hw1/group1/$1-res/ ~/hw1/group1/results/$1.txt