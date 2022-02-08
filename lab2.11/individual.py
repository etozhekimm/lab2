#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func(func_type: str):
    def inner(value):
        gen = (e for e in value.split())
        if func_type == 'list':
            return list(gen)
        return tuple(gen)

    return inner


if __name__ == '__main__':
    x = input()
    y = input()
    print(func(x)(y))
