#!/usr/bin/env python

import sys
import shlex

total = 0

for line in sys.stdin:
	items = line.split('\t')
	ip, count = items[0], int(items[1])
	total += 1

print total