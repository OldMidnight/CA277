#!/usr/bin/env python

with open('input.txt', 'r') as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    print lines[i].rstrip('\n')
    i += 1
