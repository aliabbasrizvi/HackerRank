#!/bin/python

import os


def sockMerchant(n, ar):
    sock_to_count_map = {}
    pair_count = 0
    for sock in ar:
      sock_to_count_map[sock] = sock_to_count_map.get(sock, 0) + 1

    for count in sock_to_count_map.values():
      pair_count += count / 2

    return pair_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
