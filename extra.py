#!/usr/bin/env python

import sys

s = sys.stdin.read().strip()

i = 0
k = 0
while i < len(s):
    while i < len(s) and s[i] != ">":
        i += 1
    i += 1
    s1 = s[i:]
    j = 0
    while j < len(s1) and s1[j] != "<":
        j += 1
    if s1[j - 3:j] == ".py":
        print s1[:j]
    k += 1
