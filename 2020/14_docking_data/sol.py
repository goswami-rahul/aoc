#!/usr/bin/env python
import sys
from rich import print
import re

def Read():
  infile = 'in' if len(sys.argv) <= 1 else sys.argv[1]
  with open(infile) as f:
    return [tuple(line.strip().split(' = ')) for line in f]

def Easy(lines: list[tuple[str, str]]):
  one, zer = 0, 0
  mem = {}
  for key, val in lines:
    if key == 'mask':
      one = int(val.replace('X', '0'), 2)
      zer = int(val.replace('X', '1'), 2)
    else:
      at = int(re.search('\d+', key).group())
      mem[at] = int(val) & zer | one
  return sum(mem.values())

def Hard(lines: list[tuple[str, str]]):
  mem = {}
  mask = ''

  for key, val in lines:
    if key == 'mask':
      mask = val[::-1]
    else:
      num = int(re.search('\d+', key).group())
      def Go(num: int, i: int):
        if i == 36: 
          mem[num] = int(val)
        else:
          if mask[i] == 'X':
            Go(num, i + 1)
            Go(num ^ (1 << i), i + 1)
          else:
            Go(num | int(mask[i]) << i, i + 1)
      Go(num, 0)
  return sum(mem.values())


input = Read()
print(Easy(input))  
print(Hard(input))