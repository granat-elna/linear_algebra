# coding: utf-8
import numpy as np
import numpy.linalg as LA
import det_n

mode = input("type '1' for randomly generated, or '2' for your specified >>> ")
if mode == 1:
    nth = 8
elif mode == 2:
    nth = input("type determinant size >>> ")
x = np.empty((0, nth))
x_row = np.empty(0)
for i in range(nth):
    for j in range(nth):
        if mode == 1:
            x_in = int(np.random.rand() * 10)
        elif mode == 2:
            x_in = input("X[{}][{}] >>> ".format(i+1, j+1))
        x_row = np.append(x_row, x_in)
    x = np.append(x, np.array([x_row]), axis=0)
    x_row = np.empty(0)
print("Requested determinant: \n{}".format(x))
print("Determinant(numpy calculated): {}".format(LA.det(x)))
print("Determinant(my program calculated): {}".format(det_n.detn(x, nth)))
