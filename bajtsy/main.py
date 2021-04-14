#!/usr/bin/env python3

from random import randrange
from sys import stdin, stdout


REPEATS = 1000
RANGE = 128

for _ in range(REPEATS):
    a, b = randrange(RANGE), randrange(RANGE)
    stdout.buffer.write(bytes([a, b]))
    stdout.buffer.flush()
    c = stdin.buffer.read(1)[0]
    if ((a + b) & 0xff) != c:
        print('nope')
        exit(1)

with open('flag.txt', 'r') as f:
    print(f.read())
