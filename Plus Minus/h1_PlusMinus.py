import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    nv, pv, zv = 0, 0, 0
    for i in arr:
        if i < 0: nv += 1
        elif i > 0: pv += 1
        else: zv += 1

    pv = pv / n 
    print(f"{pv:0,.6f}")
    
    nv = nv / n 
    print(f"{nv:0,.6f}")
    
    zv = zv / n 
    print(f"{zv:0,.6f}")
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
