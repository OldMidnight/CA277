#!/usr/bin/env python

import sys

input_lines = sys.stdin.readlines()
args = sys.argv

i = 1
while i != len(args):
    num = args[i]
    print input_lines[int(num)].strip()
    i += 1
