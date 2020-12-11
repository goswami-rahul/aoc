#!/usr/bin/env python
import sys
from rich import print

def Read():
  infile = 'in' if len(sys.argv) <= 1 else sys.argv[1]
  with open(infile) as f:
    return [int(line.strip()) for line in f]

def Easy(a: list[int]):
  a = sorted(a + [0, max(a) + 3])
  one, three = 0, 0
  for i in range(1, len(a)):
    one += a[i] - a[i - 1] == 1
    three += a[i] - a[i - 1] == 3
  return one * three

def Hard(a: list[int]):
  a = sorted(a + [0, max(a) + 3])
  ways = [0] * len(a)
  ways[0] = 1
  for i in range(1, len(a)):
    for j in range(max(0, i - 3), i):
      if a[i] - a[j] <= 3:
        ways[i] += ways[j]
  return ways[-1]

input = Read()
print(Easy(input))  
print(Hard(input))