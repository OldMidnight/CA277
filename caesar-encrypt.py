#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

original = lower + upper
rotated = lower[13:] + lower[:13] + upper[13:] + upper[:13]

caesarDict = {}

i = 0
while i < len(original):
    caesarDict[original[i]] = rotated[i]
    i += 1

i = 0
while i < len(lines):
    line = lines[i].strip()
    newline = ''
    j = 0
    while j < len(line):
        if line[j] in caesarDict:
            newline = newline + caesarDict[line[j]]
        else:
            newline = newline + line[j]
        j += 1
    print newline
    i += 1
