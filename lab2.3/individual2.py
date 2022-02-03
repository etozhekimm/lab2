#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    message = str(input("Введите строку:")) + "О"
    rule1 = "чя"
    rule2 = "щя"
    mistake = 0
    right = 1
    print("\"", end='')
    for i in range(len(message) - 1):
        if mistake == 0:
            print(message[i], end='')
            if ((message[i] + message[i + 1]) == rule1) or ((message[i] + message[i + 1]) == rule2):
                mistake = 1
                right = 0
        else:
            print('а', end='')
            mistake = 0
    if right:
        print("\" — это верное предложение!")
    else:
        print("\" — наверное, правильно так.")
