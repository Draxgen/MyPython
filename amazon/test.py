#!/bin/python3

import math
import os
import random
import re
import sys

def rowSum(arr, n):
    sum = 0
    for x in arr[n]:
        sum+=x
    return sum

def colSum(arr, n):
    sum = 0
    for x in arr:
        sum+=x[n]
    return sum

def diagSum(arr, n):
    # for n=0 it is diagnol going from top left to bottom right
    # for n=1 it is diagnol going from bottom left to top right
    sum = 0
    length = len(arr)
    if n == 0:
        for x in range(length):
            sum+=arr[x][x]
        return sum
    if n == 1:
        for x in range(length):
            sum+=arr[x][length-x-1]
        return sum
    
    
# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
