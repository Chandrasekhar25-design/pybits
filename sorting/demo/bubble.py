#!/usr/bin/env python
# coding: utf-8
#--------------------

"""
Bubble sort (Exchange sort family)
"""

N = 10

import random

def bubble_sort(x):
    print 'Illustrated bubble sort'
    num_tests = 0
    num_swaps = 0
    num_passes = 0
    unsorted = True

    while unsorted:
        num_passes += 1
        print 'Pass %i' % num_passes
        unsorted = False
        for j in range(1,len(x)):
            print x
            num_tests += 1
            if x[j-1] > x[j]:
                num_swaps += 1
                x[j-1], x[j] = x[j], x[j-1]
                unsorted = True

    print 'Number of tests: %i' % num_tests
    print 'Number of swaps: %i' % num_swaps
    return x

def main():
    a = range(N)
    random.shuffle(a)
    a = bubble_sort(a)

if __name__ == '__main__':
    main()
