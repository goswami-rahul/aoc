#!/usr/bin/env python
import sys
from rich import print

def Read():
  infile = 'in' if len(sys.argv) <= 1 else sys.argv[1]
  with open(infile) as f:
    bound = int(f.readline().strip())
    ids = f.readline().strip().split(',')
    ids = [int(i) if i != 'x' else -1 for i in ids]
    return bound, ids

def Easy(bound: int, ids: list[int]):
  opt = float('inf')
  for i in ids:
    if i != -1:
      if opt > -bound % i:
        opt =  -bound % i
        ans = opt * i
  return ans

def Hard(ids: list[int]):
  ans = 0
  prod = 1
  x = {}
  for i, e in enumerate(ids):
    if e != -1:
      a = -i % e
      for j, f in enumerate(ids):
        if j >= i: break
        if f != -1:
          a = (a - x[j]) * pow(f, -1, e) % e
      ans += prod * a
      prod *= e
      x[i] = a
  return ans


input = Read()
print(Easy(*input))  
print(Hard(input[1]))