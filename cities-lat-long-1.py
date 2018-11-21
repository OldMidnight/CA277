#!/usr/bin/env python

import sys
city = sys.argv[1]
state = sys.argv[2]

lines = sys.stdin.readlines()
i = 1

def seconds(degs, mins, secs):
    mins = (degs * 60) + mins
    secs = (mins * 60) + secs
    return secs

while i < len(lines):
    stateCheck = lines[i].split(',')[-1].strip()
    cityCheck = lines[i].split(',')[-2].strip()
    if stateCheck == state and cityCheck == city:
        line = lines[i].split(',')
        LatD = line[0].strip()
        LatM = line[1].strip()
        LatS = line[2].strip()
        LonD = line[4].strip()
        LonM = line[5].strip()
        LonS = line[6].strip()
        latInSecs = seconds(int(LatD), int(LatM), int(LatS))
        lonInSecs = seconds(int(LonD), int(LonM), int(LonS))
        print latInSecs, lonInSecs
    i += 1
