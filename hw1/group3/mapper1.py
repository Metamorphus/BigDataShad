#!/usr/bin/env python

import sys
import shlex

print >> sys.stderr, 'started mapper'

def ip_to_number(address):
	byte_0, byte_1, byte_2, byte_3 = map(int, address.split("."))
	res = byte_0 << 24 | byte_1 << 16 | byte_2 << 8 | byte_3 << 0
	return res

for line in sys.stdin:
	if line.find('/') >= 0: #log
		items = shlex.split(line.lower())
		code = int(items[6])
		if (code != 200):
			continue
		ip = ip_to_number(items[0])
		print "%d\t1" % ip
	else: #ip to country
		items = line.strip().split(',')
		low, high = int(items[0][1:-1]), int(items[1][1:-1])
		country = items[3][1:-1]
		if country == '-':
			continue
		print "%d\t0\t%s" % (low, country)

print >> sys.stderr, 'finished mapper'