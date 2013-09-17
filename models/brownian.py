from numpy.random import standard_normal


class BrownianMotion(object):

    def __init__(self, n, dt, xzero):
        self._xzero = xzero
        self._n = n
        self._dt = dt
        self._counter = 0

    def __iter__(self):
        return self

    def next(self):
        if self._counter >= self._n:
            raise StopIteration
        else:
            self._counter += 1
            return standard_normal() * self._dt ** 0.5
