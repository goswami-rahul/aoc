#!/usr/bin/env python
from typing import Set, Dict 
import re
import collections
from rich import traceback
traceback.install()

def Easy():
  def Check(have: Set[str]):
    need = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'}
    if have - need:
      return False
    need.remove('cid')
    if need - have:
      return False
    return True

  ans = 0
  with open('in') as f:
    have = set()
    for line in f:
      line = line.strip()
      have |= set(re.findall('(...):', line, ))
      if not line:
        ans += Check(have)
        have.clear()
    ans += Check(have)
    have.clear()
  return ans

def Hard():
  def HeightOk(hgt: str):
    return ((hgt.endswith('in') and 59 <= int(hgt[:-2]) <= 76) or 
      (hgt.endswith('cm') and 150 <= int(hgt[:-2]) <= 193))

  def Check(have: Dict[str, str]):
    return bool(1920 <= int(have['byr']) <= 2002 and
      2010 <= int(have['iyr']) <= 2020 and 
      2020 <= int(have['eyr']) <= 2030 and 
      HeightOk(have['hgt']) and
      re.match('^#(\d|[a-f]){6}$', have['hcl']) and 
      have['ecl'] in 'amb blu brn gry grn hzl oth'.split() and 
      re.match('^\d{9}$', have['pid'])
    )

  ans = 0
  with open('in') as f:
    have = collections.defaultdict(lambda: '0'*5)
    for line in f:
      line = line.strip()
      for key, val in re.findall('(\w+):(\S+)', line):
        have[key] = val
      if not line:
        ans += Check(have)
        have.clear()
    ans += Check(have)
    have.clear()
  return ans

print(Easy())
print(Hard())