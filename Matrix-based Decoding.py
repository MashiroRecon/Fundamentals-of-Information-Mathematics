#  Matrix-based decoding

#  Imports
import numpy as np
import sympy as sp
import random

#  復号化したいテキストの入力
text = list(input("Enter the text :"))

#  暗号化鍵の入力
password = list(input("Enter the encryption key :"))

#  mod:nの入力
N = int(input("mod ="))

#  文字を全てASCIIで変換しintにして代入
j = 0
print(password)
while j != int(len(password)):
    password[j] = int(ord(password[j]))
    j += 1

#  暗号化鍵をAへlen(text)行の配列として代入
A = np.array([int(a) for a in password]).reshape(int(len(text) / 2),
                                                 int(len(password) /
                                                 int(len(text) / 2)))
print(password)
print(A)

#  Aの逆行列を算出
A_inv = np.linalg.inv(A)
print(A_inv)
