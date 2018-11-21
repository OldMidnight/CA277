#!/usr/bin/env python

import sys
field = sys.argv[1]
i = 0
lines = sys.stdin.readlines()
tokens = lines[i].split(',')
j = 0
num = 0
while j < len(tokens):
    if tokens[j].strip() == field:
        num = j
    j += 1
i += 1
while i < len(lines):
    print lines[i].split(',')[num].strip()
    i += 1
