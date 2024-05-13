"""
Лабораторная работа №1 по курсу "Вычислительные Алгоритмы"
Орлов Алексей ИУ7-44Б
"""

import matplotlib.pyplot as plt

from point import Point
from newton import interpolation as newton


def read_points():
    points = list()
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                x, y = map(float, line.split())
                points.append(Point(x, y))
    except Exception as e:
        print(e)
    return points


def main():
    points = read_points()

    plt.clf()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.scatter(tuple(map(lambda point: point.x, points)), tuple(map(lambda point: point.y, points)))
    plt.plot(*zip(*map(lambda point: (point.x, point.y), newton(points))))
    plt.show()


if __name__ == '__main__':
    main()
