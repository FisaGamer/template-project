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
    :param kwargs:
    """
    [f(*args) for i in range(n)]


def loop(n: int, f: callable, *args) -> object:
    """
    :rtype: list
    :param n: int
    :param f: callable
    :param kwargs:
    """
    for i in range(n):
        f(*args)


def main():
    pass


if __name__ == '__main__':
    main()
