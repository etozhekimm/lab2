#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def start_func(text1, text2):
    return text1.split(), text2.split()


def decorated(func):
    def decorated_m(text1, text2):
        data = func(text1, text2)
        return dict(zip(*data))
    return decorated_m


start_func = decorated(start_func)
x = input()
y = input()
print(start_func(x, y))