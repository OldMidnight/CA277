#!/usr/bin/env python

line = raw_input()

while line != 'end':
    print line.split(',')[1]
    line = raw_input()
