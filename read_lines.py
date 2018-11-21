#!/usr/bin/env python

def get():
    l = []
    line = raw_input()
    while line != 'end':
        l.append(line)
        line = raw_input()
    return l
