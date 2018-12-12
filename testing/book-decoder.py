#!/usr/bin/env python

import sys
lines = sys.stdin.readlines()

word = ''
i = 0
while i < len(lines):
    line = lines[i].strip().split()
    page = line[0]
    p_line = int(line[1])
    letter = int(line[2])
    print line
    print letter
    with open('page-' + page + '.txt') as f:
        p_lines = f.readlines()
    print p_lines
    line = p_lines[p_line]
    print line
    letter = line[letter]
    word = word + letter
    print word
    i += 1

print word.strip()
