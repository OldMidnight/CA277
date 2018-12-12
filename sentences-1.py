#!/usr/bin/env python

import sys
line = sys.stdin.read().strip()
line = line.split()
line = ' '.join(line)
punc = ['.', '!', '?']

while 0 < len(line):
    i = 0
    while i < len(line) and line[i] not in punc:
        i += 1
    i += 1
    print line[:i]
    line = line[i:].strip()
