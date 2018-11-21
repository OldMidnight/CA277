#!/usr/bin/env python

import sys

arg = int(sys.argv[1])
s = sys.stdin.readline().strip()
i = 0
k = 0
while k != arg:
    while i < len(s) and s[i] != ',':
        i += 1
    i += 1
    k += 1
if i < len(s):
    j = i
    while j < len(s) and s[j] != ',':
        j += 1
    print s[i:j]
