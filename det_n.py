# coding: utf-8
import numpy as np


# NxN determinant
def detn(x, n):
    # 
    d = 0
    x_del = np.zeros((n, n))
    if n == 1:
        d = x[0][0]
        return d
    if n == 2:
        d = x[0][0] * x[1][1] - x[0][1] * x[1][0]
        return d
    else:
        for i in range(0, n):
            x_del = np.delete(x, 0, 0)
            x_del = np.delete(x_del, i, 1)
            d += x[0][i] * pow(-1, i) * detn(x_del, n-1)
        return d


# 3x3 determinant
def det3(x):
    d = .0
    for i in range(3):
        x_del = np.delete(x, 0, axis=0)
        x_del = np.delete(x_del, i, axis=1)
        if (i % 2) == 1:
            d -= x[0][i] * det2(x_del)
        else:
            d += x[0][i] * det2(x_del)
    print("Determinant: {}".format(d))


# 2x2 determinant
def det2(x):
    return x[0][0] * x[1][1] - x[0][1] * x[1][0]
