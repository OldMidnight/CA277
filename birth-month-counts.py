#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()

months = [0] * 12
i = 0
while i < len(lines):
    line = lines[i].strip().split()
    month = line[0].split('/')[1]
    months[int(month) - 1] += 1
    i += 1

i = 0
while i < len(months):
    if months[i] > 0:
        print i, months[i]
    i += 1
