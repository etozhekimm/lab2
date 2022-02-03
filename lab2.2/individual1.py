#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    n = int(input("Значение кВт/ч: "))
    if n <= 250:
        i = 7*n
    elif n > 250 and n <= 300:
        i = (n - 250) * 17 + 250 * 7
    else:
        i = (n - 250) * 20 + 250 * 7

    print("Оплата составила: ", i)
