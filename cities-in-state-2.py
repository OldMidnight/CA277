#!/usr/bin/env python

import sys
state = sys.argv[1]

lines = sys.stdin.readlines()
i = 1
while i < len(lines):
    if lines[i].split(',')[-1].strip() == state:
        print lines[i].split(',')[-2].strip()
    i += 1
