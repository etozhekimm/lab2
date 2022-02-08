#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def summary(mas, inx):
    if int(mas[inx]) > 0:
        return summary(mas, inx + 1) + int(mas[inx])
    else:
        return 0


if __name__ == '__main__':
    ms = input()
    print(summary(ms.split(), 0))