#!/usr/bin/env python

import sys
import random
line = sys.stdin.readline().strip()

page_dict = {}
encodings = []

i = 0
while i < 10:
    with open('page-' + str(i) + '.txt') as f:
        lines = f.readlines()
    page_dict[i] = lines
    i += 1

i = 0
while i < len(line):
    encoded = False
    letter = line[i]
    while not encoded:
        page_num = random.randint(0,9)
        lines_in_page = page_dict[page_num]
        j = random.randint(0, len(lines_in_page) - 1)
        line = lines_in_page[j].strip()
        k = 0
        while k < len(line) and not encoded:
            if letter == line[k]:
                code = str(page_num) + ' ' + str(j) + ' ' + str(k)
                if code not in encodings:
                    encodings.append(code)
                    encoded = True
                    print 'k:', str(k)
                    print 'len(line):', len(line)
                else:
                    page_num = random.randint(0,9)
                    lines_in_page = page_dict[page_num]
                    j = random.randint(0, len(lines_in_page) - 1)
            else:
                page_num = random.randint(0,9)
                lines_in_page = page_dict[page_num]
                j = random.randint(0, len(lines_in_page) - 1)
            k += 1
    i += 1

for i in encodings:
    print i
