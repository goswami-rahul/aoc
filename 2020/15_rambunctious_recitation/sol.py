#!/usr/bin/env python
import enum
import sys
from rich import print

def Read():
  infile = 'in' if len(sys.argv) <= 1 else sys.argv[1]
  with open(infile) as f:
    return list(map(int, f.readline().split(',')))

def Solve(a: list[int], k: int):
  b = {}
  for i, e in enumerate(a):
    b[e] = i
  x, y = 0, 0
  for i in range(len(a), k):
    y = x
    x = i - b[x] if x in b else 0
    b[y] = i
  return y

def Easy(a: list[int]):
  return Solve(a, 2020)

def Hard(a: list[int]):
  return Solve(a, 30000000)

input = Read()
print(Easy(input))
print(Hard(input))