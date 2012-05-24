#!/usr/bin/env python
# coding: utf-8
"""
quicksort.py
---
Quicksort (Exchange sort family)
---
Contact: Marshall Ward (marshall.ward@gmail.com)
"""
import random

def quicksort(x):
    if x:
        pivot = x[0]
        lesser  = quicksort([y for y in x[1:] if y <  pivot])
        greater = quicksort([y for y in x[1:] if y >= pivot])
        return lesser + [pivot] + greater
    else:
        return x


def main():
    a = range(10)
    random.shuffle(a)
    
    print 'Before sorting:', a
    a = quicksort(a)
    print 'After sorting:', a


if __name__ == '__main__':
    main()
