#!/usr/bin/env python

s = raw_input()

i = 0
j = 0
k = 0
while k < 2:
    i = j
    while i < len(s) and not ("0" <= s[i] and s[i] <= "9"):
        i += 1
    
    j = i
    while j < len(s) and "0" <= s[j] and s[j] <= "9":
        j += 1
    k += 1

if i < len(s):
    print s[i:j]
