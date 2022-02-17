#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    school = {'1А': 22, '1Б': 27, '1В': 18, '2А': 23, '2Б': 19}
    request = input()
    if request in school.keys():
        print('Количество учеников:', school[request])
    else:
        print('Такого класса нет')
