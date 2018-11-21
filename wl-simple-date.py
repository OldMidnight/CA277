#!/usr/bin/env python

line = raw_input()

while line != 'end':
    tokens = line.split()
    tokens[0] = ' '.join(tokens[0].split('-'))
    print ' '.join(tokens)
    line = raw_input()
