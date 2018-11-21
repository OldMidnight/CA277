#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    if i < 10:
        print lines[i].strip()
    i += 1
