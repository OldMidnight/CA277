#!/usr/bin/env python

line = raw_input()

while line != 'end':
    size = line.split()[2]
    if int(size) > 7500:
        print line
    line = raw_input()
