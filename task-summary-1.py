#!/usr/bin/env python

import sys

status = {}

lines = sys.stdin.readlines()
correct = []

for l in lines:
    l = l.strip()
    l_list = l.split('.')
    if l_list[-1] == 'incorrect':
        status['.'.join(l_list[0:2])] = False
    elif l_list[-1] == 'correct':
        status['.'.join(l_list[0:2])] = True

for s in sorted(status):
    if status[s] is True:
        print s
