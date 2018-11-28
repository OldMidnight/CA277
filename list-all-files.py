#!/usr/bin/env python

import os

dirs = ['.']
while len(dirs) != 0:
    current_dir = dirs.pop()
    files = os.listdir(current_dir)
    j = 0
    while j < len(files):
        f = files[j]
        if os.path.isfile(current_dir + '/' + f):
            print current_dir + '/' + f
        elif os.path.isdir(current_dir + '/' + f):
            dirs.append(current_dir + '/' + f)
        j += 1
