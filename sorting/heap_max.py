#!/usr/bin/env python
# content: utf-8
#--------------------

N = 10

import random    
    
def hash_max(x):
    # Node j has children 2*j+1, 2*j+2
    #   Proof:
    
    # If largest parent is n, then largest child N-1 is either 2*n+1 or 2*n+2
    # So N-1 = 2*n+1 or 2*n+2   ->  n = N/2 - 1 or (N-1)/2 - 1
    # So range(N/2) contain the parent nodes
    for j in range(N/2):
        pass
    
def main():
    a = range(N)
    random.shuffle(a)
    a_max = hash_max(a)
    
if __name__ == '__main__':
    main()