#!/usr/bin/env python

import sys
field = sys.argv[1]
lines = sys.stdin.readlines()
line = lines[0]
tokens = line.split(',')
i = 0
while i < len(tokens):
    if tokens[i].strip() == field:
        print i
    i += 1
