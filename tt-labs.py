#!/usr/bin/env python

line = raw_input()

while line != 'end':
    if line.split()[2] != '1':
        print line
    line = raw_input()
