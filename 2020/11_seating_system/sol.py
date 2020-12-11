#!/usr/bin/env python
import sys
from rich import print

def Read():
  infile = 'in' if len(sys.argv) <= 1 else sys.argv[1]
  with open(infile) as f:
    return [list(line.strip()) for line in f]

def Easy(seats: list[list[str]]):
  seats = [row[:] for row in seats]
  def Neighbors(x: int, y: int):
    cnt = 0
    for i in range(x - 1, x + 2):
      for j in range(y - 1, y + 2):
        cnt += (0 <= i < len(seats) and 0 <= j < len(seats[0]) and 
                not (i == x and j == y) and seats[i][j] == '#')
    return cnt
  while True:
    flips = []
    for i in range(len(seats)):
      for j in range(len(seats[0])):
        if seats[i][j] == 'L' and Neighbors(i, j) == 0:
          flips.append((i, j))
        if seats[i][j] == '#' and Neighbors(i, j) >= 4:
          flips.append((i, j))
    if not flips:
      break
    for i, j in flips:
      seats[i][j] = '#' if seats[i][j] == 'L' else 'L'
  return sum(row.count('#') for row in seats)

def Hard(seats: list[list[str]]):
  seats = [row[:] for row in seats]
  def Neighbors(x: int, y: int):
    cnt = 0
    for i in range(-1, 2):
      for j in range(-1, 2):
        if i == 0 and j == 0: continue
        dx, dy = x + i, y + j
        while 0 <= dx < len(seats) and 0 <= dy < len(seats[0]):
          if seats[dx][dy] != '.':
            cnt += seats[dx][dy] == '#'
            break
          dx += i
          dy += j
    return cnt
  while True:
    flips = []
    for i in range(len(seats)):
      for j in range(len(seats[0])):
        if seats[i][j] == 'L' and Neighbors(i, j) == 0:
          flips.append((i, j))
        if seats[i][j] == '#' and Neighbors(i, j) >= 5:
          flips.append((i, j))
    if not flips:
      break
    for i, j in flips:
      seats[i][j] = '#' if seats[i][j] == 'L' else 'L'
  return sum(row.count('#') for row in seats)

input = Read()
print(Easy(input))  
print(Hard(input))