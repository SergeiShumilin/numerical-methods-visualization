# -*- coding: utf-8 -*-
"""
Модуль реализует метод бисекции отыскания корней нелинейных уравнений.
"""
from __future__ import division
from math import fabs
from timeit import default_timer as timer
import support as sp
import graphics

# Максимальное число итераций для схождения по x.
MAX_ITERATIONS_X = 100
# Максимальное число итераций для схождения по y.
MAX_ITERATIONS_Y = 100


def bisection(f, a, b, delta_x=10e-5, delta_y=10e-5):
    """
    Метод бисекции.
    Метод, который всегда сходится. Если начальный интервал содержит несколько корней,
    то метод найдет один из них. Сходится, если функция претерпевает разрыв.
    :param f: функция для отыскания решения.
    :param a: левая граница отрезка для поиска корня.
    :param b: правая граница отрезка для поиска корня.
    :param delta_x: погрешность нахождения корня по оси абсцисс.
    :param delta_y: погрешность нахождения корня по оси ординат.
    :return: статус решения.
    todo работа с 1 / (x - 1) - деление на ноль
    """
    method = 'Бисекция'

    # Сохранение текущих переменных метода.
    aas = [a]
    bbs = [b]
    mms = []

    start = timer()

    fa = f(a)
    fb = f(b)

    # Проверка диапазона на корректность.
    assert a < b, 'Неправильно задан диапазон'
    # Проверяем, что корень есть на отрезке.
    assert (f(a) * f(b)) <= 0, 'Нет корня на заданном отрезке.'

    # Допустимое число итераций по x.
    i = 0
    # Допустимое число итераций по y.
    j = 0
    # Число итераций по x.
    nx = 0
    # Число итераций по y.
    ny = 0

    if fa == 0:
        sp.print_result(method, f, a, nx, ny, timer() - start)
        return a

    if fb == 0:
        sp.print_result(method, f, b, nx, ny, timer() - start)
        return b

    # Середина отрезка.
    m = (a + b) / 2
    fm = f(m)
    mms.append(m)
    # Сходимся по x.
    while fabs(a - b) > delta_x and i < MAX_ITERATIONS_X:

        # todo а если функция очень пологая?
        if fabs(fm) < delta_y:
            break

        if fa * fm > 0:
            a = m
            fa = fm

        else:
            b = m
            fb = fm

        m = (a + b) / 2.0
        fm = f(m)

        aas.append(a)
        bbs.append(b)
        mms.append(m)

        i += 1
        nx += 1

    # Если метод не сошелся. При этом если функция
    if i >= MAX_ITERATIONS_X:
        sp.print_iter_exceeded(method, f, nx, timer() - start)
        return 'Метод не сходится'

    # Сходимся по y.
    while fabs(fm) > delta_y and j < MAX_ITERATIONS_Y:

        if fa * fm > 0:
            a = m
            fa = fm
        else:
            b = m
            fb = fm

        # Середина отрезка.
        m = (a + b) / 2
        fm = f(m)

        j += 1
        ny += 1

    # Отобразить графики для бисекции.
    graphics.plot_bisection(f, aas, bbs, mms)

    if fabs(fm) <= delta_y:
        sp.print_result(method, f, m, nx, ny, timer() - start)
        return "Корень найден"
    else:
        sp.print_doesnt_converge(method, f, m, nx, ny, timer() - start)
        return "Функция претерпевает разрыв"


def false_position(f, a, b, delta_x=10e-5, delta_y=10e-5, show_iter_info=False):
    """
    Find root of the equation f by false position method.
    :param f: функция для отыскания решения.
    :param a: левая граница отрезка для поиска корня.
    :param b: правая граница отрезка для поиска корня.
    :param delta_x: погрешность нахождения корня по оси абсцисс.
    :param delta_y: погрешность нахождения корня по оси ординат.
    :param show_iter_info: show table of iteration values.
    :return: статус решения.
    """
    method = 'Хорд'

    # Сохранение текущих переменных метода.
    aas = [a]
    bbs = [b]
    rtfs = []

    start = timer()

    fa = f(a)
    fb = f(b)

    # Проверяем, что корень есть на отрезке.
    assert (f(a) * f(b)) <= 0, 'Нет корня на заданном отрезке.'

    # Делаем f(a) < f(b)
    if fa > 0:
        t = a
        a = b
        b = t

        t = fa
        fa = fb
        fb = t

    # Число итераций по x.
    nx = 0
    # Число итераций по y.
    ny = 0

    if fa == 0:
        sp.print_result(method, f, a, nx, ny, timer() - start)
        return a

    if fb == 0:
        sp.print_result(method, f, b, nx, ny, timer() - start)
        return b

    dx = b - a
    rtf = a
    f_rtf = fa
    while fabs(dx) > delta_x and nx < MAX_ITERATIONS_X:

        rtf = a + dx * fa / (fa - fb)
        rtfs.append(rtf)
        f_rtf = f(rtf)

        if fabs(f_rtf) < delta_y:
            break

        if f_rtf < 0:
            a = rtf
            fa = f_rtf
            aas.append(a)
        else:
            b = rtf
            fb = f_rtf
            bbs.append(b)

        dx = b - a
        nx += 1

    # Если метод не сошелся.
    if nx >= MAX_ITERATIONS_X:
        sp.print_iter_exceeded(method, f, nx, timer() - start)
        return 'Метод не сходится'

    # Сходимся по y.
    while fabs(f_rtf) > delta_y and ny < MAX_ITERATIONS_Y:

        rtf = a + fa * dx / (fa - fb)
        rtfs.append(rtf)

        f_rtf = f(rtf)

        if f_rtf < 0:
            a = rtf
            fa = f_rtf
        else:
            b = rtf
            fb = f_rtf

        dx = a - b
        ny += 1

    if show_iter_info:
        sp.show_iterations_info(aas, bbs, rtfs)

    if fabs(f_rtf) <= delta_y:
        sp.print_result(method, f, rtf, nx, ny, timer() - start)
        return "Корень найден"
    else:
        sp.print_doesnt_converge(method, f, rtf, nx, ny, timer() - start)
        return "Функция претерпевает разрыв"
