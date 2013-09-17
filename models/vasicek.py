from pypriceengine.models.brownian import BrownianMotion

class Vasicek(object):

    def __init__(self, n, a, b, r, dt, sigma):

        self._n = n
        self._a = a
        self._b = b
        self._r = r
        self._sigma = sigma
        self._dt = dt
        self._res = 0
        self._i = 0
        self.wiener =  [x for x in BrownianMotion(self._n, self._dt, 0)]

    def __iter__(self):
        return self


    def next(self):
        if self._i >= self._n:
            raise StopIteration
        else:
            self._res = self._res + self._a * (self._b - self._r) * self._dt +\
                        (self._sigma * self.wiener[self._i])
            self._i += 1
            return self._res


