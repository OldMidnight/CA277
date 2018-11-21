#!/usr/bin/env python

line = raw_input()

while line != 'end':
    tokens = line.split(',')
    tokens2 = tokens[5].split('/')
    if tokens2[-1] == 'viewform':
        print tokens[0], tokens[-1]
    line = raw_input()
