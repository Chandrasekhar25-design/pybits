#!/usr/bin/env python
# coding: utf-8
"""
bubble.py
---
Bubble sort (Exchange sort family)
---
Contact: Marshall Ward (marshall.ward@gmail.com)
"""
import random

def bubble_sort(x):
    unsorted = True
    while unsorted:
        unsorted = False
        for j in range(1,len(x)):
            if x[j-1] > x[j]:
                x[j-1], x[j] = x[j], x[j-1]
                unsorted = True
    return x


def main():
    a = range(10)
    random.shuffle(a)
    
    print 'Before sorting:', a
    a = bubble_sort(a)
    print 'After sorting:', a


if __name__ == '__main__':
    main()
