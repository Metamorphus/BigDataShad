#!/usr/bin/env python

import sys

sum = 0

for line in sys.stdin:
	items = line.strip().split()
	print items[-1]
	sum += int(items[-1])

print sum
print >> sys.stderr, 'finished mapper'