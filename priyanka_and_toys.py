##############################################################
#### Arguments to be passed to the program like below:-
#### python priyanka_and_toys.py

#### What is the smallest number of containers that can be contracted to ship the items based on the given list of weights?

#### For example, there are items with weights w = [1,2,3,4,5,10,11,12,13]. 
#### This can be broken into two containers: [1,2,3,4,5] and [10,11,12,13]. 
#### Each container will contain items weighing within  units of the minimum weight item.
##############################################################

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w = list(dict.fromkeys(w))
    w = sorted(w)
    res = 0
    limit = -1
    
    for el in w:
        if el > limit:
            limit = el + 4
            res += 1
    
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    w = list(map(int, input().rstrip().split()))
    result = toys(w)
    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()