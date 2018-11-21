#!/usr/bin/env python

import sys

num = sys.argv[1]
lines = sys.stdin.readlines()
lines = lines[-int(num):]

i = 0
while i != len(lines):
    print lines[i].strip()
    i += 1
