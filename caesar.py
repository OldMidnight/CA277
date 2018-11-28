#!/usr/bin/env python

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

original = lower + upper
rotated = lower[13:] + lower[:13] + upper[13:] + upper[:13]

caesarDict = {}

i = 0
while i < len(original):
    caesarDict[original[i]] = rotated[i]
    i += 1

def encrypt(line):
    newline = ''
    j = 0
    while j < len(line):
        if line[j] in caesarDict:
            newline = newline + caesarDict[line[j]]
        else:
            newline = newline + line[j]
        j += 1
    return newline
