###############################################################
#### Arguments to be passed to the program like below:-
#### python permuting2Arrays.py
###############################################################

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    res = 'YES'
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    for el in zip(A, B):
        if sum(el) < k:
            res = 'NO'
            break
    
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        result = twoArrays(k, A, B)
        #fptr.write(result + '\n')

    #fptr.close()