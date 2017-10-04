#!/usr/bin/env python

import sys
import shlex
from datetime import datetime

print >> sys.stderr, 'started mapper'

for line in sys.stdin:
	items = shlex.split(line.lower())
	code = int(items[6])
	if (code != 200):
		continue
	ip = items[0]
	date_part = items[3].split(':')[0]
	day_of_year = datetime.strptime(date_part, "[%d/%b/%Y").timetuple().tm_yday
	print "%s\t%d" % (ip, day_of_year)

print >> sys.stderr, 'finished mapper'