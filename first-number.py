#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s) and not ("0" <= s[i] and s[i] <= "9"):
    i += 1

if i < len(s):
    j = 0
    s = s[i:]
    while j < len(s) and not ("A" <= s[j] and s[j] <= "Z") and s[j] != " ":
        j += 1
    if j < len(s):
        print s[:j], i
