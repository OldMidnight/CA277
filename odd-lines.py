#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()

i = 0
while i != len(lines):
    if int(lines[i]) % 2 == 1:
        print lines[i].strip()
    i += 1
