#!/usr/bin/env python

import sys

arg = sys.argv[1]

with open(arg) as f:
    lines = f.readlines()

count = 0
i = 0

while i < len(lines):
    count = count + int(lines[i].strip())
    i += 1
print count
