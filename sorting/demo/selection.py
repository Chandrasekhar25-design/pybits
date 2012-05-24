#!/usr/bin/env python
# coding: utf-8
#--------------------
"""
selection.py
---
Selection sort (Selection sort family)
---
Contact: Marshall Ward (marshall.ward@gmail.com)
"""
import random

N = 10

def selection_sort(x):
    print 'Illustrated Selection Sort'
    num_tests = 0
    num_swaps = 0
    for i in range(len(x)):
        print x
        x_min = x[i]
        j_min = i
        for j in range(i+1,len(x)):
            num_tests += 1
            if x[j] < x_min:
                num_swaps += 1
                x_min = x[j]
                j_min = j
        if j != i:
            x[i], x[j_min] = x[j_min], x[i]

    print 'Number of tests: %i' % num_tests
    print 'Number of swaps: %i' % num_swaps

def main():
    a = range(N)
    random.shuffle(a)
    a = selection_sort(a)

if __name__ == '__main__':
    main()
