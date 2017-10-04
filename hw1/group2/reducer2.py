#!/usr/bin/env python

import sys

total_sessions, total_time, total_length = 0, 0, 0

for line in sys.stdin:
	items = line.strip().split('\t')
	total_time += int(items[0])
	total_length += int(items[1])
	total_sessions += int(items[2])

print "%.3f\t%.3f" % (float(total_time) / total_sessions, 
	float(total_length) / total_sessions)