#!/usr/bin/env python

import sys
import shlex

print >> sys.stderr, "reducer started"

total_sessions, total_time, total_length = -1, 0, 0
cur_time, cur_length = 0, 0
prev_ip, prev_moment = None, -3000

for line in sys.stdin:
    items = line.strip().split('\t')
    ip, moment = items[0], int(items[1])
    if ip != prev_ip or moment - prev_moment > 1800:
        prev_ip = ip
        total_time += cur_time
        total_length += cur_length
        total_sessions += 1
        cur_time, cur_length = 0, 1
    else:
        cur_length += 1
        cur_time += moment - prev_moment
    print >> sys.stderr, ip, moment, cur_time
    prev_moment = moment

total_time += cur_time
total_length += cur_length
total_sessions += 1

print "%d\t%d\t%d" % (total_time, total_length, total_sessions) 
print >> sys.stderr, "reducer finished"