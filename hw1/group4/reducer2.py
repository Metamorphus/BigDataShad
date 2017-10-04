#!/usr/bin/env python

import sys
import shlex

print >> sys.stderr, "reducer started"

sn, sl = 0, 0

for line in sys.stdin:
	items = line.strip().split('\t')
	sn += int(items[0])
	sl += int(items[1])

print "%s\t%d" % (sn, sl)

print >> sys.stderr, "reducer finished"