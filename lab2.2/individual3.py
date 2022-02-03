#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    n = 20
    a = 0
    while n < 100:
        n += 1
        if n % 3 == 0:
            a += n

    print(a)
