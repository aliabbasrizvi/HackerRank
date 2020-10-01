#!/bin/python

import os

def rotLeft(a, d):
  rotated_list = []
  num_count = len(a)
  for idx, num in enumerate(a):
    rotated_list.append(a[(idx + d) % num_count])

  return rotated_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
