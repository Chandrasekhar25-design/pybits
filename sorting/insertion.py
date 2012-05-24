#!/usr/bin/env python
# coding: utf-8
#--------------------

"""
insertion.py
Insertion sort (Insertion sort family)
Contact: Marshall Ward (marshall.ward@gmail.com)
"""
import random

def insertion_sort(x):
    for i, xi in enumerate(x):
        for j, xj in enumerate(x[:i]):
            if xj > xi:
                x[j], x[j+1:i+1] = x[i], x[j:i]
                break
    return x


def main():
    a = range(10)
    random.shuffle(a)
    print 'Before sort:', a
    a = insertion_sort(a)
    print 'After sort:', a


if __name__ == '__main__':
    main()
