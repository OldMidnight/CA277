#!/usr/bin/env python

line = raw_input()

while line != 'end':
    print " ".join(line.split()[5:])
    line = raw_input()
