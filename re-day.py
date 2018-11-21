#!/usr/bin/env python

import sys
day = sys.argv[1]

lines = sys.stdin.readlines()
i = 0
while i < len(lines):
    line = lines[i]
    if line.split(',')[8].split()[0] == day:
        print line.strip()
    i += 1
