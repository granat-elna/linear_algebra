import numpy as np
import det_n

nth = 3
x = np.empty((0, nth))
x_row = np.empty(0)
for i in range(nth):
    for j in range(nth):
        x_in = input("X[{}][{}] >>> ".format(i+1, j+1))
        x_row = np.append(x_row, x_in)
    x = np.append(x, np.array([x_row]), axis=0)
    x_row = np.empty(0)
print(x)
det_n.det3(x)
