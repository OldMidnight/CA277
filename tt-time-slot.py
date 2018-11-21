#!/usr/bin/env python

line = raw_input()

while line != 'end':
    line_parts = []
    i = 0
    while i != 3:
        line_parts.append(line.split()[i])
        if i == 1:
            time = int(line_parts[i])
            line_parts[i] = str(time) + ':00'
        elif i == 2:
            time = time + int(line_parts[i]) - 1
            line_parts[i] = str(time) + ':50'
        i += 1
    full_line = line_parts + line.split()[3:]
    print ' '.join(full_line)
    line = raw_input()
