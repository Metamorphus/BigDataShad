#!/usr/bin/env python

import sys
import shlex

print >> sys.stderr, "reducer started"

cur_country = None
ip_count = 0

for line in sys.stdin:
	items = line.strip().split('\t')
	if (items[1] == '0'):
		if cur_country != None:
			print "%s\t%d" % (cur_country, ip_count)
		cur_country = items[2]
		ip_count = 0

print "%s\t%d" % (prev_country, cur_users)

print >> sys.stderr, "reducer finished"