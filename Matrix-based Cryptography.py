#  Matrix-based cryptography

#  Imports
import numpy as np
import sympy as sp

text = input("Enter the text :")
text_arr = list(text)

if len(text_arr) % 2 == 1:
    text_arr.append(" ")
i = len(text_arr) / 2
j = 0

print(text_arr)
while j != len(text_arr):
    text_arr[j] = int(ord(text_arr[j]))
    j = j + 1
text_arr = [int(a) for a in text_arr]
print(text_arr)

P = np.array([int(a) for a in text_arr]).reshape(2, i)
print(text_arr)
