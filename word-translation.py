#!/usr/bin/env python

import sys

with open('translation.txt') as f:
    lines = f.readlines()

translations = {}

i = 0
while i < len(lines):
    line = lines[i].strip()
    line = line.split()
    translations[line[0]] = line[1]
    i += 1

lines = sys.stdin.readlines()
i = 0
while i < len(lines):
    line = lines[i].strip()
    print translations[line]
    i += 1
