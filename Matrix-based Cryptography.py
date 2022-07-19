#  Matrix-based cryptography

#  Imports
import numpy as np
import sympy as sp
import scipy.linalg as spl
import random

#  暗号化したいテキストの入力
text = list(input("Enter the text :"))

#  mod:nの入力
N = int(input("mod ="))

#  暗号化したい文字列を内包することのできる最低の正方行列の大きさを求める
q = 1
while int(len(text)) > q**2:
    q += 1

#  暗号化したい文の文字数がqの二乗でないときに最後尾に空白を入力
while int(len(text)) != q**2:
    text.append(" ")

#  文字を全てASCIIで変換しintにして代入
print(text)
j = 0
while j != int(len(text)):
    text[j] = int(ord(text[j]))
    j += 1

#  listをPへq行の配列として代入
P = np.array([int(a) for a in text]).reshape(q, q)
print(text)
print(P)

#  暗号化鍵がqの二乗でないときに最後尾にランダムな文字を入力
#  ASCII:42~126("*" ~ "~")
password = list(chr(random.randint(42, 126)))
while int(len(password)) != q**2:
    password.append(chr(random.randint(42, 126)))

#  文字を全てASCIIで変換しintにして代入
print(password)
j = 0
while j != int(len(password)):
    password[j] = int(ord(password[j]))
    j += 1

#  暗号化鍵をAへq行の配列として代入
A = np.array([int(a) for a in password]).reshape(q, q)
print(password)
print(A)

#  暗号化
C = np.dot(A, P) % N
print(C)

#  1行に変換
cipher = np.ravel(C)
print(cipher)

#  暗号化鍵作成時にランダム関数を用いて必要な行数を確保できる文字列を生成
#  その後文字列を数列に変換し暗号化処理を実行
#  再度ASCIIを通して文字列に変換し出力

#  復号化処理

#  A逆行列の算出
A_inv = np.linalg.inv(A) % N

A_inv = np.ravel(A_inv)
A_inv = [int(a) for a in A_inv]
A_inv = np.array([int(a) for a in A_inv]).reshape(q, q)

decod = np.dot(A_inv, C)
print(decod)
# print(np.dot(A, A_inv) % N)
# print(np.dot(A_inv, A) % N)

decod = np.ravel(decod)
decod = [int(a) for a in decod]
print(decod)

j = 0
while j != int(len(decod)):
    decod[j] = chr(int(decod[j]))
    j += 1
print(decod)
