#!/usr/bin/env python3

from sys import stdin


class Foo:
    with open('flag.txt') as f:
        flag = f.read()

stack = []
stack.append(Foo)

for line in stdin:
    line = line.rstrip()
    cmd, *args = line.split(' ')
    if cmd == 'push':
        o = args[0]
        stack.append(o)
    elif cmd == 'pushi':
        o = int(args[0], 10)
        stack.append(o)
    elif cmd == 'pop':
        stack.pop()
    elif cmd == 'dup':
        o = stack[-1]
        stack.append(o)
    elif cmd == 'swap':
        stack[-2:] = stack[:-3:-1]
    elif cmd == 'attr':
        obj = stack.pop()
        attr_name = stack.pop()
        o = getattr(obj, attr_name)
        stack.append(o)
    elif cmd == 'item':
        obj = stack.pop()
        idx = stack.pop()
        o = obj[idx]
        stack.append(o)
    elif cmd == 'print':
        o = stack.pop()
        if 'wwi2021-depyton' in o:
            o = 'REDACTED'
        print(o, flush=True)
    else:
        assert False, f'Invalid cmd {repr(cmd)}.'
