#!/usr/bin/env python

import sys

arg = sys.argv[1]
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    line = lines[i].strip()
    j = 1
    while j < len(line) and line[-j - 1] != '/':
        j += 1
    file_name = line[-j:]
    if file_name[-len(arg) - 1:] == '.' + arg:
        print file_name
    i += 1
