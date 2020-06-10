





import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
    maxcur = max(arr)
    positions = {}

    for ind in range(len(arr)):
        positions[arr[ind]] = ind
    
    for ind in range(len(arr)):
        if k == 0:
            break
            
        if arr[ind] == maxcur:
            maxcur -= 1
            
        if arr[ind] < maxcur:
            mind = positions[maxcur]
            positions[maxcur], positions[arr[ind]] = positions[arr[ind]], positions[maxcur]
            arr[ind], arr[mind] = arr[mind], arr[ind]
            maxcur -= 1
            k -= 1
    return arr

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = largestPermutation(k, arr)
    print(result)
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')
    #fptr.close()