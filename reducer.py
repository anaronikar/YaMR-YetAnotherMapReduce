#!/usr/bin/env python3
import sys 

timestamp = {}
total_count = 0
for row in sys.stdin:
    tmpstmp = row.strip()
    if tmpstmp not in timestamp.keys():
        timestamp[tmpstmp] = 1
    else:
        timestamp[tmpstmp] += 1

for i in sorted(timestamp):
    print(i, timestamp[i])

