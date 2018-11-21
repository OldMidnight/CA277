#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()
snaps = {}

i = 0
while i < len(lines) and lines[i].strip() not in snaps:
    snaps[lines[i].strip()] = True
    i += 1

if i < len(lines):
    print 'snap:', lines[i].strip()
