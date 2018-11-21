#!/usr/bin/env python

line = raw_input()

while line != 'end':
    testword = line.split(':')[-1].split('/')[-1]
    if testword != 'nologin' and testword != 'false':
        print line.split(':')[0], line.split(':')[-1]
    line = raw_input()
