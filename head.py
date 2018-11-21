#!/usr/bin/env python

import sys

num = sys.argv[1]
lines = sys.stdin.readlines()

i = 0
while i != int(num):
    if i < len(lines):
        print lines[i].strip()
    i += 1
