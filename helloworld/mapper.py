#!/usr/bin/env python

import sys
import shlex

print >> sys.stderr, 'started mapper'

for line in sys.stdin:
	items = shlex.split(line.lower())
	ip = items[0]
	date_items = items[3].split(':')
	request_time = int(date_items[1]) * 3600 + int(date_items[2]) * 60 + int(date_items[3])
	print "%s\t%s" % (ip, request_time)