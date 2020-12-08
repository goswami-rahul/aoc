#!/usr/bin/env python
import sys
from rich import print

def Read():
  infile = 'in' if len(sys.argv) <= 1 else sys.argv[1]
  code = []
  with open(infile) as f:
    for line in f:
      op, arg = line.strip().split()
      code.append((op, int(arg)))
  return code

def Easy(code: list[tuple[str, int]]):
  acc = 0
  saw = [False] * len(code)
  ptr = 0
  while ptr < len(code) and not saw[ptr]:
    saw[ptr] = True
    if code[ptr][0] == 'jmp':
      ptr += code[ptr][1]
    else:
      if code[ptr][0] == 'acc':
        acc += code[ptr][1]
      ptr += 1
  return acc

def Hard(code: list[tuple[str, int]]):
  def HasLoop(code):
    ptr = 0
    saw = [False] * len(code)
    while 0 <= ptr < len(code) and not saw[ptr]:
      saw[ptr] = True
      if code[ptr][0] == 'jmp':
        ptr += code[ptr][1]
      else:
        ptr += 1
    return ptr != len(code)

  code = code[::]
  for i, (op, arg) in enumerate(code):
    if op == 'nop':
      code[i] = ('jmp', arg)
      if not HasLoop(code):
        break
      code[i] = (op, arg)
    if op == 'jmp':
      code[i] = ('nop', arg)
      if not HasLoop(code):
        break
      code[i] = (op, arg)
  return Easy(code)

input = Read()
print(Easy(input))
print(Hard(input))