#!/usr/bin/env python

import sys
files = sys.argv[1:]

i = 0
while i < len(files):
    with open(files[i]) as f:
        lines = f.readlines()
    j = 0
    while j < len(lines):
        line = lines[j].strip()
        print line
        j += 1
    i += 1
