import math as m
import numpy as np
import sympy as sp
import statistics as s
import sys
import os
import argparse


def loop_list(n: int, f: callable, *args) -> object:
    """
    :rtype: list
    :param n: int
    :param f: callable
    :param kwargs: args
    """
    [f(*args) for i in range(n)]


def loop(n: int, f: callable, *args) -> object:
    """
    :rtype: list
    :param n: int
    :param f: callable
    :param kwargs: args
    """
    for i in range(n):
        f(*args)


def main():
    pass


class CustomString(str):
    def tolist(self):
        return [self[i] for i in range(len(self))]


if __name__ == '__main__':
    main()
    moi = CustomString("coucou")
    print(moi.tolist())
