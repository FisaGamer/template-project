import math as m
import numpy as np
import sympy as sp
import statistics as s
import sys
import os
import argparse
import random as r
import pprint

def loop_list(n: int, f: callable, *args) -> object:
    """
    :rtype: list
    :param n: int
    :param f: callable
    :param kwargs: args
    """
    return [f(*args) for i in range(n)]


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

def add(f, liste):
    return liste.append(f)


if __name__ == '__main__':
    liste = loop_list(100, loop_list, 10, r.randint, 0, 1)
    pprint.pprint(liste)
    average = []
    for i in liste:
        average.append(s.mean(i))
    pprint.pprint(s.mean(average))
    help()