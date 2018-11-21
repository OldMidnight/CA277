#!/usr/bin/env python

hours = 0
line = raw_input()

while line != 'end':
    hours = hours + int(line.split()[2])
    line = raw_input()

print hours
