#!/usr/bin/env python

import sys

numbers = {
    'one': 'eins',
    'two': 'zwei',
    'three': 'drei',
    'four': 'view',
    'five': 'funf',
    'six': 'sechs',
    'seven': 'sieben',
    'eight': 'acht',
    'nine': 'neun',
    'ten': 'zehn'
}

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    l = lines[i].strip()
    if l in numbers:
        print numbers[l]
    i += 1
