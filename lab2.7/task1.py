#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    gl = set("aeiouy")
    string = set(input("Введите строку: ").lower())
    print(gl & string)

