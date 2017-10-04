#!/usr/bin/env python

import sys
import shlex

print >> sys.stderr, 'started mapper'

total_hits = 0

for line in sys.stdin:
	items = shlex.split(line.lower())
	ip, code = items[0], int(items[6])
	if (code != 200):
		continue
	date_items = items[3].split(':')
	request_time = int(date_items[1]) * 3600 + int(date_items[2]) * 60 + int(date_items[3])
	print "%s\t%d" % (ip, request_time)
	total_hits += 1

print >> sys.stderr, 'finished mapper'