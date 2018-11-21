#!/usr/bin/env python

import sys

#ops = "= < >".split()
op = sys.argv[1][-2]
value = sys.argv[1][-1]
field = sys.argv[1][:-2]
if op != '=' and op != '>' and op != '<':
    op = sys.argv[1][-3]
    value = sys.argv[1][-2:]
    field = sys.argv[1][:-3]

lines = sys.stdin.readlines()
i = 0
header = lines[i]
tokens = header.split(',')
j = 0
num = 0
while j < len(tokens):
    if tokens[j].strip() == field:
        num = j
    j += 1
i += 1
while i < len(lines):
    if op == '=':
        if lines[i].split(',')[num].strip() == value:
            print lines[i].strip()
    elif op == '<':
        if lines[i].split(',')[num].strip() < value:
            print lines[i].strip()
    elif op == '>':
        if lines[i].split(',')[num].strip() > value:
            print lines[i].strip()
    i += 1
