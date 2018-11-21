#!/usr/bin/env python

line = raw_input()

while line != 'end':
    if line.split()[0] == '3':
        print line
    line = raw_input()
