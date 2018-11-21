#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s) and not ("A" <= s[i] and s[i] <= "Z"):
    i += 1
if i < len(s):
    j = 0
    s = s[i:]
    while j < len(s) and s[j] >= "A" and s[j] <= "Z":
        j += 1
    print s[:j], i
