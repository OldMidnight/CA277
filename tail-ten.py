#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()
lines = lines[-10:]

i = 0
while i != len(lines):
    print lines[i].strip()
    i += 1
