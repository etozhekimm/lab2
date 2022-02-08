#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    first_string = set(input("Введите первую строку: ").lower())
    second_string = set(input("Введите вторую строку: ").lower())
    print(first_string & second_string)
