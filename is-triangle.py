#!/usr/bin/env python
a = input()
b = input()
c = input()

if a < b + c and b < a + c and c < a + b:
    print 'yes'
else:
    print 'no'
