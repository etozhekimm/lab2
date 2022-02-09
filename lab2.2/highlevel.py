#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def intsin(x):
    eps = 0.000000000000001
    term = x
    sum = x
    n = 1
    while (term * term) > (eps * eps):
        k = 2 * n + 1
        term *= -x * x * (k - 2) / (2 * k * k * n)
        sum += term
        n += 1
    return sum


if __name__ == '__main__':
    print(intsin(float(input("Введите х: "))))