#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mid_harm(*args):
    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        sum_of_reversed = 0
        for value in values:
            sum_of_reversed += (1 / value)
        return n / sum_of_reversed
    else:
        return None


if __name__ == "__main__":
    arguments = [float(i) for i in input().split()]
    print(mid_harm(*arguments))
