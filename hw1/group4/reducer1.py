#!/usr/bin/env python

import sys

print >> sys.stderr, "reducer started"

prev_day = 0
prev_ip = None
new_users, lost_users = 0, 0
days_set = set()
final_map = dict()

for line in sys.stdin:
	items = line.strip().split('\t')
	ip, day = items[0], int(items[1])
	if ip == prev_ip:
		days_set.add(day)
	else:
		if len(days_set) == 1:
			for d in days_set:
				if d not in final_map.keys():
					final_map[d] = 0
				else:
					final_map[d] += 1
		days_set = set()
	prev_ip = ip

sorted_keys = sorted(final_map.keys())
print >> sys.stderr, final_map
print "%d\t%d" % (final_map[sorted_keys[-1]], final_map[sorted_keys[0]])

print >> sys.stderr, "reducer finished"