#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    A = set("abhkor")
    B = set("bghls")
    C = set("klz")
    D = set("gjpquv")
    U = set("abcdefghijklmnopqrstuvwxyz")
    X = ((A & C) | B)
    Y = (((U - A) & (U - B)) - (C | D))
    print("X =", X)
    print("Y =", Y)
