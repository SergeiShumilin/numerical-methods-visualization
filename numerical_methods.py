# -*- coding: utf-8 -*-
"""
Модуль реализует метод бисекции отыскания корней нелинейных уравнений.
"""
import math
from timeit import default_timer as timer
import support as sp
import graphics

# Максимальное число итераций для схождения по x.
XMAX = 100
# Максимальное число итераций для схождения по y.
YMAX = 100


def bisection(f, a, b, delta_x=10e-5, delta_y=10e-5):
    """
    Метод бисекции.
    :param f: функция для отыскания решения.
    :param a: левая граница отрезка для поиска корня.
    :param b: правая граница отрезка для поиска корня.
    :param delta_x: погрешность нахождения корня по оси абсцисс.
    :param delta_y: погрешность нахождения корня по оси ординат.
    :return: корень уравнения.
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
    while math.fabs(a - b) > delta_x and i < XMAX:

        if math.fabs(fm) < delta_y:
            break

        if fa * fm > 0:
            a = m
            fa = fm

        else:
            b = m
            fb = fm

        m = (a + b) / 2
        fm = f(m)

        aas.append(a)
        bbs.append(b)
        mms.append(m)

        i += 1
        nx += 1

    # Если метод не сошелся. При этом если функция
    if i >= XMAX:
        sp.print_iter_exceeded(method, f, nx, timer() - start)
        return 'Метод не сходится'

    # Сходимся по y.
    while math.fabs(fm) > delta_y and j < YMAX:

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

    if math.fabs(fm) <= delta_y:
        sp.print_result(method, f, m, nx, ny, timer() - start)
        return "Корень найден"
    else:
        sp.print_doesnt_converge(method, f, m, nx, ny, timer() - start)
        return "Функция претерпевает разрыв"
