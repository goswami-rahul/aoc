#!/usr/bin/env python
import sys
from rich import print

def Read():
  infile = 'in' if len(sys.argv) <= 1 else sys.argv[1]
  with open(infile) as f:
    return [(line[:1], int(line[1:].strip())) for line in f]

def Easy(a: list[tuple[str, int]]):
  x, y = 0, 0
  f = 'E'
  for d, u in a:
    if d in 'RL':
      u = u if d == 'L' else 360 - u
      dirs = 'NWSENWSE'
      f = dirs[dirs.find(f) + u // 90]
    if d == 'F':
      d = f
    if d == 'N':
      y += u
    if d == 'S':
      y -= u
    if d == 'E':
      x += u
    if d == 'W':
      x -= u
  return abs(x) + abs(y)

def Hard(a: list[tuple[str, int]]):
  sx, sy, wx, wy = 0, 0, 10, 1
  for d, u in a:
    if d in 'RL':
      u = u if d == 'L' else 360 - u
      for _ in range(0, u, 90):
        wx, wy = -wy, wx
    if d == 'F':
      sx += wx * u
      sy += wy * u
    if d == 'N':
      wy += u
    if d == 'S':
      wy -= u
    if d == 'E':
      wx += u
    if d == 'W':
      wx -= u
  return abs(sx) + abs(sy)

input = Read()
print(Easy(input))  
print(Hard(input))