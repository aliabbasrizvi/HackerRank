#!/bin/python

import os


def alternatingCharacters(s):
  del_chars = 0

  if len(s) == 0 or len(s) == 1:
    return 0

  all_chars = list(s)

  comp_char = all_chars[0]
  for idx in xrange(1, len(all_chars)):
    if all_chars[idx] == comp_char:
      del_chars += 1
    else:
      comp_char = all_chars[idx]

  return del_chars

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
