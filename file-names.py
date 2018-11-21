#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()
i = 0
j = 1
while i < len(lines):
    line = lines[i].strip()
    j = 1
    while j < len(line) and line[-j - 1] != '/':
        j += 1
    print line[-j:]
    i += 1
