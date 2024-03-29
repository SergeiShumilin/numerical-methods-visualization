# -*- coding: utf-8 -*-
"""
Данный модуль предназначен для рисования графиков.
"""
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np


def plot_bisection(f, aas, bbs, mms):
    """
    Отобразить процесс бисекции графически.
    :param f: функция.
    :param aas: массив левых границ отрезка.
    :param bbs: массив правых границ отрезка.
    :param mms: массив середин отрезков.
    """
    fig = plt.figure()
    length = len(aas)
    rows, columns = calc_row_and_columns(length)
    gs = GridSpec(rows, columns, figure=fig)

    # Массив значений х.
    xs = np.arange(aas[0], bbs[0], 0.01)

    # Отобразить итерации метода.
    for i, splot in enumerate(gs):
        ax = fig.add_subplot(splot)

        # Отобразить функцию.
        ax.plot(xs, [f(x) for x in xs], color='r')

        # Отобразить координатные оси.
        ax.axhline(0, color='gray', lw=1)
        ax.axvline(0, color='gray', lw=1)

        plot_point(ax, f, aas[i], 'a', with_line=True)
        plot_point(ax, f, bbs[i], 'b', with_line=True)
        plot_point(ax, f, mms[i], 'm', with_line=False)

    plt.show()


def plot_point(ax, f, x, letter, with_line=False):
    """
    Отобразить вертикальную линию над точкой на оси х,
    если параметор with_line установлен в True.
    Подписать координату.
    :param ax: subplot для отображения.
    :param f: функция.
    :param x: координата х точки.
    :param letter: буква для обозначения точки на оси.
    :param with_line: проводить вертикальную прямую до функции.
    """
    ax.text(x + 0.05, 5, letter, style='italic', fontsize=15)
    ax.plot(x, 0, marker='o', color='black', markersize=5)
    if with_line:
        ax.plot((x, x), (0, f(x)), 'b', lw=0.5, linestyle='--')


def plot_line(ax, f, x1, x2):
    """
    Plot line with coordinates.
    :param x1: x1
    :param x2: x2
    """
    ax.plot((x1, x2), (f(x1), f(x2)), 'b', lw=0.5, linestyle='--')


def calc_row_and_columns(length):
    """
    Рассчитать размер сетки графиков в зависимости от
    числа итераций метода.
    :param length: длина массива равная числу итераций метода.
    """
    assert length > 0, 'Массив итераций пуст.'

    if length == 1:
        return 1, 1
    elif length == 2:
        return 1, 2
    elif length == 3:
        return 2, 2
    else:
        return 2, 2


def plot_false_position(f, aas, bbs, rts):
    """
    Plot the process of false position method.
    :param f: function.
    :param aas: left borders.
    :param bbs: right borders.
    :param rts: roots.
    """
    fig = plt.figure()
    length = max(len(aas), len(bbs), len(rts))
    rows, columns = calc_row_and_columns(length)
    gs = GridSpec(rows, columns, figure=fig)

    # Массив значений х.
    xs = np.arange(aas[0], bbs[0], 0.01)

    ai = aas[0]
    bi = bbs[0]
    rtsi = rts[0]

    # Отобразить итерации метода.
    for i, splot in enumerate(gs):
        ax = fig.add_subplot(splot)

        ax.set_title(str(i + 1) + ' iteration', fontsize=15)

        if len(aas) > i:
            ai = aas[i]

        if len(bbs) > i:
            bi = bbs[i]

        if len(rts) > i:
            rtsi = rts[i]

        # Отобразить функцию.
        ax.plot(xs, [f(x) for x in xs], color='r')

        # Отобразить координатные оси.
        ax.axhline(0, color='gray', lw=1)
        ax.axvline(0, color='gray', lw=1)

        plot_point(ax, f, ai, 'a', with_line=True)
        plot_point(ax, f, bi, 'b', with_line=True)
        plot_point(ax, f, rtsi, 'm', with_line=True)

        # The only addition from false position method todo consider make base function for depiction.
        # line linking two boundary points.
        plot_line(ax, f, ai, bi)

    plt.show()
