#!/usr/bin/env python

with open('/etc/passwd') as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip().split(':')
    print line[0]
    i += 1
