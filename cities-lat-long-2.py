#!/usr/bin/env python

import sys
longInSecs = sys.argv[1]

lines = sys.stdin.readlines()
i = 1

def seconds(degs, mins, secs):
    mins = (degs * 60) + mins
    secs = (mins * 60) + secs
    return secs

while i < len(lines):
    line = lines[i].split(',')
    LonD = line[4].strip()
    LonM = line[5].strip()
    LonS = line[6].strip()
    if seconds(int(LonD), int(LonM), int(LonS)) > int(longInSecs):
        print line[-2].strip() + ', ' + line[-1].strip()
    i += 1
