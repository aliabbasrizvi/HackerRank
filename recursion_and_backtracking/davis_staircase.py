#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
  if n < 0:
    return 0

  if n == 0:
    return 1

  stored_count = steps_to_count.get(n)
  if stored_count:
    return stored_count

  res = stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)
  steps_to_count[n] = res
  return res


steps_to_count = {}
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)
        steps_to_count[n] = res
        res = res % (10 ** 10 + 7)

        fptr.write(str(res) + '\n')

    fptr.close()
