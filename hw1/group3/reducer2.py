#!/usr/bin/env python

import sys
import shlex

print >> sys.stderr, "reducer started"

prev_country = None
cur_users = 0

for line in sys.stdin:
	items = line.strip().split('\t')
	country, count = items[0], int(items[1])
	if country == prev_country:
		cur_users += count
	else:
		if prev_country != None:
			print "%s\t%d" % (prev_country, cur_users)
		cur_users = count
	prev_country = country

print "%s\t%d" % (prev_country, cur_users)

print >> sys.stderr, "reducer finished"