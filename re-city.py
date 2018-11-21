#!/usr/bin/env python

import sys
city = sys.argv[1]

lines = sys.stdin.readlines()
i = 0
while i < len(lines):
    line = lines[i]
    if line.split(',')[1] == city:
        print line.strip()
    i += 1
