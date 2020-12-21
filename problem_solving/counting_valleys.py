#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley_count = 0
    current_height = 0
    for step in s:
      if step == 'D':
        current_height -= 1
      if step == 'U':
        current_height += 1
        if current_height == 0:
          valley_count += 1

    return valley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
