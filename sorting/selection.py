#!/usr/bin/env python
# coding: utf-8
"""
selection.py
---
Selection sort (Selection sort family)
---
Contact: Marshall Ward (marshall.ward@gmail.com)
"""
import random

def selection_sort(x):
    for i, xi in enumerate(x):
        j_min, x_min = i, xi
        for j, xj in enumerate(x[i+1:], start=i+1):
            if xj < x_min:
                j_min, x_min = j, xj
        if j != i:
            x[i], x[j_min] = x[j_min], x[i]
    return x


def main():
    a = range(10)
    random.shuffle(a)

    print 'Before sort:', a
    a = selection_sort(a)
    print 'After sort:', a


if __name__ == '__main__':
    main()
