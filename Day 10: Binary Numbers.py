# Link : https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    n = bin(n)
    n = n[2:]
    print (max(map(len, n.split('0'))))  
