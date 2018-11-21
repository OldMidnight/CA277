#!/usr/bin/env python

import sys
arg = sys.argv[1]
s = sys.stdin.readline().strip()
i = 0
count = 0
j = 0
while 0 < len(s):
    while i < len(s) and s[i] != ',':
        i += 1
    if s[:i] == arg:
        print count
        s = ''
    else:
        i += 1
        s = s[i:]
        i = 0
        count += 1
