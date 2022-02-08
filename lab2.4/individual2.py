#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    lst = list(map(float, input().split()))
    if not lst:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    a = int(input("Введите левую границу интервала (a):"))
    b = int(input("Введите правую границу интервала (b):"))

    new = []
    result = 0
    plus = 0
    maximum = 0
    last = 0

    for i in range(len(lst)):
        if abs(lst[maximum]) <= abs(lst[i]):
            maximum = i
        if plus == 1:
            result += lst[i]
        if lst[i] > 0:
            plus = 1
        if int(lst[i]) in range(a, b + 1):
            lst[i], lst[last] = lst[last], lst[i]
            last += 1

    print("Элемент номер", maximum + 1, " - максимальный по модулю")
    print(result, " - Сумма элементов после первого положительного")
    print("Преобразованный список: ", lst)

