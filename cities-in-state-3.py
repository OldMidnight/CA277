#!/usr/bin/env python

import sys
state = sys.argv[1]

lines = sys.stdin.readlines()
i = 1
while i < len(lines):
    if lines[i].split(',')[-1].strip() == state:
        line = lines[i].split(',')
        city = line[-2].strip()
        LatD = line[0].strip()
        LatM = line[1].strip()
        LatS = line[2].strip()
        NS = line[3].strip()
        LonD = line[4].strip()
        LonM = line[5].strip()
        LonS = line[6].strip()
        EW = line[7].strip()
        p1 = city + ':' + ' ' + LatD + 'o' + LatM + "'" + LatS + '"' + ' ' + NS
        p2 = LonD + 'o' + LonM + "'" + LonS + '"' + ' ' + EW
        print p1 + ',', p2
    i += 1
