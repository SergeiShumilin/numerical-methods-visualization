# -*- coding: utf-8 -*-
"""Модуль описывает набор различных функций. """
import numpy as np


def f1(x):
    """x^3 + x^2 + x + 1"""
    return x ** 3 + x ** 2 + x + 1


def f2(x):
    """
    Разрывная в т. 0 функция.
           |1, если x > 0
    f(x) = |
           |-16, если x <= 0
    """
    if x > 0:
        return 5
    else:
        return -5


def f3(x):
    """1 / (x - 1)"""
    if x == 1:
        return np.nan
    return 1.0 / (x - 1)
