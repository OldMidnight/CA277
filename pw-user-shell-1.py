#!/usr/bin/env python

line = raw_input()
while line != 'end':
    tokens = line.split(':')
    print tokens[0], tokens[-1]
    line = raw_input()
