#!/usr/bin/env python

import sys
import shlex

print >> sys.stderr, "reducer started"

cur_country = None
ip_count = 0
prev_ip = None

for line in sys.stdin:
	items = line.strip().split('\t')
	if items[1] == '0':
		if cur_country != None and ip_count > 0:
			print "%s\t%d" % (cur_country, ip_count)
		cur_country = items[2]
		ip_count = 0
	else:
		if items[0] != prev_ip:
			ip_count += 1
		prev_ip = items[0]

if cur_country != None and ip_count > 0:
	print "%s\t%d" % (cur_country, ip_count)

print >> sys.stderr, "reducer finished"