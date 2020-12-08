#!/usr/bin/env python
import re

ans = 0
with open('in') as f:
  for line in f:
    m: re.Match = re.match("(.*)-(.*) (.): (.*)", line)
    groups = m.groups()
    low = int(groups[0])
    high = int(groups[1])
    char = groups[2]
    password = groups[3]
    ans += low <= password.count(char) <= high

print(ans)

ans = 0
with open('in') as f:
  for line in f:
    m: re.Match = re.match("(.*)-(.*) (.): (.*)", line)
    groups = m.groups()
    one = int(groups[0]) - 1
    two = int(groups[1]) - 1
    char = groups[2]
    password = groups[3]
    ans += (password[one] == char) ^ (password[two] == char)

print(ans)