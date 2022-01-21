from collections.abc import Iterable
import math

class RGB:
    def __init__(self, r, g, b):
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

    def __str__(self):
        return "(%i, %i, %i)" % (self.r, self.g, self.b)

    def __add__(self, other):
        return RGB(self.r + other.r, self.g + other.g, self.b + other.b)

    def __pow__(self, n):
        return RGB(self.r ** n, self.g ** n, self.b ** n)

def zero () -> RGB:
    return RGB(0, 0, 0)

def rgb_dist (r1 : RGB, r2 : RGB) -> int:
    return (r1.r - r2.r) ** 2 + (r1.g - r2.g) ** 2 + (r1.b - r2.b) ** 2

def average (rs : Iterable[RGB]) -> RGB:
    i = 0
    sq_sum = zero()
    for rgb in rs:
        i += 1
        sq_sum += rgb ** 2
    return RGB (math.sqrt(sq_sum.r) / i, math.sqrt(sq_sum.r) / i, math.sqrt(sq_sum.r) / i)
