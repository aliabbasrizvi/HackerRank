#!/bin/python

import os

def isValid(s):
  all_chars = list(s)

  char_to_freq = {}
  for char in all_chars:
    char_to_freq[char] = char_to_freq.get(char, 0) + 1

  all_counts = sorted(list(char_to_freq.values()))
  for idx in xrange(1, len(all_counts) - 2):
    if all_counts[idx] != all_counts[idx + 1]:
      return 'NO'

  if len(all_counts) == 1 or \
      all_counts[-1] == all_counts[-2] or \
      (all_counts[-1] == all_counts[-2] + 1 and not (all_counts[0] == all_counts[1] - 1)) or \
      (not (all_counts[-1] == all_counts[-2] + 1) and (all_counts[0] == all_counts[1] - 1)):
    return 'YES'

  return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
