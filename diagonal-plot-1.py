#!/usr/bin/env python

import sys

n = 20

def should_plot(x,y):
    return x == y

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
