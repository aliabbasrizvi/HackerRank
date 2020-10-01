#!/bin/python

import os

def maxSubsetSum(arr):
  if len(arr) == 1 or len(arr) == 2:
    return max(arr)

  high_sum = [arr[0], max([arr[0], arr[1]])]

  for idx in xrange(2, len(arr)):
    high_sum.append(max([high_sum[idx - 1], high_sum[idx - 2] + arr[idx], arr[idx]]))

  return high_sum[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
