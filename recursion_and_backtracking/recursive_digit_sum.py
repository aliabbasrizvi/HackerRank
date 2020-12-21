#!/bin/python

import math
import os
import random
import re
import sys

def get_sum_of_digits(num):
  sum = 0
  for char in num:
    sum += int(char)

  return sum


# Complete the superDigit function below.
def superDigit(n, k):
  if int(n) < 10 and k == 1:
    return n

  sum = get_sum_of_digits(n) * k
  return superDigit(str(sum), 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


