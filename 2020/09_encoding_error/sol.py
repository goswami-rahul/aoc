#!/usr/bin/env python
import sys
from rich import print

def Read():
  infile = 'in' if len(sys.argv) <= 1 else sys.argv[1]
  with open(infile) as f:
    return [int(x.strip()) for x in f]

def Easy(a: list[int]):
  for i in range(25, len(a)):
    ok = False
    for j in range(25):
      for k in range(j):
        if a[i - 1 - j] + a[i - 1 - k] == a[i]:
          ok = True
    if not ok:
        return a[i]

def Hard(a: list[int]):
  easy = Easy(a)
  n = len(a)
  for l in range(n):
    s = a[l]
    mn, mx = a[l], a[l]
    for r in range(l + 1, n):
      s += a[r]
      mn = min(mn, a[r])
      mx = max(mx, a[r])
      if s == easy:
        return mn + mx

input = Read()
print(Easy(input))  
print(Hard(input))