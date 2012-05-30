#!/usr/bin/env python
"""
binary.py
---
Binary search
---
Marshall Ward (marshall.ward@gmail.com)
"""

def binary_search(x, value, lo=0, hi=None):
    
    if not hi:
        hi = len(x)
    
    i_mid = (lo + hi) // 2
    mid_val = x[i_mid]
    
    if mid_val > value:
        return binary_search(x, value, lo, i_mid - 1)
    elif mid_val < value:
        return binary_search(x, value, i_mid + 1, hi)
    else:
        return i_mid


def main():
    a = [1, 2, 5, 7, 11, 21, 23, 34, 55, 107]
    value = 34
    print 'Find value %s in list %s' % (value, a)
    i_val = binary_search(a, value)
    print 'Index:', i_val


if __name__ == '__main__':
    main()
