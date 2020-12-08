#!/usr/bin/env python
a = []
with open('in') as f:
  for n in f:
    a.append(int(n))

for x in a:
  if 2020 - x in a:
    print(x * (2020 - x))     
    break

for x in a:
  for y in a:
    if 2020 - x - y in a:
      print(x * y * (2020 - x - y))
      exit()