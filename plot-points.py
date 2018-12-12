#!/usr/bin/env python

import sys

n = 20

lines = sys.stdin.readlines()
points = {}

i = 0
while i < len(lines):
    tokens = lines[i].split()
    key = tokens[0] + '-' + tokens[1]
    points[key] = True
    i += 1

def should_plot(x,y):
    key = str(x) + '-' + str(y)
    return key in points

print ' ' + '-' * n

i = 0
while i < n:
    y = n - i - 1

    output = []
    x = 0
    while x < n:
        if should_plot(x,y):
            output.append('*')
        else:
            output.append(' ')
        x += 1
    print '|' + ''.join(output) + '|'
    i += 1

print ' ' + '-' * n
