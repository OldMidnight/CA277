#!/usr/bin/env python

s = raw_input()

i = 0
while i < len(s) and not ("0" <= s[i] and s[i] <= "9"):
    i += 1

if i < len(s):
    print s[i], i
