#!/usr/bin/env python3

from random import randrange
from sys import stdin


REPEATS = 1000
RANGE = 128

for _ in range(REPEATS):
    a, b = randrange(RANGE), randrange(RANGE)
    print(f'{a} + {b}', flush=True)
    line = stdin.readline().removesuffix('\n')
    c = int(line, 10)
    if a + b != c:
        print('nope')
        exit(1)

with open('flag.txt', 'r') as f:
    print(f.read())
