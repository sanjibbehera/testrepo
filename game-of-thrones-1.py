###############################################################
#### Arguments to be passed to the program like below:-
#### python game-of-thrones-1.py
###############################################################

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    cnt = Counter(s)
    if len(s)%2 == 0:
        ret = all([x%2 == 0 for x in cnt.values()])
    else:
        if len(list(filter(lambda x: x%2 == 1, cnt.values()))) == 1:
            ret = True
        else:
            ret = False
    return 'YES' if ret else 'NO'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = gameOfThrones(s)
    print(result)

    #fptr.write(result + '\n')
    #fptr.close()