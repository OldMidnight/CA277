#!/usr/bin/env python

count = 0
with open('numbers.txt') as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    count = count + int(lines[i].strip())
    i += 1
print count
