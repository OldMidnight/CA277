#!/usr/bin/env python

line = raw_input()
count = 0

while line != 'end':
    method = line.split()[4]
    if method == 'POST':
        count += 1
    line = raw_input()

print count
