#!/usr/bin/env python

import sys
import shlex

print >> sys.stderr, "reducer started"

total_hits, unique_users = 0, 0
prev_ip = None

for line in sys.stdin:
	items = line.strip().split('\t')
	ip, count = items[0], int(items[1])
	if ip != prev_ip:
		prev_ip = ip
		unique_users += 1
	total_hits += 1

print "%d\t%d" % (total_hits, unique_users)
print >> sys.stderr, "reducer finished"