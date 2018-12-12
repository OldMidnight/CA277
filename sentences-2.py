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
    l = line[:i].capitalize()
    l = l.split()
    j = 0
    while j < len(l):
        if l[j] == 'mary':
            l[j] = l[j].capitalize()
        j += 1
    l = ' '.join(l)
    print l
    line = line[i:].strip()
