#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
  magazine_words = {}
  for word in magazine:
    magazine_words[word] = magazine_words.get(word, 0) + 1

  for word in note:
    word_count = magazine_words.get(word, 0)
    if word_count == 0:
      print 'No'
      return
    magazine_words[word] = word_count - 1

  print 'Yes'
