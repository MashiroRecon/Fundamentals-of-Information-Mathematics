#  Matrix-based cryptography

#  Imports
import numpy as np
import sympy as sp

#  暗号化したいテキストの入力
text = input("Enter the text :")

#  文字列のリスト化
text_arr = list(text)

#  暗号化したい文の文字数が2の倍数でないときに最後尾に空白を入力
if len(text_arr) % 2 == 1:
    text_arr.append(" ")
i = len(text_arr) / 2
j = 0

#  文字を全てASCIIで変換しintにして代入
print(text_arr)
while j != len(text_arr):
    text_arr[j] = int(ord(text_arr[j]))
    j = j + 1

#  list全体をint型へ再定義
text_arr = [int(a) for a in text_arr]
print(text_arr)

#  listをPへ2行の配列として代入
P = np.array([int(a) for a in text_arr]).reshape(2, i)
print(text_arr)
