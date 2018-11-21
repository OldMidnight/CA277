#!/usr/bin/env python

s = raw_input()
i = 0
caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
caps2 = ['I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
caps3 = ['Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
while i != len(s):
    j = 0
    while j != len(caps):
        if s[i] == caps[j]:
            print s[i]
        j += 1
    j = 0
    while j != len(caps2):
        if s[i] == caps2[j]:
            print s[i]
        j += 1
    j = 0
    while j != len(caps3):
        if s[i] == caps3[j]:
            print s[i]
        j += 1
    i += 1
