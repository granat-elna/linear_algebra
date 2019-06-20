# coding: utf-8
# n次正方行列を求める実行用プログラム
import numpy as np
import numpy.linalg as LA
import time
import det_n

# 行列のサイズを指定
n = int(input("type determinant size n >>> "))
# 行列の生成モードの選択. 1を入力するとランダム生成、2を入力するとマニュアル生成
while True:
    mode = int(input(
        "type '1' to generate randomly, or '2' to specify manually >>> "))
    if mode == 1 or mode == 2:
        break
    print("type just 1 or 2.")

x = np.empty((0, n))  # (n)次正方行列を生成, すべての要素を0に初期化

for i in range(n):
    x_row = np.empty(0)  # (n)次正方行列の行部分を同様に0に初期化
    for j in range(n):
        # ランダム生成モードの場合、0.0から10.0の範囲の値を生成
        if mode == 1:
            x_in = int(np.random.rand() * 100) * 0.1
        # マニュアル生成モードの場合、各要素を手動で入力
        elif mode == 2:
            x_in = input("X[{}][{}] >>> ".format(i+1, j+1))
        # 生成した値をx_rowの最後尾に追加
        x_row = np.append(x_row, x_in)
    # 生成したx_rowを行列xに追加
    x = np.append(x, np.array([x_row]), axis=0)

print("Requested determinant: \n{}".format(x))
t1 = time.time()
numpy_d = LA.det(x)
t2 = time.time() - t1
# NumPyの標準機能で求めた行列式(理論上の正解)
print("Determinant(numpy calculated): {}\nexecution time: {} sec."
      .format(numpy_d, t2))
t1 = time.time()
my_d = det_n.detn(x, n)
t2 = time.time() - t1
# detn関数で求めた行列式
print("Determinant(my program calculated): {}\nexecution time: {} sec."
      .format(my_d, t2))
