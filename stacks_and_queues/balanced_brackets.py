#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
  str_stack = ''
  for char in s:
    if char == '(' or char == '{' or char == '[':
      str_stack = char + str_stack
      continue
    if (char == ')' and len(str_stack) > 0 and str_stack[0] == '(') or \
       (char == '}' and len(str_stack) > 0 and str_stack[0] == '{') or \
       (char == ']' and len(str_stack) > 0 and str_stack[0] == '['):
      str_stack = str_stack[1:]
    else:
      return 'NO'

  if len(str_stack) == 0:
    return 'YES'

  return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
