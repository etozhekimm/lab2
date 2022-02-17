#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    diction = {1: 'Атос', 2: 'Портос', 3: 'Арамис'}
    print(diction)
    diction_swap = {v:k for k, v in diction.items()}
    print(diction_swap)

