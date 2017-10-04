#!/usr/bin/env python

import sys
import shlex

print >> sys.stderr, "mapper started"

for line in sys.stdin:
	items = shlex.split(line.lower())
	ip, code = items[0], int(items[6])
	if code != 200:
		continue
	print "%s\t1" % ip

print >> sys.stderr, "mapper finished"
