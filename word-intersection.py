#!/usr/bin/env python

with open('words-1.txt') as f:
    lines1 = f.readlines()
with open('words-2.txt') as f:
    lines2 = f.readlines()

intersects = {}

i = 0
while i < len(lines1):
    line = lines1[i].strip()
    intersects[line] = False
    i += 1

i = 0
while i < len(lines2):
    line = lines2[i].strip()
    if line in intersects:
        intersects[line] = True
    i += 1

for l in sorted(intersects):
    if intersects[l]:
        print l
