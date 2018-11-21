#!/usr/bin/env python

import sys
long1 = int(sys.argv[1])
long2 = int(sys.argv[2])

lines = sys.stdin.readlines()

def seconds(degs, mins, secs):
    mins = (degs * 60) + mins
    secs = (mins * 60) + secs
    return secs

i = 1
while i < len(lines):
    line = lines[i].split(',')
    LonD = int(line[4].strip())
    LonM = int(line[5].strip())
    LonS = int(line[6].strip())
    secs = seconds(LonD, LonM, LonS)
    if secs > long1 and secs < long2:
        print line[-2].strip() + ', ' + line[-1].strip()
    i += 1
