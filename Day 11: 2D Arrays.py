#!/bin/python3

import math
import os
import random
import re
import sys


def hourglassSum(arr):
    maximum_sum = -63
    for i in range(4):
        for j in range(4):
            sum_hourglass = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum_hourglass > maximum_sum:
                maximum_sum = sum_hourglass
    return maximum_sum

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    print(hourglassSum(arr))
