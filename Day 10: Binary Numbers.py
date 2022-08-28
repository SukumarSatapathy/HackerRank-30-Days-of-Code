#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    b = bin(n)
    binary = b[2:]
    count = maxx = 0
    for i in binary:
        if i == '1':
            count += 1
        else:
            if count > maxx:
                maxx = count
            count = 0
    print(max(count,maxx))
