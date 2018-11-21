#!/usr/bin/env python

user = raw_input()
line = raw_input()

while line != 'end':
    user2 = line.split()[1]
    if user2 == user:
        print line
    line = raw_input()
