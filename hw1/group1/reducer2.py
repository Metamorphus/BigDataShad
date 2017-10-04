#!/usr/bin/env python

import sys
import shlex

print >> sys.stderr, "reducer started"

total_hits, unique_users = 0, 0

for line in sys.stdin:
	items = line.strip().split('\t')
	total, unique = int(items[0]), int(items[1])
	total_hits += total
	unique_users += unique

print "%d\t%d" % (total_hits, unique_users)
print >> sys.stderr, "reducer finished"