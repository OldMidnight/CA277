#!/usr/bin/env python

def union(a, b):
    union_d = {}
    unionized = []
    for l in a:
        union_d[l] = True
    for l in b:
        union_d[l] = True
    for l in union_d:
        unionized.append(l)
    return unionized

def intersection(a, b):
    inter_d = {}
    intersected = []
    for l in a:
        inter_d[l] = False
    for l in b:
        if l in inter_d:
            inter_d[l] = True
    for l in inter_d:
        if inter_d[l] is True:
            intersected.append(l)
    return intersected
