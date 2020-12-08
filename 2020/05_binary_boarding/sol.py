#!/usr/bin/env python

def GetId(seat: str):
  seat = seat.replace('F', '0')
  seat = seat.replace('B', '1')
  seat = seat.replace('L', '0')
  seat = seat.replace('R', '1')
  return int(seat, 2)

def Easy():
  with open('in') as f:
    return max(GetId(line.strip()) for line in f)

def Hard():
  with open('in') as f:
    ids = [GetId(line.strip()) for line in f]
  ids.sort()
  for i in range(1, len(ids)):
    if ids[i] == ids[i - 1] + 2:
      return ids[i] - 1

print(Easy())
print(Hard())