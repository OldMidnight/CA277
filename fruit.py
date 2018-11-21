#!/usr/bin/env python

import sys

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    l = lines[i].strip()
    if l in fruit:
        print l
    i += 1
