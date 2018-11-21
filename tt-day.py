#!/usr/bin/env python

l = []

line = raw_input()
while line != 'end':
    l.append(line)
    line = raw_input()

day = input()
i = 0
while i < len(l):
    line = str(l[i])
    if line.split()[0] == str(day):
        print line
    i += 1
