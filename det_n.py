# coding: utf-8
# n次正方行列を求める本体のプログラム
import numpy as np


# NxN determinant(完成版)
def detn(x, n):
    d = 0  # 行列の値
    x_del = np.zeros((n, n))  # 縮小した行列
    # 行列のサイズが1
    if n == 1:
        return x[0][0]
    # 行列のサイズが2
    elif n == 2:
        return x[0][0] * x[1][1] - x[0][1] * x[1][0]
    # 行列のサイズが3以上
    else:
        for i in range(0, n):
            # 行列xの第1行を削除
            x_del = np.delete(x, 0, 0)
            # 行列xの第i行を削除 これで元の行列のサイズnに対して(n-1)次正方行列ができた
            x_del = np.delete(x_del, i, 1)
            # 縮小した行列を再帰してサイズを2以下にし、その値を結果dに足し合わせていく
            # x[0][i]は余因子、pow(-1, i)は正負の値(i+jが奇数ならば(-1)を掛ける)
            d += x[0][i] * pow(-1, i) * detn(x_del, n-1)
        return d


# 3x3 determinant(テスト用)
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


# 2x2 determinant(テスト用)
def det2(x):
    return x[0][0] * x[1][1] - x[0][1] * x[1][0]
