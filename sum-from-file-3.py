#!/usr/bin/env python

import sys

arg = sys.argv[1]

with open(arg) as f:
    line = f.read()
count = 0
l = line.split()
print l
j = 0
while j < len(l):
    count = count + int(l[j])
    j += 1

print count
