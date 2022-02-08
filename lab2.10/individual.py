#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def after_sum(*args):
    if args:
        i = 0
        for index, arg in enumerate(args):
            if arg > 0:
                i = index
        pos_s = sum(arg for index, arg in enumerate(args) if index < i)
        return pos_s
    else:
        return None


if __name__ == "__main__":
    arguments = [int(i) for i in input().split()]
    arguments.reverse()
    print(after_sum(*arguments))