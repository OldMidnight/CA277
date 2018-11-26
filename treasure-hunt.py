#!/usr/bin/env python

import os

with open('start.txt') as f:
    line = f.readline().strip()

while os.path.isfile(line) is True:
    with open(line) as f:
        line = f.readline().strip()

print line
