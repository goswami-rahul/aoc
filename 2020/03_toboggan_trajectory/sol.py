#!/usr/bin/env python
from typing import List

grid: List[str] = []
with open('in') as f:
  for line in f:
    grid.append(line.strip())
width = len(grid[0])

def Calc(right, down):
  trees = 0
  for i in range(0, len(grid), down):
    trees += grid[i][right * i % width] == '#'
  return trees

print(Calc(3, 1))

ans = 1
for right, down in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
  ans *= Calc(right, down)

print(ans)