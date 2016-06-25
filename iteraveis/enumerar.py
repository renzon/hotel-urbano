"""
>>> g = enumerar(range(3), 1)
>>> next(g)
(1, 0)
>>> next(g)
(2, 1)
>>> next(g)
(3, 2)
>>> next(g)
Traceback (most recent call last):
  ...
StopIteration

"""