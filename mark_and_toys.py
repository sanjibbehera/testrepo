##############################################################
#### Arguments to be passed to the program like below:-
#### python mark_and_toys.py

#### Complete the function maximumToys in the editor below. It should return an integer representing the maximum number of toys Mark can purchase.
#### maximumToys has the following parameter(s):

#### prices: an array of integers representing toy prices
#### k: an integer, Mark's budget
##############################################################

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    total_arr = []
    prices.sort()
    temp = prices[0]
    total_arr.append(prices[0])
    for x in range(len(prices)):
        if x == len(prices)-1:
            break
        else:
            temp += prices[x+1]
            if temp<= k:
                total_arr.append(temp)
                continue
            else:
                break
    return len(total_arr)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()