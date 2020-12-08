#!/usr/bin/env python
from functools import cache
import re
import sys

def Read():
  infile = 'in' if len(sys.argv) <= 1 else sys.argv[1]
  g = {}
  with open(infile) as f:
    for line in f:
      bag, = re.findall('^(\w+ \w+)', line)
      inside = re.findall('(\d+) (\w+ \w+) bag', line)
      g[bag] = inside
  return g

def Easy(g):
  @cache
  def HasGold(bag):
    return bag == 'shiny gold' or any(HasGold(has) for _, has in g[bag])
  return sum(HasGold(bag) for bag in g) - 1

def Hard(g):
  @cache
  def CountBags(bag):
    return 1 + sum(int(cnt) * CountBags(has) for cnt, has in g[bag])
  return CountBags('shiny gold') - 1

input = Read()
print(Easy(input))
print(Hard(input))