#!/usr/bin/env python3

from sys import stdin


class Foo:
    def __init__(a, b, c): pass
    with open('flag.txt') as f:
        flag = f.read()

stack = []
stack.append(Foo)

for line in stdin:
    line = line.removesuffix('\n')
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
    elif cmd == 'call':
        obj = stack.pop()
        attr_name = stack.pop()
        f = getattr(obj, attr_name)
        arg = stack.pop()
        stack.append(f(arg))
    elif cmd == 'print':
        o = stack.pop()
        if 'wwi2021-depyton' in o:
            o = 'REDACTED'
        print(o, flush=True)
    else:
        assert False, f'Invalid cmd {repr(cmd)}.'
