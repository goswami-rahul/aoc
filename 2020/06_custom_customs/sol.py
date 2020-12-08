#!/usr/bin/env python
from functools import reduce

def Read():
  groups = []
  with open('in') as f:
    now = []
    for line in f:
      line = line.strip()
      if line:
        now.append(line)
      else:
        groups.append(now)
        now = []
    groups.append(now)
  return groups

def Easy(groups):
  return sum(len(reduce(lambda x, y: set(x) | set(y), g)) for g in groups)

def Hard(groups):
  return sum(len(reduce(lambda x, y: set(x) & set(y), g)) for g in groups)

input = Read()
print(Easy(input))
print(Hard(input))