# -*- coding: utf-8 -*-
""" Модуль включает вспомогательные функции для численных методов"""


def print_result(method, func, root, nx, ny, time):
    """
    Отобразить информацию о найденном корне.
    :param method: используемый метод.
    :param func: функция.
    :param root: корень уравнения.
    :param nx: число итераций при схождении по x.
    :param ny: число итераций при схождении по y.
    :param time: время выполнения метода.
    """
    print('Метод : {}\n'
          'Корень найден\n'
          'Функция: {}\n'
          'Корень уравнения: {}\n'
          'Число итераций по х: {}\n'
          'Число итераций по y: {}\n'
          'Время выполнения: {} c\n\n'.format(method, func.__doc__, root, nx, ny, time))


def print_iter_exceeded(method, func, nx, time):
    """
    Отобразить информацию о превышении допустимого числа итераций.
    :param method: используемый метод.
    :param fucn: функция.
    :param nx: число итераций при схождении по x.
    :param ny: число итераций при схождении по y.
    :param time: время выполнения метода.
    """
    print('Метод : {}\n'
          'Метод не сходится по х.\n'
          'Функция: {}\n'
          'Число итераций по х: {}\n'
          'Время выполнения: {} c\n\n'.format(method, func.__doc__, nx, time))


def print_doesnt_converge(method, func, root, nx, ny, time):
    """
    Отобразить информацию о превышении допустимого числа итераций.
    :param method: используемый метод.
    :param fucn: функция.
    :param nx: число итераций при схождении по x.
    :param ny: число итераций при схождении по y.
    :param time: время выполнения метода.
    """
    print('Метод : {}\n'
          'Функция претерпевает разрыв\n'
          'Функция: {}\n'
          'Предпологаемый корень уравнения: {}\n'
          'Число итераций по х: {}\n'
          'Число итераций по y: {}\n'
          'Время выполнения: {} c\n\n'.format(method, func.__doc__, root, nx, ny, time))


def show_iterations_info(a, b, rts):
    """
    Show information about calculation process
    iteration-wise.
    :param a array : left borders.
    :param b: array right borders.
    :param rts: array roots.
    :return:
    """

    print('  |   a   |   b   |   root')

    ai = a[0]
    bi = b[0]
    rtsi = rts[0]

    for i in range(max(len(a), len(b), len(rts))):

        if len(a) > i:
            ai = a[i]

        if len(b) > i:
            bi = b[i]

        if len(rts) > i:
            rtsi = rts[i]

        print('{} |   {}   |   {}   |   {}   '.format(i, ai, bi, rtsi))