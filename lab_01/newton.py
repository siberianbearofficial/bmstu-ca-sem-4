import math
from typing import Sequence, Iterable
from point import Point


def diff(a):
    return list(a[i] - a[i + 1] for i in range(len(a) - 1))


def diffs(a, ready=None):
    if ready is None:
        ready = []
    d = diff(a)
    if len(d) <= 1:
        return [el[-1] for el in (ready + [d])]
    return diffs(d, ready + [d])


def interpolation(points: Sequence[Point], step: float | None = None) -> Iterable[Point]:
    if len(points) < 2:
        return points
    if not step or step is not None and step <= 0:
        step = abs(points[0].x - points[1].x)

    d = [points[0].y] + diffs(tuple(map(lambda point: point.y, reversed(points))))
    a = [d[k] / math.factorial(k) / (step ** k) for k in range(len(d))]

    x = points[0].x
    while x <= points[-1].x:
        y = a[0]
        for i in range(1, len(a)):
            ans = a[i]
            for j in range(i):
                ans *= (x - points[j].x)
            y += ans
        yield Point(x, y)
        x += step / 10
