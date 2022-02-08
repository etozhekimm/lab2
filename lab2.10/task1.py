#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def geom(*args):
    if args:
        multi = 1
        values = [float(arg) for arg in args]
        n = len(values)
        for elem in values:
            multi *= elem
        return multi ** (1 / n)
    else:
        return None


if __name__ == '__main__':
    arguments = [float(i) for i in input().split()]
    print(geom(*arguments))
