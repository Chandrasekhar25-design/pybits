#!/usr/bin/env python
# coding: utf-8
"""
mergesort.py
---
Merge Sort (Exchange sort family)
---
Contact: Marshall Ward (marshall.ward@gmail.com)
"""
import random

def mergesort(x):
    n = len(x)
    if n <= 1:
        return x
    left = mergesort(x[:n/2])
    right = mergesort(x[n/2:])
    
    return merge(left, right)


def merge(left, right):
    result = []
    
    while left or right:
        if not left:    
            result.append(right.pop())
        elif not right or left[-1] > right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    result.reverse()
    
    return result


def main():
    a = range(10)
    random.shuffle(a)
    
    print 'Before sorting:', a
    a = mergesort(a)
    print 'After sorting:', a


if __name__ == '__main__':
    main()
