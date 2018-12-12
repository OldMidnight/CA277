#!/usr/bin/env python

import sys

n = int(sys.argv[1])
main_x = int(sys.argv[2])
main_y = int(sys.argv[3])
size = int(sys.argv[4])

tlc_y = main_y + size - 1
tlc_x = main_x + size - 1
trc_y = tlc_x + size - 1
trc_x = tlc_y +size - 1
brc_y = trc_y - size + 1
brc_x = trc_x - size + 1

points = {}

def should_plot1(x,y):
    plot = False
    if y >= main_y and y <= brc_y:
        if x == main_x or x == tlc_x:
            plot = True
        else:
            plot = False
    else:
        plot = False
    return plot

def should_plot2(x,y):
    plot = False
    if x >= main_x and x <= brc_x:
        if y == main_y or y == tlc_y:
            plot = True
        else:
            plot = False
    else:
        plot = False
    return plot

print ' ' + '-' * n

i = 0
while i < n:
    y = n - i - 1

    output = []
    
    x = 0
    while x < n:
        if should_plot1(x,y):
            output.append('*')
        else:
            output.append(' ')
        x += 1
    x = 0
    while x < len(output):
        if should_plot2(x,y):
            output[x] = '*'
        x += 1
    print '|' + ''.join(output) + '|'
    i += 1

print ' ' + '-' * n
