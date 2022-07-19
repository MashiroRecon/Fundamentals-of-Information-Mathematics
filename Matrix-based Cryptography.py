#  Matrix-based cryptography

#  Imports
import numpy as np
import random

#  暗号化したいテキストの入力
text = list(input("Enter the text :"))

#  暗号化したい文の文字数が2の倍数でないときに最後尾に空白を入力
j = 0
if int(len(text) % 2) == 1:
    text.append(" ")

#  文字を全てASCIIで変換しintにして代入
print(text)
while j != int(len(text)):
    text[j] = int(ord(text[j]))
    j += 1

#  listをPへ2行の配列として代入
P = np.array([int(a) for a in text]).reshape(2, int(len(text) / 2))
print(text)
print(P)

#  暗号化鍵の作成
password = list(input("Enter the encryption key :"))

#  暗号化鍵が2の倍数でないときに最後尾にランダムな文字を入力
#  ASCII:42~126("*" ~ "~")
j = 0
while int(len(password) % int(len(text) / 2)) != 0:
    password.append(chr(random.randint(42, 126)))

#  文字を全てASCIIで変換しintにして代入
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

#  mod:nの入力
N = int(input("mod ="))

#  暗号化
C = np.dot(A, P) % N
print(C)

#  1行に変換
j = 1
cipher = np.ravel(C)
print(cipher)

#  暗号化鍵作成時にランダム関数を用いて必要な行数を確保できる文字列を生成
#  その後文字列を数列に変換し暗号化処理を実行
#  再度ASCIIを通して文字列に変換し出力
