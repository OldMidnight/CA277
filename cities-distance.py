#!/usr/bin/env python

import sys
import math

city1 = sys.argv[1]
state1 = sys.argv[2]
city2 = sys.argv[3]
state2 = sys.argv[4]

lines = sys.stdin.readlines()

def seconds(degs, mins, secs):
    mins = (degs * 60) + mins
    secs = (mins * 60) + secs
    return secs

def get_kms(degrees):
    return degrees * 111

i = 1
while i < len(lines):
    line = lines[i].split(',')
    if line[-2].strip() == city1 and line[-1].strip() == state1:
        LonDCity1 = int(line[4].strip())
        LonMCity1 = int(line[5].strip())
        LonSCity1 = int(line[6].strip())
        LatDCity1 = int(line[0].strip())
        LatMCity1 = int(line[1].strip())
        LatSCity1 = int(line[2].strip())
    if line[-2].strip() == city2 and line[-1].strip() == state2:
        LonDCity2 = int(line[4].strip())
        LonMCity2 = int(line[5].strip())
        LonSCity2 = int(line[6].strip())
        LatDCity2 = int(line[0].strip())
        LatMCity2 = int(line[1].strip())
        LatSCity2 = int(line[2].strip())
    i += 1

secsLongCity1 = seconds(LonDCity1, LonMCity1, LonSCity1)
secsLatCity1 = seconds(LatDCity1, LatMCity1, LatSCity1)

secsLongCity2 = seconds(LonDCity2, LonMCity2, LonSCity2)
secsLatCity2 = seconds(LatDCity2, LatMCity2, LatSCity2)
x = (secsLongCity2 - secsLongCity1)
y = (secsLatCity2 - secsLatCity1)
distInSecs = math.sqrt((x) ** 2 + (y) ** 2)

def degrees(secs):
    mins = secs / 60
    return mins / 60

print int(round(get_kms(degrees(distInSecs))))
